# Hexo Theme CyberMind

Un thème Hexo moderne et professionnel pour blogs techniques, avec un design noir/orange inspiré du cyberpunk.

## Fonctionnalités

- ✨ Design moderne et responsive
- 🎨 Palette de couleurs personnalisée (noir/orange/ambre)
- 📱 Mobile-first et adaptatif
- 🔍 SEO optimisé
- 📝 Support complet Markdown
- 🎯 Catégories colorées
- 🏷️ Système de tags
- 📄 Pagination
- 💬 Support commentaires (optionnel)
- 🔗 Intégration réseaux sociaux
- 📧 Formulaire de contact (Formspree)
- 🎬 Intégration YouTube
- 🔧 Applications Streamlit intégrables
- 🚀 Performances optimisées

## Installation

### 1. Cloner le thème

```bash
cd your-hexo-blog
git clone https://github.com/votre-repo/hexo-theme-cybermind.git themes/cybermind
```

### 2. Activer le thème

Dans votre `_config.yml` racine :

```yaml
theme: cybermind
```

### 3. Installer les dépendances

```bash
npm install hexo-renderer-ejs --save
```

## Configuration

### Configuration du thème

Éditez `themes/cybermind/_config.yml` :

```yaml
# Menu
menu:
  Accueil: /
  Articles: /archives/
  Catégories: /categories/
  À propos: /about/
  Contact: /contact/

# Réseaux sociaux
social:
  email: contact@cybermind.fr
  website: https://cybermind.fr
  linkedin: https://linkedin.com
  github: https://github.com/username

# Section Hero
hero:
  badge: "📝 Blog • Articles • Réflexions"
  title: "Blog &<br><span class='highlight'>Publications</span><br>Techniques"
  subtitle: "Votre description..."
```

### Catégories avec couleurs

Les catégories suivantes sont préconfigurées avec leurs couleurs :

- `security` (🔐 Cybersécurité) - #00d4ff
- `kernel` (🐧 Linux Kernel) - #3b82f6
- `embedded` (⚙️ Systèmes Embarqués) - #9945ff
- `opensource` (📦 Open Source) - #10b981
- `iot` (📡 IoT & Réseau) - #8b5cf6
- `tutorials` (📝 Tutoriels) - #f59e0b

### Ajouter des catégories personnalisées

```yaml
categories:
  votre-categorie:
    name: "Nom affiché"
    icon: "🎯"
    color: "#hexcolor"
```

### Intégration Streamlit Apps

```yaml
apps:
  - name: "Mon Application"
    icon: "🔧"
    url: "https://mon-app.streamlit.app/"
    description: "Description de l'app..."
```

### Formulaire de contact (Formspree)

```yaml
contact:
  formspree_id: "votre_id_formspree"
  subjects:
    - value: "sujet-1"
      label: "Premier sujet"
    - value: "sujet-2"
      label: "Deuxième sujet"
```

## Création de contenu

### Nouvel article

```bash
hexo new post "Titre de l'article"
```

Front-matter recommandé :

```yaml
---
title: "Titre de l'article"
date: 2025-12-16 18:00:00
categories:
  - security
tags:
  - pentesting
  - web-security
description: "Description courte pour SEO"
thumbnail: "/images/article-thumbnail.jpg"
---
```

### Nouvelle page

```bash
hexo new page "about"
```

## Structure du projet

```
themes/cybermind/
├── _config.yml           # Configuration du thème
├── layout/
│   ├── layout.ejs        # Layout principal
│   ├── index.ejs         # Page d'accueil
│   ├── post.ejs          # Article individuel
│   ├── page.ejs          # Page statique
│   ├── archive.ejs       # Archives
│   ├── category.ejs      # Page de catégorie
│   └── partials/
│       ├── head.ejs      # <head> HTML
│       ├── meta.ejs      # Meta tags SEO
│       ├── header.ejs    # Navigation
│       ├── footer.ejs    # Footer
│       └── article.ejs   # Carte article
├── source/
│   ├── css/
│   │   └── style.css     # Styles principaux
│   └── js/
│       └── script.js     # Scripts
└── README.md
```

## Personnalisation CSS

Les variables CSS principales :

```css
:root {
    --bg-primary: #000000;
    --bg-secondary: #0a0a0f;
    --bg-tertiary: #111116;
    --accent-orange: #f97316;
    --accent-amber: #f59e0b;
    --accent-purple: #9945ff;
    --accent-cyan: #00d4ff;
    --text-primary: #e8e8ed;
    --text-secondary: #9898a6;
    --text-muted: #5a5a6e;
}
```

## Déploiement

### Générer le site

```bash
hexo clean
hexo generate
```

### Déployer

Configurez votre méthode de déploiement dans `_config.yml` :

```yaml
deploy:
  type: git
  repo: https://github.com/username/username.github.io.git
  branch: main
```

Puis :

```bash
hexo deploy
```

## Support et contributions

Pour signaler un bug ou proposer une amélioration :
- Issues: https://github.com/votre-repo/hexo-theme-cybermind/issues
- Pull requests bienvenues !

## Licence

MIT License - voir LICENSE pour plus de détails

## Crédits

- Polices : Space Grotesk & JetBrains Mono (Google Fonts)
- Thème créé pour CyberMind.fr
- Inspiré par le design cyberpunk moderne

## Changelog

### Version 1.0.0 (2025-12-16)
- Release initiale
- Support complet articles et pages
- Intégrations Streamlit et YouTube
- Formulaire de contact Formspree
- SEO optimisé
- Design responsive
