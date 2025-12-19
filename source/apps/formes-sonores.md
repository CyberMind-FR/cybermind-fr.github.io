---
title: "Formes Sonores"
layout: app
icon: 🎵
description: "Générateur de sons à partir de polygones évolutifs. Sonification géométrique interactive avec Web Audio API."
category: creative
embed_url: "/demos/formes-sonores.html"
embed_height: 550
status: active
version: "1.0"
featured: false
tags_list:
  - generative
  - audio
  - p5js
  - art
  - sonification
---

## 🎨 Présentation

**Formes Sonores** est une expérience audiovisuelle générative où des polygones évoluent et produisent des sons en fonction de leurs propriétés géométriques.

Chaque forme devient un instrument : sa taille, sa position, sa complexité et sa vélocité influencent le son qu'elle produit.

## 🎹 Mapping Sonore

| Propriété | Paramètre Audio |
|-----------|-----------------|
| **Vertices** (3-8) | Hauteur (pitch) |
| **Surface** | Volume |
| **Position X** | Panoramique stéréo |
| **Complexité** | Timbre (forme d'onde) |
| **Vélocité** | Vitesse du tremolo |
| **Divisions** | Percussions |

## 🎼 Modes musicaux

- **Pentatonique** — Gamme universelle, harmonieuse
- **Mineur naturel** — Ambiance mélancolique
- **Tons entiers** — Atmosphère onirique, Debussy-esque

## ⚡ Fonctionnalités

- **Clic pour créer** — Ajoutez des polygones n'importe où sur le canvas
- **Évolution autonome** — Les formes grandissent, bougent et se divisent
- **Polyphonie** — Jusqu'à 12 voix simultanées
- **Feedback visuel** — Glow et trails selon l'activité audio

## 🛠️ Technologies

- **p5.js** — Rendu graphique et animation
- **Web Audio API** — Synthèse sonore en temps réel
- **Oscillateurs** — Sine, triangle, square, sawtooth
- **LFO** — Tremolo dynamique par polygone
