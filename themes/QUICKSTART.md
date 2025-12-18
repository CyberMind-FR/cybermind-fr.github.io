# 🚀 CyberMind Theme v4.1 - Quick Start

## Installation

```bash
cd mon-blog-hexo
rm -rf themes/cybermind
cd themes && tar -xzf hexo-theme-cybermind-v4.1-dynamic.tar.gz
mv hexo-theme-cybermind cybermind
cd ..
```

## Configuration minimale

Éditez `themes/cybermind/_config.yml` :

```yaml
branding:
  logo_text: "MonSite_"

hero:
  title: "Mon<br><span class='highlight'>Super</span><br>Site"
  subtitle: "Ma description"

social:
  github: "https://github.com/moi"
  email: "contact@monsite.fr"

about:
  name: "Mon Nom"
  title: "Mon Métier"
```

## Créer du contenu

### Service (`source/services/dev.md`)
```yaml
---
title: "Développement"
layout: service
icon: 💻
description: "Services de dev"
order: 1
tags: [dev, web]
---
```

### App (`source/apps/mon-app.md`)
```yaml
---
title: "Mon App"
layout: app
icon: 🚀
embed_url: "https://..."
category: tools
---
```

### Portfolio (`source/portfolio/client-x.md`)
```yaml
---
title: "Client X"
layout: portfolio
type: client
thumbnail: /images/client-x.jpg
---
```

## Lancer

```bash
hexo clean && hexo server
# http://localhost:4000
```

## Mode jour/nuit

Le switch est automatiquement dans le header. Pour changer le mode par défaut :

```yaml
theme:
  default_mode: light  # ou dark
```
