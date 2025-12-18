# 📚 Architecture Blog CyberMind - Organisation par Sujets

## 🎯 Objectif

Organiser les articles par **dossiers thématiques** avec possibilité de les lier à des **apps**, **démos**, **services** ou **projets portfolio**.

---

## 📁 Structure des dossiers

```
source/
├── _posts/                    # Articles de blog (legacy, à migrer)
│
├── blog/                      # 📚 ARTICLES ORGANISÉS PAR SUJET
│   ├── index.md               # Page d'accueil blog avec navigation
│   │
│   ├── cybersecurity/         # 🛡️ Cybersécurité
│   │   ├── index.md           # Index catégorie + intro
│   │   ├── crowdsec-basics.md
│   │   ├── openwrt-firewall.md
│   │   └── pentest-methodology.md
│   │
│   ├── embedded/              # ⚙️ Systèmes embarqués
│   │   ├── index.md
│   │   ├── armbian-mochabin.md
│   │   ├── raspberry-pi-debug.md
│   │   └── uboot-customization.md
│   │
│   ├── linux/                 # 🐧 Linux & Open Source
│   │   ├── index.md
│   │   ├── kernel-drivers.md
│   │   ├── systemd-services.md
│   │   └── bash-scripting.md
│   │
│   ├── creative/              # 🎨 Créativité & Art Génératif
│   │   ├── index.md
│   │   ├── generative-geometry.md
│   │   ├── poetry-music-suno.md
│   │   └── sacred-geometry.md
│   │
│   ├── philosophy/            # 🧘 Philosophie & Yi Jing
│   │   ├── index.md
│   │   ├── yijing-intro.md
│   │   ├── critical-thinking.md
│   │   └── mood-philosophy.md
│   │
│   └── tutorials/             # 📖 Tutoriels & Guides
│       ├── index.md
│       ├── hexo-theme-setup.md
│       ├── streamlit-apps.md
│       └── svg-generation.md
│
├── apps/                      # 🚀 Applications (existant)
│   ├── tresse-lemniscate/
│   ├── yijing/
│   └── ...
│
├── services/                  # 🛡️ Services (existant)
│   ├── pentest/
│   ├── creative/
│   └── ...
│
├── portfolio/                 # 💼 Portfolio (existant)
│   ├── archives/
│   └── ...
│
└── demos/                     # 🎪 NOUVEAU - Démos interactives
    ├── index.md
    ├── crowdsec-dashboard/
    ├── geometry-playground/
    └── yijing-oracle/
```

---

## 📝 Front Matter Standardisé

### Article de blog avec liaisons

```yaml
---
title: "Générer des motifs géométriques avec A000940"
layout: post
date: 2025-01-15
updated: 2025-01-20

# Catégorisation
category: creative           # Dossier parent
subcategory: generative-art  # Sous-catégorie optionnelle
tags:
  - géométrie
  - mathématiques
  - canvas
  - javascript

# Métadonnées
author: G.Kerma
reading_time: 8              # Minutes estimées
difficulty: intermediate     # beginner, intermediate, advanced

# Description SEO
description: "Découvrez comment créer des motifs géométriques animés basés sur la suite mathématique A000940."
thumbnail: /images/blog/creative/a000940-cover.jpg

# 🔗 LIAISONS - Associer à des ressources
related_app: tresse-lemniscate           # Lien vers /apps/tresse-lemniscate/
related_service: creative                 # Lien vers /services/creative/
related_demo: geometry-playground         # Lien vers /demos/geometry-playground/
related_portfolio: ganimed                # Lien vers /portfolio/archives/ganimed/

# Articles connexes (slugs)
related_posts:
  - sacred-geometry
  - poetry-music-suno

# Ressources externes
external_links:
  - title: "OEIS A000940"
    url: "https://oeis.org/A000940"
  - title: "Code source GitHub"
    url: "https://github.com/CyberMind-FR/tresse-lemniscate"

# Série d'articles (optionnel)
series:
  name: "Art Génératif avec JavaScript"
  part: 2
  total: 5
---
```

### Index de catégorie (blog/creative/index.md)

```yaml
---
title: "🎨 Créativité & Art Génératif"
layout: category
category: creative
description: "Articles sur l'art génératif, la géométrie sacrée, la musique et la poésie."
icon: 🎨
color: "#ff6699"
order: 4

# Apps/Services liés à cette catégorie
featured_apps:
  - tresse-lemniscate
  - formes-sonores
featured_services:
  - creative
featured_demos:
  - geometry-playground

# Image de bannière
banner: /images/blog/creative/banner.jpg
---
```

---

## 🏷️ Système de Tags Hiérarchique

### Catégories principales (dossiers)

| Catégorie | Slug | Icône | Couleur |
|-----------|------|-------|---------|
| Cybersécurité | `cybersecurity` | 🛡️ | `#00ff88` |
| Embarqué | `embedded` | ⚙️ | `#ff6600` |
| Linux | `linux` | 🐧 | `#ffcc00` |
| Créativité | `creative` | 🎨 | `#ff6699` |
| Philosophie | `philosophy` | 🧘 | `#9966ff` |
| Tutoriels | `tutorials` | 📖 | `#66ccff` |

### Tags transversaux

```yaml
# Thèmes techniques
- crowdsec
- openwrt
- armbian
- raspberry-pi
- kernel
- systemd

# Thèmes créatifs
- géométrie
- musique
- poésie
- yi-jing

# Niveaux
- beginner
- intermediate
- advanced

# Types
- tutorial
- concept
- project
- review
```

---

## 🔗 Types de Liaisons

### 1. Article → App

```yaml
related_app: tresse-lemniscate
```

Affiche un encart "🚀 Essayer l'application" avec lien vers `/apps/tresse-lemniscate/`

### 2. Article → Service

```yaml
related_service: pentest
```

Affiche un encart "🛡️ Service associé" avec lien vers `/services/pentest/`

### 3. Article → Démo

```yaml
related_demo: crowdsec-dashboard
```

Affiche un encart "🎪 Démo interactive" avec iframe ou lien

### 4. Article → Portfolio

```yaml
related_portfolio: ganimed
```

Affiche un encart "💼 Projet associé" avec lien vers `/portfolio/archives/ganimed/`

### 5. Articles connexes

```yaml
related_posts:
  - sacred-geometry
  - poetry-music-suno
```

Affiche "📚 Articles connexes" en bas de page

---

## 📄 Layouts Hexo

### layout/post.ejs (Article)

```ejs
<article class="post">
  <header class="post-header">
    <div class="post-meta">
      <span class="category"><%= page.category %></span>
      <span class="date"><%= date(page.date, 'DD/MM/YYYY') %></span>
      <span class="reading-time"><%= page.reading_time %> min</span>
    </div>
    <h1><%= page.title %></h1>
  </header>

  <div class="post-content">
    <%- page.content %>
  </div>

  <!-- Liaisons -->
  <aside class="post-relations">
    <% if (page.related_app) { %>
    <div class="relation-card app">
      <span class="icon">🚀</span>
      <div>
        <strong>Application associée</strong>
        <a href="/apps/<%= page.related_app %>/">Essayer <%= page.related_app %></a>
      </div>
    </div>
    <% } %>

    <% if (page.related_service) { %>
    <div class="relation-card service">
      <span class="icon">🛡️</span>
      <div>
        <strong>Service professionnel</strong>
        <a href="/services/<%= page.related_service %>/">En savoir plus</a>
      </div>
    </div>
    <% } %>

    <% if (page.related_demo) { %>
    <div class="relation-card demo">
      <span class="icon">🎪</span>
      <div>
        <strong>Démo interactive</strong>
        <a href="/demos/<%= page.related_demo %>/">Tester la démo</a>
      </div>
    </div>
    <% } %>
  </aside>

  <!-- Articles connexes -->
  <% if (page.related_posts && page.related_posts.length) { %>
  <nav class="related-posts">
    <h3>📚 Articles connexes</h3>
    <ul>
      <% page.related_posts.forEach(function(slug) { %>
      <li><a href="/blog/<%= page.category %>/<%= slug %>/"><%= slug %></a></li>
      <% }); %>
    </ul>
  </nav>
  <% } %>
</article>
```

### layout/category.ejs (Index catégorie)

```ejs
<div class="category-page">
  <header class="category-header" style="--cat-color: <%= page.color %>">
    <span class="icon"><%= page.icon %></span>
    <h1><%= page.title %></h1>
    <p><%= page.description %></p>
  </header>

  <!-- Apps/Services liés -->
  <% if (page.featured_apps && page.featured_apps.length) { %>
  <section class="featured-resources">
    <h2>🚀 Applications</h2>
    <div class="resource-grid">
      <% page.featured_apps.forEach(function(app) { %>
      <a href="/apps/<%= app %>/" class="resource-card">
        <img src="/images/apps/<%= app %>.svg" alt="<%= app %>">
        <span><%= app %></span>
      </a>
      <% }); %>
    </div>
  </section>
  <% } %>

  <!-- Liste des articles -->
  <section class="article-list">
    <h2>📝 Articles</h2>
    <% site.posts.filter(p => p.category === page.category).sort('date', -1).each(function(post) { %>
    <article class="article-card">
      <a href="<%= url_for(post.path) %>">
        <h3><%= post.title %></h3>
        <p><%= post.description %></p>
        <div class="meta">
          <span><%= date(post.date, 'DD/MM/YYYY') %></span>
          <span><%= post.reading_time %> min</span>
        </div>
      </a>
    </article>
    <% }); %>
  </section>
</div>
```

---

## 🧭 Navigation

### Menu principal (config.yml)

```yaml
menu:
  Accueil: /
  Blog:
    _path: /blog/
    Cybersécurité: /blog/cybersecurity/
    Embarqué: /blog/embedded/
    Linux: /blog/linux/
    Créativité: /blog/creative/
    Philosophie: /blog/philosophy/
    Tutoriels: /blog/tutorials/
  Apps: /apps/
  Services: /services/
  Portfolio: /portfolio/
  Contact: /contact/
```

### Sidebar catégories (widget)

```ejs
<nav class="sidebar-categories">
  <h3>📁 Catégories</h3>
  <ul>
    <li><a href="/blog/cybersecurity/">🛡️ Cybersécurité</a></li>
    <li><a href="/blog/embedded/">⚙️ Embarqué</a></li>
    <li><a href="/blog/linux/">🐧 Linux</a></li>
    <li><a href="/blog/creative/">🎨 Créativité</a></li>
    <li><a href="/blog/philosophy/">🧘 Philosophie</a></li>
    <li><a href="/blog/tutorials/">📖 Tutoriels</a></li>
  </ul>
</nav>
```

---

## 📊 Exemples concrets

### Exemple 1 : Article Cybersécurité + Service

**Fichier** : `source/blog/cybersecurity/crowdsec-installation.md`

```yaml
---
title: "Installer CrowdSec sur OpenWrt"
layout: post
date: 2025-01-10
category: cybersecurity
tags: [crowdsec, openwrt, firewall, security]
reading_time: 12
difficulty: intermediate

related_service: pentest
related_demo: crowdsec-dashboard
related_posts:
  - openwrt-firewall
  - crowdsec-bouncer-setup
---

## Introduction

CrowdSec est un IPS collaboratif open source...

[Contenu de l'article]
```

### Exemple 2 : Article Créatif + App

**Fichier** : `source/blog/creative/generative-geometry.md`

```yaml
---
title: "Créer des motifs avec la suite A000940"
layout: post
date: 2025-01-15
category: creative
tags: [géométrie, mathématiques, canvas, art-génératif]
reading_time: 8
difficulty: intermediate

related_app: tresse-lemniscate
related_portfolio: ganimed
related_posts:
  - sacred-geometry
  - svg-export-tips
---

## La beauté des mathématiques

La suite A000940 de l'OEIS produit des motifs fascinants...

[Contenu de l'article]
```

### Exemple 3 : Tutoriel + Démo

**Fichier** : `source/blog/tutorials/hexo-theme-customization.md`

```yaml
---
title: "Personnaliser le thème Hexo CyberMind"
layout: post
date: 2025-01-20
category: tutorials
tags: [hexo, theme, css, javascript]
reading_time: 15
difficulty: beginner

series:
  name: "Maîtriser Hexo"
  part: 3
  total: 5

related_demo: theme-playground
external_links:
  - title: "Documentation Hexo"
    url: "https://hexo.io/docs/"
  - title: "GitHub du thème"
    url: "https://github.com/CyberMind-FR/hexo-theme-cybermind"
---
```

---

## 🚀 Migration depuis _posts/

### Script de migration

```bash
#!/bin/bash
# migrate-posts.sh - Migrer les anciens articles vers la nouvelle structure

SOURCE_DIR="source/_posts"
DEST_DIR="source/blog"

# Créer les dossiers de catégories
mkdir -p "$DEST_DIR"/{cybersecurity,embedded,linux,creative,philosophy,tutorials}

# Pour chaque article, détecter la catégorie et déplacer
for file in "$SOURCE_DIR"/*.md; do
  # Extraire la catégorie du front matter
  category=$(grep -m1 "^category:" "$file" | cut -d: -f2 | tr -d ' ')
  
  if [ -n "$category" ] && [ -d "$DEST_DIR/$category" ]; then
    cp "$file" "$DEST_DIR/$category/"
    echo "Migré: $(basename $file) → $category/"
  else
    echo "⚠️ Catégorie inconnue pour: $(basename $file)"
  fi
done
```

---

## 📈 Avantages de cette organisation

| Aspect | Bénéfice |
|--------|----------|
| **SEO** | URLs propres `/blog/cybersecurity/crowdsec-install/` |
| **Navigation** | Parcours thématique intuitif |
| **Maintenance** | Articles groupés par sujet |
| **Liaisons** | Connexions articles ↔ apps/services naturelles |
| **Découverte** | Articles connexes et ressources liées |
| **Séries** | Support des séries d'articles numérotées |
| **Extensibilité** | Nouvelles catégories faciles à ajouter |

---

## ✅ Checklist d'implémentation

1. [ ] Créer la structure de dossiers `source/blog/*/`
2. [ ] Créer les `index.md` pour chaque catégorie
3. [ ] Ajouter les layouts `post.ejs` et `category.ejs`
4. [ ] Configurer le menu dans `_config.yml`
5. [ ] Créer le widget sidebar catégories
6. [ ] Migrer les articles existants
7. [ ] Créer le dossier `source/demos/`
8. [ ] Ajouter les styles CSS pour les cartes de liaison
9. [ ] Tester les permalinks et la navigation
10. [ ] Mettre à jour le sitemap

---

*Architecture proposée par CyberMind - Décembre 2025*
