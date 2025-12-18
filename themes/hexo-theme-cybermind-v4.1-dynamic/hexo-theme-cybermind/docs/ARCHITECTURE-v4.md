# 🏗️ Architecture CyberMind Theme v4.0

## Vision

Transformer le thème en une **plateforme complète** avec :
- 📱 **Apps** — Démos interactives (Yi Jing, outils sécurité...)
- 💼 **Portfolio** — Réalisations clients (sites web, projets)
- 🖼️ **Gallery** — Galerie artistique (créations, photos, art IA)
- 📚 **Guides** — Documentation technique & tutoriels
- 🏪 **Showcase** — Vitrine style boutique (comme icieb.fr)

---

## 📁 Structure des dossiers

```
mon-blog-cybermind/
├── source/
│   ├── _posts/                    # Articles de blog (existant)
│   │
│   ├── services/                  # Pages services (existant)
│   │   ├── pentest/
│   │   ├── dev/
│   │   └── ...
│   │
│   ├── apps/                      # 📱 NOUVEAU - Applications
│   │   ├── index.md               # Page listing /apps/
│   │   ├── yi-jing-64-hexagrammes.md
│   │   ├── password-checker.md
│   │   └── poetry-generator.md
│   │
│   ├── portfolio/                 # 💼 NOUVEAU - Réalisations
│   │   ├── index.md               # Page listing /portfolio/
│   │   ├── clients/               # Sites clients
│   │   │   ├── ganimed.md
│   │   │   ├── icieb.md
│   │   │   └── association-cordeliers.md
│   │   ├── projects/              # Projets personnels
│   │   │   ├── cybermind-v1.md    # Ancienne version
│   │   │   ├── cybermind-v2.md
│   │   │   └── gk2net-historic.md
│   │   └── opensource/            # Contributions OSS
│   │       ├── linux-kernel.md
│   │       └── openwrt.md
│   │
│   ├── gallery/                   # 🖼️ NOUVEAU - Galerie
│   │   ├── index.md               # Page listing /gallery/
│   │   ├── art-ia/                # Créations IA
│   │   │   ├── cyberpunk-manga.md
│   │   │   └── synthwave-posters.md
│   │   ├── photos/                # Photographies
│   │   │   └── savoie-landscapes.md
│   │   └── music/                 # Musique (Suno)
│   │       └── french-poetry-songs.md
│   │
│   ├── guides/                    # 📚 NOUVEAU - Documentation
│   │   ├── index.md               # Page listing /guides/
│   │   ├── theme-installation.md
│   │   ├── theme-customization.md
│   │   └── changelog.md
│   │
│   └── showcase/                  # 🏪 NOUVEAU - Vitrine boutique
│       └── index.md               # Style icieb.fr
│
└── themes/
    └── cybermind/
        ├── layout/
        │   ├── app.ejs            # Layout single app
        │   ├── apps.ejs           # Layout listing apps
        │   ├── portfolio.ejs      # Layout single portfolio item
        │   ├── portfolio-index.ejs # Layout listing portfolio
        │   ├── gallery.ejs        # Layout galerie
        │   ├── gallery-item.ejs   # Layout single gallery item
        │   ├── guide.ejs          # Layout guide/doc
        │   └── showcase.ejs       # Layout vitrine boutique
        └── _config.yml
```

---

## 📝 Format Markdown unifié

### App (`source/apps/yi-jing-64-hexagrammes.md`)

```yaml
---
title: "64 Hexagrammes du Yi Jing"
layout: app
date: 2024-12-18
icon: ☯️
category: philosophy
tags:
  - yi-jing
  - animation
  - interactive

# Embedding
embed_url: "https://cybermind.fr/demos/64-hexagrammes-animation.html"
embed_height: 600

# Références croisées
related_article: "/2024/12/15/introduction-yi-jing/"
related_portfolio: "/portfolio/projects/yijing-oracle/"

# Métadonnées
featured: true
order: 1
status: active  # active | beta | deprecated
version: "2.1"

# SEO
description: "Animation interactive des 64 hexagrammes du Yi Jing"
thumbnail: /images/apps/yi-jing-thumb.jpg
---

## Description

Explorez les 64 hexagrammes du Livre des Mutations à travers 
cette animation interactive...

## Fonctionnalités

- Navigation intuitive entre hexagrammes
- Affichage des trigrammes composants
- Symbolique traditionnelle chinoise

## Utilisation

{% embed yi-jing-64-hexagrammes %}

## Changelog

- v2.1 : Ajout mode sombre
- v2.0 : Refonte complète
- v1.0 : Version initiale
```

---

### Portfolio Client (`source/portfolio/clients/ganimed.md`)

```yaml
---
title: "Ganimed.fr - Site Vitrine"
layout: portfolio
date: 2024-06-15
icon: 🌐
type: client  # client | project | opensource

# Client info
client:
  name: "Ganimed"
  logo: /images/portfolio/ganimed-logo.png
  sector: "Services"
  location: "Savoie, France"

# Projet
project:
  type: "Site vitrine responsive"
  technologies:
    - HTML5
    - CSS3
    - JavaScript
    - PHP
  duration: "3 semaines"
  year: 2024

# URLs
live_url: "https://ganimed.fr"
demo_url: "https://demo.cybermind.fr/ganimed/"
github_url: null  # Si opensource

# Visuels
thumbnail: /images/portfolio/ganimed-thumb.jpg
screenshots:
  - url: /images/portfolio/ganimed-home.jpg
    caption: "Page d'accueil"
  - url: /images/portfolio/ganimed-services.jpg
    caption: "Page services"
  - url: /images/portfolio/ganimed-mobile.jpg
    caption: "Version mobile"

# Avant/Après (optionnel)
before_after:
  before: /images/portfolio/ganimed-before.jpg
  after: /images/portfolio/ganimed-after.jpg

# Références
related_article: "/2024/06/20/creation-site-ganimed/"
testimonial:
  text: "Excellent travail, site livré dans les délais..."
  author: "Jean D., Gérant Ganimed"

# Métadonnées
featured: true
order: 1
status: live  # live | archived | demo
---

## Le Projet

Création d'un site vitrine moderne pour Ganimed...

## Objectifs

- Présenter les services
- Générer des contacts
- Optimisation SEO local

## Solutions apportées

...

## Résultats

- +150% de visibilité Google
- 50 demandes de contact/mois
```

---

### Gallery Item (`source/gallery/art-ia/cyberpunk-manga.md`)

```yaml
---
title: "Cyberpunk Manga - Série Philosophique"
layout: gallery-item
date: 2024-11-20
icon: 🎨
type: art-ia  # art-ia | photo | music | video

# Artwork info
artwork:
  medium: "IA Générative (Midjourney)"
  style: "Synthwave Cyberpunk Manga"
  dimensions: "1920x1080"
  license: "CC BY-NC 4.0"

# Images
images:
  - url: /images/gallery/cyberpunk-01.jpg
    title: "Le Penseur Digital"
    description: "Réflexion sur l'IA et la conscience"
  - url: /images/gallery/cyberpunk-02.jpg
    title: "Neon Philosophy"
    description: "Taoïsme dans la métropole"
  - url: /images/gallery/cyberpunk-03.jpg
    title: "Code & Méditation"
    description: "Hacker zen"

# Pour la musique
audio_url: null
spotify_url: null
youtube_url: null

# Achat/Contact
shop_url: null  # Lien boutique si disponible
price: null
available: true

# Références
related_article: "/2024/11/25/creation-art-ia-midjourney/"
related_music: "/gallery/music/synthwave-meditation/"

# Métadonnées
featured: true
tags:
  - cyberpunk
  - manga
  - philosophie
  - ia
---

## Concept

Cette série explore la fusion entre philosophie orientale 
et esthétique cyberpunk...

## Processus créatif

1. Conception des prompts
2. Génération Midjourney
3. Post-traitement
4. Composition finale

## Téléchargement

Disponible en haute résolution pour usage personnel.
```

---

## 🏷️ Tag d'Embedding

### Syntaxe dans les articles

```markdown
# Dans un article de blog

Voici une démonstration de l'application :

{% app yi-jing-64-hexagrammes %}

Ou avec options :

{% app yi-jing-64-hexagrammes height=400 %}

# Embedding portfolio
{% portfolio ganimed %}

# Embedding galerie
{% gallery cyberpunk-manga %}
```

### Helper Hexo (`scripts/embed-helper.js`)

```javascript
hexo.extend.tag.register('app', function(args) {
  const slug = args[0];
  const options = parseArgs(args.slice(1));
  const height = options.height || 500;
  
  const app = hexo.locals.get('pages').find(p => 
    p.layout === 'app' && p.slug === slug
  );
  
  if (!app) return `<!-- App not found: ${slug} -->`;
  
  return `
    <div class="embed-app" data-app="${slug}">
      <div class="embed-header">
        <span class="embed-icon">${app.icon || '🚀'}</span>
        <span class="embed-title">${app.title}</span>
        <a href="${app.embed_url}" target="_blank" class="embed-fullscreen">↗</a>
      </div>
      <iframe 
        src="${app.embed_url}?embedded=true" 
        height="${height}"
        loading="lazy"
        title="${app.title}">
      </iframe>
    </div>
  `;
});
```

---

## 🏪 Page Showcase (style icieb.fr)

### Layout boutique avec sections

```
┌─────────────────────────────────────────────────────────────┐
│  🏪 SHOWCASE - Réalisations & Services                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─── SITES WEB ───────────────────────────────────────┐   │
│  │  [ganimed.fr] [icieb.fr] [cordeliers] [+3 autres]   │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─── APPLICATIONS ────────────────────────────────────┐   │
│  │  [Yi Jing] [Password] [Poetry] [+2 autres]          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─── CRÉATIONS ARTISTIQUES ───────────────────────────┐   │
│  │  [Cyberpunk] [Photos] [Musique] [+5 autres]         │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─── OPEN SOURCE ─────────────────────────────────────┐   │
│  │  [Linux Kernel] [OpenWrt] [Armbian] [Theme Hexo]    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│            [💬 Demander un devis]                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Versioning du thème

### Fichier `CHANGELOG.md`

```markdown
# Changelog CyberMind Theme

## [4.0.0] - 2024-12-18

### Added
- 📱 Système Apps dynamique (layout app.ejs)
- 💼 Portfolio avec clients/projets/opensource
- 🖼️ Galerie artistique avec lightbox
- 📚 Section Guides & Documentation
- 🏪 Page Showcase style boutique
- 🏷️ Tags d'embedding {% app %} {% portfolio %}
- 🔗 Références croisées entre contenus

### Changed
- Refonte complète du footer avec liens GitHub
- Articles style fenêtre GUI
- Catégories groupées par contexte

### Fixed
- Menu mobile hamburger
- Responsive amélioré

## [3.0.0] - 2024-12-17
...
```

---

## 🐙 Structure GitHub

### Repository : `CyberMind-FR/hexo-theme-cybermind`

```
hexo-theme-cybermind/
├── README.md
├── LICENSE (MIT)
├── CHANGELOG.md
├── package.json
├── _config.yml
├── layout/
├── source/
│   ├── css/
│   ├── js/
│   └── images/
├── scripts/
│   └── embed-helper.js
├── docs/
│   ├── INSTALLATION.md
│   ├── CONFIGURATION.md
│   ├── APPS-GUIDE.md
│   ├── PORTFOLIO-GUIDE.md
│   └── GALLERY-GUIDE.md
└── examples/
    ├── _config.yml.example
    └── sample-content/
        ├── apps/
        ├── portfolio/
        └── gallery/
```

### Footer avec lien GitHub

```html
<footer>
  ...
  <div class="footer-theme">
    <a href="https://github.com/CyberMind-FR/hexo-theme-cybermind">
      🎨 Theme CyberMind v4.0
    </a>
    <span>•</span>
    <a href="https://github.com/CyberMind-FR/hexo-theme-cybermind/releases">
      📦 Releases
    </a>
  </div>
</footer>
```

---

## 🎯 Roadmap v4.0

### Phase 1 : Structure de base
- [ ] Créer layouts app.ejs, portfolio.ejs, gallery.ejs
- [ ] Créer pages index pour chaque section
- [ ] Implémenter tag {% embed %}

### Phase 2 : Contenu exemple
- [ ] Apps : Yi Jing, Password checker
- [ ] Portfolio : ganimed.fr, icieb.fr, cybermind v1
- [ ] Gallery : Art IA, Photos Savoie

### Phase 3 : Showcase
- [ ] Layout showcase.ejs style boutique
- [ ] Intégration formulaire devis
- [ ] Lightbox pour galerie

### Phase 4 : GitHub
- [ ] Créer repository public
- [ ] Documentation complète
- [ ] Release v4.0.0

---

## 💡 Avantages de cette architecture

| Aspect | Bénéfice |
|--------|----------|
| **Contenu dynamique** | Markdown → HTML automatique |
| **Références croisées** | App ↔ Article ↔ Portfolio |
| **SEO** | Pages dédiées indexables |
| **Maintenance** | Un fichier .md par item |
| **Extensible** | Nouveaux types facilement |
| **Partageable** | Thème GitHub réutilisable |
| **Professionnel** | Showcase clients impressionnant |
