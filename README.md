<div align="center">

<!-- TITRE PRINCIPAL avec fond bleu + texte vert + grenouille -->
<img src="https://img.shields.io/badge/🐸_SCRAPO-33FF66?style=for-the-badge&labelColor=1565C0&color=1565C0&label=%F0%9F%90%B8+SCRAPO" height="50" alt="Scrapo"/>

<br/>

<!-- SVG custom : SCRAPO fond bleu texte vert avec grenouille -->
<img src="https://img.shields.io/badge/%F0%9F%90%B8%20SCRAPO-brightgreen?style=for-the-badge&color=1A56DB&labelColor=1A56DB&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMiAzMiI+PHRleHQgeT0iMjQiIGZvbnQtc2l6ZT0iMjQiPvCfkLg8L3RleHQ+PC9zdmc+" height="0"/>

<!-- Titre visuel SVG fait main : fond bleu, texte vert, grenouille -->
<svg width="400" height="80" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="80" rx="12" fill="#1A56DB"/>
  <text x="200" y="52" font-family="Arial Black, Arial" font-size="38" font-weight="900" fill="#22C55E" text-anchor="middle" letter-spacing="4">🐸 SCRAPO</text>
</svg>

**Client Jellyfin musical · Style Spotify · Sombre & Violet**

<br/>

<!-- BADGES PRINCIPAUX -->
[![Version](https://img.shields.io/badge/version-1.0.0--demo-22C55E?style=flat-square&logo=github&logoColor=white)](../../releases)
[![Statut](https://img.shields.io/badge/statut-en%20développement-orange?style=flat-square&logo=github-actions&logoColor=white)](../../releases)
[![Flutter](https://img.shields.io/badge/Flutter-3.16+-02569B?style=flat-square&logo=flutter&logoColor=white)](https://flutter.dev)
[![Android](https://img.shields.io/badge/Android-5.0%2B-3DDC84?style=flat-square&logo=android&logoColor=white)](../../releases)
[![Jellyfin](https://img.shields.io/badge/Jellyfin-10.8%2B-00A4DC?style=flat-square&logo=jellyfin&logoColor=white)](https://jellyfin.org)
[![Licence MIT](https://img.shields.io/badge/licence-MIT-blue?style=flat-square&logo=opensourceinitiative&logoColor=white)](LICENSE)

<br/>

<!-- STATS REPO -->
![GitHub stars](https://img.shields.io/github/stars/TONUSER/scrapo?style=flat-square&logo=github&color=yellow)
![GitHub forks](https://img.shields.io/github/forks/TONUSER/scrapo?style=flat-square&logo=github&color=blue)
![GitHub issues](https://img.shields.io/github/issues/TONUSER/scrapo?style=flat-square&logo=github&color=red)
![GitHub last commit](https://img.shields.io/github/last-commit/TONUSER/scrapo?style=flat-square&logo=github)

</div>

---

> [!WARNING]
> **🚧 VERSION DÉMO — EN DÉVELOPPEMENT ACTIF 🚧**
>
> Scrapo est actuellement en phase de démonstration. Le code source est disponible pour compiler vous-même l'application.  
> Les binaires précompilés **(APK Android & EXE Windows)** arrivent prochainement dans les [**Releases**](../../releases). 🐸

---

<br/>

## 📸 Aperçu

<div align="center">

| 🔐 Connexion | 🏠 Accueil | 🎧 Lecteur |
|:---:|:---:|:---:|
| <img src="https://placehold.co/160x290/0D0D1A/22C55E?text=%F0%9F%90%B8+Login%0A%0ADEMO&font=roboto" width="150"/> | <img src="https://placehold.co/160x290/0D0D1A/1A56DB?text=%F0%9F%90%B8+Accueil%0A%0ADEMO&font=roboto" width="150"/> | <img src="https://placehold.co/160x290/1A0533/22C55E?text=%F0%9F%90%B8+Player%0A%0ADEMO&font=roboto" width="150"/> |

| 🔍 Recherche | 📚 Bibliothèque | 🎶 Playlists |
|:---:|:---:|:---:|
| <img src="https://placehold.co/160x290/0D0D1A/22C55E?text=%F0%9F%90%B8+Search%0A%0ADEMO&font=roboto" width="150"/> | <img src="https://placehold.co/160x290/0D0D1A/1A56DB?text=%F0%9F%90%B8+Biblio%0A%0ADEMO&font=roboto" width="150"/> | <img src="https://placehold.co/160x290/0D0D1A/22C55E?text=%F0%9F%90%B8+Playlist%0A%0ADEMO&font=roboto" width="150"/> |

*📸 Captures d'écran réelles à venir lors de la première release officielle*

</div>

<br/>

---

## 📦 Téléchargement

<div align="center">

| Plateforme | Statut | Action |
|:---:|:---:|:---:|
| 📱 **Android APK** | ![soon](https://img.shields.io/badge/🔜-Bientôt-1A56DB?style=flat-square) | [Voir les Releases](../../releases) |
| 🖥️ **Windows EXE** | ![wip](https://img.shields.io/badge/🛠️-En%20développement-orange?style=flat-square) | — |
| 🍎 **iOS / macOS** | ![planned](https://img.shields.io/badge/📋-Prévu-grey?style=flat-square) | — |

</div>

> 💡 En attendant, compilez l'APK vous-même en 3 commandes → [voir ici](#-compiler-lapk-soi-même)

<br/>

---

## ✨ Fonctionnalités

<table>
<tr>
<td valign="top" width="50%">

### 🔐 Connexion & Session
- Saisie libre de l'adresse IP, port, login/mdp
- Session persistante (reconnexion automatique)
- Déconnexion propre depuis le profil

### 🎧 Lecture audio
- Streaming direct depuis votre serveur Jellyfin
- Play / Pause / Suivant / Précédent
- Barre de progression interactive et draggable
- Répétition : off / tout / titre en cours
- Lecture aléatoire (shuffle)

### 📻 Mini-player
- Toujours visible en bas pendant la navigation
- Contrôles complets sans quitter l'écran

</td>
<td valign="top" width="50%">

### 🏠 Navigation style Spotify
- Accueil : albums récents & derniers ajouts
- Recherche temps réel (titres, albums, artistes)
- Bibliothèque : Artistes · Albums · Favoris
- Vue artiste avec discographie complète
- Vue album avec tracklist numérotée

### 🎶 Playlists locales
- Créer, renommer, supprimer
- Ajouter / retirer des titres
- Réorganiser par glisser-déposer
- Lecture depuis n'importe quelle position

### ❤️ Favoris
- Synchronisés directement avec Jellyfin
- Accessibles depuis la bibliothèque

</td>
</tr>
</table>

<br/>

---

## 🎨 Design

Thème **100% sombre** avec dégradés bleu/violet :

<div align="center">

| Rôle | Aperçu | Code hex |
|------|:------:|----------|
| Fond principal | ![#080812](https://img.shields.io/badge/-%20-080812?style=flat-square) | `#080812` |
| Accent violet | ![#7B2FBE](https://img.shields.io/badge/-%20-7B2FBE?style=flat-square) | `#7B2FBE` |
| Accent bleu | ![#4A90D9](https://img.shields.io/badge/-%20-4A90D9?style=flat-square) | `#4A90D9` |
| Surfaces | ![#12122A](https://img.shields.io/badge/-%20-12122A?style=flat-square) | `#12122A` |
| Texte secondaire | ![#8888AA](https://img.shields.io/badge/-%20-8888AA?style=flat-square) | `#8888AA` |

</div>

<br/>

---

## 🚀 Compiler l'APK soi-même

### Prérequis

[![Flutter](https://img.shields.io/badge/Flutter%20SDK-3.0+-02569B?style=flat-square&logo=flutter)](https://flutter.dev/docs/get-started/install)
[![Android SDK](https://img.shields.io/badge/Android%20SDK-API%2021+-3DDC84?style=flat-square&logo=android)](https://developer.android.com/studio)
[![Java](https://img.shields.io/badge/Java-11+-ED8B00?style=flat-square&logo=openjdk&logoColor=white)](https://adoptium.net)

### En 3 commandes

```bash
# 1. Installer les dépendances
flutter pub get

# 2. Compiler l'APK release
flutter build apk --release

# ✅ L'APK est prêt ici :
#    build/app/outputs/flutter-apk/app-release.apk
```

> **Mode debug** (plus rapide, pas besoin de signature) :
> ```bash
> flutter build apk --debug
> ```

### Installer sur Android

```bash
# Via ADB (câble USB + debug USB activé)
adb install build/app/outputs/flutter-apk/app-release.apk
```

Ou copiez le fichier `.apk` directement sur le téléphone et installez-le  
*(activer "Sources inconnues" dans Paramètres → Sécurité)*

<br/>

---

## ☁️ Compiler via GitHub Actions

> Pas Flutter sur votre machine ? Pas de problème. Forkez le repo et créez ce fichier :

**`.github/workflows/build.yml`**

```yaml
name: 🐸 Build Scrapo APK

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  build-android:
    name: Build APK Android
    runs-on: ubuntu-latest

    steps:
      - name: 📥 Checkout
        uses: actions/checkout@v4

      - name: 🐦 Setup Flutter
        uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.16.0'
          channel: 'stable'

      - name: 📦 Installer les dépendances
        run: flutter pub get

      - name: 🔨 Compiler l'APK
        run: flutter build apk --release

      - name: 📤 Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: scrapo-apk
          path: build/app/outputs/flutter-apk/app-release.apk
          retention-days: 30
```

L'APK sera disponible dans **Actions → votre workflow → Artifacts**.

<br/>

---

## 📁 Structure du projet

```
scrapo/
├── 📄 pubspec.yaml                        # Dépendances Flutter
├── lib/
│   ├── 📄 main.dart                       # Point d'entrée & thème global
│   │
│   ├── models/
│   │   └── 📄 media_item_model.dart       # Modèle de données unifié
│   │
│   ├── services/
│   │   ├── 📄 jellyfin_service.dart       # API Jellyfin (auth, stream, search…)
│   │   ├── 📄 player_service.dart         # Lecteur audio (just_audio)
│   │   └── 📄 playlist_service.dart       # Playlists locales (SharedPreferences)
│   │
│   ├── screens/
│   │   ├── 📄 login_screen.dart           # Écran de connexion
│   │   ├── 📄 home_screen.dart            # Navigation principale (BottomNav)
│   │   ├── 📄 home_tab.dart               # Onglet Accueil
│   │   ├── 📄 library_screen.dart         # Bibliothèque + ArtistScreen
│   │   ├── 📄 search_screen.dart          # Recherche temps réel
│   │   ├── 📄 playlists_screen.dart       # Playlists + PlaylistDetailScreen
│   │   ├── 📄 album_screen.dart           # Vue album avec tracklist
│   │   └── 📄 player_screen.dart          # Lecteur plein écran
│   │
│   └── widgets/
│       ├── 📄 mini_player.dart            # Barre de lecture persistante
│       ├── 📄 album_card.dart             # Carte album (grille / liste)
│       └── 📄 track_tile.dart             # Ligne de piste + menu contextuel
│
└── android/
    └── app/
        ├── 📄 build.gradle                # Configuration build Android
        └── src/main/
            ├── 📄 AndroidManifest.xml     # Permissions & déclaration d'activité
            └── kotlin/…/MainActivity.kt
```

<br/>

---

## ⚙️ Configuration Jellyfin

```
✅  Jellyfin Server v10.8 ou supérieur
✅  Bibliothèque musicale configurée
✅  Accessible en HTTP (local) ou HTTPS (distant)
```

**Format de l'adresse :**
```
Local   →  http://192.168.1.42:8096
Distant →  https://jellyfin.mondomaine.com
```
> ⚠️ Ne pas mettre de `/` à la fin de l'URL

<br/>

---

## 🗺️ Roadmap

| # | Fonctionnalité | Statut |
|---|----------------|:------:|
| ✅ | Authentification Jellyfin | Fait |
| ✅ | Streaming audio natif | Fait |
| ✅ | Navigation 4 onglets (Accueil / Recherche / Biblio / Playlists) | Fait |
| ✅ | Lecteur plein écran style Spotify | Fait |
| ✅ | Mini-player persistant | Fait |
| ✅ | Playlists locales (CRUD + réorganisation) | Fait |
| ✅ | Favoris synchronisés Jellyfin | Fait |
| 🔜 | **APK release publique** | Bientôt |
| 🛠️ | **Version Windows EXE** | En cours |
| 📋 | File d'attente éditable | Prévu |
| 📋 | Paroles synchronisées (LRC) | Prévu |
| 📋 | Widget Android (écran verrouillé) | Prévu |
| 📋 | Égaliseur audio | Prévu |
| 📋 | Thèmes de couleur personnalisables | Prévu |

<br/>

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! 🐸

```bash
# 1. Forkez le projet sur GitHub
# 2. Créez votre branche
git checkout -b feature/ma-super-fonctionnalite

# 3. Committez vos changements
git commit -m "feat: ajout de X"

# 4. Poussez
git push origin feature/ma-super-fonctionnalite

# 5. Ouvrez une Pull Request 🎉
```

Pour signaler un bug ou proposer une idée → [**Ouvrir une Issue**](../../issues) 🐛

<br/>

---

## 📄 Licence

Ce projet est distribué sous licence **MIT** — voir [LICENSE](LICENSE) pour les détails.

[![Licence MIT](https://img.shields.io/badge/Licence-MIT-blue?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)

<br/>

---

<div align="center">

🐸 Fait avec amour, Flutter et caféine

Propulsé par [**Jellyfin**](https://jellyfin.org) · Inspiré de [**Spotify**](https://spotify.com)

*Scrapo n'est pas affilié à Jellyfin ni à Spotify.*

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-TONUSER%2Fscrapo-181717?style=flat-square&logo=github)](../../)
[![Issues](https://img.shields.io/badge/Issues-Signaler%20un%20bug-red?style=flat-square&logo=github)](../../issues)
[![Pull Requests](https://img.shields.io/badge/PR-Contribuer-22C55E?style=flat-square&logo=github)](../../pulls)

</div>
