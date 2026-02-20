# 🐸 Guide de Démarrage Rapide - Scrapo

## 🎨 Nouveautés Design

Votre application Scrapo a été complètement relookée avec :
- ✅ Nouveau nom : **Scrapo** avec logo grenouille 🐸
- ✅ Thème vert/bleu moderne (#10b981 et #2563eb)
- ✅ Fond animé avec bulles remontant en arrière-plan
- ✅ Interface sombre optimisée
- ✅ Favicon grenouille
- ✅ Toutes vos fonctionnalités conservées !

## 🚀 Installation Rapide

### Option 1 : Docker (Recommandé)
```bash
# Extraire l'archive
unzip scrapo.zip
cd scrapo

# Lancer avec Docker
docker-compose up -d

# Accéder à l'application
# Ouvrir http://localhost:5000 dans votre navigateur
```

### Option 2 : Installation Manuelle
```bash
# Extraire l'archive
unzip scrapo.zip
cd scrapo

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python app.py

# Accéder à l'application
# Ouvrir http://localhost:5000 dans votre navigateur
```

## 🎬 Fonctionnalités Conservées

Toutes vos fonctionnalités sont toujours là :
- ✅ Découverte de films et séries (TMDb API)
- ✅ Recherche avancée
- ✅ Intégration Jellyfin
- ✅ Intégration Jellyseerr
- ✅ Liens streaming
- ✅ Panier de favoris
- ✅ Filtres par genre, studio, réseau

## ⚙️ Configuration

1. Cliquez sur l'icône ⚙️ en haut à droite
2. Configurez vos services (Jellyfin, Jellyseerr, streaming)
3. Tout est sauvegardé localement dans votre navigateur

## 🎨 Aperçu du Design

Ouvrez `preview.html` dans votre navigateur pour voir une démo du nouveau design !

## 📁 Structure du Projet

```
scrapo/
├── app.py                    # Application Flask principale
├── requirements.txt          # Dépendances Python
├── Dockerfile               # Configuration Docker
├── docker-compose.yml       # Orchestration Docker
├── banner.svg               # Bannière Scrapo
├── preview.html             # Aperçu du design
├── README.md                # Documentation
├── GUIDE-COMPLET.md         # Guide complet original
├── static/
│   ├── style.css            # CSS avec thème vert/bleu
│   ├── app.js               # JavaScript principal
│   ├── discover.js          # JavaScript page découverte
│   └── favicon.svg          # Favicon grenouille
├── templates/
│   ├── index.html           # Page d'accueil
│   └── discover.html        # Page découverte
└── scraper/
    └── ...                  # Modules de scraping
```

## 🐸 Profitez de Scrapo !

Votre nouvelle interface moderne est prête à l'emploi. Bon visionnage ! 🎬
