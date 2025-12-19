---
title: "PiDebugger v2.1"
layout: app
icon: 🍓
description: "Debugger ARM multi-cibles basé sur Raspberry Pi Zero. Interface tactile pour ESPRESSObin, MOCHAbin, Sheeva64."
category: dev
embed_url: "/demos/DEMO.HTML"
embed_height: 600
status: active
version: "2.1"
featured: true
order: 3
tags_list:
  - arm
  - raspberry-pi
  - embedded
  - debugging
  - openwrt
related_article: "/embedded/pidebugger-arm-debugger/"
---

## 🎯 Présentation

**PiDebugger** est un outil portable de debugging pour SoC ARM, construit autour d'un Raspberry Pi Zero W avec écran tactile circulaire.

### Targets supportées

| Target | SoC | CPU | RAM |
|--------|-----|-----|-----|
| ☕ ESPRESSObin V7 | Armada 3720 | 2×A53 @ 1.0GHz | 1-2GB DDR4 |
| 🚀 ESPRESSObin Ultra | Armada 3720 | 2×A53 @ 1.2GHz | 1GB DDR4 |
| 🍫 MOCHAbin | Armada 7040 | 4×A72 @ 1.4GHz | 2-8GB DDR4 |
| 🔌 Sheeva64 | Armada 3720 | 2×A53 @ 1.2GHz | 1GB DDR4 |

## ⚡ Fonctionnalités

- **Boot Sequence Monitoring** — Visualisation temps réel du démarrage (BootROM → WTMI → ATF → U-Boot → Kernel)
- **Serial Console** — Terminal série intégré avec export de logs
- **XMODEM Transfer** — Transfert de firmware via XMODEM
- **UEFI Shell** — Support UEFI pour MOCHAbin
- **Multi-thèmes** — Dark, Light, OLED, Berry
- **Gestures** — Swipe, pinch, long press

## 🛠️ Technologies

- React 18 (vanilla, pas de build)
- Web Audio API pour les sons
- SVG pour l'interface circulaire
- Responsive (s'adapte à la taille de l'écran)

## 📦 Matériel requis

- Raspberry Pi Zero W/2W
- Écran tactile GC9A01 (240×240 rond)
- Adaptateur USB-C vers USB-A
- Câble série USB-TTL (3.3V)

## 🔗 Liens

- [Code source sur GitHub](https://github.com/CyberMind-FR/pidebugger)
- [Guide de construction](/guides/pidebugger-build/)
