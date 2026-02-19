"""
Scraper Selenium pour extraire les films depuis fs9.lol
Version avec webdriver-manager (alternative robuste)
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


class FilmScraper:
    """Classe pour scraper les films avec Selenium"""
    
    def __init__(self, headless=True):
        """Initialise le driver Selenium avec webdriver-manager"""
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        try:
            # Tentative avec webdriver-manager
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            print("✅ ChromeDriver installé via webdriver-manager")
        except Exception as e:
            print(f"⚠️ webdriver-manager a échoué: {e}")
            print("🔄 Tentative avec ChromeDriver système...")
            # Fallback sur le ChromeDriver système
            self.driver = webdriver.Chrome(options=chrome_options)
        
        self.base_url = "https://fs9.lol"
    
    def get_films_from_page(self, page_number):
        """
        Récupère tous les films d'une page donnée
        
        Args:
            page_number (int): Numéro de la page à scraper
            
        Returns:
            list: Liste de dictionnaires contenant les infos des films
        """
        url = f"{self.base_url}/page/{page_number}/"
        print(f"📄 Scraping page {page_number}: {url}")
        
        try:
            self.driver.get(url)
            # Attendre que la page charge
            time.sleep(2)
            
            # Récupérer tous les éléments de films
            film_elements = self.driver.find_elements(By.CSS_SELECTOR, "a.short-poster.img-box.with-mask")
            
            if not film_elements:
                print(f"❌ Aucun film trouvé sur la page {page_number}")
                return []
            
            films = []
            for element in film_elements:
                try:
                    # Extraire les données
                    href = element.get_attribute("href")
                    title = element.get_attribute("alt")
                    
                    # Image
                    img_element = element.find_element(By.TAG_NAME, "img")
                    img_src = img_element.get_attribute("src")
                    
                    # Score (optionnel)
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
    
    def scrape_multiple_pages(self, max_pages=5):
        """
        Scrape plusieurs pages consécutives
        
        Args:
            max_pages (int): Nombre maximum de pages à scraper
            
        Returns:
            list: Liste de tous les films trouvés
        """
        all_films = []
        
        for page_num in range(1, max_pages + 1):
            films = self.get_films_from_page(page_num)
            
            # Si aucun film trouvé, on arrête
            if not films:
                print(f"🛑 Arrêt du scraping à la page {page_num} (aucun film)")
                break
            
            all_films.extend(films)
            
            # Pause entre les pages pour ne pas surcharger le serveur
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
            
            # Retourner le HTML complet de la page
            return self.driver.page_source
            
        except Exception as e:
            print(f"❌ Erreur lors du chargement de la page: {e}")
            return None
    
    def close(self):
        """Ferme le driver Selenium"""
        if self.driver:
            self.driver.quit()
            print("🔒 Driver Selenium fermé")
