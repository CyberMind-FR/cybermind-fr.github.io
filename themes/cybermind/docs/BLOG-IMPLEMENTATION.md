# 🔧 Implémentation du système de liaison Blog

## Modifications à apporter aux layouts existants

### 1. Ajouter dans `layout/post.ejs`

Après le contenu de l'article, ajouter cette section :

```ejs
<%# Section Liaisons %>
<aside class="post-relations">
  
  <% if (page.related_app) { %>
  <div class="relation-card relation-app">
    <div class="relation-icon">🚀</div>
    <div class="relation-content">
      <strong>Application associée</strong>
      <a href="/apps/<%= page.related_app %>/">
        Ouvrir <%= page.related_app %> →
      </a>
    </div>
  </div>
  <% } %>
  
  <% if (page.related_service) { %>
  <div class="relation-card relation-service">
    <div class="relation-icon">🛡️</div>
    <div class="relation-content">
      <strong>Service professionnel</strong>
      <a href="/services/<%= page.related_service %>/">
        Découvrir →
      </a>
    </div>
  </div>
  <% } %>
  
  <% if (page.related_demo) { %>
  <div class="relation-card relation-demo">
    <div class="relation-icon">🎪</div>
    <div class="relation-content">
      <strong>Démo interactive</strong>
      <a href="/demos/<%= page.related_demo %>/">
        Tester →
      </a>
    </div>
  </div>
  <% } %>
  
  <% if (page.related_portfolio) { %>
  <div class="relation-card relation-portfolio">
    <div class="relation-icon">💼</div>
    <div class="relation-content">
      <strong>Projet associé</strong>
      <a href="/portfolio/archives/<%= page.related_portfolio %>/">
        Voir →
      </a>
    </div>
  </div>
  <% } %>
  
</aside>
```

### 2. Ajouter dans `source/css/style.css`

```css
/* ══════════════════════════════════════════════════════════════
   CARTES DE LIAISON ARTICLE → RESSOURCES
   ══════════════════════════════════════════════════════════════ */

.post-relations {
  display: grid;
  gap: 1rem;
  margin: 2rem 0;
  padding: 1.5rem;
  background: var(--bg-secondary);
  border-radius: 12px;
}

.relation-card {
  display: flex;
  gap: 1rem;
  padding: 1rem;
  background: var(--bg-primary);
  border-radius: 8px;
  border-left: 4px solid;
  transition: transform 0.2s, box-shadow 0.2s;
}

.relation-card:hover {
  transform: translateX(5px);
  box-shadow: 0 5px 20px rgba(0,0,0,0.2);
}

.relation-icon {
  font-size: 1.5rem;
  line-height: 1;
}

.relation-content {
  flex: 1;
}

.relation-content strong {
  display: block;
  margin-bottom: 0.25rem;
}

.relation-content a {
  text-decoration: none;
  font-weight: 500;
}

.relation-content a:hover {
  text-decoration: underline;
}

/* Couleurs par type */
.relation-app {
  border-color: #00F6FF;
}
.relation-app strong,
.relation-app a {
  color: #00F6FF;
}

.relation-service {
  border-color: #00ff88;
}
.relation-service strong,
.relation-service a {
  color: #00ff88;
}

.relation-demo {
  border-color: #ffcc00;
}
.relation-demo strong,
.relation-demo a {
  color: #ffcc00;
}

.relation-portfolio {
  border-color: #9966ff;
}
.relation-portfolio strong,
.relation-portfolio a {
  color: #9966ff;
}
```

### 3. Créer `layout/category.ejs`

```ejs
<div class="category-page" style="--cat-color: <%= page.color %>">
  
  <header class="category-header">
    <span class="category-icon"><%= page.icon %></span>
    <h1><%= page.title %></h1>
    <p><%= page.description %></p>
  </header>

  <%# Ressources liées à la catégorie %>
  <% if (page.featured_apps && page.featured_apps.length) { %>
  <section class="category-resources">
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

  <%# Liste des articles de cette catégorie %>
  <section class="category-articles">
    <h2>📝 Articles</h2>
    <% 
    const categoryPosts = site.posts.filter(function(post) {
      return post.category === page.category;
    }).sort('date', -1);
    %>
    <% categoryPosts.each(function(post) { %>
    <article class="article-card">
      <a href="<%- url_for(post.path) %>">
        <h3><%= post.title %></h3>
        <p><%= post.description %></p>
        <div class="article-meta">
          <span><%= date(post.date, 'DD/MM/YYYY') %></span>
          <% if (post.reading_time) { %>
          <span><%= post.reading_time %> min</span>
          <% } %>
        </div>
      </a>
    </article>
    <% }); %>
  </section>
  
</div>
```

## Configuration Hexo

### _config.yml

```yaml
# Permalinks pour les articles par catégorie
permalink: blog/:category/:title/

# Nouveau dossier source pour les articles
source_dir: source

# Menu avec sous-catégories
menu:
  Accueil: /
  Blog:
    _path: /blog/
    🛡️ Cybersécurité: /blog/cybersecurity/
    ⚙️ Embarqué: /blog/embedded/
    🐧 Linux: /blog/linux/
    🎨 Créativité: /blog/creative/
    🧘 Philosophie: /blog/philosophy/
    📖 Tutoriels: /blog/tutorials/
  Apps: /apps/
  Services: /services/
  Portfolio: /portfolio/
```

## Migration des articles existants

```bash
#!/bin/bash
# Script de migration

for file in source/_posts/*.md; do
  # Extraire la catégorie
  cat=$(grep -m1 "^category:" "$file" | cut -d: -f2 | tr -d ' ')
  
  if [ -d "source/blog/$cat" ]; then
    mv "$file" "source/blog/$cat/"
    echo "✅ Migré: $(basename $file) → blog/$cat/"
  else
    echo "⚠️ Catégorie inconnue: $cat pour $(basename $file)"
  fi
done
```
