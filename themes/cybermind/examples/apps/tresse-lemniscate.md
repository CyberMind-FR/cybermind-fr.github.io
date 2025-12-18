---
title: "Tresse × Lemniscate — Fusion A000940"
layout: app
icon: ∞
type: app
status: active
description: "Générateur de motifs géométriques basé sur la suite A000940 (OEIS). Visualisation interactive de tresses et lemniscates avec animations, palettes de couleurs et export PNG/SVG haute résolution."
thumbnail: "/images/apps/tresse-lemniscate.svg"
featured: true
order: 1
date: 2025-01-01
tags_list:
  - géométrie
  - mathématiques
  - visualisation
  - canvas
  - svg
  - pwa
  - generatif
  - art
live_url: "https://cybermind.fr/apps/tresse-lemniscate/"
app:
  version: "1.0"
  type: "PWA"
  technologies:
    - HTML5 Canvas
    - JavaScript
    - CSS3
    - PWA (Service Worker)
---

## ∞ Tresse × Lemniscate — Fusion A000940

> *« L'intelligence n'est pas un sommet, mais une trame. »*

Application de visualisation géométrique générative basée sur la **suite A000940** de l'OEIS, créant des motifs de tresses et lemniscates animés.

### 🎨 Fonctionnalités

| Fonction | Description |
|----------|-------------|
| **Paramètres** | n (3-64), profondeur, rotation, vitesse, épaisseur |
| **Presets** | Conservatif, Neon CM, Orbitron, Monochrome |
| **Palettes** | Cuivre/Argent/Or, Violet/Cyan, Mono, Sunset |
| **Animation** | Start/Stop, vitesse variable, lueur optionnelle |
| **Export** | PNG (2K/4K/8K), SVG vectoriel |
| **PWA** | Fonctionne hors-ligne |

### ⚙️ Contrôles

| Paramètre | Plage | Description |
|-----------|-------|-------------|
| **n** | 3-64 | Nombre de points (A000940-ish) |
| **Profondeur** | 0-1 | Amplitude de la déformation |
| **Rotation** | 0-360° | Angle de rotation global |
| **Vitesse** | -2 à +2 | Vitesse d'animation |
| **Épaisseur** | 0.2-6 | Largeur du trait |

### 🎹 Raccourcis clavier

- `r` — Reset aux valeurs par défaut
- `s` — Start/Stop animation

### 📐 Mathématiques

L'application utilise la suite **A000940** de l'OEIS (Online Encyclopedia of Integer Sequences) pour générer les coordonnées des points formant les courbes de tresses et lemniscates.

La fusion crée un ruban tri-bande avec effet de profondeur et lueur optionnelle.

### 💾 Export

| Format | Résolutions |
|--------|-------------|
| **PNG** | 2048×2048, 4096×4096, 8192×8192 |
| **SVG** | Vectoriel 2048×2048 |

Fond transparent optionnel pour intégration facile.

### 🌐 PWA

Application Progressive Web App :
- ✅ Installable sur mobile/desktop
- ✅ Fonctionne hors-ligne
- ✅ Paramètres persistants (LocalStorage + URL)

### 🔗 Liens

| Type | URL |
|------|-----|
| 🚀 Live | [cybermind.fr/apps/tresse-lemniscate/](https://cybermind.fr/apps/tresse-lemniscate/) |
| 📚 OEIS A000940 | [oeis.org/A000940](https://oeis.org/A000940) |

### 📅 Changelog

- **v1.0** — Version initiale avec presets, palettes et export
