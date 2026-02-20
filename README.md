<div align="center">

![Scrapo Banner](./banner.svg)

# 🐸 Scrapo

### L'interface ultime pour découvrir films & séries

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-ready-brightgreen.svg)](https://www.docker.com/)

[Démo](#-aperçu) • [Installation](#-installation) • [Fonctionnalités](#-fonctionnalités) • [Configuration](#%EF%B8%8F-configuration)

</div>

---

## 📸 Aperçu

<div align="center">

![Scrapo Interface](https://img.shields.io/badge/Design-Modern%20%26%20Responsive-10b981?style=for-the-badge)

### Interface Moderne avec Animations Fluides

Découvrez films et séries avec une interface élégante aux couleurs **vert émeraude** (#10b981) et **bleu** (#2563eb), avec des **bulles animées** en arrière-plan pour une expérience visuelle unique.

</div>

### ✨ Points Forts du Design

- 🎨 **Thème moderne** : Palette de couleurs vert/bleu apaisante
- 🫧 **Animations fluides** : Bulles ondulantes en arrière-plan
- 🐸 **Branding unique** : Logo grenouille distinctif
- 🌙 **Mode sombre** : Optimisé pour le confort visuel
- 📱 **100% Responsive** : Parfait sur tous les écrans

---

## 🎬 Fonctionnalités

<table>
<tr>
<td width="50%">

### 🔍 Découverte
- **Tendances** en temps réel
- **Films populaires** et nouveautés
- **Séries** les plus regardées
- **À venir** : anticipez les sorties
- **Genres** : Action, Comédie, Drame, etc.

</td>
<td width="50%">

### 🔗 Intégrations
- **Jellyfin** : Voir votre bibliothèque
- **Jellyseerr** : Requêter du contenu
- **Streaming** : Liens directs
- **TMDb API** : Données à jour
- **Panier** : Sauvegardez vos favoris

</td>
</tr>
</table>

### 🎯 Fonctionnalités Détaillées

| Fonctionnalité | Description |
|---------------|-------------|
| 🔎 **Recherche Avancée** | Trouvez n'importe quel film ou série instantanément |
| 📚 **Bibliothèque Jellyfin** | Badge vert sur les contenus déjà dans votre bibliothèque |
| 📺 **Requêtes Jellyseerr** | Demandez du nouveau contenu en un clic |
| 🌐 **Sites de Streaming** | Liens vers des plateformes de streaming (configurable) |
| ❤️ **Panier de Favoris** | Sauvegardez vos découvertes pour plus tard |
| 🎭 **Filtres par Genre** | Action, Comédie, Drame, Horreur, Sci-Fi, Thriller |
| 🏢 **Filtres par Studio** | Disney, Warner, Marvel, Pixar, A24, etc. |
| 📡 **Filtres par Réseau** | Netflix, Disney+, Prime Video, Apple TV+, etc. |

---

## 🚀 Installation

### 🐋 Avec Docker (Recommandé)

```bash
# Cloner le repository
git clone https://github.com/votre-username/scrapo.git
cd scrapo

# Lancer avec Docker Compose
docker-compose up -d

# L'application sera accessible sur http://localhost:5000
```

### 🐍 Installation Manuelle

```bash
# Cloner le repository
git clone https://github.com/votre-username/scrapo.git
cd scrapo

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python app.py

# Accéder à http://localhost:5000
```

---

## ⚙️ Configuration

### 1️⃣ Interface de Configuration

Cliquez sur l'icône ⚙️ en haut à droite pour accéder aux paramètres.

### 2️⃣ Jellyfin (Optionnel)

Pour voir quels films/séries sont déjà dans votre bibliothèque :

```
URL : http://votre-serveur-jellyfin:8096
Clé API : Votre clé API Jellyfin
```

### 3️⃣ Jellyseerr (Optionnel)

Pour requêter du nouveau contenu :

```
URL : http://votre-serveur-jellyseerr:5055
Clé API : Votre clé API Jellyseerr
```

### 4️⃣ Site de Streaming

Configurez l'URL du site de streaming (par défaut : `https://fs12.lol`) :

```
URL : https://votre-site-streaming.com
```

> ⚠️ **Note** : Vous pouvez modifier cette URL à tout moment dans les paramètres.

---

## 🎨 Design & Thème

### Palette de Couleurs

```css
/* Primaire */
--vert-emeraude: #10b981
--bleu: #2563eb

/* Fond */
--bleu-fonce: #0a1929
--bleu-moyen: #0d2847

/* Texte */
--texte-clair: #e2e8f0
--texte-meta: #10b981
```

### Animations

- **Bulles flottantes** : 12 bulles bleues à 50% d'opacité avec mouvement ondulant
- **Transitions fluides** : 0.3s sur tous les éléments interactifs
- **Effets de survol** : Élévation et ombre colorée
- **Gradients dynamiques** : Sur les cartes de films

---

## 📁 Structure du Projet

```
scrapo/
├── 📄 app.py                    # Application Flask principale
├── 📄 requirements.txt          # Dépendances Python
├── 🐳 Dockerfile               # Image Docker
├── 🐳 docker-compose.yml       # Orchestration
├── 🎨 banner.svg               # Bannière du projet
│
├── 📂 static/
│   ├── style.css              # CSS avec thème vert/bleu
│   ├── app.js                 # JavaScript principal
│   ├── discover.js            # JS page découverte
│   └── favicon.svg            # Favicon grenouille
│
├── 📂 templates/
│   ├── index.html             # Page d'accueil
│   └── discover.html          # Page découverte
│
└── 📂 scraper/
    ├── __init__.py
    ├── selenium_scraper.py
    └── selenium_scraper_webdriver_manager.py
```

---

## 🛠️ Technologies

<div align="center">

| Backend | Frontend | APIs & Intégrations |
|---------|----------|---------------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) | ![TMDb](https://img.shields.io/badge/TMDb-01D277?style=for-the-badge&logo=themoviedatabase&logoColor=white) |
| ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) | ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) | ![Jellyfin](https://img.shields.io/badge/Jellyfin-00A4DC?style=for-the-badge&logo=jellyfin&logoColor=white) |
| ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) | ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) | Custom Streaming APIs |

</div>

---

## 📖 Utilisation

### Navigation Principale

1. **🏠 Page d'Accueil** : Découvrez les tendances et nouveautés
2. **🔍 Recherche** : Utilisez la barre de recherche pour trouver un titre spécifique
3. **📂 Genres** : Explorez par genre (Action, Comédie, etc.)
4. **🏢 Studios** : Filtrez par studio (Disney, Marvel, etc.)
5. **📡 Réseaux** : Naviguez par plateforme (Netflix, Disney+, etc.)

### Actions sur les Cartes

| Icône | Action | Description |
|-------|--------|-------------|
| ❤️ | Favoris | Ajouter au panier de favoris |
| 🔍 | Rechercher | Trouver des liens de téléchargement/streaming |
| ✓ | Badge Vert | Déjà dans votre bibliothèque Jellyfin |
| 🎬 | Badge Série | Indique qu'il s'agit d'une série |

### Panier de Favoris

Cliquez sur ❤️ en haut à droite pour :
- Voir tous vos favoris
- Rechercher des liens de streaming
- Gérer votre liste

---

## 🐸 À Propos

**Scrapo** est une interface moderne et intuitive pour découvrir et gérer votre collection de films et séries. Avec son design unique inspiré par une grenouille (symbole de transformation et d'agilité), Scrapo vous offre une expérience fluide et agréable.

### Pourquoi "Scrapo" ? 🐸

- **S**treaming
- **C**ontent
- **R**etrieval
- **A**nd
- **P**layback
- **O**rganizer

---

## 📝 Licence

Ce projet est fourni à des fins éducatives et personnelles.

---

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. 🍴 Fork le projet
2. 🔧 Créer une branche (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push vers la branche (`git push origin feature/AmazingFeature`)
5. 🎉 Ouvrir une Pull Request

---

## 💬 Support

Besoin d'aide ? Plusieurs options :

- 📧 Ouvrir une [issue](https://github.com/votre-username/scrapo/issues)
- 💬 Discussions dans la section [Discussions](https://github.com/votre-username/scrapo/discussions)
- 📖 Consulter la [documentation complète](./GUIDE-COMPLET.md)

---

<div align="center">

### 🐸 Fait avec ❤️ par la communauté

![Scrapo](https://img.shields.io/badge/Scrapo-Discover%20Movies%20%26%20Series-10b981?style=for-the-badge)

**Scrapo** - L'interface ultime pour découvrir films & séries ! 🎬

⭐ **Si vous aimez ce projet, n'oubliez pas de laisser une étoile !** ⭐

</div>
