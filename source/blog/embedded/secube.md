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

          Internet
              |
            [WAN]
              |
      +------------------+
      |   Netifyd        |
      | (Traffic Intel) |
      +------------------+
              |
      +------------------+
      | CrowdSec Bouncer |
      +------------------+
              |
      +------------------+
      | Firewall Zones   |
      +------------------+
        |        |       |
      LAN      Wi-Fi    VPN


---

## 🧱 Composants du MVP

### 🔌 Base système
- OpenWrt (stable)
- nftables
- procd / uci

---

### 🔥 Firewall & Segmentation
- Zones : `wan`, `lan`, `guest`, `vpn`
- Politique restrictive par défaut
- NAT uniquement sur WAN

---

### 👁️ Netifyd – Traffic Intelligence

**Netifyd** remplace un IDS classique dans le MVP.

Fonctions :
- Identification des applications et protocoles
- Classification par catégorie (Cloud, IoT, Social, Malware, etc.)
- Statistiques par hôte / interface
- Données exploitables par firewall (v2)

> Netifyd privilégie la **visibilité réseau** plutôt que l’inspection profonde.

---

### 🌐 CrowdSec

- Agent CrowdSec
- Bouncer nftables
- Protection contre :
  - Scans réseau
  - Bruteforce
  - Attaques automatisées

---

### 🔐 VPN – WireGuard

- Accès distant sécurisé
- Tunnel chiffré performant
- Segmentation réseau VPN dédiée

---

### 📊 Monitoring – Netdata

- Charge CPU / RAM
- Interfaces réseau
- Services critiques
- Accès local uniquement

---

## 📦 Paquets OpenWrt (indicatif)

```bash
# Base
opkg install nftables luci luci-ssl

# Traffic Intelligence
opkg install netifyd luci-app-netifyd

# Threat Intelligence
opkg install crowdsec crowdsec-firewall-bouncer-nftables

# VPN
opkg install wireguard-tools luci-app-wireguard

# Monitoring
opkg install netdata
