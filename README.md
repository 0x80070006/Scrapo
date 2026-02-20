# 🐸 Scrapo

L'interface ultime pour découvrir films & séries

## 🎬 Fonctionnalités

- **Découverte de contenu** : Parcourez les films et séries tendances, populaires et à venir
- **Recherche avancée** : Trouvez exactement ce que vous cherchez
- **Intégration Jellyfin** : Voyez ce qui est déjà dans votre bibliothèque
- **Intégration Jellyseerr** : Requêtez facilement du nouveau contenu
- **Streaming direct** : Liens vers des sites de streaming
- **Design moderne** : Interface élégante avec thème bleu/vert et animations de bulles
- **Responsive** : Fonctionne sur ordinateur, tablette et mobile

## 🚀 Installation

### Avec Docker (recommandé)

```bash
docker-compose up -d
```

L'application sera accessible sur `http://localhost:5000`

### Installation manuelle

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python app.py
```

## ⚙️ Configuration

### Jellyfin (optionnel)
1. Cliquez sur l'icône ⚙️ en haut à droite
2. Allez dans l'onglet "Jellyfin"
3. Entrez l'URL de votre serveur Jellyfin et votre clé API

### Jellyseerr (optionnel)
1. Cliquez sur l'icône ⚙️ en haut à droite
2. Allez dans l'onglet "Jellyseerr"
3. Entrez l'URL de votre instance Jellyseerr et votre clé API

### Site de streaming
1. Cliquez sur l'icône ⚙️ en haut à droite
2. Allez dans l'onglet "Site Streaming"
3. Configurez l'URL du site de streaming (par défaut: https://fs9.lol)

## 🎨 Design

Scrapo arbore un design moderne avec :
- Couleurs principales : Vert (#10b981) et Bleu (#2563eb)
- Fond animé avec des bulles remontant doucement
- Logo grenouille 🐸 pour un look unique et reconnaissable
- Interface sombre optimisée pour le visionnage
- Animations fluides et transitions douces

## 📚 Utilisation

1. **Navigation** : Explorez les différentes catégories sur la page d'accueil
2. **Recherche** : Utilisez la barre de recherche en haut pour trouver un titre spécifique
3. **Actions** :
   - ❤️ Ajouter aux favoris
   - ⬇️ Télécharger (lien streaming)
   - 📺 Requête Jellyseerr (si configuré)
4. **Panier** : Cliquez sur le ❤️ en haut à droite pour voir vos favoris

## 🛠️ Technologies

- **Backend** : Python / Flask
- **Frontend** : HTML5, CSS3, JavaScript (Vanilla)
- **API** : The Movie Database (TMDb)
- **Intégrations** : Jellyfin, Jellyseerr
- **Design** : CSS personnalisé avec animations

## 📝 Licence

Ce projet est fourni tel quel, à des fins éducatives et personnelles.

## 🐸 À propos

Scrapo - L'interface ultime pour découvrir et gérer vos films & séries !
