---
title: Yi Jing 易經 — Oracle des Mutations
date: 2025-12-13 18:00:00
updated: 2025-12-13 18:00:00
categories:
  - Spiritualité
  - Divination
  - Philosophie Chinoise
tags:
  - yi-jing
  - i-ching
  - oracle
  - divination
  - taoïsme
  - hexagrammes
  - sagesse-orientale
  - application-interactive
keywords:
  - Yi Jing
  - I Ching
  - Livre des Transformations
  - Oracle chinois
  - Hexagrammes
  - Tirage en ligne
  - Méthode des 3 pièces
description: Application interactive complète du Yi Jing (I Ching) avec tirage traditionnel aux 3 pièces, interprétation des 64 hexagrammes et analyse des lignes mutables.
cover: /images/yijing-banner.jpg
toc: true
toc_number: true
mathjax: false
---

## Introduction au Yi Jing

Le **Yi Jing** (易經), également connu sous le nom de **I Ching** ou **Livre des Transformations**, est l'un des textes fondateurs de la civilisation chinoise. Datant de plus de 3000 ans, cet ouvrage oraculaire et philosophique constitue l'une des sources essentielles de la pensée taoïste et confucéenne.
<!-- more -->
Le Yi Jing repose sur un système de **64 hexagrammes**, figures composées de six lignes superposées, chacune pouvant être pleine (Yang ⚊) ou brisée (Yin ⚋). Ces hexagrammes représentent les différentes configurations des forces cosmiques et offrent une grille de lecture pour comprendre les situations de la vie.

{% note info %}
**Traduction utilisée** : Wilhelm/Perrot, considérée comme l'une des traductions les plus fidèles et les plus profondes du texte original.
{% endnote %}

---

## Application de Tirage Interactive

<div id="yijing-app-container" style="width:100%; min-height:600px; border:none; margin: 20px 0;">
</div>

<script>
// Données Yi Jing embarquées (version compacte pour les 64 hexagrammes)
// Le fichier complet yijing_complet.json doit être placé dans le même répertoire
document.addEventListener('DOMContentLoaded', function() {
    // Créer l'iframe pour l'application
    var container = document.getElementById('yijing-app-container');
    var iframe = document.createElement('iframe');
    iframe.src = '/apps/yijing_oracle.html';
    iframe.style.width = '100%';
    iframe.style.height = '800px';
    iframe.style.border = 'none';
    iframe.style.borderRadius = '15px';
    iframe.style.boxShadow = '0 10px 40px rgba(0,0,0,0.2)';
    container.appendChild(iframe);
});
</script>

{% note warning %}
**Alternative** : Si l'application embarquée ne s'affiche pas, vous pouvez [ouvrir l'oracle Yi Jing en pleine page](/apps/yijing_oracle.html) ou [télécharger l'application Streamlit](#téléchargement).
{% endnote %}

---

## Méthode de Tirage aux 3 Pièces

La méthode traditionnelle des trois pièces est la plus répandue pour consulter le Yi Jing. Elle offre un bon équilibre entre simplicité et respect de la tradition.

### Principe du lancer

On lance simultanément trois pièces. Chaque pièce peut tomber sur **Face** (valeur 3, Yang) ou **Pile** (valeur 2, Yin). La somme des trois pièces détermine le type de ligne :

| Valeur | Combinaison | Nom | Symbole | Nature |
|:------:|:-----------:|:----|:-------:|:-------|
| **6** | 2+2+2 | Vieux Yin | ━━━ ○ ━━━ | Ligne brisée **mutable** → Yang |
| **7** | 2+2+3 | Jeune Yang | ━━━━━━━━━ | Ligne pleine fixe |
| **8** | 2+3+3 | Jeune Yin | ━━━   ━━━ | Ligne brisée fixe |
| **9** | 3+3+3 | Vieux Yang | ━━━━●━━━━ | Ligne pleine **mutable** → Yin |

### Construction de l'hexagramme

L'hexagramme se construit de **bas en haut** : le premier lancer donne la ligne 1 (en bas), le sixième lancer donne la ligne 6 (en haut).

```
Lancer 6 → Ligne 6 (haut)    ━━━   ━━━
Lancer 5 → Ligne 5           ━━━━━━━━━
Lancer 4 → Ligne 4           ━━━━━━━━━
Lancer 3 → Ligne 3           ━━━   ━━━
Lancer 2 → Ligne 2           ━━━━●━━━━  ← mutable
Lancer 1 → Ligne 1 (bas)     ━━━━━━━━━
```

---

## Les Lignes Mutables

Les lignes mutables (6 et 9) sont au cœur du système divinatoire du Yi Jing. Elles indiquent les **points de transformation** de la situation consultée.

### Signification

- **Vieux Yin (6)** : Une situation Yin à son apogée, prête à se transformer en Yang
- **Vieux Yang (9)** : Une situation Yang à son apogée, prête à se transformer en Yin

### Hexagramme de transformation

Lorsque des lignes mutables sont présentes, elles génèrent un **second hexagramme** appelé hexagramme de transformation. Ce dernier indique l'évolution probable de la situation.

{% note success %}
**Lecture du tirage** :
1. L'hexagramme principal décrit la situation actuelle
2. Les lignes mutables indiquent les points d'attention et de changement
3. L'hexagramme de transformation montre vers quoi la situation évolue
{% endnote %}

### Affichage des interprétations

L'application affiche **tous les traits** de chaque hexagramme avec leurs interprétations complètes :

- **Traits mutables** (en orange) : affichés en priorité dans une section dédiée, toujours dépliés
- **Traits fixes** : repliés par défaut quand des traits mutables existent, dépliables individuellement
- **Boutons globaux** : "Tout déplier" / "Tout replier" pour naviguer facilement

Cette organisation permet de se concentrer sur les lignes en mouvement tout en gardant accès au contexte complet.

---

## Structure d'un Hexagramme

Chaque hexagramme est composé de deux **trigrammes** superposés :

```
┌─────────────────────┐
│  Trigramme supérieur │  (lignes 4, 5, 6)
│     ═══════════     │
│     ═══   ═══       │
│     ═══════════     │
├─────────────────────┤
│  Trigramme inférieur │  (lignes 1, 2, 3)
│     ═══   ═══       │
│     ═══════════     │
│     ═══   ═══       │
└─────────────────────┘
```

### Les 8 Trigrammes (Ba Gua)

| Trigramme | Nom | Symbole | Attribut | Élément |
|:---------:|:----|:-------:|:---------|:--------|
| ☰ | **Qian** (K'ien) | ≡ | Le Créateur | Ciel |
| ☷ | **Kun** (K'ouen) | ⚏ | Le Réceptif | Terre |
| ☳ | **Zhen** (Tchen) | ⚌ | L'Éveilleur | Tonnerre |
| ☵ | **Kan** (K'an) | ⚎ | L'Insondable | Eau |
| ☶ | **Gen** (Ken) | ⚍ | L'Immobilisation | Montagne |
| ☴ | **Xun** (Souen) | ⚏ | Le Doux | Vent |
| ☲ | **Li** | ⚌ | Ce qui s'attache | Feu |
| ☱ | **Dui** (Touei) | ⚍ | Le Joyeux | Lac |

---

## Les 64 Hexagrammes

Les 64 hexagrammes couvrent l'ensemble des situations possibles de l'existence. Voici les huit premiers hexagrammes, fondamentaux pour comprendre le système :

### 1. 乾 Qian — Le Créateur
Six lignes Yang. Puissance créatrice, initiative, force du ciel.
*« Le Créateur accomplit le sublime. Tout est propice. »*

### 2. 坤 Kun — Le Réceptif  
Six lignes Yin. Réceptivité, accueil, force de la terre.
*« Le Réceptif accomplit le sublime dans la persévérance. »*

### 3. 屯 Zhun — La Difficulté Initiale
Commencement difficile, germination, naissance.

### 4. 蒙 Meng — La Folie Juvénile
Inexpérience, apprentissage, éducation nécessaire.

### 5. 需 Xu — L'Attente
Patience nécessaire, nourriture, attendre le bon moment.

### 6. 訟 Song — Le Conflit
Opposition, procès, nécessité de médiation.

### 7. 師 Shi — L'Armée
Organisation, discipline, leadership collectif.

### 8. 比 Bi — La Solidarité
Union, rapprochement, alliance bénéfique.

{% note info %}
L'application ci-dessus contient les **64 hexagrammes complets** avec leurs descriptions, jugements et interprétations de chaque trait.
{% endnote %}

---

## Conseils pour la Consultation

### Préparation

1. **Trouvez un moment calme** : La qualité de la consultation dépend de votre état d'esprit
2. **Formulez clairement votre question** : Évitez les questions fermées (oui/non)
3. **Concentrez-vous** : Gardez votre question à l'esprit pendant le tirage

### Formulation des questions

{% note success %}
**Bonnes formulations** :
- « Quelle est la nature de ma situation concernant... ? »
- « Que dois-je comprendre à propos de... ? »
- « Comment puis-je aborder... ? »
{% endnote %}

{% note danger %}
**À éviter** :
- Questions fermées : « Dois-je accepter ce travail ? »
- Questions prédictives : « Vais-je gagner au loto ? »
- Questions multiples en une seule consultation
{% endnote %}

### Interprétation

L'interprétation du Yi Jing n'est pas une science exacte mais un **dialogue avec soi-même**. Le texte ancien agit comme un miroir qui reflète votre situation et vous invite à la réflexion.

---

## Installation Locale

### Version Streamlit (Python)

Pour une utilisation locale avec toutes les fonctionnalités :

```bash
# Cloner ou télécharger les fichiers
# yijing_app.py + yijing_complet.json + requirements.txt

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run yijing_app.py
```

L'application s'ouvrira dans votre navigateur à l'adresse `http://localhost:8501`.

### Version HTML autonome

La version HTML (`yijing_oracle.html`) fonctionne directement dans un navigateur sans installation. Il suffit de placer le fichier `yijing_complet.json` dans le même répertoire.

**Fonctionnalités de la version HTML :**
- Tirage animé avec progression visuelle
- Affichage des 6 traits avec interprétations complètes
- **Mise en évidence des lignes mutables** (en orange) avec section prioritaire
- Traits dépliables/repliables individuellement ou globalement
- Hexagramme de transformation avec ses 6 traits
- Mode consultation pour parcourir les 64 hexagrammes

---

## Téléchargement

{% btn /downloads/yijing_app.py, Application Streamlit (Python), download fa-fw %}
{% btn /downloads/yijing_oracle.html, Application HTML autonome, download fa-fw %}
{% btn /downloads/yijing_complet.json, Données des 64 hexagrammes (JSON), download fa-fw %}
{% btn /downloads/requirements.txt, Dépendances Python, download fa-fw %}

---

## Intégration dans votre site

### Méthode iframe

```html
<iframe 
    src="/apps/yijing_oracle.html" 
    width="100%" 
    height="800" 
    frameborder="0"
    style="border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.2);">
</iframe>
```

### Méthode JavaScript (chargement dynamique)

```html
<div id="yijing-container"></div>
<script>
fetch('/apps/yijing_oracle.html')
    .then(r => r.text())
    .then(html => {
        const container = document.getElementById('yijing-container');
        const shadow = container.attachShadow({mode: 'open'});
        shadow.innerHTML = html;
    });
</script>
```

### Intégration Hexo avec tag personnalisé

Créez le fichier `scripts/yijing.js` dans votre thème Hexo :

```javascript
hexo.extend.tag.register('yijing', function(args) {
    const height = args[0] || '800px';
    return `
        <div class="yijing-oracle-embed">
            <iframe 
                src="/apps/yijing_oracle.html" 
                style="width:100%;height:${height};border:none;border-radius:15px;box-shadow:0 10px 40px rgba(0,0,0,0.2);">
            </iframe>
        </div>
    `;
}, {async: true});
```

Utilisation dans vos posts :

```markdown
{% yijing 900px %}
```

---

## Structure des Fichiers

```
├── source/
│   ├── _posts/
│   │   └── yijing-oracle.md          # Cet article
│   ├── apps/
│   │   ├── yijing_oracle.html        # Application HTML embarquable
│   │   └── yijing_complet.json       # Données des hexagrammes
│   └── downloads/
│       ├── yijing_app.py             # Version Streamlit
│       ├── yijing_oracle.html
│       ├── yijing_complet.json
│       └── requirements.txt
└── themes/
    └── [votre-theme]/
        └── scripts/
            └── yijing.js             # Tag Hexo personnalisé (optionnel)
```

---

## Références et Lectures

- **Wilhelm, Richard** — *Yi King, Le Livre des Transformations* (traduction allemande de référence)
- **Perrot, Étienne** — Traduction française de l'œuvre de Wilhelm
- **Javary, Cyrille** — *Le Yi Jing, le livre des changements*
- **Cleary, Thomas** — *The Taoist I Ching*

---

## Licence et Crédits

- **Texte du Yi Jing** : Domaine public (traduction Wilhelm/Perrot)
- **Source des données** : wengu.tartarie.com
- **Application** : Libre d'utilisation et de modification

---

*易經 — « Le changement est la seule constante »*

{% note quote %}
*« L'homme supérieur, quand il est au repos, contemple l'image [de l'hexagramme] et médite sur les paroles. Quand il agit, il contemple les transformations et médite sur les oracles. »*
— Confucius, commentaire du Yi Jing
{% endnote %}
