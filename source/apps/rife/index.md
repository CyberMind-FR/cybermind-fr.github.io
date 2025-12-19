---
title: "Rife Generator - s2 Spooky2 Controller"
layout: app
icon: "〰️"
description: "Générateur de fréquences Rife et contrôleur Spooky2 pour le bien-être"
embed_url: "http://rife.maegia.tv"
embed_height: "750px"
cover: /images/rife-cover.jpg
github: "https://github.com/gkerma/s2"
category: wellness
featured: true
tags:
  - frequencies
  - wellness
  - rife
  - spooky2
  - audio
---

## 〰️ Rife Generator - s2

**Contrôleur Spooky2 et générateur de fréquences Rife**

Application web pour générer des fréquences Rife et contrôler les générateurs Spooky2. Fonctionne en mode simulation autonome ou connecté à un vrai générateur XM.

### 🎛️ Panneau de Contrôle

- **Fréquence** : 0.01 Hz à 100 kHz
- **Amplitude** : 0 - 100%
- **Dwell** : Durée par fréquence (1 - 3600s)
- **Visualiseur** : Forme d'onde en temps réel

### 📊 Formes d'Onde

| Forme | Icône | Usage |
|-------|-------|-------|
| **Sine** | 〰️ | Doux, relaxation |
| **Square** | ⬜ | Plus intense |
| **Triangle** | 🔺 | Intermédiaire |
| **Sawtooth** | 📐 | Harmoniques riches |

### ⚡ Fréquences Rapides

| Fréquence | Nom | Description |
|-----------|-----|-------------|
| **7.83 Hz** | 🌍 Schumann | Résonance terrestre |
| **528 Hz** | 💚 Healing | Fréquence de guérison |
| **432 Hz** | 🎵 Verdi | Accordage naturel |
| **440 Hz** | 🎹 LA | Note de référence |
| **727 Hz** | 〰️ Rife | Fréquence Rife classique |

### 📋 Programmes Préchargés

- **🌍 Schumann** : 7.83, 14.3, 20.8, 27.3, 33.8 Hz
- **🎵 Solfège** : 174, 285, 396, 417, 528, 639, 741, 852, 963 Hz
- **〰️ Rife General** : 20, 727, 787, 800, 880, 5000, 10000 Hz
- **🧬 Detox** : 0.5, 522, 146, 1552, 800 Hz
- **😴 Sleep** : 0.5, 1.5, 3, 4, 7.83 Hz
- **🧠 Focus** : 10, 12, 15, 18, 40 Hz
- **💪 Energy** : 7.83, 10, 33, 136.1, 528 Hz
- **🛡️ Immune** : 432, 528, 727, 787, 880 Hz

### 💻 CLI Spooky2

Interface ligne de commande intégrée pour contrôler les générateurs s2 :

```bash
s2 status              # État du générateur
s2 list                # Liste des générateurs
s2 run generator=1 frequency=528 waveform=sine amplitude=100 duration=60s
```

### 💾 Export

| Format | Description |
|--------|-------------|
| **Spooky2 .txt** | Compatible logiciel Spooky2 |
| **CSV** | Tableur, analyse |
| **JSON** | Développeurs, automatisation |
| **Bash .sh** | Script Linux/Mac |
| **Windows .bat** | Script Windows |

### 📱 PWA

- ✅ Installation sur écran d'accueil
- ✅ Fonctionne hors-ligne
- ✅ Mode plein écran

### ⚠️ Avertissement

Cette application est destinée à la **relaxation et au bien-être** uniquement.
Elle ne remplace en aucun cas un avis médical professionnel.

### 📚 Ressources

- [Spooky2](https://www.spooky2.com/) - Générateurs Rife
- [Royal Rife - Wikipedia](https://en.wikipedia.org/wiki/Royal_Raymond_Rife)
- [Résonance de Schumann](https://fr.wikipedia.org/wiki/R%C3%A9sonance_de_Schumann)
