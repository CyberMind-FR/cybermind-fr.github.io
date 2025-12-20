---
title: "SecuBox : La Solution de Cybersécurité Tout-en-Un pour Votre Réseau"
date: 2024-12-20
categories: [Security, OpenWrt, Crowdfunding]
tags: [secubox, openwrt, security, crowdsec, wireguard, nac, firewall, crowdfunding, open-source]
author: Gandalf
image: /images/secubox-hero.png
description: "SecuBox réunit 7 modules de sécurité open source sur une box dédiée : CrowdSec, WireGuard, NAC, DPI, Monitoring et plus. Campagne participative 2026."
featured: true
---

# SecuBox : Reprenez le Contrôle Total de Votre Réseau

**Votre réseau domestique ou professionnel mérite une protection de niveau entreprise, sans la complexité ni le coût.**

Après des années de développement de solutions de sécurité open source pour OpenWrt, nous sommes fiers de présenter **SecuBox** — une appliance de cybersécurité tout-en-un qui réunit nos 7 modules dans un boîtier prêt à l'emploi.

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

SecuBox est une **box physique dédiée** qui se place entre votre box opérateur et votre réseau local. Elle embarque tous nos modules de sécurité, préconfigurés et prêts à fonctionner.

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   Internet  │──────│   SECUBOX   │──────│ Votre Réseau│
│  (Box FAI)  │      │  🛡️ 7 modules │      │   (LAN)     │
└─────────────┘      └─────────────┘      └─────────────┘
```

---

## 🧩 Les 7 Modules Intégrés

### 1. 🛡️ CrowdSec — Cybersécurité Collaborative

**Blocage proactif des menaces grâce à l'intelligence collective.**

- 🌍 Base de données mondiale de 15M+ IPs malveillantes
- 🤖 Détection comportementale (brute-force, scans, bots)
- 🔄 Mise à jour temps réel de la threat intelligence
- 📊 Dashboard avec visualisation des attaques bloquées

[📖 Documentation](/apps/crowdsec) | [💻 GitHub](https://github.com/gkerma/luci-app-crowdsec-status)

---

### 2. 📊 Netdata — Monitoring Temps Réel

**Surveillance complète de votre système avec alertes.**

- 📈 1000+ métriques collectées automatiquement
- ⚡ Rafraîchissement seconde par seconde
- 🚨 Alertes configurables (CPU, RAM, disque, réseau)
- 📱 Interface responsive mobile/desktop

[📖 Documentation](/apps/netdata) | [💻 GitHub](https://github.com/gkerma/luci-app-netdata-status)

---

### 3. 🔍 Netifyd — Deep Packet Inspection

**Identifiez chaque application et protocole sur votre réseau.**

- 🎯 Reconnaissance de 300+ applications (Netflix, YouTube, Teams...)
- 📊 Statistiques de bande passante par app/client
- 🔒 Détection des protocoles à risque
- 📋 Catégorisation automatique du trafic

[📖 Documentation](/apps/netifyd) | [💻 GitHub](https://github.com/gkerma/luci-app-netifyd-status)

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

## 📊 Comparatif des Solutions

| Fonctionnalité | Box FAI | Pare-feu Pro | SecuBox |
|----------------|---------|--------------|---------|
| Prix | "Gratuit"* | 500-2000€/an | **1990€ (une fois)** |
| Threat Intelligence | ❌ | ✅ | ✅ CrowdSec |
| VPN intégré | ❌ | ✅ | ✅ WireGuard |
| Contrôle parental | Basique | ✅ | ✅ Avancé |
| Deep Packet Inspection | ❌ | ✅ | ✅ Netifyd |
| Quarantaine auto | ❌ | Partiel | ✅ Client Guardian |
| Monitoring temps réel | ❌ | ✅ | ✅ Netdata |
| Open Source | ❌ | ❌ | ✅ 100% |
| Données locales | ❌ Cloud FAI | ❌ Cloud vendor | ✅ Chez vous |
| Mises à jour | Rares | Payantes | ✅ Gratuites à vie |

*\* Le prix est inclus dans votre abonnement, mais vos données transitent par leurs serveurs.*

---

## 🔧 Spécifications Techniques

### Hardware SecuBox v1 (Prévisionnel)

| Composant | Spécification |
|-----------|---------------|
| **CPU** | ARM Cortex-A72 Quad-Core 1.5GHz |
| **RAM** | 4 GB DDR4 |
| **Stockage** | 32 GB eMMC + slot microSD |
| **Ethernet** | 2x Gigabit (WAN + LAN) |
| **WiFi** | WiFi 6 (802.11ax) dual-band |
| **USB** | 2x USB 3.0 |
| **Alimentation** | USB-C 5V/3A (15W) |
| **Dimensions** | 12 x 12 x 3 cm |
| **Consommation** | < 10W idle, < 15W charge |

### Software Stack

| Couche | Technologie |
|--------|-------------|
| **OS** | OpenWrt 23.05+ |
| **Interface** | LuCI + Modules CyberMind |
| **Sécurité** | CrowdSec, iptables, WireGuard |
| **Monitoring** | Netdata, Netifyd |
| **Backend** | RPCD, UCI, ubus |

---

## 🎯 Cas d'Usage

### 🏠 Maison Connectée

> *"J'ai 15 objets connectés et 2 enfants. SecuBox isole automatiquement les IoT, bloque les contenus inappropriés et me prévient si un nouvel appareil se connecte."*

- Isolation IoT automatique
- Contrôle parental avec horaires
- Alertes intrusion SMS
- VPN pour accès distant

### 🏢 Petite Entreprise

> *"Nos 10 employés travaillent en hybride. SecuBox sécurise le bureau et leur permet de se connecter en VPN de n'importe où."*

- Portail captif pour visiteurs
- VPN employés avec QR codes
- Logs de connexion pour audit
- Blocage menaces CrowdSec

### 🏨 Location Airbnb

> *"Chaque voyageur a son propre réseau isolé avec portail de bienvenue. Mes caméras restent sur un réseau séparé."*

- Portail captif personnalisé
- Réseau invités isolé
- Protection des équipements propriétaire
- Quota de bande passante

### 🧑‍💻 Télétravailleur

> *"Je travaille sur des données sensibles. SecuBox chiffre tout mon trafic et bloque les tentatives de phishing."*

- VPN permanent vers le bureau
- Blocage sites malveillants
- Monitoring du trafic
- Alertes activité suspecte

---

## 🚀 Campagne Participative 2027

### Pourquoi le Crowdfunding ?

Nous croyons en la transparence et la communauté. Le crowdfunding nous permet de :

1. **Valider l'intérêt** du marché avant production
2. **Impliquer la communauté** dans le développement
3. **Rester indépendants** des investisseurs traditionnels
4. **Offrir des prix early-bird** avantageux

### Calendrier Prévisionnel

```
2024 Q4  ████████░░░░  Développement modules (FAIT ✅)
2025 Q1  ░░░░░░░░░░░░  Finalisation System Hub
2025 Q2  ░░░░░░░░░░░░  Prototypage hardware
2025 Q3  ░░░░░░░░░░░░  Beta testeurs (100 unités)
2025 Q4  ░░░░░░░░░░░░  Préparation campagne
Q2 2027  ░░░░░░░░░░░░  🚀 LANCEMENT CROWDFUNDING
Q3 2027  ░░░░░░░░░░░░  Production
2026 Q3  ░░░░░░░░░░░░  📦 Livraison backers
```

### Paliers de Financement

| Objectif | Déblocage |
|----------|-----------|
| **50 000 €** | Production 500 unités |
| **100 000 €** | + App mobile iOS/Android |
| **200 000 €** | + Boîtier aluminium premium |
| **500 000 €** | + WiFi 6E + 2.5Gb Ethernet |

### Récompenses Early Bird

| Tier | Prix | Inclus | Limité à |
|------|------|--------|----------|
| 🥉 **Pioneer** | 1490€ | SecuBox + 1 an support | 100 |
| 🥈 **Guardian** | 1990€ | SecuBox + 2 ans support + stickers | 500 |
| 🥇 **Protector** | 2990€ | SecuBox + lifetime support + t-shirt | 200 |
| 💎 **Defender** | 4990€ | 2x SecuBox + nom dans les crédits | 50 |
| 🏆 **Champion** | 9990€ | SecuBox custom + visite atelier | 10 |

---

## 🤝 Rejoignez la Communauté

### Newsletter

Inscrivez-vous pour être informé du lancement :

👉 **[newsletter.secubox.io](https://newsletter.secubox.io)**

### Discord

Rejoignez notre serveur pour échanger avec l'équipe et les beta-testeurs :

👉 **[discord.gg/secubox](https://discord.gg/secubox)**

### GitHub

Tous nos modules sont open source :

👉 **[github.com/gkerma](https://github.com/gkerma)**

| Repository | Description |
|------------|-------------|
| [luci-app-crowdsec-status](https://github.com/gkerma/luci-app-crowdsec-status) | Dashboard CrowdSec |
| [luci-app-netdata-status](https://github.com/gkerma/luci-app-netdata-status) | Dashboard Netdata |
| [luci-app-netifyd-status](https://github.com/gkerma/luci-app-netifyd-status) | Dashboard Netifyd |
| [luci-app-wireguard-dashboard](https://github.com/gkerma/luci-app-wireguard-dashboard) | Dashboard WireGuard |
| [luci-app-network-modes](https://github.com/gkerma/luci-app-network-modes) | Multi-mode réseau |
| [luci-app-client-guardian](https://github.com/gkerma/luci-app-client-guardian) | NAC & Portail Captif |
| [luci-app-system-hub](https://github.com/gkerma/luci-app-system-hub) | Centre de contrôle |

---

## ❓ FAQ

### Le logiciel est-il vraiment gratuit ?

**Oui, 100%.** Tous les modules sont sous licence Apache-2.0. Vous pouvez les installer sur n'importe quel routeur OpenWrt compatible. SecuBox est simplement une version "clé en main" avec hardware optimisé.

### Puis-je installer les modules sur mon routeur existant ?

**Absolument.** Consultez nos [démos interactives](/demos) et [guides d'installation](/docs). Nous recommandons un routeur avec au moins 256 MB de RAM et OpenWrt 22.03+.

### Mes données restent-elles chez moi ?

**Oui.** Aucune donnée ne quitte votre réseau. Les seules connexions sortantes sont :
- CrowdSec : synchronisation de la blocklist (anonymisée)
- Mises à jour : vérification des nouvelles versions

### Quelle est la différence avec un Pi-hole ?

Pi-hole bloque uniquement les publicités via DNS. SecuBox est une solution complète : firewall, VPN, NAC, monitoring, DPI. Pi-hole peut être installé en complément sur SecuBox.

### Y a-t-il un abonnement ?

**Non.** Prix unique, mises à jour gratuites à vie. Le support premium (prioritaire + assistance remote) est optionnel (49€/an).

---

## 📞 Contact

**CyberMind.fr** — Solutions de Cybersécurité Open Source

- 🌐 Website : [cybermind.fr](https://cybermind.fr)
- 📧 Email : [contact@cybermind.fr](mailto:contact@cybermind.fr)
- 🐦 Twitter : [@cybermind_fr](https://twitter.com/cybermind_fr)
- 💼 LinkedIn : [CyberMind](https://linkedin.com/company/cybermind-fr)

---

## 🎬 Conclusion

**SecuBox** représente des années de travail pour démocratiser la cybersécurité réseau. En combinant 7 modules open source éprouvés dans une appliance dédiée, nous rendons accessible à tous une protection de niveau professionnel.

La campagne participative de 2027 sera l'occasion de concrétiser cette vision avec votre soutien.

> *"La sécurité n'est pas un produit, mais un processus. SecuBox automatise ce processus pour vous."*

**Inscrivez-vous à la newsletter pour ne pas manquer le lancement !**

👉 **[newsletter.secubox.io](https://newsletter.secubox.io)**

---

*Article par [Gandalf @ CyberMind.fr](https://cybermind.fr) — Décembre 2024*

#SecuBox #OpenSource #Cybersécurité #Crowdfunding #OpenWrt #MadeInFrance
