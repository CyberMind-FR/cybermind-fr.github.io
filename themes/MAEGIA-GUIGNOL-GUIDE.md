# 📦 Hexo Theme CyberMind v4.1 - Guide de mise à jour

## ✅ Corrections YAML

Les fichiers EJS problématiques ont été corrigés pour éviter les erreurs de parsing YAML :
- `apps.ejs` - Restructuré avec début `<%`
- `gallery.ejs` - Restructuré avec début `<%`
- `portfolio-index.ejs` - Restructuré avec début `<%`
- `archive.ejs`, `categories.ejs`, `contact.ejs`, `page.ejs`, `services.ejs`, `tags.ejs` - Ajout `<%/* Layout */%>`

## 🎭 Nouveau contenu : Maegia.tv

### Applications Streamlit

| Fichier | Application | URL |
|---------|-------------|-----|
| `apps/maegia/console-game.md` | 🎮 Console Game | game.maegia.tv |
| `apps/maegia/oracle-pali.md` | ☯️ Oracle Yi Jing | oracle.maegia.tv |
| `apps/maegia/kragzouy.md` | 🧙 Kragzouy | kragzouy.maegia.tv |
| `apps/maegia/landing-cybersecurity.md` | 🛡️ CyberSecurity | maegia.tv |
| `apps/maegia/creative-thinking.md` | 💡 Creative Thinking | www.maegia.tv |

## 🏛️ Nouveau contenu : Guignol.net Archives

### Sites historiques

| Fichier | Archive | Époque |
|---------|---------|--------|
| `portfolio/archives/gk2-net.md` | 🌐 GK2.NET (Premier ISP) | 1996 |
| `portfolio/archives/ganimed.md` | 💼 Ganimed.fr | 2010-2024 |
| `portfolio/archives/icieb.md` | 🏛️ ICIEB.fr | 2015-2021 |
| `portfolio/archives/kragzouy-blog.md` | 🧙 Kragzouy Blog | 1982-présent |
| `portfolio/archives/wengu-yijing.md` | ☯️ Wengu Yi Jing | 2000-2025 |
| `portfolio/archives/michel-murty.md` | 👤 Michel Murty | 2000-présent |

### Pages améliorées

| Fichier | Contenu |
|---------|---------|
| `pages/projets.md` | Page projets avec sections Maegia & Guignol |
| `pages/domaines-archives.md` | Cartographie complète de tous les domaines |

## 🚀 Installation

```bash
cd ~/CyberMindStudio/CyberMood/mon-blog-cybermind

# 1. SUPPRIMER l'ancien thème
rm -rf themes/cybermind

# 2. Extraire le nouveau
cd themes
tar -xzf hexo-theme-cybermind-v4.1-dynamic.tar.gz
mv hexo-theme-cybermind cybermind
cd ..

# 3. Copier les exemples
cp -r themes/cybermind/examples/apps/maegia source/apps/
cp -r themes/cybermind/examples/portfolio/archives source/portfolio/
cp themes/cybermind/examples/pages/domaines-archives.md source/pages/
cp themes/cybermind/examples/pages/projets.md source/pages/

# 4. Régénérer
rm -rf db.json public/
hexo clean && hexo generate && hexo server
```

## 📊 Structure finale

```
source/
├── apps/
│   ├── maegia/
│   │   ├── console-game.md      # 🎮 Game
│   │   ├── oracle-pali.md       # ☯️ Oracle
│   │   ├── kragzouy.md          # 🧙 Kragzouy
│   │   ├── landing-cybersecurity.md
│   │   └── creative-thinking.md
│   ├── pidebugger.md
│   ├── formes-sonores.md
│   └── index.md
├── portfolio/
│   ├── archives/
│   │   ├── gk2-net.md           # 🌐 1996
│   │   ├── ganimed.md           # 💼 Services
│   │   ├── wengu-yijing.md      # ☯️ Yi Jing
│   │   ├── kragzouy-blog.md     # 🧙 Créatif
│   │   └── ...
│   ├── armbian-wui.md
│   ├── enigmasuite.md
│   └── index.md
├── pages/
│   ├── projets.md               # Page projets améliorée
│   └── domaines-archives.md     # Cartographie domaines
└── ...
```

## 🔗 URLs résultantes

### Apps Maegia
- `/apps/maegia/console-game/` → 🎮 Jeu d'aventure
- `/apps/maegia/oracle-pali/` → ☯️ Oracle Yi Jing
- `/apps/maegia/kragzouy/` → 🧙 Univers créatif

### Portfolio Archives
- `/portfolio/archives/gk2-net/` → Premier ISP 1996
- `/portfolio/archives/wengu-yijing/` → Ressources Yi Jing
- `/portfolio/archives/kragzouy-blog/` → Blog depuis 1982

### Pages
- `/pages/projets/` → Vue d'ensemble projets
- `/pages/domaines-archives/` → Tous les domaines

## 📋 Domaines référencés

### Maegia.tv (6 sous-domaines)
- maegia.tv → Services CyberSecurity
- www.maegia.tv → Creative Thinking
- game.maegia.tv → Console Game
- oracle.maegia.tv → Oracle Yi Jing
- pali.maegia.tv → Oracle Pali
- kragzouy.maegia.tv → Univers Kragzouy

### Guignol.net (10 sous-domaines)
- gk2.guignol.net → Archive GK2.NET (1996)
- ganimed.guignol.net → Archive Ganimed
- gani.guignol.net → Alias Ganimed
- icieb.guignol.net → Archive ICIEB
- blog.guignol.net → Blog Kragzouy
- kragzouy.guignol.net → Univers Kragzouy
- michmur.guignol.net → Michel Murty
- wengu.guignol.net → Wengu Yi Jing
- yijing.guignol.net → Yi Jing Textes
- cybermood.guignol.net → Redirection CyberMind
