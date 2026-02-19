# 📝 Changelog - Scrapo

Toutes les modifications notables de ce projet seront documentées ici.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

---

## [5.0.0] - 2025-02-19

### 🎉 Version Majeure - Rebranding "Scrapo"

### ✨ Ajouté
- 🐸 **Nouveau nom** : "Film Scraper Ultimate" → "Scrapo"
- 🎨 **Bannière customisée** : Fond bleu + Texte vert + Logo grenouille
- 🏢 **11 Studios** : Disney, Marvel, Warner Bros, Universal, Paramount, Sony, Pixar, DreamWorks, DC, A24, 20th Century
- 📺 **6 Networks TV** : Netflix, Disney+, Amazon Prime, Hulu, Apple TV+, Peacock
- ♾️ **Scroll infini** : Chargement automatique des pages suivantes sur toutes les pages discover
- 🟢 **Détection Jellyfin** : Contour vert + pastille ✓ pour films déjà possédés
- 🔴 **Badge SÉRIE** : Badge rouge automatique sur toutes les séries TV
- ❤️ **Icônes discover** : Boutons cœur (panier) et loupe (recherche) sur pages discover
- 📊 **README GitHub** : Documentation complète avec logos, badges, et sections pliables

### 🔧 Amélioré
- ⚡ **Performance scroll** : Détection à 200px au lieu de 80% pour chargement plus fluide
- 🎯 **Backend dynamique** : Gestion automatique studios/networks via format `studio_ID` et `network_ID`
- 💅 **Design Jellyseerr** : Interface 100% fidèle à Jellyseerr avec 9 sections
- 🔍 **Recherche optimisée** : Extraction API plus rapide et fiable
- 📱 **Responsive** : Amélioration mobile et tablette

### 🐛 Corrigé
- ✅ Scroll infini qui ne chargeait pas les pages suivantes
- ✅ Icônes ❤️🔍 absentes sur pages discover
- ✅ Extraction newsId échouait avec certaines URLs (format `/{id}-title.html`)
- ✅ Section "Recent Requests" bugée (supprimée)
- ✅ Studios avec IDs incorrects (maintenant conformes TMDB)

### 🗑️ Supprimé
- ❌ Section "Recent Requests" (bugée et non pertinente)
- ❌ Ancien système studios avec noms (remplacé par IDs TMDB)

---

## [4.0.0] - 2025-02-09

### ✨ Ajouté
- 🎨 Interface Jellyseerr complète
- 🏠 Homepage avec carousels
- ⚙️ Panneau settings dual (Jellyfin + Jellyseerr)
- 🛒 Panier unifié
- 🔍 Panneau recherche dynamique
- 🌐 URL streaming configurable

---

## [3.0.0] - 2025-02-09

### ✨ Ajouté
- 🐳 Support Docker Compose
- 🔗 Intégration Jellyfin
- 🎯 Intégration Jellyseerr
- 🎬 Affichage bibliothèque Jellyfin
- 📥 Système téléchargement basique

---

## [2.0.0] - 2025-02-08

### ✨ Ajouté
- 🔍 Recherche films
- 📥 Extraction liens streaming
- 🎨 Interface web Flask

---

## [1.0.0] - 2025-02-07

### 🎉 Version Initiale
- 🤖 Scraper Selenium de base
- 📦 Extraction liens depuis site streaming
- 🐍 Backend Python Flask minimal

---

## 🔮 À Venir

### [5.1.0] - Authentification
- 🔐 Système login/password
- 👥 Multi-utilisateurs
- 🎫 Tokens JWT

### [5.2.0] - Multi-langues
- 🌍 Support EN, ES, DE
- 🇫🇷 Français par défaut
- 🔄 Switcher de langue

### [5.3.0] - Notifications
- 🔔 Discord webhooks
- 📱 Telegram bot
- 📧 Email SMTP

### [6.0.0] - IA & Automation
- 🤖 Téléchargement automatique
- 🧠 Recommandations IA
- 📊 Analytics avancées

---

## 📋 Format

### Types de changements
- `✨ Ajouté` : Nouvelles fonctionnalités
- `🔧 Amélioré` : Modifications de fonctionnalités existantes
- `🐛 Corrigé` : Corrections de bugs
- `🗑️ Supprimé` : Fonctionnalités retirées
- `🔒 Sécurité` : Corrections de vulnérabilités

---

**Légende des Emojis** :
🎉 Version majeure | ✨ Nouveau | 🔧 Amélioration | 🐛 Bug fix | 🗑️ Suppression | 🔒 Sécurité | 🐸 Scrapo | 🎬 Cinéma | 📺 TV | 🏢 Studios | 📊 Stats | 🌍 I18n | 🔔 Notifications | 🤖 IA | 🐳 Docker
