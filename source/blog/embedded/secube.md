---
title: "Secube v1 – MVP d’une box de cybersécurité OpenWrt"
date: 2025-12-20
author: CyberMind
tags:
  - OpenWrt
  - Cybersécurité
  - Firewall
  - Netifyd
  - VPN
  - CrowdSec
categories:
  - Projets
  - CyberMind
---

## 🧠 Projet CyberMind – Secube v1 (MVP)

**Secube** est une box de cybersécurité open-source basée sur **OpenWrt**, conçue pour fournir une protection réseau avancée **clé en main**, légère et souveraine.

Cette version décrit le **MVP v1**, volontairement pragmatique et compatible matériel modeste.

---

## 🎯 Objectifs du MVP

- 🔥 Sécuriser le trafic réseau (LAN / WAN / Wi-Fi)
- 👁️ Obtenir une visibilité applicative du trafic
- 🌍 Bloquer les menaces connues via Threat Intelligence
- 🔐 Fournir un accès distant sécurisé
- 📊 Superviser l’état du système

---

## 🧩 Périmètre fonctionnel (v1)

### Fonctions incluses

- Pare-feu avancé (nftables)
- Segmentation réseau (zones OpenWrt)
- Classification du trafic (Netifyd)
- CrowdSec (détection et blocage collaboratif)
- VPN WireGuard
- Monitoring local (Netdata)
- Wi-Fi sécurisé

### Hors périmètre (v1)

- IPS profond
- DPI lourd
- Analyse payload
- SIEM externe
- Interface graphique dédiée complète

---

## 🏗️ Architecture logique

