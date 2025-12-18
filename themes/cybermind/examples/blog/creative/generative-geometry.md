---
title: "Créer des motifs géométriques avec A000940"
layout: post
date: 2025-01-15
updated: 2025-01-20

# ═══════════════════════════════════════════════════════════
# 📁 CATÉGORISATION
# ═══════════════════════════════════════════════════════════
category: creative              # Dossier parent (obligatoire)
subcategory: generative-art     # Sous-catégorie (optionnel)

tags:
  - géométrie
  - mathématiques
  - canvas
  - javascript
  - art-génératif

# ═══════════════════════════════════════════════════════════
# 📝 MÉTADONNÉES
# ═══════════════════════════════════════════════════════════
author: G.Kerma
reading_time: 8                 # Minutes de lecture
difficulty: intermediate        # beginner | intermediate | advanced
description: "Découvrez comment créer des motifs géométriques animés basés sur la suite mathématique A000940."
thumbnail: /images/blog/creative/a000940-cover.jpg

# ═══════════════════════════════════════════════════════════
# 🔗 LIAISONS - Le cœur du système !
# ═══════════════════════════════════════════════════════════

# Lier à une application
related_app: tresse-lemniscate
# → Affiche encart "🚀 Essayer l'app" vers /apps/tresse-lemniscate/

# Lier à un service professionnel
related_service: creative
# → Affiche encart "🛡️ Service associé" vers /services/creative/

# Lier à une démo interactive
related_demo: geometry-playground
# → Affiche encart "🎪 Démo" avec iframe ou lien vers /demos/geometry-playground/

# Lier à un projet portfolio
related_portfolio: ganimed
# → Affiche encart "💼 Projet" vers /portfolio/archives/ganimed/

# ═══════════════════════════════════════════════════════════
# 📚 ARTICLES CONNEXES
# ═══════════════════════════════════════════════════════════
related_posts:
  - sacred-geometry              # Autre article du même dossier
  - poetry-music-suno
  - ../philosophy/yijing-intro   # Article d'un autre dossier

# ═══════════════════════════════════════════════════════════
# 🔗 RESSOURCES EXTERNES
# ═══════════════════════════════════════════════════════════
external_links:
  - title: "OEIS A000940"
    url: "https://oeis.org/A000940"
  - title: "Code source GitHub"
    url: "https://github.com/CyberMind-FR/tresse-lemniscate"

# ═══════════════════════════════════════════════════════════
# 📖 SÉRIE D'ARTICLES (optionnel)
# ═══════════════════════════════════════════════════════════
series:
  name: "Art Génératif avec JavaScript"
  part: 2
  total: 5
---

## Introduction

La suite **A000940** de l'OEIS produit des motifs géométriques fascinants qui mêlent tresses et lemniscates...

## Le code

```javascript
function computePoints(n, depth, rotation, t) {
  const pts = [];
  for (let i = 0; i < n * 100; i++) {
    const angle = (i / 100) * Math.PI * 2;
    // ... calculs A000940
  }
  return pts;
}
```

## Résultat

Les motifs générés combinent beauté mathématique et expression artistique.

---

> 💡 **Essayez vous-même !** L'application Tresse × Lemniscate vous permet d'explorer ces motifs en temps réel avec export PNG/SVG.
