"""
Scraper Selenium utilisant l'API du site pour récupérer les vrais liens
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import re
import json


class FilmScraper:
    """Classe pour scraper les films avec Selenium"""
    
    def __init__(self, headless=True, base_url="https://fs9.lol"):
        """Initialise le driver Selenium"""
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.base_url = base_url
    
    def get_films_from_page(self, page_number, base_url="/films/"):
        """
        Récupère tous les films d'une page donnée
        
        Args:
            page_number (int): Numéro de la page à scraper
            base_url (str): URL de base (catégorie ou recherche)
            
        Returns:
            list: Liste de dictionnaires contenant les infos des films
        """
        # Construire l'URL selon le type de base_url
        if "search" in base_url:
            # URL de recherche
            url = f"{self.base_url}{base_url}&search_start={page_number}"
        else:
            # URL de catégorie
            url = f"{self.base_url}{base_url}page/{page_number}/"
        
        print(f"📄 Scraping page {page_number}: {url}")
        
        try:
            self.driver.get(url)
            time.sleep(2)
            
            film_elements = self.driver.find_elements(By.CSS_SELECTOR, "a.short-poster.img-box.with-mask")
            
            if not film_elements:
                print(f"❌ Aucun film trouvé sur la page {page_number}")
                return []
            
            films = []
            for element in film_elements:
                try:
                    href = element.get_attribute("href")
                    title = element.get_attribute("alt")
                    
                    img_element = element.find_element(By.TAG_NAME, "img")
                    img_src = img_element.get_attribute("src")
                    
                    score = None
                    try:
                        vote_element = element.find_element(By.CSS_SELECTOR, ".vote-score")
                        score = vote_element.text
                    except NoSuchElementException:
                        pass
                    
                    film_data = {
                        "url": href,
                        "title": title,
                        "image": img_src,
                        "score": score
                    }
                    
                    films.append(film_data)
                    print(f"✅ Film trouvé: {title}")
                    
                except Exception as e:
                    print(f"⚠️ Erreur lors de l'extraction d'un film: {e}")
                    continue
            
            print(f"✨ {len(films)} films extraits de la page {page_number}")
            return films
            
        except Exception as e:
            print(f"❌ Erreur lors du scraping de la page {page_number}: {e}")
            return []
    
    def scrape_multiple_pages(self, max_pages=5, base_url="/films/"):
        """
        Scrape plusieurs pages consécutives
        
        Args:
            max_pages (int): Nombre maximum de pages à scraper
            base_url (str): URL de base (catégorie ou recherche)
            
        Returns:
            list: Liste de tous les films trouvés
        """
        all_films = []
        
        for page_num in range(1, max_pages + 1):
            films = self.get_films_from_page(page_num, base_url=base_url)
            
            if not films:
                print(f"🛑 Arrêt du scraping à la page {page_num} (aucun film)")
                break
            
            all_films.extend(films)
            time.sleep(1)
        
        print(f"\n🎬 Total: {len(all_films)} films récupérés")
        return all_films
    
    def get_film_page_content(self, film_url):
        """
        Charge une page de film spécifique et retourne son HTML
        
        Args:
            film_url (str): URL de la page du film
            
        Returns:
            str: HTML de la page
        """
        try:
            print(f"🎬 Chargement de la page: {film_url}")
            self.driver.get(film_url)
            time.sleep(2)
            
            return self.driver.page_source
            
        except Exception as e:
            print(f"❌ Erreur lors du chargement de la page: {e}")
            return None
    
    def extract_news_id(self, film_url):
        """
        Extrait le newsId de l'URL du film
        
        Args:
            film_url (str): URL du film (ex: https://fs9.lol/films/15124368-fabian.html
                           ou https://fs9.lol/15124161-david.html)
            
        Returns:
            str: newsId (ex: 15124368)
        """
        # Essayer avec /films/ d'abord
        match = re.search(r'/films/(\d+)-', film_url)
        if match:
            return match.group(1)
        
        # Sinon chercher directement /{nombre}-
        match = re.search(r'/(\d+)-', film_url)
        if match:
            return match.group(1)
        
        return None
    
    def call_film_api(self, news_id):
        """
        Appelle l'API du site pour récupérer les liens de téléchargement
        
        Args:
            news_id (str): ID du film
            
        Returns:
            dict: Données de l'API ou None
        """
        try:
            api_url = f"{self.base_url}/engine/ajax/film_api.php?id={news_id}"
            print(f"🔌 Appel API: {api_url}")
            
            self.driver.get(api_url)
            time.sleep(2)
            
            # Récupérer le JSON de la page
            page_source = self.driver.page_source
            
            # Extraire le JSON (il est souvent dans un <pre> ou directement dans le body)
            try:
                # Essayer de parser directement
                json_data = json.loads(page_source)
                return json_data
            except:
                # Sinon chercher dans les balises
                try:
                    pre_element = self.driver.find_element(By.TAG_NAME, "pre")
                    json_text = pre_element.text
                    json_data = json.loads(json_text)
                    return json_data
                except:
                    try:
                        body_element = self.driver.find_element(By.TAG_NAME, "body")
                        json_text = body_element.text
                        json_data = json.loads(json_text)
                        return json_data
                    except Exception as e:
                        print(f"❌ Impossible de parser le JSON: {e}")
                        print(f"Page source: {page_source[:500]}")
                        return None
            
        except Exception as e:
            print(f"❌ Erreur lors de l'appel API: {e}")
            return None
    
    def transform_embed_to_download(self, embed_url):
        """
        Transforme une URL /embed-xxx en /d/xxx pour le téléchargement
        Exemple: https://vidzy.org/embed-m6ev8a1muyi1.html
              → https://vidzy.org/d/m6ev8a1muyi1.html
        
        Args:
            embed_url (str): URL avec /embed-
            
        Returns:
            str: URL transformée avec /d/
        """
        return embed_url.replace('/embed-', '/d/')
    
    def extract_real_download_link(self, vidzy_url):
        """
        Va sur la page vidzy.org/d/xxx et extrait le VRAI lien .mp4
        
        Args:
            vidzy_url (str): URL vidzy (ex: https://vidzy.org/embed-xxx.html ou /d/xxx.html)
            
        Returns:
            str: URL directe du fichier .mp4 ou None
        """
        try:
            # Transformer /embed- en /d/ si nécessaire
            if '/embed-' in vidzy_url:
                download_url = self.transform_embed_to_download(vidzy_url)
                print(f"🔄 Transformation: {vidzy_url}")
                print(f"             → {download_url}")
            else:
                download_url = vidzy_url
            
            print(f"🔗 Extraction du lien réel depuis: {download_url}")
            self.driver.get(download_url)
            time.sleep(3)
            
            # Chercher le lien avec la classe "main-button"
            try:
                main_button = self.driver.find_element(By.CSS_SELECTOR, "a.main-button")
                real_link = main_button.get_attribute("href")
                
                if real_link and ('.mp4' in real_link or 'vidzy.org' in real_link):
                    print(f"✅ Lien réel trouvé: {real_link[:100]}...")
                    return real_link
            except NoSuchElementException:
                print("⚠️ Bouton main-button non trouvé")
            
            # Méthode alternative: chercher tous les liens avec .mp4
            all_links = self.driver.find_elements(By.TAG_NAME, "a")
            for link in all_links:
                href = link.get_attribute("href")
                if href and '.mp4' in href:
                    print(f"✅ Lien .mp4 trouvé: {href[:100]}...")
                    return href
            
            print("❌ Aucun lien de téléchargement trouvé sur la page")
            return None
            
        except Exception as e:
            print(f"❌ Erreur lors de l'extraction du lien réel: {e}")
            return None
    
    def get_download_links(self, film_url):
        """
        Extrait les VRAIS liens de téléchargement via l'API du site
        
        Args:
            film_url (str): URL de la page du film
            
        Returns:
            dict: Dictionnaire avec les vrais liens de téléchargement par qualité/langue
        """
        try:
            print(f"🔍 Extraction des liens de téléchargement: {film_url}")
            
            # 1. Extraire le newsId de l'URL
            news_id = self.extract_news_id(film_url)
            
            if not news_id:
                print("❌ Impossible d'extraire le newsId de l'URL")
                return {'truefrench': None, 'french': None, 'vostfr': None}
            
            print(f"📋 NewsID: {news_id}")
            
            # 2. Appeler l'API
            api_data = self.call_film_api(news_id)
            
            if not api_data or 'players' not in api_data:
                print("❌ Pas de données players dans l'API")
                return {'truefrench': None, 'french': None, 'vostfr': None}
            
            players = api_data.get('players', {})
            vidzy = players.get('vidzy', {})
            
            print(f"📦 Données ViDZY: {vidzy}")
            
            download_links = {
                'truefrench': None,
                'french': None,
                'vostfr': None
            }
            
            # 3. Récupérer les liens ViDZY
            # VFF = TRUEFRENCH
            # VFQ = FRENCH  
            # VOSTFR = VOSTFR
            
            vidzy_vff = vidzy.get('vff') or vidzy.get('default')
            vidzy_vfq = vidzy.get('vfq')
            vidzy_vostfr = vidzy.get('vostfr')
            
            # 4. Extraire les vrais liens .mp4 depuis les pages vidzy
            if vidzy_vff:
                print(f"🎯 Extraction TRUEFRENCH depuis: {vidzy_vff}")
                real_link = self.extract_real_download_link(vidzy_vff)
                if real_link:
                    download_links['truefrench'] = real_link
                    print(f"✅ TRUEFRENCH enregistré")
            
            if vidzy_vfq:
                print(f"🎯 Extraction FRENCH depuis: {vidzy_vfq}")
                real_link = self.extract_real_download_link(vidzy_vfq)
                if real_link:
                    download_links['french'] = real_link
                    print(f"✅ FRENCH enregistré")
            
            if vidzy_vostfr:
                print(f"🎯 Extraction VOSTFR depuis: {vidzy_vostfr}")
                real_link = self.extract_real_download_link(vidzy_vostfr)
                if real_link:
                    download_links['vostfr'] = real_link
                    print(f"✅ VOSTFR enregistré")
            
            # Afficher un résumé
            available = [k for k, v in download_links.items() if v]
            if available:
                print(f"📊 Liens trouvés: {', '.join(available)}")
            else:
                print(f"📊 Liens trouvés: Aucun")
            
            return download_links
            
        except Exception as e:
            print(f"❌ Erreur lors de l'extraction des liens: {e}")
            import traceback
            traceback.print_exc()
            return {'truefrench': None, 'french': None, 'vostfr': None}
    
    def close(self):
        """Ferme le driver Selenium"""
        if self.driver:
            self.driver.quit()
            print("🔒 Driver Selenium fermé")
