---
title: "Network Modes Dashboard : Configuration Multi-Mode pour OpenWrt"
date: 2024-12-20
author: Gandalf
categories: [OpenWrt, LuCI, Réseau, Sécurité]
tags: [openwrt, luci, network-modes, firewall, wifi, wireguard, proxy, nginx]
image: /images/network-modes-dashboard-hero.png
description: "Dashboard LuCI pour configurer OpenWrt en différents modes réseau : Sniffer, Point d'Accès, Relay et Routeur complet"
---

# Network Modes Dashboard : La Flexibilité Réseau Ultime

Votre routeur OpenWrt peut être bien plus qu'un simple routeur. Avec **Network Modes Dashboard**, transformez-le instantanément en analyseur réseau, point d'accès WiFi optimisé, relais VPN ou routeur complet avec reverse proxy.

## 🎯 Quatre Modes, Infinies Possibilités

| Mode | Usage Principal | Fonctionnalités Clés |
|------|-----------------|---------------------|
| 🔍 **Sniffer** | Analyse réseau passive | Bridge transparent, Netifyd DPI, Promiscuous |
| 📶 **Access Point** | WiFi haute performance | 802.11r/k/v, Band Steering, Beamforming |
| 🔄 **Relay** | Extension réseau sécurisée | Relayd, WireGuard, Optimisation MTU/MSS |
| 🌐 **Router** | Routeur complet | NAT, Firewall, Proxy, HTTPS Frontend |

## 🔍 Mode Sniffer / Passthrough

Le mode **Sniffer** transforme votre routeur en pont Ethernet transparent, idéal pour l'analyse réseau avec Netifyd.

### Caractéristiques

- **Pas d'adresse IP** : Le routeur est invisible sur le réseau
- **Bridge Ethernet pur** : Tout le trafic passe sans modification
- **Mode promiscuous** : Capture de tous les paquets
- **Intégration Netifyd** : Deep Packet Inspection en temps réel

### Cas d'usage

- Audit de sécurité réseau
- Analyse de trafic pour troubleshooting
- Détection d'anomalies et intrusions
- Formation et démonstration

```
┌─────────┐     ┌──────────────┐     ┌─────────┐
│ Réseau  │────▶│   OpenWrt    │────▶│ Réseau  │
│  LAN    │     │   (Bridge)   │     │  WAN    │
└─────────┘     │   Netifyd    │     └─────────┘
                └──────────────┘
                      │
                      ▼
                 [Analyse DPI]
```

## 📶 Mode Access Point

Optimisez votre WiFi avec les dernières technologies de roaming et de gestion radio.

### Technologies supportées

#### 802.11r - Fast BSS Transition
Roaming rapide entre points d'accès (< 50ms). Essentiel pour la VoIP et le streaming.

#### 802.11k - Radio Resource Management
Le client reçoit des informations sur les AP voisins pour un roaming intelligent.

#### 802.11v - BSS Transition Management
L'AP peut suggérer au client de se déplacer vers un meilleur point d'accès.

#### Band Steering
Dirige automatiquement les clients compatibles vers la bande 5 GHz moins encombrée.

### Configuration recommandée

| Paramètre | Valeur | Description |
|-----------|--------|-------------|
| Channel 5GHz | 36 ou 149 | Éviter DFS si possible |
| HT Mode | VHT80 | Bon compromis performance/compatibilité |
| TX Power | 17-20 dBm | Éviter la surpuissance |
| Beacon Interval | 100ms | Standard |

## 🔄 Mode Relay / Extender

Étendez votre réseau avec une connexion sécurisée via WireGuard.

### Architecture Relay

```
┌─────────────┐                    ┌─────────────┐
│   Réseau    │◀───── WiFi ───────▶│   OpenWrt   │
│  Principal  │      Client        │   Relay     │
└─────────────┘                    └──────┬──────┘
                                          │
                    ┌─────────────────────┼─────────────────────┐
                    │                     │                     │
                    ▼                     ▼                     ▼
              [LAN Devices]        [WireGuard VPN]        [WiFi AP]
```

### Optimisations incluses

- **MTU automatique** : Calcul optimal pour les tunnels
- **MSS Clamping** : Évite la fragmentation TCP
- **TCP BBR** : Contrôle de congestion moderne
- **Conntrack optimisé** : Gestion efficace des connexions

### Configuration WireGuard

Le mode Relay intègre WireGuard pour :
- Chiffrement de tout le trafic sortant
- Site-to-site VPN vers le réseau principal
- Split tunneling configurable

## 🌐 Mode Router

Le mode complet avec toutes les fonctionnalités d'un routeur professionnel.

### Gestion WAN

- **DHCP** : Configuration automatique
- **Static** : IP fixe avec gateway
- **PPPoE** : Pour connexions ADSL/Fibre
- **L2TP/PPTP** : VPN opérateur

### Firewall

Protection complète avec :
- Zones WAN/LAN/VPN
- Protection SYN flood
- Port forwarding
- DMZ configurable

### Proxy Web

Choix entre plusieurs solutions :

| Proxy | Avantages | Usage |
|-------|-----------|-------|
| **Squid** | Cache HTTP, ACLs avancées | Entreprise |
| **TinyProxy** | Léger, simple | Ressources limitées |
| **Privoxy** | Filtrage contenu, vie privée | Usage personnel |

### Reverse Proxy HTTPS

Exposez plusieurs services sur une seule IP publique :

```
                          ┌──────────────────┐
                          │    Internet      │
                          └────────┬─────────┘
                                   │
                          ┌────────▼─────────┐
                          │  OpenWrt Router  │
                          │  (Nginx/HAProxy) │
                          │   Let's Encrypt  │
                          └────────┬─────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
        ▼                          ▼                          ▼
┌───────────────┐        ┌───────────────┐        ┌───────────────┐
│  Nextcloud    │        │ Home Assistant │        │   Jellyfin    │
│ :443 → :443   │        │ :443 → :8123   │        │ :443 → :8096  │
└───────────────┘        └───────────────┘        └───────────────┘
```

#### Virtual Hosts

Configurez facilement plusieurs domaines :
- Certificats Let's Encrypt automatiques
- Backends avec health checks
- Headers de sécurité (HSTS, CSP)

## 🎨 Interface Utilisateur

Le dashboard adopte un thème **orange/ambre** évoquant la flexibilité et la configuration.

### Design System

- **Couleur primaire** : Orange #f97316
- **Gradient** : Orange → Ambre → Jaune
- **Fond** : Noir profond #0c0a09
- **Typographie** : Inter (UI) + JetBrains Mono (données)

### Couleurs par Mode

| Mode | Couleur | Code |
|------|---------|------|
| Sniffer | Violet | #8b5cf6 |
| Access Point | Cyan | #06b6d4 |
| Relay | Vert | #10b981 |
| Router | Orange | #f97316 |

## 📦 Installation

### Prérequis

```bash
opkg update
opkg install luci-base rpcd
```

### Dépendances par mode

```bash
# Sniffer
opkg install netifyd

# Access Point
opkg install hostapd-openssl wpad-openssl

# Relay
opkg install relayd wireguard-tools

# Router
opkg install squid nginx-ssl acme
```

### Installation du package

```bash
# Depuis les sources
git clone https://github.com/gkerma/luci-app-network-modes.git
cd luci-app-network-modes
make package/luci-app-network-modes/compile V=s

# Ou installation manuelle
scp luci-app-network-modes_*.ipk root@router:/tmp/
ssh root@router "opkg install /tmp/luci-app-network-modes_*.ipk"
```

### Accès

**Network → Network Modes**

## 🔒 Sécurité

### Changement de mode

- **Backup automatique** avant chaque changement
- Configuration précédente restaurable
- Journal des modifications

### Isolation des modes

- Le mode Sniffer désactive le routage IP
- Les clés WireGuard ne sont jamais exposées
- ACL LuCI pour contrôle d'accès

## 📊 Comparaison des Modes

| Fonctionnalité | Sniffer | AP | Relay | Router |
|----------------|:-------:|:--:|:-----:|:------:|
| Adresse IP | ❌ | ✅ | ✅ | ✅ |
| WiFi AP | ❌ | ✅ | ⚡ | ⚡ |
| NAT | ❌ | ❌ | ❌ | ✅ |
| Firewall | ❌ | ❌ | ⚡ | ✅ |
| WireGuard | ❌ | ❌ | ✅ | ⚡ |
| Proxy | ❌ | ❌ | ❌ | ✅ |
| Netifyd DPI | ✅ | ⚡ | ⚡ | ⚡ |

✅ = Inclus | ⚡ = Optionnel | ❌ = Non disponible

## 🚀 Roadmap

- [ ] Mode Mesh (802.11s)
- [ ] Intégration CrowdSec
- [ ] Failover WAN automatique
- [ ] QoS par application
- [ ] Dashboard statistiques temps réel
- [ ] Export/Import configuration

## 🔗 Ressources

- **Démo interactive** : [Essayer la démo](/demos/network-modes/)
- **GitHub** : [github.com/gkerma/luci-app-network-modes](https://github.com/gkerma/luci-app-network-modes)
- **Documentation OpenWrt** : [openwrt.org/docs](https://openwrt.org/docs/)

---

*Network Modes Dashboard - La flexibilité réseau à portée de clic* ⚙️
