---
title: "SecuBox : La Solution de Cybersécurité Tout-en-Un pour Votre Réseau"
date: 2025-12-20
categories: [Security, OpenWrt, Crowdfunding]
tags: [secubox, openwrt, security, crowdsec, wireguard, nac, firewall, crowdfunding, open-source, globalscale]
author: Gandalf
image: /images/secubox-hero.png
description: "SecuBox réunit 7 modules de sécurité open source sur appliances GlobalScale : CrowdSec, WireGuard, NAC, DPI, Monitoring. Campagne participative 2027."
featured: true
---

# SecuBox : Reprenez le Contrôle Total de Votre Réseau

**Votre réseau domestique ou professionnel mérite une protection de niveau entreprise, sans la complexité ni le coût prohibitif.**

Après des années de développement de solutions de sécurité open source pour OpenWrt, nous sommes fiers de présenter **SecuBox** — une appliance de cybersécurité tout-en-un qui réunit nos 7 modules sur du hardware **GlobalScale Technologies** éprouvé et supporté.

---

## 🎯 Le Constat

Aujourd'hui, sécuriser son réseau implique de :

- ❌ Jongler entre multiples solutions incompatibles
- ❌ Passer des heures en configuration manuelle
- ❌ Payer des abonnements mensuels coûteux
- ❌ Faire confiance à des clouds propriétaires
- ❌ Manquer de visibilité sur son propre trafic

**SecuBox change la donne.**

---

## 💡 Notre Vision

> *"La sécurité réseau ne devrait pas être réservée aux grandes entreprises."*

SecuBox est une **appliance physique dédiée** basée sur les plateformes GlobalScale Technologies qui se place entre votre box opérateur et votre réseau local. Elle embarque tous nos modules de sécurité, préconfigurés et prêts à fonctionner.

```
┌─────────────┐      ┌─────────────────────┐      ┌─────────────┐
│   Internet  │──────│      SECUBOX        │──────│ Votre Réseau│
│  (Box FAI)  │      │  GlobalScale Inside │      │   (LAN)     │
└─────────────┘      └─────────────────────┘      └─────────────┘
```

---

## 🧩 Les 7 Modules Intégrés

### 1. 🛡️ CrowdSec — Cybersécurité Collaborative

**Blocage proactif des menaces grâce à l'intelligence collective.**

- 🌍 Base de données mondiale de 15M+ IPs malveillantes
- 🤖 Détection comportementale (brute-force, scans, bots)
- 🔄 Mise à jour temps réel de la threat intelligence
- 📊 Dashboard avec visualisation des attaques bloquées

[📖 Documentation](/apps/crowdsec) | [💻 GitHub](https://github.com/gkerma/luci-app-crowdsec-dashboard)

---

### 2. 📊 Netdata — Monitoring Temps Réel

**Surveillance complète de votre système avec alertes.**

- 📈 1000+ métriques collectées automatiquement
- ⚡ Rafraîchissement seconde par seconde
- 🚨 Alertes configurables (CPU, RAM, disque, réseau)
- 📱 Interface responsive mobile/desktop

[📖 Documentation](/apps/netdata) | [💻 GitHub](https://github.com/gkerma/luci-app-netdata-dashboard)

---

### 3. 🔍 Netifyd — Deep Packet Inspection

**Identifiez chaque application et protocole sur votre réseau.**

- 🎯 Reconnaissance de 300+ applications (Netflix, YouTube, Teams...)
- 📊 Statistiques de bande passante par app/client
- 🔒 Détection des protocoles à risque
- 📋 Catégorisation automatique du trafic

[📖 Documentation](/apps/netifyd) | [💻 GitHub](https://github.com/gkerma/luci-app-netifyd-dashboard)

---

### 4. 🔒 WireGuard — VPN Moderne

**Accès distant sécurisé à votre réseau, partout dans le monde.**

- ⚡ Performance supérieure (vs OpenVPN)
- 🔐 Cryptographie état de l'art
- 📱 QR codes pour configuration mobile instantanée
- 🌐 Multi-peers avec gestion simplifiée

[📖 Documentation](/apps/wireguard) | [💻 GitHub](https://github.com/gkerma/luci-app-wireguard-dashboard)

---

### 5. 🔀 Network Modes — Flexibilité Réseau

**Adaptez votre topologie selon vos besoins.**

- 🏠 Mode Routeur classique
- 🌉 Mode Bridge transparent
- 📡 Mode Point d'Accès WiFi
- 🔁 Mode Répéteur
- 🎭 Mode Travel Router

[📖 Documentation](/apps/network-modes) | [💻 GitHub](https://github.com/gkerma/luci-app-network-modes)

---

### 6. 🛡️ Client Guardian — NAC & Portail Captif

**Contrôle d'accès réseau de nouvelle génération.**

- ⏳ Quarantaine automatique des appareils inconnus
- 🚪 Portail captif personnalisable
- 👨‍👩‍👧‍👦 Contrôle parental avec plages horaires
- 🔔 Alertes SMS/Email en temps réel
- 🏠 Zones de sécurité (LAN, IoT, Invités, Enfants)

[📖 Documentation](/apps/client-guardian) | [💻 GitHub](https://github.com/gkerma/luci-app-client-guardian)

---

### 7. 🎛️ System Hub — Centre de Contrôle

**Une interface unifiée pour tout gérer.**

- 🧩 Vue d'ensemble de tous les modules
- 💚 Rapports de santé automatisés
- 🖥️ Assistance remote RustDesk intégrée
- 🔍 Collecte de diagnostics en un clic
- 📋 Logs unifiés de tous les composants

[📖 Documentation](/apps/system-hub) | [💻 GitHub](https://github.com/gkerma/luci-app-system-hub)

---

## 🔧 Gamme SecuBox — Hardware GlobalScale Technologies

### Pourquoi GlobalScale Technologies ?

- ✅ **Éprouvé** : Marvell Armada SoC depuis 2008 (SheevaPlug legacy)
- ✅ **Support Linux** : Mainline kernel, OpenWrt officiel
- ✅ **Networking natif** : Switch Topaz intégré, multi-Gigabit
- ✅ **Faible consommation** : < 15W
- ✅ **Made for networking** : Conçu spécifiquement pour routage/firewall
- ✅ **Certifié** : FCC, CE

---

## 📦 Les 4 Modèles SecuBox

### ☕ SecuBox Espresso — ESPRESSObin V7

*Idéal pour : Appartement, studio, télétravailleur solo*

| Spécification | Détail |
|---------------|--------|
| **SoC** | Marvell Armada 3720 Dual-Core A53 @1.2GHz |
| **RAM** | 1 GB ou 2 GB DDR4 |
| **Stockage** | microSD ou 4 GB eMMC |
| **Réseau** | 1x WAN + 2x LAN Gigabit (Switch Topaz 6341) |
| **WiFi** | Option miniPCIe 802.11ac |
| **Interfaces** | USB 3.0, SATA 3.0, miniPCIe |
| **Consommation** | < 5W |

| Variante | Hardware | Marge Dev | **Prix Campagne** |
|----------|----------|-----------|-------------------|
| 1GB DDR4 + SD | ~70€ | +130€ | **199€** |
| 2GB DDR4 + eMMC | ~90€ | +160€ | **249€** |

---

### ☕ SecuBox Espresso Ultra — ESPRESSObin Ultra

*Idéal pour : Maison connectée, famille, petit bureau*

| Spécification | Détail |
|---------------|--------|
| **SoC** | Marvell Armada 3720 Dual-Core A53 @1.2GHz |
| **RAM** | 1 GB ou 2 GB DDR4 |
| **Stockage** | 4 GB eMMC + M.2 2280 slot |
| **Réseau** | 1x WAN PoE (30W) + 4x LAN Gigabit |
| **WiFi** | 802.11ac dual-band intégré |
| **Interfaces** | USB 3.0, M.2, miniPCIe, NanoSIM |
| **PoE** | 30W via WAN |
| **Consommation** | < 8W |

| Variante | Hardware | Marge Dev | **Prix Campagne** |
|----------|----------|-----------|-------------------|
| 1GB + WiFi | ~120€ | +180€ | **299€** |
| 2GB + WiFi + PoE | ~150€ | +200€ | **349€** |

---

### 🔌 SecuBox Sheeva — Sheeva64 WiFi

*Idéal pour : Discret, plug & play, location Airbnb*

| Spécification | Détail |
|---------------|--------|
| **SoC** | Marvell Armada 3720 Dual-Core A53 @1.2GHz |
| **RAM** | 1 GB DDR4 |
| **Stockage** | 4 GB eMMC + microSD |
| **Réseau** | 2x Gigabit Ethernet natif |
| **WiFi** | 802.11ac 2x2 + Bluetooth 4.2 |
| **USB** | 2x USB 2.0 Type-A + micro-USB OTG |
| **Format** | Plug mural compact (alimentation intégrée) |
| **Consommation** | < 5W |

| Variante | Hardware | Marge Dev | **Prix Campagne** |
|----------|----------|-----------|-------------------|
| Sheeva64 (sans WiFi) | ~90€ | +160€ | **249€** |
| Sheeva64 WiFi | ~110€ | +190€ | **299€** |

---

### ☕ SecuBox Mocha — MOCHAbin

*Idéal pour : PME, grande maison, multi-sites, edge computing*

| Spécification | Détail |
|---------------|--------|
| **SoC** | Marvell Armada 7040 Quad-Core A72 @1.4GHz |
| **RAM** | 4 GB ou 8 GB DDR4 |
| **Stockage** | 16 GB eMMC + M.2 SATA + SATA HDD |
| **Réseau** | 1x WAN + 4x LAN Gigabit + **SFP+ 10G** |
| **WiFi** | Option WiFi 6 (802.11ax) + BT 5.0 |
| **Cellular** | Slot M.2 pour modem 4G/5G |
| **Interfaces** | 2x USB 3.0, PCIe, M.2 |
| **PoE** | Support 30W via WAN |
| **Consommation** | < 12W |

| Variante | Hardware | Marge Dev | **Prix Campagne** |
|----------|----------|-----------|-------------------|
| 4GB DDR4 | ~180€ | +270€ | **449€** |
| 4GB + WiFi 6 | ~220€ | +330€ | **549€** |
| 8GB DDR4 | ~220€ | +330€ | **549€** |
| 8GB + WiFi 6 + 5G | ~350€ | +450€ | **799€** |

---

## 💳 Abonnements SecuBox Care

### Pourquoi un abonnement optionnel ?

Le logiciel SecuBox est **100% open source et gratuit**. Les abonnements financent :

- 🔧 **Développement continu** de nouvelles fonctionnalités
- 🛡️ **Threat Intelligence premium** (au-delà de CrowdSec community)
- 📞 **Support technique** réactif
- 🖥️ **Assistance remote** via RustDesk
- ☁️ **Services cloud** optionnels (backup, monitoring externe)
- 🔬 **R&D** : nouveaux modules, intégrations, optimisations

---

### 🆓 SecuBox Care Free

**Gratuit à vie**

- ✅ Tous les 7 modules inclus
- ✅ Mises à jour de sécurité critiques
- ✅ CrowdSec Community blocklist
- ✅ Documentation en ligne
- ✅ Forum communautaire
- ❌ Support direct
- ❌ Threat Intel premium

---

### 🥉 SecuBox Care Basic

**9€/mois** ou **89€/an** *(2 mois offerts)*

- ✅ Tout Free +
- ✅ Support email (réponse 48h)
- ✅ Mises à jour fonctionnelles prioritaires
- ✅ Newsletter développeurs mensuelle
- ✅ Accès bêta nouvelles features
- ✅ 1 session assistance RustDesk/mois (30min)
- ✅ Guides de configuration avancés

---

### 🥈 SecuBox Care Pro

**19€/mois** ou **189€/an** *(2 mois offerts)*

- ✅ Tout Basic +
- ✅ Support email prioritaire (réponse 24h)
- ✅ **Threat Intelligence Premium** :
  - Blocklists sectorielles (finance, santé, industrie)
  - IOC (Indicators of Compromise) avancés
  - Alertes zero-day et CVE critiques
  - Réputation IP/domaine enrichie
- ✅ Sessions RustDesk illimitées
- ✅ Backup configuration cloud chiffré (E2E)
- ✅ Dashboard monitoring externe 24/7
- ✅ Rapports de sécurité mensuels PDF
- ✅ Webhooks et notifications Slack/Teams

---

### 🥇 SecuBox Care Enterprise

**49€/mois** ou **490€/an** *(2 mois offerts)*

- ✅ Tout Pro +
- ✅ Support téléphone (lun-ven 9h-18h)
- ✅ **SLA garanti** : réponse < 4h critique
- ✅ **Multi-sites** : jusqu'à 5 SecuBox
- ✅ API REST accès programmatique
- ✅ Intégration SIEM (Splunk, ELK, Graylog, Wazuh)
- ✅ Audit de sécurité annuel (rapport)
- ✅ Formation administrateur (2h visio)
- ✅ Personnalisation portail captif
- ✅ DNS sécurisé premium (malware, phishing)

---

### 🏢 SecuBox Care Corporate

**Sur devis** — *À partir de 149€/mois*

- ✅ Tout Enterprise +
- ✅ Support 24/7/365
- ✅ SLA < 1h incidents critiques
- ✅ **Sites illimités**
- ✅ Account manager dédié
- ✅ Développements sur mesure
- ✅ Formation sur site (France)
- ✅ Audit pentest annuel
- ✅ Conformité RGPD, ISO 27001
- ✅ Contrat de maintenance hardware

---

## 📊 Récapitulatif Tarifs

### Hardware SecuBox (achat unique)

| Modèle | Base | Usage Cible | Prix |
|--------|------|-------------|------|
| **Espresso** | ESPRESSObin V7 1GB | Studio/Solo | **199€** |
| **Espresso+** | ESPRESSObin V7 2GB | Appartement | **249€** |
| **Espresso Ultra** | ESPRESSObin Ultra 1GB | Maison | **299€** |
| **Espresso Ultra+** | ESPRESSObin Ultra 2GB PoE | Famille | **349€** |
| **Sheeva** | Sheeva64 | Discret/Airbnb | **249€** |
| **Sheeva WiFi** | Sheeva64 WiFi+BT | Plug & Play | **299€** |
| **Mocha** | MOCHAbin 4GB | PME | **449€** |
| **Mocha Pro** | MOCHAbin 4GB WiFi6 | Business | **549€** |
| **Mocha Max** | MOCHAbin 8GB | Multi-sites | **549€** |
| **Mocha Ultimate** | MOCHAbin 8GB WiFi6+5G | Enterprise | **799€** |

### Abonnements SecuBox Care (optionnel)

| Plan | Mensuel | Annuel | Inclus |
|------|---------|--------|--------|
| **Free** | 0€ | 0€ | Modules + MAJ sécurité |
| **Basic** | 9€ | 89€ | + Support email + Bêta |
| **Pro** | 19€ | 189€ | + Threat Intel + Backup cloud |
| **Enterprise** | 49€ | 490€ | + Multi-sites + SIEM + Formation |
| **Corporate** | 149€+ | Sur devis | + 24/7 + Illimité + Sur mesure |

---

## 🎁 Bundles Campagne Participative

### Early Bird (quantités limitées)

| Bundle | Contenu | Prix | Économie |
|--------|---------|------|----------|
| 🥉 **Starter** | Espresso + Basic 1 an | **249€** | 39€ |
| 🥈 **Family** | Espresso Ultra+ + Pro 1 an | **489€** | 49€ |
| 🥇 **Business** | Mocha Pro + Enterprise 1 an | **899€** | 140€ |
| 💎 **Multi-Site** | 2x Mocha + Enterprise 1 an | **1399€** | 189€ |
| 👑 **Founder** | Mocha Ultimate + Corporate 1 an | **1999€** | ~400€ |

---

## 🗓️ Calendrier Projet

```
Q1 2026  ████████████  Développement modules ✅
Q2 2026  ████████░░░░  Finalisation System Hub
Q3 2026  ░░░░░░░░░░░░  Intégration hardware GlobalScale
Q4 2026  ░░░░░░░░░░░░  Beta testeurs (100 unités)
Q1 2027  ░░░░░░░░░░░░  Préparation campagne
Q2 2027  ░░░░░░░░░░░░  🚀 LANCEMENT CROWDFUNDING
Q3 2027  ░░░░░░░░░░░░  Production & Tests
Q4 2027  ░░░░░░░░░░░░  📦 Livraison backers
```

---

## 🤝 Rejoignez la Communauté

### Newsletter

👉 **[newsletter.secubox.io](https://newsletter.secubox.io)**

### Discord

👉 **[discord.gg/secubox](https://discord.gg/secubox)**

### GitHub — Tous nos modules open source

| Repository | Description |
|------------|-------------|
| [luci-app-crowdsec-dashboard](https://github.com/gkerma/luci-app-crowdsec-dashboard) | Dashboard CrowdSec |
| [luci-app-netdata-dashboard](https://github.com/gkerma/luci-app-netdata-dashboard) | Dashboard Netdata |
| [luci-app-netifyd-dashboard](https://github.com/gkerma/luci-app-netifyd-dashboard) | Dashboard Netifyd |
| [luci-app-wireguard-dashboard](https://github.com/gkerma/luci-app-wireguard-dashboard) | Dashboard WireGuard |
| [luci-app-network-modes](https://github.com/gkerma/luci-app-network-modes) | Multi-mode réseau |
| [luci-app-client-guardian](https://github.com/gkerma/luci-app-client-guardian) | NAC & Portail Captif |
| [luci-app-system-hub](https://github.com/gkerma/luci-app-system-hub) | Centre de contrôle |

---

## 📞 Contact

**CyberMind.fr** — Solutions de Cybersécurité Open Source

- 🌐 [cybermind.fr](https://cybermind.fr)
- 📧 [contact@cybermind.fr](mailto:contact@cybermind.fr)
- 🐦 [@cybermind_fr](https://twitter.com/cybermind_fr)

---

**Inscrivez-vous à la newsletter pour ne pas manquer le lancement Q2 2027 !**

👉 **[newsletter.secubox.io](https://newsletter.secubox.io)**

---

*Article par [Gandalf @ CyberMind.fr](https://cybermind.fr) — Décembre 2025*

#SecuBox #OpenSource #Cybersécurité #Crowdfunding #OpenWrt #GlobalScale #MadeInFrance
