---
title: "EnigmaSuite"
layout: portfolio
type: opensource
icon: 🔐
description: "Réseau overlay sécurisé basé sur OpenWrt. Chiffrement E2E, builds reproductibles, CI/CD zero-trust."
thumbnail: /images/portfolio/enigmasuite.jpg
status: development
featured: true
order: 1
tags_list:
  - openwrt
  - security
  - encryption
  - overlay
  - crowdfunding
project:
  type: "Firmware Sécurisé"
  technologies:
    - OpenWrt
    - X25519
    - ChaCha20-Poly1305
    - Sigstore
    - GitHub Actions
  duration: "En cours"
  year: 2024
live_url: "/demos/enigmasuite.html"
github_url: "https://github.com/CyberMind-FR/enigmasuite"
---

## 🎯 Vision

**EnigmaSuite** est une pile réseau open-source, cryptographiquement durcie, construite sur :

- **Firmware OpenWrt custom** — Buildroot personnalisé, patches kernel
- **Overlay chiffré multipoint** — Réseau mesh sécurisé
- **Pipeline CI/CD reproductible** — Builds déterministes et signés

## 🔒 Sécurité

### Cryptographie
- **X25519** — Échange de clés Curve25519
- **ChaCha20-Poly1305** — Chiffrement authentifié
- **Routage adaptatif** — Multi-hop dynamique
- **Gestion d'identité** — PKI intégrée

### Builds Reproductibles
- **Déterminisme** — Même source = même binaire
- **Cosign/Sigstore** — Signature cryptographique
- **SBOM** — Bill of Materials logiciel
- **Attestations** — Provenance vérifiable

## 💰 Objectifs de Financement

| Palier | Montant | Objectif |
|--------|---------|----------|
| 🏗️ Base | €18,000 | Pipelines de build reproductibles |
| 🔍 Audit | €35,000 | Audits crypto & réseau |
| 🌐 Backbone | €55,000 | Overlay multi-région |
| 🏭 Production | €80,000 | Fabrication Enigmabox v3 |

## 🤝 Partenaires

- **CrowdSec** — Intelligence collective contre les menaces
- **GlobalScale Technologies** — Hardware Marvell ARM

## 🎁 Contreparties

- €10 — Mention supporter public
- €25 — Accès aux rapports de dev
- €50 — Firmware pre-release
- €100 — Badge contributeur + observateur CI/CD
- €250 — Q&A technique privé
- €500 — Audit de configuration
- €1000+ — Partenaire technique (logo & collaboration)
