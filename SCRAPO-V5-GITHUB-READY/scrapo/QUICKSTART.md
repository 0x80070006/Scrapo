# 🚀 Quickstart - Scrapo

Lancez Scrapo en **moins de 5 minutes** ! 🐸

---

## ⚡ Installation Express

### Option 1️⃣ : Docker (Recommandé)

```bash
# Cloner
git clone https://github.com/votre-username/scrapo.git
cd scrapo

# Lancer
docker-compose up -d

# Accéder
open http://localhost:5000
```

**C'est tout ! ✨**

---

### Option 2️⃣ : Installation Locale

```bash
# Cloner
git clone https://github.com/votre-username/scrapo.git
cd scrapo

# Installer
pip install -r requirements.txt

# Lancer
python app.py
```

---

## 🎯 Configuration Rapide

### 1. Jellyseerr (Requis)

```
http://localhost:5000 → ⚙️ Settings

Jellyseerr URL : http://192.168.1.100:5055
API Key        : [Votre clé API]
```

💡 **Où trouver l'API Key ?**  
Jellyseerr → Settings → General → API Key

---

### 2. Jellyfin (Optionnel)

```
Jellyfin URL : http://192.168.1.100:8096
API Key      : [Votre clé API]
```

💡 **Pourquoi configurer Jellyfin ?**
- Section "Recently Added"
- Contour vert sur films déjà possédés
- Évite les doublons

---

### 3. Site Streaming (Optionnel)

```
URL : https://fs9.lol (par défaut)
```

💡 **Pour quoi faire ?**
- Rechercher et télécharger films
- Formats : TRUEFRENCH / FRENCH / VOSTFR

---

## 🎬 Première Utilisation

### Découvrir des Films

```
1. Page d'accueil → 9 sections
2. Cliquer "See More →" sur n'importe quelle section
3. Scroller pour charger plus (scroll infini)
```

### Télécharger un Film

```
1. Cliquer 🔍 en haut à droite
2. Taper le nom du film
3. Cliquer sur un résultat
4. Cliquer 📥
5. Choisir TRUEFRENCH / FRENCH / VOSTFR
```

### Utiliser le Panier

```
1. Hover sur un film
2. Cliquer ❤️
3. Panier accessible via 🛒 (header)
```

---

## 🏢 Catégories Disponibles

### 🎬 Films
- Trending
- Popular Movies
- Upcoming Movies
- 6 Genres : Action, Comedy, Drama, Horror, Sci-Fi, Thriller
- 11 Studios : Disney, Marvel, Warner, Universal, Paramount, Sony, Pixar, DreamWorks, DC, A24, 20th Century

### 📺 Séries
- Popular Series
- 6 Genres : Action, Comedy, Drama, Sci-Fi, Mystery, Animation
- 6 Networks : Netflix, Disney+, Amazon Prime, Hulu, Apple TV+, Peacock

---

## 🐛 Problèmes Courants

### Pas de films affichés

```bash
# Vérifier Jellyseerr
curl http://localhost:5055/api/v1/discover/movies \
  -H "X-Api-Key: VOTRE_CLE"

# Si erreur → Vérifier URL et API Key dans Settings
```

### Scroll infini ne fonctionne pas

```
1. Ouvrir Console (F12)
2. Scroller vers le bas
3. Chercher log : "🔄 Scroll détecté - Chargement page 2"
4. Si absent → Vérifier configuration Jellyseerr
```

### Docker ne démarre pas

```bash
# Voir les logs
docker-compose logs -f

# Relancer
docker-compose down
docker-compose up --build
```

---

## 📚 Documentation Complète

- 📖 [README.md](README.md) - Documentation complète
- 📝 [CHANGELOG.md](CHANGELOG.md) - Historique versions
- 🔧 [GUIDE-COMPLET.md](GUIDE-COMPLET.md) - Guide technique

---

## 💬 Support

**Besoin d'aide ?**

- 🐛 [Issues GitHub](https://github.com/votre-username/scrapo/issues)
- 💬 [Discussions](https://github.com/votre-username/scrapo/discussions)
- 💬 [Discord](https://discord.gg/votre-serveur)

---

## ⭐ Prochaines Étapes

```
✅ Scrapo installé et configuré
✅ Films et séries affichés
✅ Téléchargement fonctionnel

Maintenant :
→ Explorez les studios (Marvel, Disney...)
→ Découvrez les networks (Netflix, Disney+...)
→ Ajoutez des films au panier
→ Téléchargez en TRUEFRENCH !
```

---

<div align="center">

**🐸 Scrapo bondit dans votre collection !**

Fait avec ❤️ pour la communauté française 🇫🇷

</div>
