---
title: "SecuBox OpenWrt : Analyse Technique Complète de la Suite de Sécurité"
date: 2026-01-11
updated: 2026-01-11
categories:
  - Sécurité
  - OpenWrt
  - Projets
tags:
  - secubox
  - openwrt
  - crowdsec
  - firewall
  - iot
  - vpn
  - cybersecurity
  - open-source
keywords:
  - SecuBox
  - OpenWrt sécurité
  - CrowdSec dashboard
  - routeur sécurisé
  - pare-feu embarqué
  - domotique sécurisée
description: "Découvrez SecuBox, la suite de sécurité modulaire pour OpenWrt développée par CyberMind.FR. Analyse approfondie des 35+ modules : CrowdSec, DPI, contrôle parental, IoT, VPN et plus encore."
thumbnail: /images/secubox/secubox-hero.png
cover: /images/secubox/secubox-banner.png
author: Gandalf
toc: true
comments: true
---

# 🛡️ SecuBox OpenWrt : La Suite de Sécurité Nouvelle Génération

> **SecuBox** est une suite de sécurité et de gestion réseau complète pour routeurs OpenWrt, développée par **CyberMind.FR**. Avec plus de **35 modules**, elle transforme n'importe quel routeur compatible en appliance de sécurité professionnelle.

<!-- more -->

## 📊 Vue d'Ensemble du Projet

| 📈 Métrique | 📋 Valeur |
|-------------|-----------|
| 📦 Packages totaux | **35+** |
| 🖥️ Applications LuCI | **22** |
| ⚙️ Services backend | **13** |
| 🏗️ Architectures supportées | **15+** |
| 🔌 Méthodes RPCD | **150+** |
| 📅 Versions OpenWrt | **21.02 → 25.12** |

---

## 🎯 Capacités Principales

SecuBox offre un écosystème unifié couvrant tous les aspects de la sécurité réseau :

- 🛡️ **Intelligence Collaborative** : Intégration CrowdSec avec réputation IP communautaire
- 🔍 **Inspection Profonde** : Détection d'applications et protocoles via Netifyd DPI
- 🚪 **Contrôle d'Accès** : Client Guardian avec portail captif et contrôle parental
- 🔐 **Sécurité Matérielle** : Gestion de clés HSM (Nitrokey/YubiKey)
- 📡 **Pont IoT** : MQTT avec 17+ types d'adaptateurs USB (Zigbee, Z-Wave, ModBus)
- 🎬 **Intelligence Média** : Détection de streaming avec estimation de qualité
- 🌐 **Réseau Avancé** : VPN, proxy inverse, cache CDN, gestion QoS

---

## 🔒 Modules de Sécurité

### 🛡️ CrowdSec Dashboard (v0.6.0)

Le module phare de SecuBox intègre **CrowdSec**, le moteur de sécurité collaboratif open-source. Il offre une surveillance en temps réel des menaces avec partage communautaire de l'intelligence.

#### ✨ Fonctionnalités

| 🎯 Fonction | 📝 Description |
|-------------|----------------|
| 🚫 Gestion des bans | Visualisation et contrôle des IP bloquées |
| ⚠️ Alertes temps réel | Notification des tentatives d'intrusion |
| 📊 Métriques moteur | Statistiques parseurs, scénarios, bouncers |
| 🌍 Géolocalisation | Carte des menaces par pays |
| 🔧 Hub Collections | Installation/suppression de parseurs et scénarios |
| 🖥️ Console CrowdSec | Enrôlement pour gestion centralisée |

#### 🔌 API RPCD (22 endpoints)

```bash
# Exemples d'appels ubus
ubus call luci.crowdsec-dashboard decisions      # Liste des bans actifs
ubus call luci.crowdsec-dashboard alerts '{"limit":50}'  # Alertes récentes
ubus call luci.crowdsec-dashboard ban '{"ip":"1.2.3.4","duration":"24h"}'
ubus call luci.crowdsec-dashboard metrics        # Statistiques moteur
ubus call luci.crowdsec-dashboard console_enroll '{"key":"xxx"}'
```

#### 🔐 Séparation ACL

Les permissions sont strictement séparées :
- **📖 Lecture** : decisions, alerts, metrics, status, bouncers, collections
- **✏️ Écriture** : ban, unban, configure_metrics, install_collection, service_control

---

### 🔑 Key Storage Manager - KSM (v0.4.0)

Gestion cryptographique de niveau entreprise avec support **HSM matériel** pour Nitrokey et YubiKey.

#### 🔐 Périphériques HSM Supportés

| 🔧 Appareil | 🆔 VID:PID | 💪 Capacités |
|-------------|------------|--------------|
| 🔴 Nitrokey Pro 2 | `20a0:42b1` | RSA, ECDSA, Ed25519 |
| 🔴 Nitrokey Storage | `20a0:42b2` | + Stockage chiffré |
| 🟢 YubiKey 5 | `1050:*` | FIDO2, PIV, OpenPGP |

#### ✨ Fonctionnalités Clés

- 🔑 **Génération de clés** : RSA (2048/4096), ECDSA (P-256/P-384), Ed25519
- 📤 **Import/Export** : Formats PEM, DER, PKCS#12 avec protection par phrase de passe
- 📜 **Gestion certificats** : Génération CSR, vérification chaîne, alertes expiration
- 🔒 **Stockage secrets** : Chiffrement AES-256-GCM avec rotation automatique
- 📋 **Journalisation** : Audit complet avec export CSV

```bash
# Génération de clé sur HSM
ubus call luci.ksm-manager generate_hsm_key '{
  "serial": "NITROKEY-001",
  "key_type": "ed25519",
  "label": "vpn-server-key"
}'
```

---

### 👨‍👩‍👧‍👦 Client Guardian NAC (v0.4.0)

Système de **Contrôle d'Accès Réseau** implémentant les principes Zero Trust avec quarantaine automatique des appareils inconnus.

#### 🏠 Architecture des Zones

| 🏷️ Zone | 🌐 Internet | 🏠 Local | 🔒 Isolation | 🚪 Portail |
|---------|-------------|----------|--------------|------------|
| 🟢 **LAN Privé** | ✅ Complet | ✅ Complet | ❌ Non | ❌ Non |
| 🔵 **IoT** | ✅ Complet | ❌ Non | ✅ Oui | ❌ Non |
| 🟡 **Enfants** | ⚠️ Filtré | ✅ Complet | ❌ Non | ❌ Non |
| 🟠 **Invités** | ⚠️ Limité | ❌ Non | ✅ Oui | ✅ Oui |
| 🔴 **Quarantaine** | ❌ Portail seul | ❌ Non | ✅ Oui | ✅ Oui |
| ⚫ **Bloqué** | ❌ Aucun | ❌ Aucun | ✅ Oui | ❌ Non |

#### 👶 Contrôle Parental

- ⏰ **Plages horaires** : Blocage nocturne, heures scolaires configurables
- 🚫 **Filtrage contenu** : Adulte, violence, jeux d'argent
- 🔍 **SafeSearch forcé** : Google, Bing, YouTube mode restreint
- ⏱️ **Quotas écran** : Limites journalières avec application automatique
- 📱 **Alertes** : SMS (Twilio/Nexmo/OVH) et notifications email

```bash
# Approuver un client en quarantaine
ubus call luci.client-guardian approve_client '{
  "mac": "AA:BB:CC:DD:EE:FF",
  "name": "iPhone de Marie",
  "zone": "children"
}'
```

---

### 🔐 Auth Guardian (v0.4.0)

Système d'authentification complet avec support **OAuth2/OIDC**.

#### 🎫 Fonctionnalités

- 🎨 **Portail captif** personnalisable avec logo et CGU
- 🔑 **OAuth intégré** : Google, GitHub, Facebook, Twitter/X
- 🎟️ **Système vouchers** : Codes d'accès temporaires avec limites bande passante
- 🍪 **Sessions sécurisées** : HttpOnly, SameSite, timeout configurable
- ⏭️ **Règles bypass** : Whitelist MAC, IP, domaines

---

## 🌐 Modules Réseau

### 🔄 Network Modes (v0.3.6)

Changement de configuration réseau en **un clic** avec gestion automatique des services.

#### 📡 Modes Disponibles

| 🎯 Mode | 📝 Configuration |
|---------|------------------|
| 🔍 **Sniffer Bridge** | Pont L2 transparent, mode promiscuité, analyse inline |
| 👁️ **Sniffer Passive** | Monitoring via SPAN/TAP, zero impact réseau |
| 📶 **Point d'Accès** | WiFi AP avec roaming 802.11r/k/v, band steering |
| 🔄 **Relay/Extender** | Relais réseau avec VPN WireGuard, optimisation MTU/BBR |
| 🌐 **Routeur** | Routeur complet avec proxy, DNS-over-HTTPS, reverse proxy |

#### 🆕 Nouveautés v0.3.6

- 🔐 **Automatisation WireGuard** : Génération paires de clés, déploiement interface `wg0`
- ⚡ **Optimisations TCP** : MTU clamping, TCP BBR automatique
- 🔧 **Proxies intégrés** : Squid/TinyProxy/Privoxy avec redirection transparente

---

### 📊 Bandwidth Manager (v0.4.0)

Gestion avancée de la **QoS** avec intégration SQM/CAKE et quotas par client.

#### 🎚️ Classes de Priorité QoS

| ⬆️ Priorité | 🎯 Usage Typique | ⚙️ Comportement |
|-------------|------------------|-----------------|
| 1️⃣ (Haute) | VoIP, Visio | Bande passante garantie, latence minimale |
| 2️⃣ | Gaming | Priorité faible latence |
| 3️⃣-4️⃣ | Interactif | Navigation web, SSH |
| 5️⃣ (Normal) | Défaut | Trafic standard |
| 6️⃣-7️⃣ | Streaming | Téléchargements avec burst autorisé |
| 8️⃣ (Basse) | Background | Torrents, sauvegardes, mises à jour |

#### 📏 Gestion des Quotas

```bash
# Définir un quota mensuel
ubus call luci.bandwidth-manager set_quota '{
  "mac": "AA:BB:CC:DD:EE:FF",
  "name": "Tablette Enfant",
  "limit_mb": 10240,
  "action": "throttle",
  "reset_day": 1
}'
```

- 📊 Quotas mensuels par adresse MAC
- ⚙️ Actions configurables : throttle, block, notify
- 🔄 Reset automatique mensuel
- 📈 Dashboard temps réel avec visualisation progression

---

### 🏠 VHost Manager (v2.0.0)

Gestion de **proxy inverse nginx** avec certificats SSL Let's Encrypt automatisés.

#### 📦 Templates de Services Internes (19 disponibles)

| 🎯 Service | 📂 Catégorie | ⚙️ Configuration |
|------------|--------------|------------------|
| ☁️ Nextcloud | Productivité | SSL, WebSocket, auth personnalisée |
| 🏠 Home Assistant | IoT | SSL requis, WebSocket |
| 🎬 Jellyfin | Media | SSL, optimisé streaming |
| 🔐 Vaultwarden | Sécurité | SSL requis, WebSocket |
| 🐙 Gitea | Productivité | SSL, support protocole Git |
| 🐳 Portainer | Hosting | SSL, gestion Docker |
| 📊 Netdata | Monitoring | SSL optionnel |
| 🛡️ CrowdSec | Sécurité | SSL, API locale |

#### ↪️ Règles de Redirection

| 🏷️ Template | 📤 Code HTTP | 🎯 Usage |
|-------------|--------------|----------|
| 🎮 Steam CDN cache | 302 | Redirection vers cache local |
| 🔒 YouTube → Invidious | 307 | Redirection vie privée |
| 📧 Mail failover | 302 | Basculement serveur mail |
| 🚫 Ad Blocker | 301 | Redirection serveurs pub |

---

### 💾 CDN Cache (v0.5.0)

Proxy cache **CDN local** pour optimiser la bande passante.

#### 📊 Performances Typiques

- 🎯 **Hit ratio** : 60-80%
- 💰 **Économies** : 40-60% de bande passante
- ⚡ **Latence** : < 1ms pour les hits

#### 📋 Policies de Cache

| 📦 Policy | 🌐 Domaines | 📁 Extensions | ⏱️ Durée |
|-----------|-------------|---------------|----------|
| 🪟 Windows Update | windowsupdate.com | exe, msu, cab | 7 jours |
| 🐧 Linux Repos | archive.ubuntu.com, deb.debian.org | deb, rpm | 3 jours |
| 📄 Contenu Statique | * | js, css, png, jpg, woff | 1 jour |

---

### 🔐 WireGuard Dashboard (v0.5.0)

Tableau de bord moderne pour la supervision **VPN WireGuard**.

#### 📊 Indicateurs de Statut Peer

| 🔵 Statut | 📝 Signification | ⏱️ Âge Handshake |
|-----------|------------------|------------------|
| 🟢 Actif | Communication récente | < 3 minutes |
| 🟡 Idle | Pas de trafic récent | 3-10 minutes |
| ⚪ Inactif | Pas de handshake | > 10 minutes |

#### 🔒 Sécurité

> ⚠️ **Important** : Les clés privées ne sont **jamais** exposées via le dashboard. Seules les clés publiques et configurations sont affichées.

---

## 📡 IoT & Domotique

### 🔌 MQTT IoT Bridge (v0.5.0)

Pont **USB vers MQTT** avec détection automatique de 17+ types d'adaptateurs IoT.

#### 📻 Adaptateurs USB Supportés

##### 📡 Zigbee (6 appareils)

| 🔧 Appareil | 🆔 VID:PID | 📝 Notes |
|-------------|------------|----------|
| 🔵 Texas Instruments CC2531 | `0451:16a8` | Classique, bien supporté |
| 🟣 ConBee II (Dresden) | `1cf1:0030` | Recommandé |
| 🟢 Sonoff Zigbee 3.0 Plus | `1a86:55d4` | Bon rapport qualité/prix |
| ⚪ Silicon Labs CP2102 | `10c4:ea60` | Générique |

##### 📻 Z-Wave (3 appareils)

| 🔧 Appareil | 🆔 VID:PID |
|-------------|------------|
| 🔵 Aeotec Z-Stick Gen5 | `0658:0200` |
| 🟢 Aeotec Z-Stick 7 | `0658:0280` |
| ⚪ Z-Wave.Me UZB | `10c4:8a2a` |

##### 🔌 ModBus RTU (4 appareils)

| 🔧 Appareil | 🆔 VID:PID |
|-------------|------------|
| 🔵 FTDI FT232 | `0403:6001` |
| 🟣 Prolific PL2303 | `067b:2303` |
| 🟢 CH340 | `1a86:7523` |
| ⚪ CP210x UART | `10c4:ea60` |

#### 🔗 Intégrations

```yaml
# Home Assistant - configuration.yaml
mqtt:
  broker: <ip-routeur-openwrt>
  port: 1883
  username: secubox
  password: secubox
  discovery: true
  discovery_prefix: homeassistant
```

```yaml
# Zigbee2MQTT - configuration.yaml
serial:
  port: /dev/ttyUSB0
  adapter: zstack
mqtt:
  base_topic: zigbee2mqtt
  server: mqtt://<ip-routeur-openwrt>
```

---

### 🎬 Media Flow (v0.5.2)

Détection en temps réel des **services de streaming** avec estimation de qualité.

#### 📺 Services Détectés

| 📂 Catégorie | 🎯 Services |
|--------------|-------------|
| 🎬 **Vidéo** | Netflix, YouTube, Disney+, Prime Video, Twitch, HBO, Hulu, Vimeo |
| 🎵 **Audio** | Spotify, Apple Music, Deezer, SoundCloud, Tidal, Pandora |
| 📹 **Visio** | Zoom, Microsoft Teams, Google Meet, Discord, Skype, WebEx |

#### 📊 Estimation de Qualité

| 📺 Qualité | 📈 Bande Passante |
|------------|-------------------|
| 📺 SD | < 1 Mbps |
| 📺 HD | 1-3 Mbps |
| 📺 FHD (1080p) | 3-8 Mbps |
| 📺 4K UHD | > 8 Mbps |

```bash
# Configurer une alerte de consommation
ubus call luci.media-flow set_alert '{
  "service": "Netflix",
  "threshold_hours": 4,
  "action": "notify"
}'
```

---

## 🖥️ Système & Infrastructure

### 🎛️ System Hub (v1.0.0)

Centre de contrôle **système unifié** pour OpenWrt.

#### ✨ Fonctionnalités

- 📊 **Monitoring temps réel** : CPU, RAM, Disque avec jauges visuelles
- ⚙️ **Gestion services** : Start/Stop/Restart/Enable/Disable
- 📋 **Journaux système** : Visualiseur avec filtrage (50-1000 lignes)
- 💾 **Backup/Restore** : Sauvegarde configuration avec téléchargement
- 🌡️ **Température** : Monitoring zones thermiques (vert < 60°C, orange < 80°C, rouge ≥ 80°C)

---

### 📊 Netdata Dashboard (v0.5.0)

Tableau de bord **monitoring système** avec métriques temps réel.

- 📈 Graphiques CPU, mémoire, disque, réseau
- 🌡️ Capteurs température
- ⚙️ Moniteur processus avec utilisation ressources
- 🎨 Jauges animées et sparklines
- 🔄 Rafraîchissement auto 2 secondes

---

### 🔍 Netifyd DPI Dashboard

Interface complète pour le moteur **Deep Packet Inspection** Netifyd.

#### 📡 Capacités

- 🔍 **Tracking flux temps réel** via interface socket
- 📱 **Détection applications** : HTTP, HTTPS, SSH, DNS, QUIC, etc.
- 💻 **Découverte appareils** automatique avec corrélation MAC/IP
- 📊 **Catégorisation trafic** : Web, Streaming, Gaming, VoIP
- 🔐 **Inspection SSL/TLS** : Extraction certificats et détails cipher
- 📤 **Export** : JSON ou CSV des flux

---

## 🎨 Système de Thème

### 🌈 CyberMood Design System

Le package `luci-theme-secubox` fournit un **système de design unifié** pour tous les modules SecuBox.

#### 🎭 Variantes de Thème

| 🎨 Thème | 🖌️ Couleurs | 🎯 Usage |
|----------|-------------|----------|
| 🌑 **Dark** | `#0a0a0f` bg, `#6366f1` accent | Par défaut, environnements sombres |
| ☀️ **Light** | `#ffffff` bg, `#4f46e5` accent | Forte luminosité ambiante |
| 🌆 **Cyberpunk** | `#0d0d1a` bg, gradients néon | Contraste élevé, accessibilité |

#### 🔤 Typographie

- 🚀 **Display** : Orbitron (titres futuristes)
- 📖 **Body** : Inter (contenu lisible)
- 💻 **Monospace** : JetBrains Mono (code, valeurs)

#### 🧩 Bibliothèque de Composants

```javascript
// Utilisation du thème
'require secubox-theme/theme as Theme';

// Création d'une carte
Theme.createCard({
    title: Theme.t('dashboard.title'),
    icon: '🚀',
    content: E('p', {}, 'Contenu ici'),
    badge: Theme.createBadge('Actif', 'success')
});

// Création d'un bouton
Theme.createButton({
    label: Theme.t('common.save'),
    variant: 'primary',  // primary, secondary, danger, ghost
    attrs: { 'click': handleSave }
});

// Traduction avec paramètres
Theme.t('dashboard.welcome', { name: 'Jean' });
// → "Bienvenue, Jean"
```

#### 🌍 Internationalisation

4 langues incluses : **Français** (fr), **Anglais** (en), **Allemand** (de), **Espagnol** (es)

Clés organisées par domaine : `common.*`, `dashboard.*`, `modules.*`, `settings.*`, `errors.*`

---

## 🏗️ Architecture Technique

### 📁 Structure Standard des Packages

```
luci-app-*/
├── 📄 Makefile                    # Définition package OpenWrt
├── 📄 README.md                   # Documentation module
├── 📂 htdocs/luci-static/resources/
│   ├── 📂 view/*/                 # Modules JavaScript ES6
│   └── 📂 */
│       ├── 📄 api.js              # Wrapper API RPC
│       └── 📄 dashboard.css       # Styles module
└── 📂 root/
    ├── 📂 etc/config/             # Configuration UCI
    └── 📂 usr/
        ├── 📂 libexec/rpcd/       # Backend RPCD (shell/exec)
        └── 📂 share/
            ├── 📂 luci/menu.d/    # JSON menu
            └── 📂 rpcd/acl.d/     # JSON permissions ACL
```

### 🔧 Permissions Fichiers

| 📁 Type | 🔐 Permissions | 📝 Notes |
|---------|----------------|----------|
| Scripts RPCD | `755` | Exécutables par root, requis pour ubus |
| Scripts helper | `755` | Si exécutables |
| Fichiers config | `644` | Lisibles par tous, modifiables par root |
| CSS/JS | `644` | Défini automatiquement par luci.mk |

---

### 🔄 Pipeline CI/CD

Les workflows **GitHub Actions** automatisent la compilation, les tests et les releases.

#### 🏗️ Matrice de Build

| 📂 Catégorie | 🎯 Cibles |
|--------------|-----------|
| 🦾 **ARM64** | aarch64-cortex-a53, aarch64-cortex-a72, mediatek-filogic, rockchip-armv8 |
| 💪 **ARM32** | arm-cortex-a7-neon, arm-cortex-a9-neon, qualcomm-ipq40xx/806x |
| 🔧 **MIPS** | mips-24kc, mipsel-24kc, mipsel-74kc |
| 🖥️ **x86** | x86-64, x86-generic |

#### 📦 Appareils Supportés

| 🎯 Architecture | 📱 Appareils |
|-----------------|--------------|
| aarch64-cortex-a53 | ESPRESSObin, Sheeva64, BananaPi R64 |
| aarch64-cortex-a72 | **MOCHAbin**, Raspberry Pi 4, NanoPi R4S |
| mediatek-filogic | GL.iNet MT3000, BananaPi R3 |
| rockchip-armv8 | NanoPi R4S/R5S, FriendlyARM |
| qualcomm-ipq40xx | Google WiFi, Zyxel NBG6617 |
| mips-24kc | TP-Link Archer, Ubiquiti |
| x86-64 | PC, VMs, Docker, Proxmox |

---

## 🔒 Évaluation Sécurité

### ✅ Bonnes Pratiques Implémentées

1. 🔐 **Séparation ACL** : Isolation stricte permissions lecture/écriture
2. ✔️ **Validation entrées** : Extraction paramètres jsonfilter avec gestion null
3. 🏠 **Isolation services** : Espaces de noms configuration indépendants
4. 📋 **Journalisation audit** : Intégration secubox-log pour analyse forensique
5. 🚫 **Gestion erreurs** : Réponses JSON sans exposition stack trace
6. 📁 **Permissions fichiers** : RPCD=755, config=644 appliquées dans Makefiles
7. 🔑 **Protection clés privées** : Dashboard WireGuard n'expose jamais les clés privées
8. 🔐 **Intégration HSM** : Option stockage clés matériel

### 📋 Recommandations

1. ⏱️ **Rate limiting** : Ajouter throttling endpoints sensibles (ban/unban)
2. ✍️ **Signatures modules** : Activer vérification signatures en production
3. 🔒 **Durcissement TLS** : Imposer TLS 1.3 pour communications API externes
4. ⏰ **Timeout session** : Revoir configurations session LuCI modules sensibles
5. 🛡️ **Protection CSRF** : Vérifier validation tokens sur opérations modificatrices

---

## 📦 Installation

### 🚀 Depuis les Packages Pré-compilés

```bash
# Télécharger depuis GitHub Releases
wget https://github.com/gkerma/secubox-openwrt/releases/latest/download/packages-aarch64-cortex-a72.tar.gz

# Installer les modules souhaités
opkg update
opkg install luci-app-secubox_*.ipk
opkg install luci-app-crowdsec-dashboard_*.ipk
opkg install luci-app-client-guardian_*.ipk

# Redémarrer les services
/etc/init.d/rpcd restart
/etc/init.d/uhttpd restart
```

### 🔧 Compilation depuis les Sources

```bash
# Cloner dans le répertoire packages du SDK OpenWrt
cd ~/openwrt-sdk/package/
git clone https://github.com/gkerma/secubox-openwrt.git secubox

# Compiler tous les packages
cd ~/openwrt-sdk/
make package/secubox/luci-app-secubox/compile V=s
make package/secubox/luci-app-crowdsec-dashboard/compile V=s
# ... etc pour les autres modules
```

### 📡 Ajout au Feed OpenWrt

Ajouter dans `feeds.conf.default` :

```
src-git secubox https://github.com/gkerma/secubox-openwrt.git
```

Puis :

```bash
./scripts/feeds update secubox
./scripts/feeds install -a -p secubox
make menuconfig  # Sélectionner modules sous LuCI > Applications
make V=s
```

---

## 🔗 Ressources

| 📚 Ressource | 🔗 Lien |
|--------------|---------|
| 📦 Repository | [github.com/gkerma/secubox-openwrt](https://github.com/gkerma/secubox-openwrt) |
| 📖 Documentation | [cybermind.fr/secubox](https://cybermind.fr/secubox) |
| 🎮 Démo Live | [secubox.cybermood.eu](https://secubox.cybermood.eu) |
| 🏢 Site Entreprise | [cybermind.fr](https://cybermind.fr) |
| 🐛 Issues | [GitHub Issues](https://github.com/gkerma/secubox-openwrt/issues) |

---

## 🎯 Conclusion

**SecuBox** représente une suite de sécurité mature et professionnellement architecturée pour les plateformes OpenWrt. Son design modulaire permet un déploiement flexible, du réseau domestique à l'appliance de sécurité périmétrique d'entreprise.

### 🏆 Points Forts Différenciants

- 🛡️ **Intégration Complète** : CrowdSec + Netifyd DPI + Support HSM matériel
- 🏢 **Fonctionnalités Entreprise** : NAC avec quarantaine, OAuth/OIDC, gestion VPN
- 📡 **Prêt pour l'IoT** : 17+ types d'adaptateurs USB avec pont MQTT
- 🎨 **UX Professionnelle** : Système de thème unifié multi-langues
- ⚙️ **Qualité Production** : CI/CD automatisé sur 15+ architectures

---

*📝 Article rédigé par **Gandalf** - [CyberMind.FR](https://cybermind.fr)*
*🇫🇷 Made with ❤️ in France*

{% note info %}
**💡 Vous souhaitez contribuer ?** SecuBox est open-source sous licence Apache-2.0. Les contributions sont les bienvenues sur [GitHub](https://github.com/gkerma/secubox-openwrt) !
{% endnote %}
