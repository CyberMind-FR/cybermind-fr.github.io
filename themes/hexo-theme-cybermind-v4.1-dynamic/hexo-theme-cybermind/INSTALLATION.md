# Installation Rapide - Hexo Theme CyberMind

## Prérequis

- Node.js 14+ installé
- Hexo CLI installé globalement : `npm install -g hexo-cli`

## Installation

### 1. Créer un nouveau blog Hexo (si pas déjà fait)

```bash
hexo init mon-blog
cd mon-blog
npm install
```

### 2. Installer le thème CyberMind

```bash
# Depuis le dossier racine de votre blog
cd themes
git clone https://github.com/CyberMind-FR/hexo-theme-cybermind.git cybermind
cd ..
```

Ou télécharger et extraire le thème dans `themes/cybermind/`

### 3. Installer les dépendances nécessaires

```bash
npm install hexo-renderer-ejs --save
npm install hexo-generator-feed --save       # Optionnel - RSS
npm install hexo-generator-sitemap --save    # Optionnel - Sitemap
```

### 4. Configuration de base

Éditez `_config.yml` à la racine :

```yaml
# Site
title: Mon Blog Technique
subtitle: 'Articles & Tutoriels'
description: 'Votre description'
author: Votre Nom

# URL
url: https://votre-domaine.fr

# Theme
theme: cybermind

# Language
language: fr
timezone: 'Europe/Paris'
```

### 5. Configuration du thème

Copiez et éditez `themes/cybermind/_config.yml` :

```yaml
# Menu
menu:
  Accueil: /
  Articles: /archives/
  À propos: /about/

# Social
social:
  email: votre@email.fr
  website: https://votre-site.fr

# Contact (Formspree)
contact:
  formspree_id: votre_formspree_id
```

### 6. Créer vos premières pages

```bash
# Page À propos
hexo new page "about"

# Premier article
hexo new post "Mon premier article"
```

Éditez `source/about/index.md` :

```markdown
---
title: À propos
date: 2025-12-16
---

Bienvenue sur mon blog technique...
```

### 7. Tester localement

```bash
hexo clean
hexo generate
hexo server
```

Visitez : http://localhost:4000

### 8. Créer des articles avec catégories

Éditez vos articles dans `source/_posts/` :

```markdown
---
title: "Titre de l'article"
date: 2025-12-16 18:00:00
categories:
  - security
tags:
  - pentesting
  - web-security
---

Contenu de l'article...
```

### 9. Déploiement

#### GitHub Pages

1. Installez le déployeur :
```bash
npm install hexo-deployer-git --save
```

2. Configurez `_config.yml` :
```yaml
deploy:
  type: git
  repo: https://github.com/username/username.github.io.git
  branch: main
```

3. Déployez :
```bash
hexo clean && hexo deploy
```

#### Netlify / Vercel

Créez un fichier `netlify.toml` ou `vercel.json` à la racine et connectez votre repo.

## Personnalisation rapide

### Changer les couleurs

Éditez `themes/cybermind/source/css/style.css` :

```css
:root {
    --accent-orange: #votre-couleur;
    --accent-amber: #votre-couleur;
}
```

### Ajouter une catégorie

Dans `themes/cybermind/_config.yml` :

```yaml
categories:
  ma-categorie:
    name: "Ma Catégorie"
    icon: "🎯"
    color: "#3b82f6"
```

### Intégrer une application Streamlit

```yaml
apps:
  - name: "Mon App"
    icon: "🔧"
    url: "https://mon-app.streamlit.app/"
    description: "Description..."
```

## Commandes utiles

```bash
# Nouveau post
hexo new post "titre"

# Nouvelle page
hexo new page "nom-page"

# Nettoyer
hexo clean

# Générer
hexo generate
# ou
hexo g

# Serveur local
hexo server
# ou
hexo s

# Déployer
hexo deploy
# ou
hexo d

# Générer et déployer
hexo g -d
```

## Aide et Support

- Documentation complète : README.md
- Issues : https://github.com/CyberMind-FR/hexo-theme-cybermind/issues
- Documentation Hexo : https://hexo.io/docs/

## Troubleshooting

### Le thème ne s'applique pas

Vérifiez que :
1. Le dossier s'appelle bien `themes/cybermind`
2. `_config.yml` contient `theme: cybermind`
3. Vous avez fait `hexo clean` puis `hexo generate`

### Les styles ne s'affichent pas

Vérifiez que `hexo-renderer-ejs` est installé :
```bash
npm list hexo-renderer-ejs
```

Si non installé :
```bash
npm install hexo-renderer-ejs --save
```

### Erreur de rendu

```bash
hexo clean
rm -rf node_modules package-lock.json
npm install
hexo generate
```
