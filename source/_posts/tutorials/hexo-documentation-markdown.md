---
title: Documentation Hexo - Guide Markdown Complet pour CyberMind
date: 2025-12-12 08:00:00
updated: 2025-12-12 08:00:00
category: tutoriels
tags:
excerpt: Guide de référence complet pour la rédaction d'articles Hexo sur CyberMind.FR. Front-matter YAML, syntaxe Markdown, Tag Plugins, gestion des assets et bonnes pratiques.
comments: true
lang: fr
---
# 📚 Documentation Hexo - Guide Markdown Complet

> Guide de référence rapide pour la rédaction d'articles sur **CyberMind.FR**
> 
> Auteur: Gandalf @ CyberMind  
> Dernière mise à jour: 2025-12-12

<!-- more -->

---

## 📑 Table des matières

1. [Structure d'un article](#1-structure-dun-article)
2. [Front-matter (métadonnées YAML)](#2-front-matter-metadonnees-yaml)
3. [Syntaxe Markdown](#3-syntaxe-markdown)
4. [Tag Plugins Hexo](#4-tag-plugins-hexo)
5. [Gestion des assets (images, fichiers)](#5-gestion-des-assets)
6. [Commandes Hexo](#6-commandes-hexo)
7. [Bonnes pratiques](#7-bonnes-pratiques)
8. [Templates d'articles](#8-templates-darticles)

---

## 1. Structure d'un article

Un article Hexo est composé de deux parties :

```markdown
---
# Front-matter (métadonnées YAML)
title: Mon titre d'article
date: 2025-12-12 10:30:00
---

# Contenu de l'article en Markdown

Votre texte ici...
```

### Emplacements des fichiers

| Type | Dossier | Description |
|------|---------|-------------|
| **Posts** | `source/_posts/` | Articles publiés |
| **Drafts** | `source/_drafts/` | Brouillons (non publiés) |
| **Pages** | `source/` | Pages statiques (about, contact...) |

---

## 2. Front-matter (métadonnées YAML)

Le front-matter est un bloc YAML au début du fichier, délimité par `---`.

### 2.1 Template complet

```yaml
---
title: Titre de l'Article
date: 2025-12-12 14:30:00
updated: 2025-12-12 16:00:00
categories:
  - Catégorie Principale
  - Sous-catégorie
tags:
  - Tag1
  - Tag2
  - Tag3
layout: post
comments: true
permalink: custom-url/
excerpt: Description courte de l'article pour les previews et le SEO (150-200 caractères).
published: true
lang: fr
disableNunjucks: false
---
```

### 2.2 Variables détaillées

| Variable | Type | Défaut | Description |
|----------|------|--------|-------------|
| `title` | String | Nom du fichier | Titre affiché |
| `date` | DateTime | Date création | Date de publication |
| `updated` | DateTime | Date modif | Dernière mise à jour |
| `tags` | Liste | - | Tags de l'article |
| `categories` | Liste | - | Catégories hiérarchiques |
| `layout` | String | `post` | Template utilisé |
| `comments` | Boolean | `true` | Commentaires activés |
| `permalink` | String | Auto | URL personnalisée |
| `excerpt` | String | - | Extrait pour les listes |
| `disableNunjucks` | Boolean | `false` | Désactive les tag plugins |
| `published` | Boolean | `true` | Article publié |
| `lang` | String | Config | Langue (fr, en...) |

### 2.3 Catégories CyberMind.FR

```yaml
# Catégories principales du site
categories:
  - Cyber              # Cybersécurité, hacking éthique
  - Mind               # Réflexions, philosophie, psychologie
  - Mood               # Bien-être, lifestyle, spiritualité
  - Tutoriels          # Guides techniques
  - Hardware           # Matériel, embedded, ARM
  - Poèmes             # Créations poétiques
  - FabLab             # Fabrication, DIY, laser
  - Nouvelles          # Récits, histoires
  - Histoire           # Histoire, patrimoine
  - Intelligence Artificielle  # IA, LLM, ChatGPT
  - Network            # Réseau, DNS, VPN
  - Engineering        # DevOps, Fullstack
  - contrib            # Contributions, fiches
```

### 2.4 Catégories hiérarchiques

```yaml
# Simple - Une seule catégorie
categories:
  - Cyber

# Hiérarchie - Chemin de sous-catégories
categories:
  - Tutoriels
  - Embedded-Systems
  - Development

# Multiples hiérarchies indépendantes
categories:
  - [Tutoriels, Embedded-Systems, ARM64]
  - [Hardware, Projets-DIY]
```

### 2.5 Format JSON alternatif

```json
"title": "Mon Article",
"date": "2025-12-12 14:30:00",
"tags": ["Cyber", "OpenWrt"],
"categories": ["Tutoriels"]
;;;
```

---

## 3. Syntaxe Markdown

### 3.1 Titres

```markdown
# Titre H1
## Titre H2
### Titre H3
#### Titre H4
##### Titre H5
###### Titre H6
```

### 3.2 Formatage du texte

| Syntaxe | Résultat |
|---------|----------|
| `**gras**` | **gras** |
| `*italique*` | *italique* |
| `***gras italique***` | ***gras italique*** |
| `~~barré~~` | ~~barré~~ |
| `` `code` `` | `code` |

### 3.3 Citations

```markdown
> Citation simple

> Citation sur
> plusieurs lignes

> Citation niveau 1
>> Citation imbriquée niveau 2
```

### 3.4 Listes

```markdown
# Liste non ordonnée
- Élément 1
- Élément 2
  - Sous-élément 2.1
  - Sous-élément 2.2
- Élément 3

# Liste ordonnée
1. Premier
2. Deuxième
3. Troisième

# Liste de tâches
- [x] Tâche terminée
- [ ] Tâche à faire
- [ ] Autre tâche
```

### 3.5 Liens

```markdown
# Lien simple
[Texte du lien](https://cybermind.fr)

# Lien avec titre (tooltip)
[CyberMind](https://cybermind.fr "Site officiel CyberMind")

# Lien référence
[Texte][ref1]
[ref1]: https://cybermind.fr "Référence"

# Lien email
<info@cybermind.fr>

# Lien automatique
<https://cybermind.fr>
```

### 3.6 Images

```markdown
# Image simple
![Texte alternatif](/uploads/images/photo.jpg)

# Image avec titre
![Logo CyberMind](/uploads/images/avatar.jpg "Logo officiel")

# Image cliquable
[![Alt](image.jpg)](https://cybermind.fr)

# Image avec dimensions (certains renderers)
![Alt](image.jpg =400x300)
```

### 3.7 Code

````markdown
# Code inline
Utilisez la commande `hexo new post "titre"`

# Bloc de code simple
```
Code sans coloration
```

# Bloc avec langage
```python
def hello():
    print("Hello CyberMind!")
    return True
```

# Bloc avec nom de fichier
```javascript app.js
const express = require('express');
const app = express();
app.listen(3000);
```

# Langages supportés
```bash
```python
```javascript
```yaml
```json
```html
```css
```sql
```c
```cpp
```java
```go
```rust
```
````

### 3.8 Tableaux

```markdown
| Colonne 1 | Colonne 2 | Colonne 3 |
|-----------|:---------:|----------:|
| Gauche    | Centre    | Droite    |
| Texte     | Texte     | Texte     |
| Données   | Données   | Données   |
```

Alignement :
- `:---` = gauche
- `:---:` = centre
- `---:` = droite

### 3.9 Séparateurs et divers

```markdown
---
# Ligne horizontale (trois tirets)

***
# Ligne horizontale alternative

<!-- more -->
# Séparateur "Lire la suite" (crucial pour Hexo!)

<!-- Commentaire HTML invisible -->

\*Texte échappé\*
# Affiche: *Texte échappé*
```

### 3.10 Notes de bas de page

```markdown
Voici un texte avec une note[^1] et une autre[^note].

[^1]: Première note de bas de page.
[^note]: Deuxième note avec identifiant texte.
```

### 3.11 Emojis

```markdown
# Emojis Unicode directs
🔐 🧠 ✨ 📜 🚀 ⚙️ 🛠️ 📚 🎵 🌐

# Shortcodes (si plugin installé)
:rocket: :lock: :book:
```

---

## 4. Tag Plugins Hexo

Les tag plugins sont des extensions Hexo avec la syntaxe `{% tag %}`.

⚠️ **Important**: Ne jamais mixer tag plugins et syntaxe Markdown !  
❌ `[Lien]({% post_path article %})` → Ne fonctionne PAS

### 4.1 Citations (Blockquote)

```nunjucks
{% blockquote %}
Citation simple sans attribution.
{% endblockquote %}

{% blockquote Auteur %}
Citation avec auteur.
{% endblockquote %}

{% blockquote Auteur, Titre de l'œuvre %}
Citation avec auteur et source.
{% endblockquote %}

{% blockquote @CyberMindFR https://twitter.com/CyberMindFR %}
Citation depuis Twitter.
{% endblockquote %}

{% blockquote Seth Godin https://seths.blog Seth's Blog %}
Citation depuis un blog avec lien.
{% endblockquote %}
```

### 4.2 Blocs de code avancés

```nunjucks
{% codeblock %}
Code sans options
{% endcodeblock %}

{% codeblock lang:python %}
def example():
    return "Hello"
{% endcodeblock %}

{% codeblock script.py lang:python %}
# Avec nom de fichier affiché
print("CyberMind")
{% endcodeblock %}

{% codeblock lang:python line_number:false %}
# Sans numéros de ligne
code here
{% endcodeblock %}

{% codeblock lang:python mark:2,5-7 %}
# Ligne 1
# Ligne 2 - SURLIGNÉE
# Ligne 3
# Ligne 4
# Ligne 5 - SURLIGNÉE
# Ligne 6 - SURLIGNÉE
# Ligne 7 - SURLIGNÉE
# Ligne 8
{% endcodeblock %}

{% codeblock Titre https://cybermind.fr Lien %}
# Avec titre et lien source
{% endcodeblock %}
```

### 4.3 Inclure du code externe

```nunjucks
# Fichier complet
{% include_code scripts/example.py %}

# Avec titre et langage
{% include_code Mon Script lang:python scripts/example.py %}

# Lignes spécifiques
{% include_code lang:python from:5 to:15 scripts/example.py %}

# Depuis une ligne jusqu'à la fin
{% include_code lang:bash from:10 scripts/setup.sh %}
```

> 📁 Les fichiers doivent être dans `source/downloads/code/`

### 4.4 Liens vers d'autres articles

```nunjucks
# Lien avec titre automatique de l'article
{% post_link mon-autre-article %}

# Lien avec texte personnalisé
{% post_link mon-autre-article "Cliquez ici pour voir l'article" %}

# Sans échappement HTML du titre
{% post_link mon-autre-article "Titre <em>stylé</em>" false %}

# Obtenir juste le chemin (sans lien)
{% post_path mon-autre-article %}
```

### 4.5 Images et assets

```nunjucks
# Image depuis le dossier asset du post
{% asset_img image.png %}

# Avec titre
{% asset_img image.png "Titre de l'image" %}

# Avec alt et title
{% asset_img image.png "Title text" "Alt text" %}

# Avec classes CSS et dimensions
{% asset_img classe1 classe2 image.png 400 300 "Title" "Alt" %}

# Chemin vers un asset (retourne l'URL)
{% asset_path document.pdf %}

# Lien vers un asset
{% asset_link document.pdf "Télécharger le PDF" %}

# Lien sans échappement
{% asset_link document.pdf "Doc <strong>important</strong>" false %}
```

### 4.6 Vidéos intégrées

```nunjucks
# YouTube (juste l'ID de la vidéo)
{% youtube dQw4w9WgXcQ %}

# YouTube avec type (video ou playlist)
{% youtube PLplaylist123 'playlist' %}

# Vimeo
{% vimeo 123456789 %}

# Vimeo avec dimensions
{% vimeo 123456789 640 480 %}
```

### 4.7 URLs et liens

```nunjucks
# URL avec préfixe racine du site
{% url_for /about/ %}
# Résultat: /about/

# URL absolue complète
{% full_url_for /about/ %}
# Résultat: https://cybermind.fr/about/

# Lien externe avec target="_blank"
{% link CyberMind https://cybermind.fr %}

# Lien externe avec titre
{% link "Voir le site" https://cybermind.fr %}
```

### 4.8 Extrait d'article (crucial!)

```markdown
Introduction de l'article qui apparaît dans les listes,
sur la page d'accueil et dans les flux RSS.

Vous pouvez mettre plusieurs paragraphes ici.

<!-- more -->

⬆️ Tout ce qui est AU-DESSUS de <!-- more --> = extrait
⬇️ Tout ce qui est EN-DESSOUS = visible uniquement sur la page complète

Suite détaillée de l'article...
```

### 4.9 Gist GitHub

```nunjucks
# Gist complet
{% gist abc123def456 %}

# Fichier spécifique d'un gist
{% gist abc123def456 example.py %}
```

### 4.10 jsFiddle / CodePen

```nunjucks
# jsFiddle
{% jsfiddle username/fiddle_id %}
{% jsfiddle username/fiddle_id js,html,css %}
{% jsfiddle username/fiddle_id js,html,css dark %}

# iframe générique
{% iframe https://codepen.io/user/pen/xyz 100% 400 %}
```

### 4.11 Images simples

```nunjucks
# Image avec classes et dimensions
{% img [class1 class2] /path/to/image.jpg [width] [height] '"title" "alt"' %}

# Exemples
{% img /images/photo.jpg %}
{% img center /images/photo.jpg 400 300 %}
{% img /images/photo.jpg '"Mon titre" "Description"' %}
```

### 4.12 Raw (contenu non traité)

```nunjucks
{% raw %}
Ce contenu ne sera PAS traité par Nunjucks.
Les {{ variables }} et {% tags %} restent tels quels.
{% endraw %}
```

---

## 5. Gestion des assets

### 5.1 Méthode 1: Dossier global

Structure:
```
source/
├── images/
│   ├── logo.png
│   └── photos/
│       └── photo1.jpg
├── uploads/
│   ├── images/
│   │   └── avatar.jpg
│   └── documents/
│       └── guide.pdf
└── _posts/
    └── mon-article.md
```

Utilisation:
```markdown
![Logo](/images/logo.png)
![Photo](/images/photos/photo1.jpg)
![Avatar](/uploads/images/avatar.jpg)
[PDF](/uploads/documents/guide.pdf)
```

### 5.2 Méthode 2: Dossier par article (recommandé)

Configuration `_config.yml`:
```yaml
post_asset_folder: true
```

Structure créée automatiquement:
```
source/_posts/
├── mon-super-article.md
└── mon-super-article/        # Créé automatiquement
    ├── screenshot.png
    ├── diagram.svg
    └── data.json
```

Utilisation avec tag plugins:
```nunjucks
{% asset_img screenshot.png "Capture d'écran" %}
{% asset_link data.json "Données JSON" %}
{% asset_path diagram.svg %}
```

### 5.3 Méthode 3: Markdown natif avec hexo-renderer-marked 3.1+

Configuration `_config.yml`:
```yaml
post_asset_folder: true
marked:
  prependRoot: true
  postAsset: true
```

Utilisation Markdown standard:
```markdown
![Screenshot](screenshot.png)
![Diagram](diagram.svg "Mon diagramme")
```

### 5.4 Plugin hexo-asset-link

Installation:
```bash
npm install hexo-asset-link --save
```

Permet la syntaxe avec chemin relatif:
```markdown
![Alt](./mon-article/image.png "Title")
![Alt](mon-article/image.png)
[Document](./mon-article/doc.pdf)
```

✅ Compatible avec la prévisualisation VS Code et autres éditeurs Markdown.

---

## 6. Commandes Hexo

### 6.1 Créer du contenu

```bash
# Nouveau post (article publié)
hexo new "Mon Titre d'Article"
hexo new post "Mon Titre"
hexo n "Mon Titre"

# Nouveau brouillon
hexo new draft "Mon Brouillon"

# Nouvelle page statique
hexo new page "about"
hexo new page "contact"

# Avec un layout personnalisé
hexo new photo "Ma Galerie"

# Publier un brouillon (déplace vers _posts)
hexo publish "Mon Brouillon"
hexo publish draft "Mon Brouillon"
```

### 6.2 Générer le site

```bash
# Générer les fichiers statiques
hexo generate
hexo g

# Générer en mode watch (surveille les changements)
hexo generate --watch
hexo g -w

# Générer seulement les fichiers modifiés
hexo generate --bail

# Forcer la régénération complète
hexo clean && hexo generate
```

### 6.3 Prévisualisation locale

```bash
# Démarrer le serveur local
hexo server
hexo s

# Serveur sur un port spécifique
hexo server -p 4001

# Serveur avec les brouillons visibles
hexo server --draft
hexo s -d

# Serveur avec IP personnalisée
hexo server -i 192.168.1.100

# Mode statique (depuis public/)
hexo server -s
```

### 6.4 Déploiement

```bash
# Déployer vers le serveur configuré
hexo deploy
hexo d

# Générer ET déployer
hexo generate --deploy
hexo g -d
hexo d -g
```

### 6.5 Nettoyage et maintenance

```bash
# Nettoyer le cache et les fichiers générés
hexo clean

# Lister les routes générées
hexo list post
hexo list page
hexo list route
hexo list tag
hexo list category

# Afficher la configuration
hexo config

# Mode debug
hexo --debug
hexo s --debug
```

### 6.6 Workflow typique

```bash
# 1. Créer un brouillon
hexo new draft "Nouvel Article"

# 2. Éditer le fichier source/_drafts/nouvel-article.md

# 3. Prévisualiser avec brouillons
hexo s --draft

# 4. Publier le brouillon
hexo publish "Nouvel Article"

# 5. Générer et déployer
hexo clean && hexo g -d
```

---

## 7. Bonnes pratiques

### 7.1 Nommage des fichiers

```bash
# ✅ Recommandé: kebab-case
mon-super-article.md
tutoriel-openwrt-2025.md
guide-armbian-espressobin.md

# ❌ À éviter
Mon Super Article.md
mon_super_article.md
MonSuperArticle.md
```

Configuration pour nommage automatique (`_config.yml`):
```yaml
# Format: année-mois-jour-titre.md
new_post_name: :year-:month-:day-:title.md

# Ou juste le titre
new_post_name: :title.md
```

Placeholders disponibles:
- `:title` - Titre (slugifié)
- `:year` - Année (4 chiffres)
- `:month` - Mois (2 chiffres)
- `:day` - Jour (2 chiffres)
- `:i_month` - Mois sans zéro
- `:i_day` - Jour sans zéro

### 7.2 Structure de catégories CyberMind

```yaml
# Catégorie principale seule
categories:
  - Cyber

# Avec sous-catégorie
categories:
  - Cyber
  - Mood

# Chemin hiérarchique complet
categories:
  - Tutoriels
  - Embedded-Systems
  - Development
  - Cartes
```

### 7.3 Tags efficaces

```yaml
tags:
  # Technologies
  - OpenWrt
  - ARM64
  - Python
  - Linux
  
  # Outils
  - CrowdSec
  - Armbian
  - Docker
  
  # Types de contenu
  - Tutorial
  - Guide
  - Fiche
  
  # Thèmes
  - Cybersécurité
  - Embedded
  - Poésie
```

### 7.4 Excerpts optimisés pour SEO

```yaml
---
title: Mon Article
excerpt: Description concise et accrocheuse de 150-160 caractères pour un affichage optimal dans les résultats de recherche et les previews sociaux.
---
```

Alternative dans le contenu:
```markdown
Première phrase accrocheuse qui résume l'essentiel de l'article.
Cette introduction apparaîtra dans les listes et flux RSS.

<!-- more -->

Contenu détaillé qui n'apparaît que sur la page complète...
```

### 7.5 Images optimisées

| Critère | Recommandation |
|---------|----------------|
| **Format** | WebP ou JPEG (photos), PNG (captures, schémas) |
| **Largeur max** | 1920px |
| **Poids** | < 200KB idéalement |
| **Nommage** | `description-YYYY-MM.ext` |
| **Alt text** | Toujours renseigner |

### 7.6 Accessibilité

```markdown
# ✅ Bon
![Schéma d'architecture réseau montrant les flux entre le firewall et les serveurs](/images/architecture.png "Architecture réseau CyberMind")

# ❌ À éviter
![](/images/img1.png)
![image](image.png)
```

---

## 8. Templates d'articles

### 8.1 Template Article Technique

```markdown
---
title: Titre du Tutoriel Technique
date: 2025-12-12 10:00:00
updated: 2025-12-12 10:00:00
categories:
  - Tutoriels
  - Catégorie-Technique
tags:
  - Tag1
  - Tag2
  - Tag3
excerpt: Description courte du tutoriel (150-200 caractères) pour le SEO et les previews.
comments: true
lang: fr
---

# 🚀 Titre du Tutoriel

## 📖 Introduction

Présentation du contexte et objectifs du tutoriel.

<!-- more -->

## 🔧 Prérequis

- Prérequis 1
- Prérequis 2
- Prérequis 3

## 📦 Installation

```bash
# Commandes d'installation
sudo apt update
sudo apt install package
```

## ⚙️ Configuration

Explication de la configuration...

```yaml
# Fichier de configuration
option1: valeur1
option2: valeur2
```

## 🧪 Test

Comment vérifier que tout fonctionne...

## 🐛 Dépannage

| Problème | Solution |
|----------|----------|
| Erreur X | Faire Y |
| Erreur Z | Faire W |

## 📚 Ressources

- [Lien 1](https://example.com)
- [Lien 2](https://example.com)

---

*Article mis à jour le 2025-12-12*
```

### 8.2 Template Article Poétique

```markdown
---
title: Titre du Poème
date: 2025-12-12 20:00:00
categories:
  - Poèmes
tags:
  - Poésie
  - Thème1
  - Thème2
excerpt: Première ligne ou description courte du poème.
comments: true
lang: fr
---

# Titre du Poème

*Sous-titre ou dédicace*

<!-- more -->

---

*Couplet 1*

Premier vers du poème  
Deuxième vers avec rime  
Troisième vers qui s'exprime  
Quatrième vers qui aime

*Refrain*

Vers du refrain répété  
Avec sa mélodie...

*Couplet 2*

Suite du poème...

---

🎵 *Écoutez ce poème en chanson sur [Suno](https://suno.ai)*

📅 *Écrit le 12 décembre 2025*
```

### 8.3 Template Fiche Technique

```markdown
---
title: Fiche - Nom du Sujet
date: 2025-12-12 09:00:00
updated: 2025-12-12 09:00:00
categories:
  - contrib
  - Fiches
tags:
  - Fiche
  - Tag1
  - Tag2
excerpt: Fiche de référence rapide sur le sujet X.
comments: true
lang: fr
---

# 📋 Fiche - Nom du Sujet

## 🎯 Objectif

Description de l'objectif en une phrase.

<!-- more -->

## 📊 Caractéristiques

| Paramètre | Valeur |
|-----------|--------|
| Param 1 | Valeur 1 |
| Param 2 | Valeur 2 |
| Param 3 | Valeur 3 |

## 🔧 Configuration rapide

```bash
# Commande principale
commande --option valeur
```

## ⚠️ Points d'attention

- Point important 1
- Point important 2
- Point important 3

## 🔗 Liens utiles

- [Documentation officielle](https://example.com)
- [Article connexe](https://cybermind.fr/article)

---

*Fiche créée le 2025-12-12*
```

### 8.4 Template Article Projet/Hardware

```markdown
---
title: Nom du Projet - Version X.X
date: 2025-12-12 14:00:00
updated: 2025-12-12 14:00:00
categories:
  - Hardware
  - Projets-DIY
tags:
  - Projet
  - Hardware
  - DIY
  - Tag-Spécifique
excerpt: Description courte du projet hardware et ses fonctionnalités principales.
comments: true
lang: fr
---

# 🔧 Nom du Projet vX.X

> 🎯 **Résumé**: Description en une ligne du projet.

<!-- more -->

## 📸 Aperçu

{% asset_img projet-photo.jpg "Photo du projet assemblé" %}

## 🎯 Fonctionnalités

- ✅ Fonctionnalité 1
- ✅ Fonctionnalité 2
- ✅ Fonctionnalité 3
- 🔄 En développement: Fonctionnalité 4

## 📦 Matériel requis

| Composant | Quantité | Prix approx. |
|-----------|----------|--------------|
| Composant 1 | 1 | 10€ |
| Composant 2 | 2 | 5€ |
| **Total** | - | **~15€** |

## 🔌 Schéma de câblage

```
┌─────────────┐     ┌─────────────┐
│ Composant A │────▶│ Composant B │
└─────────────┘     └─────────────┘
        │
        ▼
┌─────────────┐
│ Composant C │
└─────────────┘
```

## 🛠️ Assemblage

### Étape 1: Préparation

Instructions...

### Étape 2: Câblage

Instructions...

### Étape 3: Test

Instructions...

## 💻 Code source

```python
# Code principal
def main():
    print("Projet CyberMind")
```

📁 **Repository**: [GitHub](https://github.com/CyberMind-FR/projet)

## 📋 Changelog

- **v1.0** (2025-12-12): Version initiale
- **v1.1** (2025-12-15): Ajout fonctionnalité X

## 🔗 Ressources

- [Documentation complète](https://cybermind.fr/docs)
- [Fichiers 3D](https://cybermind.fr/files)

---

*Projet développé par Gandalf @ CyberMind*
```

---

## 📎 Références

- [Documentation officielle Hexo](https://hexo.io/docs/)
- [Front-matter Hexo](https://hexo.io/docs/front-matter)
- [Tag Plugins Hexo](https://hexo.io/docs/tag-plugins)
- [Asset Folders Hexo](https://hexo.io/docs/asset-folders)
- [Writing Posts](https://hexo.io/docs/writing)
- [Plugins Hexo](https://hexo.io/plugins/)
- [Themes Hexo](https://hexo.io/themes/)

---

*Documentation générée pour CyberMind.FR - Décembre 2025*
