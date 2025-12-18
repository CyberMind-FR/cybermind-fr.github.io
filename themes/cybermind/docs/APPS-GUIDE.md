# 📱 Guide : Ajouter des Applications au Thème CyberMind

## Vue d'ensemble

Le thème CyberMind permet d'intégrer des applications web interactives (démos, outils, widgets) qui s'affichent :
- Sur la **page d'accueil** (section "Applications & Ressources")
- Sur une **page dédiée** `/apps/`
- Avec un **article de blog** associé pour la documentation

---

## 🏗️ Structure d'une Application

```
mon-blog-cybermind/
├── source/
│   ├── demos/                          # Dossier des applications
│   │   └── 64-hexagrammes-animation.html
│   ├── apps/
│   │   └── index.md                    # Page listant toutes les apps
│   └── _posts/
│       └── 2024-12-18-yi-jing-64-hexagrammes.md  # Article associé
└── themes/
    └── cybermind/
        └── _config.yml                 # Configuration des apps
```

---

## 📝 Étape 1 : Configurer l'application dans le thème

### Fichier : `themes/cybermind/_config.yml`

```yaml
# ═══════════════════════════════════════════════════════════════
# APPLICATIONS & DÉMOS
# ═══════════════════════════════════════════════════════════════

apps:
  # ─────────────────────────────────────────────────────────────
  # Exemple : Animation des 64 Hexagrammes du Yi Jing
  # ─────────────────────────────────────────────────────────────
  - name: "64 Hexagrammes du Yi Jing"
    url: "https://cybermind.fr/demos/64-hexagrammes-animation.html"
    icon: "☯️"
    description: "Animation interactive des 64 hexagrammes avec symbolique traditionnelle et transformations."
    category: "philosophy"
    tags:
      - yi-jing
      - animation
      - philosophie
      - divination
    article: "/2024/12/18/yi-jing-64-hexagrammes/"
    featured: true
    order: 1

  # ─────────────────────────────────────────────────────────────
  # Exemple : Outil de sécurité
  # ─────────────────────────────────────────────────────────────
  - name: "Password Strength Checker"
    url: "https://cybermind.fr/demos/password-checker.html"
    icon: "🔐"
    description: "Vérifiez la robustesse de vos mots de passe avec analyse entropique."
    category: "security"
    tags:
      - security
      - password
      - tool
    article: "/2024/11/15/securite-mots-de-passe/"
    featured: true
    order: 2

  # ─────────────────────────────────────────────────────────────
  # Exemple : Générateur créatif
  # ─────────────────────────────────────────────────────────────
  - name: "Générateur de Poésie IA"
    url: "https://cybermind.fr/demos/poetry-generator.html"
    icon: "✍️"
    description: "Créez des poèmes avec assistance IA dans le style classique français."
    category: "creative"
    tags:
      - poésie
      - ia
      - création
    article: "/2024/10/20/poesie-ia-generative/"
    featured: false
    order: 3

# Paramètres d'affichage sur la page d'accueil
index:
  apps_limit: 2  # Nombre d'apps affichées (0 = toutes)
```

---

## 📄 Étape 2 : Créer l'article de référence

### Fichier : `source/_posts/2024-12-18-yi-jing-64-hexagrammes.md`

```markdown
---
title: "Les 64 Hexagrammes du Yi Jing : Animation Interactive"
date: 2024-12-18 10:00:00
categories:
  - Philosophie
tags:
  - yi-jing
  - hexagrammes
  - animation
  - divination
  - taoïsme
description: "Découvrez les 64 hexagrammes du Yi Jing à travers une animation interactive explorant leur symbolique et leurs transformations."
icon: ☯️
app_url: "https://cybermind.fr/demos/64-hexagrammes-animation.html"
---

## Introduction au Yi Jing

Le Yi Jing (易經), ou "Livre des Mutations", est l'un des plus anciens textes 
classiques chinois. Il repose sur 64 hexagrammes, chacun composé de 6 lignes 
qui peuvent être pleines (Yang ─) ou brisées (Yin ╌).

<!-- more -->

## L'Application Interactive

<div class="app-embed">
  <iframe 
    src="https://cybermind.fr/demos/64-hexagrammes-animation.html?embedded=true" 
    width="100%" 
    height="600" 
    frameborder="0"
    loading="lazy">
  </iframe>
</div>

[▶ Ouvrir en plein écran](https://cybermind.fr/demos/64-hexagrammes-animation.html)

## Les 8 Trigrammes de Base

| Trigramme | Nom | Symbole | Élément |
|-----------|-----|---------|---------|
| ☰ | Qián | Ciel | Métal |
| ☷ | Kūn | Terre | Terre |
| ☳ | Zhèn | Tonnerre | Bois |
| ☵ | Kǎn | Eau | Eau |
| ☶ | Gèn | Montagne | Terre |
| ☴ | Xùn | Vent | Bois |
| ☲ | Lí | Feu | Feu |
| ☱ | Duì | Lac | Métal |

## Comment utiliser l'animation

1. **Navigation** : Cliquez sur un hexagramme pour voir ses détails
2. **Transformations** : Observez les mutations entre hexagrammes
3. **Symbolique** : Chaque hexagramme affiche son nom et sa signification

## Aspects techniques

L'animation utilise :
- **Canvas HTML5** pour le rendu graphique
- **JavaScript ES6** pour les interactions
- **CSS Animations** pour les transitions fluides

## Références

- Wilhelm, R. (1967). *I Ching ou Le Livre des Transformations*
- Javary, C. (2002). *Le Yi Jing : Le livre des changements*

---

*Cette application fait partie de la série d'outils [CyberMind Philosophy](/tags/philosophie/).*
```

---

## 📁 Étape 3 : Créer la page des applications

### Fichier : `source/apps/index.md`

```markdown
---
title: Applications & Démos
layout: apps
icon: 🚀
description: "Explorez nos applications interactives : outils de sécurité, animations philosophiques, générateurs créatifs et plus encore."
---

Bienvenue dans notre galerie d'applications interactives. Chaque outil est 
accompagné d'un article explicatif détaillant son fonctionnement et son utilisation.
```

---

## 🎨 Étape 4 : Créer le layout apps (optionnel)

### Fichier : `themes/cybermind/layout/apps.ejs`

```ejs
<section style="padding: 4rem 2rem; min-height: 60vh;">
    <div class="section-header">
        <div class="section-tag">Outils Interactifs</div>
        <h2 class="section-title"><%= page.icon || '🚀' %> <%= page.title %></h2>
        <p style="text-align: center; color: var(--text-muted); max-width: 600px; margin: 1rem auto;">
            <%= page.description || 'Découvrez nos applications et démos interactives' %>
        </p>
    </div>

    <% if (theme.apps && theme.apps.length > 0) { %>
    
    <!-- Filtres par catégorie -->
    <div class="apps-filters" style="display: flex; justify-content: center; gap: 0.5rem; margin-bottom: 2rem; flex-wrap: wrap;">
        <button class="filter-btn active" data-filter="all">🎲 Tous</button>
        <button class="filter-btn" data-filter="philosophy">🧘 Philosophie</button>
        <button class="filter-btn" data-filter="security">🔐 Sécurité</button>
        <button class="filter-btn" data-filter="creative">🎨 Créatif</button>
        <button class="filter-btn" data-filter="tools">🔧 Outils</button>
    </div>
    
    <!-- Grille des applications -->
    <div class="apps-gallery" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 2rem; max-width: 1400px; margin: 0 auto;">
        <% theme.apps.forEach(function(app) { %>
        <div class="app-card-full" data-category="<%= app.category || 'tools' %>">
            <!-- Prévisualisation iframe -->
            <div class="app-preview-large">
                <iframe src="<%= app.url %>?embedded=true" title="<%= app.name %>" loading="lazy"></iframe>
                <div class="app-overlay-full">
                    <a href="<%= app.url %>" target="_blank" class="btn btn-primary">▶ Lancer</a>
                    <% if (app.article) { %>
                    <a href="<%= app.article %>" class="btn btn-secondary">📖 Documentation</a>
                    <% } %>
                </div>
            </div>
            
            <!-- Informations -->
            <div class="app-info-full">
                <h3><%= app.icon || '🚀' %> <%= app.name %></h3>
                <p><%= app.description || '' %></p>
                
                <% if (app.tags && app.tags.length > 0) { %>
                <div class="app-tags">
                    <% app.tags.forEach(function(tag) { %>
                    <span class="app-tag">#<%= tag %></span>
                    <% }); %>
                </div>
                <% } %>
                
                <div class="app-actions">
                    <a href="<%= app.url %>" target="_blank" class="app-btn-primary">
                        Ouvrir l'application ↗
                    </a>
                </div>
            </div>
        </div>
        <% }); %>
    </div>
    
    <% } else { %>
    <div style="text-align: center; padding: 3rem; color: var(--text-muted);">
        <p style="font-size: 1.2rem;">Aucune application disponible pour le moment.</p>
        <p>Revenez bientôt pour découvrir nos outils interactifs !</p>
    </div>
    <% } %>

    <div style="text-align: center; margin-top: 4rem;">
        <a href="/" class="btn btn-secondary">← Retour à l'accueil</a>
    </div>
</section>

<style>
.apps-filters .filter-btn {
    padding: 0.5rem 1rem;
    background: var(--bg-secondary);
    border: 1px solid var(--border-subtle);
    border-radius: 8px;
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.2s ease;
}

.apps-filters .filter-btn:hover,
.apps-filters .filter-btn.active {
    background: var(--accent-orange);
    color: #000;
    border-color: var(--accent-orange);
}

.app-card-full {
    background: var(--bg-secondary);
    border: 1px solid var(--border-subtle);
    border-radius: 16px;
    overflow: hidden;
    transition: all 0.3s ease;
}

.app-card-full:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    border-color: var(--accent-orange);
}

.app-preview-large {
    position: relative;
    height: 250px;
    background: var(--bg-primary);
}

.app-preview-large iframe {
    width: 100%;
    height: 100%;
    border: none;
    pointer-events: none;
}

.app-overlay-full {
    position: absolute;
    inset: 0;
    background: rgba(0,0,0,0.7);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.app-card-full:hover .app-overlay-full {
    opacity: 1;
}

.app-info-full {
    padding: 1.5rem;
}

.app-info-full h3 {
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
}

.app-info-full p {
    color: var(--text-secondary);
    font-size: 0.9rem;
    margin-bottom: 1rem;
}

.app-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1rem;
}

.app-tag {
    font-size: 0.75rem;
    padding: 0.2rem 0.5rem;
    background: var(--bg-primary);
    border-radius: 4px;
    color: var(--text-muted);
}

.app-btn-primary {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    background: var(--accent-orange);
    color: #000;
    text-decoration: none;
    border-radius: 8px;
    font-weight: 600;
    transition: all 0.2s ease;
}

.app-btn-primary:hover {
    transform: scale(1.05);
    box-shadow: 0 5px 20px rgba(249, 115, 22, 0.4);
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const appCards = document.querySelectorAll('.app-card-full');
    
    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const filter = this.dataset.filter;
            
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            
            appCards.forEach(card => {
                if (filter === 'all' || card.dataset.category === filter) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
});
</script>
```

---

## 🖼️ Étape 5 : Héberger le fichier HTML de l'application

### Option A : Dans le dossier source (recommandé)

```
source/
└── demos/
    └── 64-hexagrammes-animation.html
```

L'URL sera : `https://cybermind.fr/demos/64-hexagrammes-animation.html`

### Option B : Lien externe

Si l'application est hébergée ailleurs, utilisez simplement l'URL complète dans la configuration.

---

## 📋 Propriétés d'une Application

| Propriété | Type | Requis | Description |
|-----------|------|--------|-------------|
| `name` | String | ✅ | Nom affiché de l'application |
| `url` | String | ✅ | URL complète de l'application |
| `icon` | Emoji | ❌ | Icône emoji (défaut: 🚀) |
| `description` | String | ❌ | Description courte |
| `category` | String | ❌ | Catégorie pour filtrage |
| `tags` | Array | ❌ | Tags pour recherche |
| `article` | String | ❌ | Lien vers l'article associé |
| `featured` | Boolean | ❌ | Mise en avant (défaut: false) |
| `order` | Number | ❌ | Ordre d'affichage |

---

## 🎯 Catégories disponibles

| Catégorie | Icône | Description |
|-----------|-------|-------------|
| `philosophy` | 🧘 | Yi Jing, méditation, réflexion |
| `security` | 🔐 | Outils de sécurité, audit |
| `creative` | 🎨 | Générateurs, art, musique |
| `tools` | 🔧 | Utilitaires divers |
| `dev` | 💻 | Outils de développement |
| `network` | 🌐 | Analyse réseau |

---

## 💡 Bonnes pratiques

### 1. Paramètre `?embedded=true`

Ajoutez ce paramètre dans votre application pour :
- Masquer les éléments de navigation
- Adapter le style pour l'intégration iframe
- Désactiver certaines fonctionnalités en mode embarqué

```javascript
// Dans votre application HTML
const isEmbedded = new URLSearchParams(window.location.search).get('embedded') === 'true';
if (isEmbedded) {
    document.body.classList.add('embedded-mode');
}
```

### 2. Responsive design

Assurez-vous que l'application s'adapte à différentes tailles d'iframe.

### 3. Performance

Utilisez `loading="lazy"` pour les iframes (déjà inclus dans le thème).

### 4. Accessibilité

Ajoutez toujours un attribut `title` descriptif.

---

## 🔧 Commandes Hexo

```bash
# Après modification de _config.yml
cd mon-blog-cybermind
hexo clean
hexo generate
hexo server

# Vérifier la page apps
open http://localhost:4000/apps/
```

---

## 📚 Exemple complet : 64 Hexagrammes

### 1. Configuration dans `_config.yml`

```yaml
apps:
  - name: "64 Hexagrammes du Yi Jing"
    url: "https://cybermind.fr/demos/64-hexagrammes-animation.html"
    icon: "☯️"
    description: "Animation interactive des 64 hexagrammes avec symbolique traditionnelle."
    category: "philosophy"
    tags:
      - yi-jing
      - hexagrammes
      - taoïsme
    article: "/2024/12/18/yi-jing-64-hexagrammes/"
    featured: true
    order: 1
```

### 2. Fichier de démo dans `source/demos/`

```
source/demos/64-hexagrammes-animation.html
```

### 3. Article dans `source/_posts/`

```
source/_posts/2024-12-18-yi-jing-64-hexagrammes.md
```

### 4. Résultat

- **Page d'accueil** : L'app apparaît dans la section "Applications"
- **Page /apps/** : L'app est listée avec filtres
- **Article** : Documentation complète avec app embarquée

---

## 🎉 Conclusion

Vous avez maintenant tous les éléments pour :
1. ✅ Configurer une nouvelle application
2. ✅ Créer l'article de documentation associé
3. ✅ Afficher l'app sur la page d'accueil et /apps/
4. ✅ Filtrer par catégorie
5. ✅ Lier article ↔ application

Pour toute question : contact@cybermind.fr
