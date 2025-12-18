---
title: Créer des motifs géométriques avec A000940
layout: post
date: 2025-01-15
updated: 2025-01-20
category: creative
subcategory: generative-art
tags:
- géométrie
- mathématiques
- canvas
- js
- art-génératif
author: G.Kerma
reading_time: 8
difficulty: intermediate
description: Découvrez comment créer des motifs géométriques animés basés sur la suite
  mathématique A000940.
thumbnail: /images/blog/creative/a000940-cover.jpg
related_app: tresse-lemniscate
related_service: creative
related_demo: geometry-playground
related_portfolio: ganimed
related_posts:
- sacred-geometry
- poetry-music-suno
- ../philosophy/yijing-intro
external_links:
- title: OEIS A000940
  url: https://oeis.org/A000940
- title: Code source GitHub
  url: https://github.com/CyberMind-FR/tresse-lemniscate
series:
  name: Art Génératif avec JavaScript
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
