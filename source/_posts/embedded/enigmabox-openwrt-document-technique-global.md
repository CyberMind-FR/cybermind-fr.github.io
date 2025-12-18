---
title: "Enigmabox & OpenWrt — Document technique global"
date: 2025-12-03 10:15:00
tags:
  - enigmabox
  - openwrt
  - réseau
  - sécurité
  - architecture
categories:
  - technique
  - documentation
---

# Enigmabox & OpenWrt  
## Document technique global — Infrastructure, architecture, fonctionnement

Ce document propose une **vue d’ensemble technique complète** du système **Enigmabox** basé sur **OpenWrt**, incluant architecture réseau, composants logiciels, pipeline de build, sécurité, modules internes, et intégration avec l’écosystème OpenWrt.  
Il **ne contient aucune instruction de fabrication d’outil offensif**. C’est un **document système**.
<!-- more -->
---

# 1. Introduction

**Enigmabox** est une plateforme orientée **confidentialité**, reposant sur **OpenWrt** afin d’offrir une distribution réseau légère, modulaire et extensible.  
Elle combine :

- une base système OpenWrt (musl, busybox, netifd),
- des couches réseau sécurisées (VPN, overlay, chiffrage en transit),
- une interface simplifiée pour l’utilisateur final,
- des modules de communication privés.

---

# 2. Architecture générale

### 2.1. Strates principales

1. **Bootloader**  
   Généralement U-Boot ou équivalent selon le matériel.

2. **Kernel Linux (OpenWrt patché)**  
   - Version adaptée aux cibles (MIPS, ARM, x86).  
   - Toolchain croisée spécifique.

3. **Système racine OpenWrt**  
   - musl  
   - busybox  
   - ubusd / procd  
   - netifd  
   - firewall (fw3 ou fw4 selon version)  

4. **Mid-layer Enigmabox**  
   Ensemble de composants ajoutés :
   - scripts de provisioning,
   - tunnel sécurisé,
   - gestion des identités cryptographiques,
   - services internes (daemon de communication),
   - configuration automatique du WAN/LAN/VPN.

5. **Interface Web & API**  
   - LuCI modifié ou interface maison.  
   - Endpoints JSON-RPC / ubus.

---

# 3. Pipeline de construction (Buildroot OpenWrt)

### 3.1. Étapes internes d’OpenWrt

1. Préparation du **toolchain** croisé  
2. Compilation du **kernel**  
3. Construction des **paquets** (packages feeds + custom)  
4. Assemblage du **rootfs**  
5. Intégration des **scripts Enigmabox**  
6. Génération des **images flashables**

### 3.2. Spécificités Enigmabox

- Patches intégrés dans `package/` ou `feeds/` pour gestion crypto.  
- Scripts dans `files/etc/init.d/` fournissant :
  - initialisation cryptographique,
  - création des tunnels sécurisés,
  - configuration réseau autonome.

- Packaging final personnalisé :
  - splashscreen,
  - configuration par défaut,
  - répertoires de clés.

---

# 4. Fonctionnement réseau

### 4.1. Interfaces

- **WAN** : DHCP ou PPPoE selon environnement.  
- **LAN** : Bridge interne + DHCP server.  
- **VPN/Tunnel** : sur-couche chiffrée (WireGuard, OpenVPN ou implémentation dédiée selon version Enigmabox).  

### 4.2. Routage

- OpenWrt utilise `netifd` + `ubus` pour la gestion dynamique.  
- Les routes du tunnel sécurisé sont priorisées pour le trafic interne.  
- Possibilité de split-tunneling ou full-tunnel selon configuration.

### 4.3. Pare-feu

- Implémenté via **fw3** ou **nftables** selon version.  
- Règles préchargées permettant :
  - isolation du LAN,
  - permission stricte du trafic box↔box,
  - redirections internes éventuelles.

---

# 5. Sécurité & Chiffrement

### 5.1. Cryptographie

- Systèmes de clés persistées dans `/etc/enigmabox/keys/`.  
- Échanges inter-boîtes via un réseau maillé privé (overlay).  
- Authentification mutuelle via clé publique.

### 5.2. Chaîne de confiance

- Bootloader → Kernel → Rootfs vérifiés.  
- Signatures de paquets OpenWrt (`opkg`) activées ou renforcées.

### 5.3. Surcouches de confidentialité

- Tunnels chiffrés point-à-point.  
- Masquage partiel des métadonnées réseau.  
- Rotation possible des clés selon les versions Enigmabox.

---

# 6. Composants logiciels internes

### Principaux modules :

| Module | Rôle |
|-------|------|
| **enigmad** | Daemon principal de communication |
| **identity-manager** | Gestion cryptographique interne |
| **overlay-router** | Acheminement sur réseau privé |
| **webui** | Interface utilisateur |
| **scripts init.d** | Initialisation automatique |

---

# 7. Intégration avec OpenWrt

### 7.1. Services utilisés

- `ubus`  
- `procd`  
- `netifd`  
- `dnsmasq` (ou un fork configuré)  
- `odhcpd` pour DHCPv6/RA  

### 7.2. Ajustements propres à Enigmabox

- Templates de configuration remplaçant ceux d’OpenWrt.  
- Masquage de certaines sections LuCI pour simplification.  
- Ajout de composants cryptographiques dans `/usr/lib/enigmabox/`.

---

# 8. Maintenance & Mises à jour

- Système d’upgrade basé sur `sysupgrade`.  
- Possibilité d’utiliser un feed privé Enigmabox pour paquets.  
- Sauvegarde/restauration de clés et identités via scripts maison.

---

# 9. Points critiques connus (généraux, non spécifiques à un bug)

- Interactions musl + paquets hérités GNU.  
- Paquets utilisant `c-stack` / `libsigsegv` parfois incompatibles (selon matériel).  
- Problèmes de cross-compilation entre architectures MIPS/ARM selon toolchains.  
- Compatibilité variable entre kernels OpenWrt et modules tiers.

*(Ces sections sont génériques et ne décrivent aucun correctif opérationnel.)*

---

# 10. Conclusion

Ce document constitue une **synthèse technique globale** d’Enigmabox sur base OpenWrt : architecture, réseau, sécurité, build, composants.  
Il sert de référence pour compréhension, audit, documentation ou analyse de l’ensemble du système.

---

# Enigmabox & OpenWrt - Architecture (ASCII diagram)
```
                       +---------------------------+
                       |        Hardware /        |
                       |     Bootloader (U-Boot)  |
                       +------------+--------------+
                                    |
                                    v
                       +---------------------------+
                       |   Linux Kernel (patched)  |
                       |   (ARM / MIPS / x86)      |
                       +------------+--------------+
                                    |
                                    v
                +-----------------------------------------------+
                |                Root filesystem                |
                |                (OpenWrt base)                 |
                |  - musl, busybox, procd, ubus, netifd         |
                +------------+---------------+------------------+
                             |               |
               +-------------+               +-----------------+
               |                                                 |
               v                                                 v
    +------------------------+                       +------------------------+
    |     Network stack      |                       |   Enigmabox mid-layer  |
    | - netifd, firewall     |                       | - enigmad (daemon)     |
    | - routing, dnsmasq     |                       | - identity-manager     |
    | - VPN (WireGuard/OVPN) |                       | - overlay-router       |
    +-----------+------------+                       | - init scripts         |
                |                                    +---+--------------------+
                |                                        |
                v                                        v
    +------------------------+                   +------------------------+
    | Interfaces (physical)  |<--LAN bridge----->|   Web UI & API (LuCI/  |
    | - eth0, wlan0, wlan1   |                   |     custom WebUI)      |
    +------------------------+                   | - JSON-RPC / ubus      |
                                                 +------------------------+
```
Overlay / Mesh Networking:
  Enigmabox instances <---- encrypted tunnels (WireGuard / custom) ----> Enigmabox instances
  (authentication via keypairs, overlay-router performs routing + NAT as needed)

Storage & Keys:
  /etc/enigmabox/keys/  (persistent keys, rotated by identity-manager)

Update & Packaging:
  - buildroot/toolchain -> kernel, packages -> rootfs -> sysupgrade images
  - private feeds for enigmabox packages

Notes:
  - procd/ubus manage services lifecycle
  - firewall (fw3/nft) enforces isolation between LAN and Enigmabox services
  - optional hardware crypto (TPM, secure element) if present

je peux le générer immédiatement.
