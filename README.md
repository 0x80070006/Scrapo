# 🎬 Film Scraper Ultimate

Interface web inspirée de **Jellyseerr** pour découvrir, rechercher et télécharger des films et séries depuis des sites de streaming français. S'intègre avec **Jellyfin** et **Jellyseerr** pour une expérience complète.

![Version](https://img.shields.io/badge/version-5.0-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-brightgreen.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📸 Aperçu

- **Interface moderne** style Jellyseerr avec thème sombre
- **9 sections** : Recently Added, Trending, Popular Movies, Genres, Studios, Networks
- **Scroll infini** sur toutes les pages discover
- **Détection Jellyfin** : contour vert pour les films déjà possédés
- **Badge SÉRIE** rouge automatique sur toutes les séries
- **Recherche & téléchargement** depuis sites streaming français
- **Panier unifié** pour gérer vos demandes

---

## ✨ Fonctionnalités

### 🎯 Découverte de Contenu
- **20+ catégories** : Trending, Popular, Upcoming, Genres films/séries
- **11 Studios** : Disney, Marvel, Warner Bros, Universal, Paramount, Sony, Pixar, DreamWorks, DC, A24, 20th Century
- **6 Networks TV** : Netflix, Disney+, Amazon Prime, Hulu, Apple TV+, Peacock
- **Scroll infini** : chargement automatique des pages suivantes
- **Badges visuels** : SÉRIE (rouge), Jellyfin (vert ✓)

### 🔍 Recherche & Téléchargement
- Recherche intelligente sur sites streaming français
- Extraction automatique des liens de téléchargement
- Formats multiples : TRUEFRENCH, FRENCH, VOSTFR
- Liens directs .mp4 prêts à télécharger

### 📦 Gestion de Panier
- Ajout de films/séries au panier en un clic
- Compteur dans le header
- Gestion complète (ajout, suppression, vidage)

### 🎨 Interface
- Design moderne inspiré de Jellyseerr
- Thème sombre optimisé pour les yeux
- Responsive et fluide
- Animations et transitions soignées

---

## 🚀 Installation

### Prérequis
- Docker & Docker Compose
- (Optionnel) Jellyfin installé et configuré
- (Optionnel) Jellyseerr installé et configuré

### Installation rapide avec Docker

```bash
# 1. Cloner le repo
git clone https://github.com/votre-username/film-scraper-ultimate.git
cd film-scraper-ultimate

# 2. Lancer l'application
docker-compose up -d

# 3. Accéder à l'interface
# Ouvrir http://localhost:5000
```

### Installation manuelle

```bash
# 1. Cloner le repo
git clone https://github.com/votre-username/film-scraper-ultimate.git
cd film-scraper-ultimate

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer l'application
python app.py

# 4. Accéder à l'interface
# Ouvrir http://localhost:5000
```

---

## ⚙️ Configuration

### 1. Jellyfin (Optionnel mais recommandé)

Permet d'afficher vos films possédés avec un contour vert :

```
URL     : http://192.168.1.100:8096
API Key : Paramètres > Tableau de bord > Clés API
```

**Avantages** :
- Section "Recently Added" avec vos derniers ajouts
- Contour vert sur les films déjà dans votre bibliothèque
- Évite les doublons

### 2. Jellyseerr (Requis)

Source de tous les films et séries affichés :

```
URL     : http://192.168.1.100:5055
API Key : Paramètres > Général > API Key
```

**Obligatoire pour** :
- Trending, Popular Movies, Popular Series
- Tous les genres, studios et networks
- Upcoming Movies

### 3. Site de Streaming (Optionnel)

Pour la recherche et le téléchargement :

```
URL par défaut : https://fs9.lol
```

Modifiable dans l'interface (⚙️ Settings)

---

## 📖 Utilisation

### Navigation

1. **Page d'accueil** : 9 sections avec aperçu
2. **"See More →"** : accès aux pages complètes avec scroll infini
3. **Hover sur film** : icônes ❤️ (panier) et 🔍 (recherche)
4. **Clic studio/network** : découvrir le contenu d'un studio/réseau TV

### Télécharger un Film

```
1. Rechercher le film (🔍 en haut)
2. Clic sur un résultat
3. Clic icône 📥
4. Choisir le format (TRUEFRENCH/FRENCH/VOSTFR)
5. Télécharger
```

### Ajouter au Panier

```
1. Hover sur un film
2. Clic sur ❤️
3. Gérer le panier via l'icône 🛒 dans le header
```

---

## 🏗️ Architecture

```
film-scraper-ultimate/
├── app.py                      # Backend Flask + API
├── templates/
│   ├── index.html              # Page d'accueil (9 sections)
│   └── discover.html           # Pages discover (scroll infini)
├── static/
│   ├── app.js                  # Logic homepage
│   ├── discover.js             # Logic scroll infini
│   └── style.css               # Styles (badges, contours)
├── scraper/
│   └── selenium_scraper.py     # Extraction liens streaming
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

### Endpoints API

```python
# Jellyfin
GET /api/jellyfin/movies                    # Liste films Jellyfin
POST /api/settings/jellyfin                 # Config Jellyfin

# Jellyseerr
GET /api/jellyseerr/trending                # Trending
GET /api/jellyseerr/movies                  # Popular Movies
GET /api/jellyseerr/category?category=X     # Catégorie spécifique
POST /api/settings/jellyseerr              # Config Jellyseerr

# Streaming
GET /api/search?q=X                         # Recherche film
GET /api/download-links?url=X               # Extraction liens
POST /api/settings/streaming               # Config site streaming

# Panier
GET /api/basket                             # Liste panier
POST /api/basket/add                        # Ajouter item
DELETE /api/basket/remove/<index>          # Supprimer item
POST /api/basket/clear                      # Vider panier
```

---

## 🎨 Personnalisation

### Modifier les Couleurs

Éditer `static/style.css` :

```css
:root {
    --bg-primary: #0f1419;      /* Fond principal */
    --bg-secondary: #1e293b;    /* Cartes */
    --text-primary: #e2e8f0;    /* Texte */
    --accent: #a78bfa;          /* Accent violet */
    --jellyfin: #10b981;        /* Vert Jellyfin */
    --serie: #ef4444;           /* Rouge série */
}
```

### Ajouter un Studio/Network

**Frontend** (`templates/index.html`) :
```html
<div class="genre-card" onclick="navigateToStudio(123)">Mon Studio</div>
```

**Backend** (automatique) :
```python
# Les studios/networks sont gérés dynamiquement
# Format : studio_123 → /api/v1/discover/movies/company/123
# Format : network_456 → /api/v1/discover/tv/network/456
```

**Titres** (`static/discover.js`) :
```javascript
const titles = {
    'studio_123': 'Mon Studio',
    'network_456': 'Mon Network'
};
```

---

## 🐛 Dépannage

### Le scroll infini ne fonctionne pas

**Symptômes** : Seulement 1-2 lignes de films, rien ne charge

**Solutions** :
1. Ouvrir Console (F12) et vérifier les logs :
   ```
   📥 Chargement page 1 pour movies
   ✅ 20 items reçus
   🔄 Scroll détecté - Chargement page 2  ← Doit apparaître
   ```
2. Vérifier que Jellyseerr est configuré
3. Tester manuellement : `/api/jellyseerr/category?category=movies&page=2`

### Pas de films affichés

**Causes possibles** :
- Jellyseerr non configuré ou URL incorrecte
- API Key invalide
- Jellyseerr non accessible depuis le container Docker

**Solution** :
```bash
# Tester depuis le container
docker exec -it film-scraper curl http://jellyseerr:5055/api/v1/discover/movies
```

### Icônes ❤️🔍 absentes

**Causes** :
- Film déjà sur Jellyfin (normal, contour vert = pas d'icônes)
- CSS non chargé

**Vérification** :
```javascript
// Console (F12)
// Hover sur carte → doit afficher :
<div class="card-overlay">
    <button class="card-btn">❤️</button>
    <button class="card-btn">🔍</button>
</div>
```

### Extraction liens échoue

**Symptômes** : "Aucun lien disponible"

**Solutions** :
1. Vérifier que le site streaming est accessible
2. Essayer un autre film (certains n'ont pas de liens)
3. Vérifier les logs Docker :
   ```bash
   docker-compose logs -f
   ```

---

## 🔒 Sécurité

⚠️ **Avertissements** :

1. **Usage personnel uniquement** : Cette application est conçue pour un usage privé
2. **Respect du droit d'auteur** : Assurez-vous d'avoir le droit de télécharger le contenu
3. **Site streaming** : La légalité dépend de votre juridiction
4. **Exposition réseau** : Ne pas exposer sur Internet sans authentification

**Recommandations** :
- Utiliser un VPN pour le téléchargement
- Héberger uniquement sur réseau local
- Changer les clés API par défaut
- Utiliser HTTPS en production

---

## 🛠️ Technologies

- **Backend** : Flask (Python 3.9+)
- **Frontend** : HTML5, CSS3, JavaScript ES6+
- **Scraping** : Selenium WebDriver
- **Container** : Docker & Docker Compose
- **API** : Jellyfin REST API, Jellyseerr REST API
- **Database** : TMDB (via Jellyseerr)

---

## 📋 Roadmap

- [ ] Authentification utilisateur
- [ ] Support multi-langues (EN, ES, DE)
- [ ] Notifications (Discord, Telegram)
- [ ] Historique des téléchargements
- [ ] Intégration Radarr/Sonarr
- [ ] Mode liste en plus du mode grille
- [ ] Filtres avancés (année, note, langue)
- [ ] Export liste panier (CSV, JSON)

---

## 🤝 Contribution

Les contributions sont les bienvenues !

1. **Fork** le projet
2. **Créer une branche** : `git checkout -b feature/AmazingFeature`
3. **Commit** : `git commit -m 'Add AmazingFeature'`
4. **Push** : `git push origin feature/AmazingFeature`
5. **Pull Request**

### Guidelines

- Code Python : suivre PEP 8
- Code JS : utiliser ES6+
- Commits : messages clairs en français ou anglais
- Tests : tester localement avec Docker

---

## 📄 License

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

## 🙏 Remerciements

- **Jellyseerr** : inspiration pour le design
- **Jellyfin** : intégration bibliothèque
- **TMDB** : base de données films/séries
- **Community** : retours et suggestions

---

## 📞 Contact

- **Issues** : [GitHub Issues](https://github.com/votre-username/film-scraper-ultimate/issues)
- **Discussions** : [GitHub Discussions](https://github.com/votre-username/film-scraper-ultimate/discussions)

---

## ⭐ Star History

Si ce projet vous a aidé, pensez à lui donner une ⭐ !

---

**Fait avec ❤️ pour la communauté française**
