---
title: 🔧 PiDebugger v2.1 - Multi-Target ARM Debugger
date: 2025-12-09 12:47:00
tags:
  - raspberry-pi
  - debug
  - soc
  - embedded
  - espressobin
  - mochabin
  - sheeva64
  - marvell
  - armada
categories:
  - Hardware
  - Embedded Development
---

# 🔧 PiDebugger v2.1

> 🍓 **Pi Zero W** + 🔲 **HyperPixel 2.1" Round 480×480** = 🎯 **Multi-Target ARM Debugger**

Outil portable basé sur Raspberry Pi Zero W et écran HyperPixel 2.1" Round (480×480 @ 60fps) pour le debug, monitoring et installation de plateformes SoC ARM Marvell/Globalscale.
<!-- more -->
## 🎯 Targets Supportés

| Emoji | Target | SoC | CPU | RAM | Réseau |
|-------|--------|-----|-----|-----|--------|
| ☕ | **ESPRESSObin V7** | Armada 3720 | 2×Cortex-A53 @ 1.0GHz | 1-2GB DDR4 | 3×GbE |
| 🚀 | **ESPRESSObin Ultra** | Armada 3720 | 2×Cortex-A53 @ 1.2GHz | 1GB DDR4 | 1WAN+4LAN PoE |
| 🍫 | **MOCHAbin** | Armada 7040 | 4×Cortex-A72 @ 1.4GHz | 2-8GB DDR4 | 10G SFP+ 4×GbE |
| 🔌 | **Sheeva64** | Armada 3720 | 2×Cortex-A53 @ 1.2GHz | 1GB DDR4 | 2×GbE |

## ✨ Fonctionnalités principales

| Emoji | Fonction | Description |
|-------|----------|-------------|
| 🕐 | Horloge | Écran de veille avec heure/date et status |
| 📊 | Dashboard | Menu principal avec 9 boutons circulaires |
| 💻 | Terminal UART | Moniteur série temps réel coloré avec parser ATF |
| 🚀 | Boot Analyzer | Timeline circulaire + Hardware info + ATF stages |
| 🔋 | Power Control | Sélection target + alimentation USB + graphiques V/A |
| 📁 | File Browser | Explorateur USB Mass Storage + export logs |
| 🌐 | Network | Status/WiFi/TFTP avec authentification WPA2/WPA3 |
| 📤 | XMODEM | Transfert fichiers via UART (CRC-16, 128B packets) |
| 🛡️ | UEFI Shell | 6 commandes interactives |
| ⚙️ | Settings | 4 thèmes + sons + gestures + stats système |

## 🏷️ Légende des emojis

### 📊 Status
- ✅ OK / Succès
- ❌ Erreur
- ⚠️ Warning
- 🟢 Actif / ON
- 🔴 Inactif / OFF
- 🟡 Standby
- 🔄 En cours

### 🔲 Hardware
- 🍓 Raspberry Pi (Master)
- ☕ ESPRESSObin V7
- 🚀 ESPRESSObin Ultra
- 🍫 MOCHAbin
- 🔌 Sheeva64
- ⚡ CPU / Power
- 💾 RAM / Storage
- 🔌 USB
- 📡 Serial/UART
- 🌐 Network
- 🔋 Power
- 🧠 SoC/Chip

### 🚀 Boot Stages
- 🔒 BootROM
- 🔑 WTMI
- 🛡️ ATF (ARM Trusted Firmware)
- 📦 SPL (Secondary Program Loader)
- 🥾 U-Boot
- 🐧 Linux Kernel
- 👤 Login

### 🔗 USB & Connexions
- 🔗 USB Gadget (composite device)
- 📟 TTY Serial (/dev/ttyGS0)
- 📡 UART liaison série
- 📥 RX (réception données)
- 📤 TX (envoi données)
- 📶 Signal WiFi
- 🎯 Target (cible SoC)

### 🎬 Actions
- ▶️ Play / Run
- ⏸️ Pause / Stop
- 🔄 Restart / Loading
- ◀️ Back (retour)
- 🧹 Clear (effacer)
- 🔍 Search (recherche)

## 🏗️ Architecture du projet

```
┌─────────────────────────────────────────────────────────┐
│           🔲 HyperPixel 2.1" Round Touch                │
│              480×480 @ 60fps • Capacitif                │
├─────────────────────────────────────────────────────────┤
│           🍓 Raspberry Pi Zero W (MASTER)               │
│   WiFi 802.11n • Bluetooth 4.1 • USB OTG Gadget         │
├─────────────────────────────────────────────────────────┤
│                    UART + USB Power                     │
│          GPIO14/15 (TX/RX) + USB 5V Control             │
├─────────────────────────────────────────────────────────┤
│                   🎯 TARGET (1 de 4)                    │
│  ☕ ESPRESSObin V7    │  🚀 ESPRESSObin Ultra           │
│  Armada 3720         │  Armada 3720 + PoE              │
│  2×A53 @ 1.0GHz      │  2×A53 @ 1.2GHz                 │
├──────────────────────┼──────────────────────────────────┤
│  🍫 MOCHAbin         │  🔌 Sheeva64                     │
│  Armada 7040         │  Armada 3720                    │
│  4×A72 @ 1.4GHz      │  2×A53 @ 1.2GHz                 │
│  10G SFP+            │  Wall Plug Form Factor          │
└─────────────────────────────────────────────────────────┘
```

### Séquences de Boot par Target

**Armada 3720 (ESPRESSObin/Ultra/Sheeva64):**
```
🔒 BootROM → 🔑 WTMI (CM3) → 🛡️ ATF (BL1/BL2/BL31) → 📦 SPL → 🥾 U-Boot → 🐧 Linux
```

**Armada 7040 (MOCHAbin):**
```
🔒 AP806 BootROM → 🛡️ ATF (BL1/BL2/BL31 PSCI/SCMI) → 📦 SPL → 🥾 U-Boot → 🐧 Linux
```

## 📊 Mini-Dashboards de Status

L'interface affiche en permanence l'état du système via deux mini-dashboards :

### 🍓 MASTER (Pi Zero W)

| Emoji | Indicateur | Description |
|-------|------------|-------------|
| 🔗 | Gadget | USB Gadget composite actif |
| 📟 | TTY | Serial /dev/ttyGS0 disponible |
| 💿 | Storage | Mass Storage 512MB monté |
| 📶 | WiFi | Connexion réseau active |
| 🌡️ | Temp | Température CPU |

### 🎯 TARGET (SoC Cible)

| Emoji | Indicateur | Description |
|-------|------------|-------------|
| 🔋 | Power | Alimentation USB/externe |
| 🔌 | USB | Connexion USB détectée |
| 📡 | Serial | Liaison UART active |
| 🔄/✅/🟡 | State | Booting / Ready / Idle |

### 📍 Affichage par écran

```
┌─ Dashboard ────────────────────────────┐
│ ┌───────────────┐ ┌───────────────┐   │
│ │ 🍓 MASTER     │ │ 🎯 TARGET     │   │
│ │ 🔗🟢 📟🟢 💿🟢│ │ 🔋🟢 🔌🟢 📡🟢│   │
│ └───────────────┘ └───────────────┘   │
│                                        │
│        🔧 PiDebugger                   │
│     [🕐] [💻] [🚀] [🔋] [📁] [⚙️]     │
└────────────────────────────────────────┘

┌─ Serial Monitor ───────────────────────┐
│ 💻 Serial Monitor                      │
│ ┌────────────────────────────────────┐│
│ │ 🔋🟢 🔗🟢 📟🟢 📡🟢   [▶️ RUN]   ││
│ └────────────────────────────────────┘│
│ ┌────────────────────────────────────┐│
│ │ 🥾 U-Boot 2024.01                 ││
│ │ ☕ ESPRESSOBin Board              ││
│ │ ⚡ Armada 3720 @ 1000 MHz         ││
│ │ ...                                ││
│ └────────────────────────────────────┘│
│  📥 1,234 bytes | ℹ️ 42 lines         │
│       [🧹 CLR]  [◀️ BACK]             │
└────────────────────────────────────────┘

┌─ Clock ────────────────────────────────┐
│                                        │
│              14:32                     │
│           ┌────────┐                   │
│           │   🕐   │                   │
│           └────────┘                   │
│          08 déc. 2025                  │
│                                        │
│      🍓🟢  🎯🔴  📡🔴                 │
│       ▶️ Touch to continue             │
└────────────────────────────────────────┘
```

## 🎯 Targets ARM Supportés

PiDebugger v2.1 supporte 4 plateformes ARM Marvell/Globalscale avec séquences de boot spécifiques.

### ☕ ESPRESSObin V7

Le board de référence pour le développement Marvell Armada.

| Caractéristique | Valeur |
|-----------------|--------|
| **SoC** | Marvell Armada 3720 (88F3720) |
| **CPU** | 2× ARM Cortex-A53 @ 1.0 GHz |
| **RAM** | 1-2 GB DDR4 @ 800 MHz |
| **Storage** | microSD, eMMC (option), SPI NOR 4MB |
| **Network** | 3× Gigabit Ethernet (Topaz 6341 Switch) |
| **USB** | 1× USB 3.0, 1× USB 2.0, micro-USB console |
| **Power** | 5V/2A micro-USB ou 12V DC jack |
| **UART** | 115200 8N1 via micro-USB (FTDI) |

**Séquence de boot:**
```
🔒 BootROM → 🔑 WTMI (CM3) → 🛡️ ATF BL1 → BL2 → BL31 → 📦 SPL → 🥾 U-Boot → 🐧 Linux
```

**Device Tree:** `armada-3720-espressobin-v7.dts`

### 🚀 ESPRESSObin Ultra

Version améliorée avec PoE et plus de ports réseau.

| Caractéristique | Valeur |
|-----------------|--------|
| **SoC** | Marvell Armada 3720 (88F3720) |
| **CPU** | 2× ARM Cortex-A53 @ 1.2 GHz |
| **RAM** | 1 GB DDR4 |
| **Storage** | 8GB eMMC, microSD, SPI NOR, M.2 2280 |
| **Network** | 1× WAN PoE 30W + 4× LAN Gigabit (Topaz 6341) |
| **WiFi** | 802.11ac 2×2 dual-band + BLE 4.2 |
| **USB** | 1× USB 3.0, 1× USB 2.0 |
| **Power** | 12V/2A DC ou PoE 30W |
| **Form Factor** | CPE Gateway avec boîtier |

**Séquence de boot:**
```
🔒 BootROM → 🔑 WTMI → 🛡️ ATF → 📦 SPL → 🥾 U-Boot → 🐧 Linux/OpenWrt
```

**Device Tree:** `armada-3720-espressobin-ultra.dts`

### 🍫 MOCHAbin

Board haute performance avec 10G SFP+ et quad-core A72.

| Caractéristique | Valeur |
|-----------------|--------|
| **SoC** | Marvell Armada 7040 (88F7040) |
| **CPU** | 4× ARM Cortex-A72 @ 1.4 GHz |
| **RAM** | 2-8 GB DDR4 ECC |
| **Storage** | 16GB eMMC, SPI NOR 4MB, M.2 SATA, SATA 7+15 |
| **Network** | 1× 10G SFP+, 1× 1G SFP, 4× GbE (Topaz 88E6141), 1× WAN PoE |
| **WiFi** | 802.11ax WiFi 6 (option) + 5G LTE (option) |
| **USB** | 2× USB 3.0 (via hub) |
| **Power** | 12V/3A DC |
| **Expansion** | Mini-PCIe, M.2 2280, M.2 2250, MikroBus |

**Séquence de boot:**
```
🔒 AP806 BootROM → 🛡️ ATF BL1 (AP init) → BL2 (CP110) → BL31 (PSCI/SCMI) → 📦 SPL → 🥾 U-Boot → 🐧 Linux
```

**Device Tree:** `armada-7040-mochabin.dts`

**Note:** Le 7040 n'a pas de WTMI (Cortex-M3) contrairement au 3720.

### 🔌 Sheeva64

Format "plug computer" compact avec alimentation intégrée.

| Caractéristique | Valeur |
|-----------------|--------|
| **SoC** | Marvell Armada 3720 (88F3720) |
| **CPU** | 2× ARM Cortex-A53 @ 1.2 GHz |
| **RAM** | 1 GB DDR4 |
| **Storage** | 4GB eMMC, microSD |
| **Network** | 2× Gigabit Ethernet |
| **USB** | 2× USB 2.0 Type-A |
| **Power** | Wall plug intégré (110-240V AC) |
| **Console** | mini-USB UART |
| **WiFi** | 802.11ac + BLE 4.2 (option) |
| **Form Factor** | 110 × 70 × 49mm plug |

**Séquence de boot:**
```
🔒 BootROM → 🔑 WTMI → 🛡️ ATF → 📦 SPL → 🥾 U-Boot → 🐧 Ubuntu 18.04
```

**Héritage:** Successeur 64-bit du SheevaPlug original (Kirkwood ARMv5).

### 🔄 Comparatif des Targets

| Feature | ☕ ESPRESSObin | 🚀 Ultra | 🍫 MOCHAbin | 🔌 Sheeva64 |
|---------|---------------|----------|-------------|-------------|
| **Cores** | 2×A53 | 2×A53 | 4×A72 | 2×A53 |
| **Freq** | 1.0 GHz | 1.2 GHz | 1.4 GHz | 1.2 GHz |
| **RAM max** | 2 GB | 1 GB | 8 GB | 1 GB |
| **10G** | ❌ | ❌ | ✅ SFP+ | ❌ |
| **PoE** | ❌ | ✅ 30W | ✅ | ❌ |
| **WiFi** | ❌ | ✅ ac | ✅ ax | Option |
| **WTMI** | ✅ | ✅ | ❌ | ✅ |
| **Prix** | ~$50 | ~$120 | ~$160 | ~$90 |

### 🔌 Connexion UART vers Target

```
Pi Zero W (Master)          Target (ESPRESSObin/etc)
─────────────────          ──────────────────────────
GPIO 14 (TXD) ────────────► RXD (micro-USB ou header)
GPIO 15 (RXD) ◄──────────── TXD
GND ──────────────────────── GND

Paramètres: 115200 8N1 (pas de flow control)
```

### ⚡ Contrôle Power USB

Le Pi Zero W peut contrôler l'alimentation du target via :

1. **Relay USB** : Module relay contrôlé par GPIO
2. **USB Hub programmable** : Hub avec contrôle power par port
3. **INA219** : Mesure V/A en temps réel (I2C)

```python
# Exemple contrôle GPIO relay
import RPi.GPIO as GPIO
RELAY_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.HIGH)  # Power ON
GPIO.output(RELAY_PIN, GPIO.LOW)   # Power OFF
```

## 📦 Phase 1 : Préparation du système

### 📌 1.1 🛒 Matériel requis

| Emoji | Composant | Modèle |
|-------|-----------|--------|
| 🍓 | SBC | Raspberry Pi Zero W (avec header GPIO) |
| 🔲 | Écran | Pimoroni HyperPixel 2.1" Round Touch |
| 💾 | Stockage | Carte microSD 16 Go+ (classe 10) |
| 🔌 | Câble | USB data (micro-USB → USB-A) |
| 🔋 | Batterie | LiPo 3.7V + module charge (optionnel) |

### 📌 1.2 💿 Installation Raspberry Pi OS Lite

```bash
# Sur machine hôte - télécharger et flasher
wget https://downloads.raspberrypi.com/raspios_lite_armhf/images/raspios_lite_armhf-2024-11-19/2024-11-19-raspios-bookworm-armhf-lite.img.xz

# Flasher avec dd ou balenaEtcher
xzcat 2024-11-19-raspios-bookworm-armhf-lite.img.xz | sudo dd of=/dev/sdX bs=4M status=progress

# Monter la partition boot
sudo mount /dev/sdX1 /mnt/boot
```

### 📌 1.3 Configuration headless initiale

```bash
# Activer SSH
sudo touch /mnt/boot/ssh

# Configuration WiFi
cat << 'EOF' | sudo tee /mnt/boot/wpa_supplicant.conf
country=FR
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="VOTRE_SSID"
    psk="VOTRE_PASSWORD"
    key_mgmt=WPA-PSK
}
EOF

# Démonter
sudo umount /mnt/boot
```

## 🏭 Phase 1.5 : Factory Boot Mode

Le PiDebugger démarre avec une séquence de boot complète simulant l'initialisation de tous les composants.

### 📋 Séquence Factory Boot

```
┌─────────────────────────────────────────────────────────────┐
│  Phase         │ Durée  │ Description                       │
├─────────────────────────────────────────────────────────────┤
│  🍓 GPU INIT   │ ~1.2s  │ Logo Raspberry Pi, init BCM2835  │
│  ⚙️ BOOTLOADER │ ~0.7s  │ config.txt, dtoverlay, kernel    │
│  🐧 LINUX      │ ~1.0s  │ Kernel, dwc2, mmc, EXT4          │
│  ▶️ SYSTEMD    │ ~0.5s  │ Services, network, SSH           │
│  🔧 FACTORY    │ ~3.0s  │ PiDebugger init (voir détail)    │
│  🚀 LAUNCH     │ ~0.6s  │ Transition vers UI               │
└─────────────────────────────────────────────────────────────┘
```

### 🔧 Détail phase FACTORY

La phase Factory initialise tous les composants du PiDebugger :

```
╔════════════════════════════════════╗
║   🔧 PIDEBUGGER FACTORY MODE       ║
╚════════════════════════════════════╝

▶️ [INIT] Loading PiDebugger v1.0
🧠 [DISP] HyperPixel 2.1" detected
✅ [DISP] Resolution: 480x480 @ 60Hz
✅ [DISP] Touch: FT5406 OK

🔗 [USB ] Configuring gadget...
📟 [USB ] ACM serial: /dev/ttyGS0
💿 [USB ] Mass storage: 512MB
✅ [USB ] Composite gadget active

🔋 [PWR ] USB OTG power control init
✅ [PWR ] VBUS detect: enabled
🟡 [PWR ] Target power: standby

✅ [STOR] FAT32 PIDEBUGGER mounted
🌐 [NET ] WiFi: Connected
✅ [NET ] IP: 192.168.1.42

🔍 [AUTO] Checking autorun.sh...
▶️ [AUTO] Executing factory setup...
  → Verifying firmware images
    ✅ armbian/espressobin.img
    ✅ uboot/flash-image-v7.bin
  → Loading UI theme: LuCI Dark
  → Calibrating touchscreen
    ✅ Touch calibration OK
  → Starting UI service...

🎉 [READY] System initialized
🚀 [READY] Launching interface...
```

### 📊 Status progressifs pendant le boot

Les indicateurs Master s'allument progressivement :

| Étape | 🔗 Gadget | 📟 TTY | 💿 Storage | 📶 WiFi |
|-------|-----------|--------|------------|---------|
| GPU   | 🔴 | 🔴 | 🔴 | 🔴 |
| Kernel| 🟢 | 🔴 | 🔴 | 🔴 |
| Systemd| 🟢 | 🟢 | 🔴 | 🔴 |
| Factory| 🟢 | 🟢 | 🟢 | 🔴 |
| Ready | 🟢 | 🟢 | 🟢 | 🟢 |

### ⏭️ Bouton SKIP

Un bouton `▶️ SKIP` permet de passer directement à l'interface sans attendre la fin du boot.

### 📌 1.4 Premier boot et mise à jour

```bash
# Connexion SSH (trouver l'IP via router ou nmap)
ssh pi@raspberrypi.local
# Password par défaut: raspberry

# Mise à jour système
sudo apt update && sudo apt upgrade -y

# Installer les outils de base
sudo apt install -y git python3-pip python3-pygame python3-dev \
    libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
    screen minicom picocom fonts-dejavu-core
```

## 📋 Phase 2 : Installation driver HyperPixel

### 📌 2.1 Installation automatique Pimoroni

```bash
# Cloner et installer
git clone https://github.com/pimoroni/hyperpixel2r
cd hyperpixel2r
sudo ./install.sh

# Redémarrer
sudo reboot
```

### 📌 2.2 Configuration écran rond

```bash
# Vérifier que l'écran fonctionne
dmesg | grep -i hyper

# Configurer la rotation si nécessaire (dans /boot/config.txt)
# display_lcd_rotate=2  # 180 degrés
```

### 📌 2.3 Test tactile

```bash
# Installer evtest
sudo apt install -y evtest

# Tester le touch
sudo evtest /dev/input/event0
```

## 📋 Phase 3 : Structure du projet Python

### 📌 3.1 Arborescence

```
/home/pi/pidebugger/
├── main.py                 # Point d'entrée
├── config.yaml             # Configuration
├── ui/
│   ├── __init__.py
│   ├── core.py            # Moteur UI circulaire
│   ├── widgets.py         # Widgets (jauges, boutons)
│   ├── screens/
│   │   ├── clock.py       # Écran horloge
│   │   ├── dashboard.py   # Dashboard principal
│   │   ├── serial.py      # Moniteur série
│   │   ├── boot.py        # Analyse boot
│   │   └── network.py     # Config réseau
│   └── themes/
│       └── luci.py        # Thème style OpenWRT
├── serial/
│   ├── __init__.py
│   ├── gadget.py          # USB Gadget mode
│   ├── console.py         # Console série
│   └── parser.py          # Parsers boot (uboot, uefi...)
├── analyzers/
│   ├── __init__.py
│   ├── uboot.py           # Analyseur U-Boot
│   ├── uefi.py            # Analyseur UEFI
│   ├── spi.py             # Analyseur SPI boot
│   └── armbian.py         # Analyseur Armbian
└── assets/
    ├── fonts/
    └── icons/
```

### 📌 3.2 Création du projet

```bash
mkdir -p /home/pi/pidebugger/{ui/screens,ui/themes,serial,analyzers,assets/fonts,assets/icons}
cd /home/pi/pidebugger

# Créer environnement virtuel (optionnel mais recommandé)
python3 -m venv venv
source venv/bin/activate
pip install pygame pyyaml pyserial
```

## 📋 Phase 4 : Moteur UI circulaire

### 📌 4.1 Core UI (`ui/core.py`)

```python
#!/usr/bin/env python3
"""
Moteur d'interface circulaire pour HyperPixel 2.1" Round
480x480 pixels, masque circulaire
"""

import pygame
import math
from typing import Callable, Optional

# Constantes écran
SCREEN_SIZE = 480
CENTER = (SCREEN_SIZE // 2, SCREEN_SIZE // 2)
RADIUS = SCREEN_SIZE // 2

# Couleurs thème LuCI
COLORS = {
    'bg': (24, 26, 31),
    'bg_light': (35, 39, 47),
    'bg_dark': (18, 20, 26),
    'primary': (0, 149, 218),
    'secondary': (76, 175, 80),
    'warning': (255, 152, 0),
    'danger': (244, 67, 54),
    'text': (224, 224, 224),
    'text_dim': (128, 128, 128),
    'border': (55, 60, 70),
    'raspberry': (197, 26, 74),
    'power': (255, 87, 34),
    'spi': (255, 150, 255),
    'uefi': (100, 255, 255),
    'uboot': (100, 200, 255),
    'kernel': (150, 255, 150),
}

# 🏷️ Emojis pour l'interface
EMOJI = {
    # Status
    'on': '🟢', 'off': '🔴', 'standby': '🟡', 'loading': '🔄',
    'ok': '✅', 'error': '❌', 'warn': '⚠️', 'info': 'ℹ️',
    
    # Hardware
    'raspberry': '🍓', 'chip': '🧠', 'cpu': '⚡', 'ram': '💾',
    'usb': '🔌', 'serial': '📡', 'network': '🌐', 'storage': '💿',
    'power': '🔋', 'volt': '⚡', 'temp': '🌡️',
    
    # USB Gadget
    'gadget': '🔗', 'tty': '📟', 'rx': '📥', 'tx': '📤', 'signal': '📶',
    
    # Actions
    'play': '▶️', 'pause': '⏸️', 'stop': '⏹️', 'restart': '🔄',
    'back': '◀️', 'forward': '▶️', 'settings': '⚙️', 'tools': '🔧',
    'search': '🔍', 'clear': '🧹', 'save': '💾', 'load': '📂',
    
    # Interface
    'clock': '🕐', 'dashboard': '📊', 'terminal': '💻', 'files': '📁',
    'boot': '🚀', 'timeline': '📈', 'config': '⚙️', 'help': '❓',
    
    # Platforms
    'espressobin': '☕', 'mochabin': '🍫', 'ultra': '⚡', 'target': '🎯',
    
    # Boot stages
    'bootrom': '🔒', 'wtmi': '🔑', 'atf': '🛡️', 'spl': '📦',
    'uboot': '🥾', 'kernel': '🐧', 'login': '👤',
    
    # Misc
    'success': '🎉', 'flash': '⚡', 'link': '🔗',
}

# Couleurs par stage de boot
STAGE_COLORS = {
    'bootrom': (200, 100, 100),   # Rouge clair
    'wtmi': (255, 150, 100),      # Orange
    'atf': (200, 255, 100),       # Jaune-vert
    'spl': (100, 200, 255),       # Bleu clair
    'uboot': (100, 150, 255),     # Bleu
    'kernel': (150, 100, 255),    # Violet
    'login': (100, 255, 150),     # Vert clair
}


class CircularUI:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        
        self.screen = pygame.display.set_mode(
            (SCREEN_SIZE, SCREEN_SIZE),
            pygame.FULLSCREEN | pygame.HWSURFACE
        )
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_screen = None
        self.screens = {}
        
        # Surface de masque circulaire
        self.mask = self._create_circular_mask()
        
        # Font
        pygame.font.init()
        self.fonts = {
            'small': pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14),
            'medium': pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 18),
            'large': pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 28),
            'xlarge': pygame.font.Font('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 48),
        }
    
    def _create_circular_mask(self) -> pygame.Surface:
        """Crée un masque circulaire pour cacher les coins."""
        mask = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE), pygame.SRCALPHA)
        mask.fill((0, 0, 0, 255))
        pygame.draw.circle(mask, (0, 0, 0, 0), CENTER, RADIUS)
        return mask
    
    def register_screen(self, name: str, screen_class):
        """Enregistre un écran."""
        self.screens[name] = screen_class(self)
    
    def switch_screen(self, name: str):
        """Change d'écran."""
        if name in self.screens:
            if self.current_screen:
                self.current_screen.on_exit()
            self.current_screen = self.screens[name]
            self.current_screen.on_enter()
    
    def draw_circular_progress(self, surface, center, radius, progress, 
                                color, width=8, start_angle=-90):
        """Dessine un arc de progression circulaire."""
        if progress <= 0:
            return
        
        rect = pygame.Rect(
            center[0] - radius,
            center[1] - radius,
            radius * 2,
            radius * 2
        )
        
        end_angle = start_angle + (360 * min(progress, 1.0))
        
        # Convertir en radians pour pygame
        start_rad = math.radians(start_angle)
        end_rad = math.radians(end_angle)
        
        pygame.draw.arc(surface, color, rect, -end_rad, -start_rad, width)
    
    def draw_radial_menu(self, surface, items: list, selected: int = 0):
        """Dessine un menu radial."""
        n_items = len(items)
        if n_items == 0:
            return
        
        angle_step = 360 / n_items
        menu_radius = RADIUS - 60
        
        for i, item in enumerate(items):
            angle = math.radians(-90 + i * angle_step)
            x = CENTER[0] + int(menu_radius * math.cos(angle))
            y = CENTER[1] + int(menu_radius * math.sin(angle))
            
            # Cercle de l'item
            color = COLORS['primary'] if i == selected else COLORS['bg_light']
            pygame.draw.circle(surface, color, (x, y), 35)
            pygame.draw.circle(surface, COLORS['border'], (x, y), 35, 2)
            
            # Icône/texte
            text = self.fonts['small'].render(item['label'][:4], True, COLORS['text'])
            text_rect = text.get_rect(center=(x, y))
            surface.blit(text, text_rect)
    
    def run(self):
        """Boucle principale."""
        while self.running:
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.current_screen:
                        self.current_screen.on_touch(event.pos)
            
            # Update
            if self.current_screen:
                self.current_screen.update()
            
            # Draw
            self.screen.fill(COLORS['bg'])
            
            if self.current_screen:
                self.current_screen.draw(self.screen)
            
            # Appliquer masque circulaire
            self.screen.blit(self.mask, (0, 0))
            
            pygame.display.flip()
            self.clock.tick(30)
        
        pygame.quit()


class Screen:
    """Classe de base pour les écrans."""
    
    def __init__(self, ui: CircularUI):
        self.ui = ui
    
    def on_enter(self):
        """Appelé quand l'écran devient actif."""
        pass
    
    def on_exit(self):
        """Appelé quand on quitte l'écran."""
        pass
    
    def on_touch(self, pos: tuple):
        """Gère les événements tactiles."""
        pass
    
    def update(self):
        """Met à jour la logique."""
        pass
    
    def draw(self, surface: pygame.Surface):
        """Dessine l'écran."""
        pass
```

### 📌 4.2 Écran Horloge (`ui/screens/clock.py`)

```python
#!/usr/bin/env python3
"""Écran horloge - premier écran du projet."""

import pygame
import math
from datetime import datetime
from ui.core import Screen, COLORS, CENTER, RADIUS


class ClockScreen(Screen):
    def __init__(self, ui):
        super().__init__(ui)
        self.last_second = -1
    
    def draw(self, surface):
        now = datetime.now()
        
        # Cercle extérieur
        pygame.draw.circle(surface, COLORS['border'], CENTER, RADIUS - 10, 2)
        
        # Marqueurs des heures
        for i in range(12):
            angle = math.radians(-90 + i * 30)
            inner_r = RADIUS - 30
            outer_r = RADIUS - 15
            
            x1 = CENTER[0] + int(inner_r * math.cos(angle))
            y1 = CENTER[1] + int(inner_r * math.sin(angle))
            x2 = CENTER[0] + int(outer_r * math.cos(angle))
            y2 = CENTER[1] + int(outer_r * math.sin(angle))
            
            width = 3 if i % 3 == 0 else 1
            pygame.draw.line(surface, COLORS['text'], (x1, y1), (x2, y2), width)
        
        # Aiguille des heures
        hour_angle = math.radians(-90 + (now.hour % 12 + now.minute / 60) * 30)
        hour_len = RADIUS * 0.5
        hx = CENTER[0] + int(hour_len * math.cos(hour_angle))
        hy = CENTER[1] + int(hour_len * math.sin(hour_angle))
        pygame.draw.line(surface, COLORS['text'], CENTER, (hx, hy), 6)
        
        # Aiguille des minutes
        min_angle = math.radians(-90 + now.minute * 6)
        min_len = RADIUS * 0.7
        mx = CENTER[0] + int(min_len * math.cos(min_angle))
        my = CENTER[1] + int(min_len * math.sin(min_angle))
        pygame.draw.line(surface, COLORS['primary'], CENTER, (mx, my), 4)
        
        # Aiguille des secondes
        sec_angle = math.radians(-90 + now.second * 6)
        sec_len = RADIUS * 0.8
        sx = CENTER[0] + int(sec_len * math.cos(sec_angle))
        sy = CENTER[1] + int(sec_len * math.sin(sec_angle))
        pygame.draw.line(surface, COLORS['danger'], CENTER, (sx, sy), 2)
        
        # Centre
        pygame.draw.circle(surface, COLORS['text'], CENTER, 8)
        pygame.draw.circle(surface, COLORS['bg'], CENTER, 4)
        
        # Date
        date_str = now.strftime('%d %b %Y')
        date_text = self.ui.fonts['medium'].render(date_str, True, COLORS['text_dim'])
        date_rect = date_text.get_rect(center=(CENTER[0], CENTER[1] + 80))
        surface.blit(date_text, date_rect)
        
        # Heure digitale
        time_str = now.strftime('%H:%M')
        time_text = self.ui.fonts['large'].render(time_str, True, COLORS['text'])
        time_rect = time_text.get_rect(center=(CENTER[0], CENTER[1] - 80))
        surface.blit(time_text, time_rect)
    
    def on_touch(self, pos):
        # Toucher pour passer au dashboard
        self.ui.switch_screen('dashboard')
```

### 📌 4.3 Écran Dashboard avec Mini-Status (`ui/screens/dashboard.py`)

```python
#!/usr/bin/env python3
"""Dashboard principal avec menu radial et mini-dashboards de status."""

import pygame
import math
from ui.core import Screen, COLORS, EMOJI, CENTER, RADIUS


class DashboardScreen(Screen):
    """Dashboard principal avec status Master/Target."""
    
    # Menu items avec emojis
    MENU_ITEMS = [
        {'id': 'clock', 'emoji': EMOJI['clock'], 'label': 'TIME', 'color': COLORS['primary']},
        {'id': 'serial', 'emoji': EMOJI['terminal'], 'label': 'UART', 'color': COLORS['secondary']},
        {'id': 'boot', 'emoji': EMOJI['boot'], 'label': 'BOOT', 'color': COLORS['warning']},
        {'id': 'power', 'emoji': EMOJI['power'], 'label': 'PWR', 'color': COLORS['power']},
        {'id': 'files', 'emoji': EMOJI['files'], 'label': 'FILE', 'color': COLORS['uboot']},
        {'id': 'conf', 'emoji': EMOJI['settings'], 'label': 'CONF', 'color': COLORS['spi']},
    ]
    
    def __init__(self, ui):
        super().__init__(ui)
        self.selected = -1
        
        # Status Master (Pi Zero)
        self.master_status = {
            'power': True,
            'gadget': False,
            'tty': False,
            'storage': False,
            'wifi': False,
            'temp': 45,
        }
        
        # Status Target (SoC cible)
        self.target_status = {
            'power': False,
            'usb': False,
            'serial': False,
            'platform': f"{EMOJI['search']} Detecting...",
            'booting': False,
            'ready': False,
        }
    
    def update_master_status(self, **kwargs):
        """Met à jour le status du Master."""
        self.master_status.update(kwargs)
    
    def update_target_status(self, **kwargs):
        """Met à jour le status de la cible."""
        self.target_status.update(kwargs)
    
    def draw(self, surface):
        # Titre
        title = f"{EMOJI['tools']} PiDebugger"
        title_text = self.ui.fonts['large'].render(title, True, COLORS['primary'])
        title_rect = title_text.get_rect(center=(CENTER[0], 45))
        surface.blit(title_text, title_rect)
        
        # Mini-dashboard Master
        self._draw_master_status(surface, 45, 55)
        
        # Mini-dashboard Target
        self._draw_target_status(surface, RADIUS + 50, 55)
        
        # Platform info
        platform_text = self.ui.fonts['small'].render(
            self.target_status['platform'], True, COLORS['text']
        )
        platform_rect = platform_text.get_rect(center=(CENTER[0], 118))
        surface.blit(platform_text, platform_rect)
        
        # Menu radial
        self._draw_menu(surface)
        
        # Footer
        footer = f"{EMOJI['info']} Touch icon to select"
        footer_text = self.ui.fonts['small'].render(footer, True, COLORS['text_dim'])
        footer_rect = footer_text.get_rect(center=(CENTER[0], RADIUS * 2 - 22))
        surface.blit(footer_text, footer_rect)
    
    def _draw_master_status(self, surface, x, y):
        """Dessine le mini-dashboard Master."""
        # Background
        pygame.draw.rect(surface, COLORS['bg_light'], (x, y, 140, 44), border_radius=8)
        
        # Titre
        title = f"{EMOJI['raspberry']} MASTER"
        title_text = self.ui.fonts['small'].render(title, True, COLORS['raspberry'])
        surface.blit(title_text, (x + 10, y + 5))
        
        # Status icons
        ms = self.master_status
        status_line = (
            f"{EMOJI['gadget']}{EMOJI['on'] if ms['gadget'] else EMOJI['off']} "
            f"{EMOJI['tty']}{EMOJI['on'] if ms['tty'] else EMOJI['off']} "
            f"{EMOJI['storage']}{EMOJI['on'] if ms['storage'] else EMOJI['off']}"
        )
        status_text = self.ui.fonts['small'].render(status_line, True, COLORS['text'])
        surface.blit(status_text, (x + 10, y + 25))
    
    def _draw_target_status(self, surface, x, y):
        """Dessine le mini-dashboard Target."""
        # Background
        pygame.draw.rect(surface, COLORS['bg_light'], (x, y, 140, 44), border_radius=8)
        
        # Titre
        title = f"{EMOJI['target']} TARGET"
        title_text = self.ui.fonts['small'].render(title, True, COLORS['primary'])
        surface.blit(title_text, (x + 10, y + 5))
        
        # Status icons
        ts = self.target_status
        status_line = (
            f"{EMOJI['power']}{EMOJI['on'] if ts['power'] else EMOJI['off']} "
            f"{EMOJI['usb']}{EMOJI['on'] if ts['usb'] else EMOJI['off']} "
            f"{EMOJI['serial']}{EMOJI['on'] if ts['serial'] else EMOJI['off']}"
        )
        status_text = self.ui.fonts['small'].render(status_line, True, COLORS['text'])
        surface.blit(status_text, (x + 10, y + 25))
    
    def _draw_menu(self, surface):
        """Dessine le menu radial avec emojis."""
        n_items = len(self.MENU_ITEMS)
        menu_radius = RADIUS - 75
        
        for i, item in enumerate(self.MENU_ITEMS):
            angle = math.radians(-90 + i * (360 / n_items))
            x = CENTER[0] + int(menu_radius * math.cos(angle))
            y = CENTER[1] + 30 + int(menu_radius * math.sin(angle))
            
            # Cercle bouton
            pygame.draw.circle(surface, COLORS['bg_light'], (x, y), 36)
            pygame.draw.circle(surface, COLORS['border'], (x, y), 36, 2)
            pygame.draw.circle(surface, item['color'], (x, y), 36, 2)
            
            # Emoji
            emoji_text = self.ui.fonts['large'].render(item['emoji'], True, COLORS['text'])
            emoji_rect = emoji_text.get_rect(center=(x, y - 2))
            surface.blit(emoji_text, emoji_rect)
            
            # Label
            label_text = self.ui.fonts['small'].render(item['label'], True, COLORS['text_dim'])
            label_rect = label_text.get_rect(center=(x, y + 16))
            surface.blit(label_text, label_rect)
    
    def on_touch(self, pos):
        """Gère le touch sur les boutons du menu."""
        n_items = len(self.MENU_ITEMS)
        menu_radius = RADIUS - 75
        
        for i, item in enumerate(self.MENU_ITEMS):
            angle = math.radians(-90 + i * (360 / n_items))
            bx = CENTER[0] + int(menu_radius * math.cos(angle))
            by = CENTER[1] + 30 + int(menu_radius * math.sin(angle))
            
            # Distance au centre du bouton
            dist = math.sqrt((pos[0] - bx) ** 2 + (pos[1] - by) ** 2)
            
            if dist < 36:
                self.ui.switch_screen(item['id'])
                return
```

## 📋 Phase 5 : Mode USB Gadget

### 📌 5.1 Configuration kernel

```bash
# Éditer /boot/config.txt
sudo nano /boot/config.txt

# Ajouter à la fin:
dtoverlay=dwc2
```

```bash
# Éditer /boot/cmdline.txt - ajouter après rootwait:
modules-load=dwc2,g_serial
```

### 📌 5.2 Module USB Gadget (`serial/gadget.py`)

```python
#!/usr/bin/env python3
"""
Gestion USB Gadget mode pour connexion série vers SoC cible.
Le Pi Zero W devient un adaptateur USB-série virtuel.
"""

import os
import subprocess
from pathlib import Path


class USBGadget:
    GADGET_PATH = '/sys/kernel/config/usb_gadget/pidebugger'
    
    def __init__(self):
        self.configured = False
    
    def setup(self, vendor_id='0x1d6b', product_id='0x0104', 
              serial='PiDebugger001', manufacturer='PiDebugger',
              product='Debug Console'):
        """Configure le gadget USB composite (serial + mass storage)."""
        
        if not os.path.exists('/sys/kernel/config/usb_gadget'):
            subprocess.run(['modprobe', 'libcomposite'], check=True)
        
        gadget = Path(self.GADGET_PATH)
        
        # Créer gadget
        gadget.mkdir(exist_ok=True)
        
        # IDs
        (gadget / 'idVendor').write_text(vendor_id)
        (gadget / 'idProduct').write_text(product_id)
        (gadget / 'bcdDevice').write_text('0x0100')
        (gadget / 'bcdUSB').write_text('0x0200')
        
        # Strings
        strings = gadget / 'strings/0x409'
        strings.mkdir(parents=True, exist_ok=True)
        (strings / 'serialnumber').write_text(serial)
        (strings / 'manufacturer').write_text(manufacturer)
        (strings / 'product').write_text(product)
        
        # Configuration
        config = gadget / 'configs/c.1'
        config.mkdir(parents=True, exist_ok=True)
        (config / 'MaxPower').write_text('250')
        
        config_strings = config / 'strings/0x409'
        config_strings.mkdir(parents=True, exist_ok=True)
        (config_strings / 'configuration').write_text('Serial + Storage')
        
        # Fonction ACM (serial)
        acm = gadget / 'functions/acm.usb0'
        acm.mkdir(exist_ok=True)
        
        # Lier fonction à config
        link = config / 'acm.usb0'
        if not link.exists():
            link.symlink_to(acm)
        
        # Activer gadget
        udc = list(Path('/sys/class/udc').iterdir())[0].name
        (gadget / 'UDC').write_text(udc)
        
        self.configured = True
        return '/dev/ttyGS0'
    
    def teardown(self):
        """Désactive le gadget USB."""
        gadget = Path(self.GADGET_PATH)
        
        if gadget.exists():
            # Désactiver
            try:
                (gadget / 'UDC').write_text('')
            except:
                pass
            
            # Supprimer liens
            for link in (gadget / 'configs/c.1').glob('*.usb*'):
                link.unlink()
            
            # Supprimer dans l'ordre inverse
            for d in ['configs/c.1/strings/0x409', 'configs/c.1',
                      'functions/acm.usb0', 'strings/0x409', '']:
                try:
                    (gadget / d).rmdir()
                except:
                    pass
        
        self.configured = False


# Script standalone pour test
if __name__ == '__main__':
    gadget = USBGadget()
    try:
        tty = gadget.setup()
        print(f'Gadget configuré: {tty}')
        input('Appuyez sur Entrée pour désactiver...')
    finally:
        gadget.teardown()
        print('Gadget désactivé')
```

### 📌 5.3 Console série (`serial/console.py`)

```python
#!/usr/bin/env python3
"""Console série avec buffer circulaire et parsing temps réel."""

import serial
import threading
from collections import deque
from typing import Callable, Optional
import re


class SerialConsole:
    def __init__(self, port: str = '/dev/ttyGS0', baudrate: int = 115200):
        self.port = port
        self.baudrate = baudrate
        self.serial: Optional[serial.Serial] = None
        self.buffer = deque(maxlen=10000)  # Buffer circulaire
        self.lines = deque(maxlen=500)     # Dernières lignes
        self.running = False
        self.thread: Optional[threading.Thread] = None
        self.callbacks: list[Callable] = []
        
        # Patterns de détection
        self.patterns = {
            'uboot_prompt': re.compile(r'^(=>|U-Boot>)\s*$'),
            'uboot_start': re.compile(r'U-Boot \d+\.\d+'),
            'linux_boot': re.compile(r'Linux version \d+\.\d+'),
            'login_prompt': re.compile(r'login:\s*$'),
            'uefi': re.compile(r'UEFI|TianoCore|EDK'),
            'spi_boot': re.compile(r'SPI|BootROM|WTMI'),
        }
        
        self.detected_stage = None
    
    def connect(self) -> bool:
        """Ouvre la connexion série."""
        try:
            self.serial = serial.Serial(
                self.port,
                self.baudrate,
                timeout=0.1,
                xonxoff=False,
                rtscts=False
            )
            return True
        except Exception as e:
            print(f'Erreur connexion: {e}')
            return False
    
    def disconnect(self):
        """Ferme la connexion."""
        self.running = False
        if self.thread:
            self.thread.join(timeout=1)
        if self.serial:
            self.serial.close()
            self.serial = None
    
    def start_reading(self):
        """Démarre la lecture en arrière-plan."""
        if not self.serial:
            return
        
        self.running = True
        self.thread = threading.Thread(target=self._read_loop, daemon=True)
        self.thread.start()
    
    def _read_loop(self):
        """Boucle de lecture."""
        line_buffer = ''
        
        while self.running and self.serial:
            try:
                data = self.serial.read(256)
                if data:
                    text = data.decode('utf-8', errors='replace')
                    
                    for char in text:
                        self.buffer.append(char)
                        
                        if char == '\n':
                            self.lines.append(line_buffer)
                            self._analyze_line(line_buffer)
                            line_buffer = ''
                        elif char != '\r':
                            line_buffer += char
                    
                    # Notifier callbacks
                    for cb in self.callbacks:
                        cb(text)
                        
            except Exception as e:
                print(f'Erreur lecture: {e}')
    
    def _analyze_line(self, line: str):
        """Analyse une ligne pour détecter le stage de boot."""
        for stage, pattern in self.patterns.items():
            if pattern.search(line):
                self.detected_stage = stage
                break
    
    def send(self, data: str):
        """Envoie des données."""
        if self.serial:
            self.serial.write(data.encode('utf-8'))
    
    def send_break(self):
        """Envoie un break (pour interrompre U-Boot)."""
        if self.serial:
            self.serial.send_break(duration=0.25)
    
    def get_recent_lines(self, n: int = 20) -> list[str]:
        """Retourne les n dernières lignes."""
        return list(self.lines)[-n:]
    
    def add_callback(self, callback: Callable):
        """Ajoute un callback pour les données reçues."""
        self.callbacks.append(callback)
```

## 📋 Phase 6 : Analyseurs de boot

### 📌 6.1 Analyseur U-Boot (`analyzers/uboot.py`)

```python
#!/usr/bin/env python3
"""Analyseur de séquence U-Boot."""

import re
from dataclasses import dataclass
from typing import Optional
from enum import Enum


class UBootStage(Enum):
    SPL = 'spl'
    TPL = 'tpl'
    MAIN = 'main'
    PROMPT = 'prompt'
    BOOT = 'boot'


@dataclass
class UBootInfo:
    version: Optional[str] = None
    board: Optional[str] = None
    cpu: Optional[str] = None
    dram: Optional[str] = None
    stage: UBootStage = UBootStage.SPL
    env_vars: dict = None
    boot_device: Optional[str] = None
    
    def __post_init__(self):
        if self.env_vars is None:
            self.env_vars = {}


class UBootAnalyzer:
    def __init__(self):
        self.info = UBootInfo()
        self.lines = []
        
        self.patterns = {
            'version': re.compile(r'U-Boot (\d+\.\d+[^\s]*)'),
            'board': re.compile(r'Board:\s*(.+)'),
            'cpu': re.compile(r'CPU:\s*(.+)'),
            'dram': re.compile(r'DRAM:\s*(.+)'),
            'spl': re.compile(r'U-Boot SPL'),
            'tpl': re.compile(r'U-Boot TPL'),
            'prompt': re.compile(r'^(=>|[a-zA-Z0-9_-]+>)\s*$'),
            'env': re.compile(r'^([a-zA-Z_][a-zA-Z0-9_]*)=(.*)$'),
            'boot_dev': re.compile(r'Boot device:\s*(.+)'),
            'loading': re.compile(r'Loading .+ from (\w+)'),
        }
    
    def feed(self, line: str) -> Optional[str]:
        """Analyse une ligne et retourne un événement si détecté."""
        self.lines.append(line)
        
        # Version
        m = self.patterns['version'].search(line)
        if m:
            self.info.version = m.group(1)
            return 'version_detected'
        
        # Board
        m = self.patterns['board'].search(line)
        if m:
            self.info.board = m.group(1).strip()
            return 'board_detected'
        
        # CPU
        m = self.patterns['cpu'].search(line)
        if m:
            self.info.cpu = m.group(1).strip()
            return 'cpu_detected'
        
        # DRAM
        m = self.patterns['dram'].search(line)
        if m:
            self.info.dram = m.group(1).strip()
            return 'dram_detected'
        
        # Stage detection
        if self.patterns['spl'].search(line):
            self.info.stage = UBootStage.SPL
            return 'spl_start'
        
        if self.patterns['tpl'].search(line):
            self.info.stage = UBootStage.TPL
            return 'tpl_start'
        
        if self.patterns['prompt'].search(line):
            self.info.stage = UBootStage.PROMPT
            return 'prompt_ready'
        
        # Boot device
        m = self.patterns['boot_dev'].search(line)
        if m:
            self.info.boot_device = m.group(1).strip()
            return 'boot_device'
        
        return None
    
    def get_summary(self) -> dict:
        """Retourne un résumé de l'analyse."""
        return {
            'version': self.info.version,
            'board': self.info.board,
            'cpu': self.info.cpu,
            'dram': self.info.dram,
            'stage': self.info.stage.value,
            'boot_device': self.info.boot_device,
        }
    
    def generate_commands(self) -> list[str]:
        """Génère des commandes U-Boot utiles pour le board détecté."""
        cmds = [
            'version',
            'bdinfo',
            'printenv',
            'mmc info',
            'usb info',
        ]
        
        if 'marvell' in (self.info.board or '').lower():
            cmds.extend([
                'bubt',  # Burn boot image
                'hw_info',
            ])
        
        return cmds
```

## 📋 Phase 7 : Dashboard principal

### 📌 7.1 Écran Dashboard (`ui/screens/dashboard.py`)

```python
#!/usr/bin/env python3
"""Dashboard principal style LuCI OpenWRT."""

import pygame
import math
from ui.core import Screen, COLORS, CENTER, RADIUS


class DashboardScreen(Screen):
    def __init__(self, ui):
        super().__init__(ui)
        
        self.menu_items = [
            {'id': 'clock', 'label': 'TIME', 'icon': '⏰'},
            {'id': 'serial', 'label': 'UART', 'icon': '📡'},
            {'id': 'boot', 'label': 'BOOT', 'icon': '🔧'},
            {'id': 'net', 'label': 'NET', 'icon': '🌐'},
            {'id': 'files', 'label': 'FILE', 'icon': '📁'},
            {'id': 'settings', 'label': 'CONF', 'icon': '⚙️'},
        ]
        
        self.selected = 0
        self.status = {
            'usb': False,
            'serial': False,
            'target': 'Unknown',
        }
    
    def draw(self, surface):
        # Titre central
        title = self.ui.fonts['large'].render('PiDebugger', True, COLORS['primary'])
        title_rect = title.get_rect(center=(CENTER[0], 60))
        surface.blit(title, title_rect)
        
        # Status bar
        status_y = 100
        status_color = COLORS['secondary'] if self.status['usb'] else COLORS['danger']
        pygame.draw.circle(surface, status_color, (CENTER[0] - 60, status_y), 6)
        usb_text = self.ui.fonts['small'].render('USB', True, COLORS['text_dim'])
        surface.blit(usb_text, (CENTER[0] - 50, status_y - 8))
        
        status_color = COLORS['secondary'] if self.status['serial'] else COLORS['danger']
        pygame.draw.circle(surface, status_color, (CENTER[0] + 40, status_y), 6)
        ser_text = self.ui.fonts['small'].render('UART', True, COLORS['text_dim'])
        surface.blit(ser_text, (CENTER[0] + 50, status_y - 8))
        
        # Target info
        target_text = self.ui.fonts['medium'].render(
            self.status['target'], True, COLORS['text']
        )
        target_rect = target_text.get_rect(center=(CENTER[0], 140))
        surface.blit(target_text, target_rect)
        
        # Menu radial
        n_items = len(self.menu_items)
        menu_radius = RADIUS - 80
        
        for i, item in enumerate(self.menu_items):
            angle = math.radians(-90 + i * (360 / n_items))
            x = CENTER[0] + int(menu_radius * math.cos(angle))
            y = CENTER[1] + int(menu_radius * math.sin(angle))
            
            # Fond du bouton
            btn_radius = 40
            if i == self.selected:
                pygame.draw.circle(surface, COLORS['primary'], (x, y), btn_radius)
                pygame.draw.circle(surface, COLORS['text'], (x, y), btn_radius, 2)
            else:
                pygame.draw.circle(surface, COLORS['bg_light'], (x, y), btn_radius)
                pygame.draw.circle(surface, COLORS['border'], (x, y), btn_radius, 2)
            
            # Label
            label = self.ui.fonts['small'].render(item['label'], True, COLORS['text'])
            label_rect = label.get_rect(center=(x, y))
            surface.blit(label, label_rect)
        
        # Instructions
        hint = self.ui.fonts['small'].render('Touch to select', True, COLORS['text_dim'])
        hint_rect = hint.get_rect(center=(CENTER[0], RADIUS * 2 - 40))
        surface.blit(hint, hint_rect)
    
    def on_touch(self, pos):
        # Détecter quel item est touché
        n_items = len(self.menu_items)
        menu_radius = RADIUS - 80
        
        for i, item in enumerate(self.menu_items):
            angle = math.radians(-90 + i * (360 / n_items))
            x = CENTER[0] + int(menu_radius * math.cos(angle))
            y = CENTER[1] + int(menu_radius * math.sin(angle))
            
            # Distance au centre du bouton
            dist = math.sqrt((pos[0] - x) ** 2 + (pos[1] - y) ** 2)
            
            if dist < 45:
                self.selected = i
                # Navigation
                screen_id = item['id']
                if screen_id in self.ui.screens:
                    self.ui.switch_screen(screen_id)
                break
    
    def update_status(self, usb: bool = None, serial: bool = None, target: str = None):
        if usb is not None:
            self.status['usb'] = usb
        if serial is not None:
            self.status['serial'] = serial
        if target is not None:
            self.status['target'] = target
```

## 📋 Phase 8 : Point d'entrée

### 📌 8.1 Main (`main.py`)

```python
#!/usr/bin/env python3
"""
PiDebugger - Outil portable de debug SoC
Point d'entrée principal
"""

import sys
import signal
from ui.core import CircularUI
from ui.screens.clock import ClockScreen
from ui.screens.dashboard import DashboardScreen
from serial.gadget import USBGadget
from serial.console import SerialConsole


def signal_handler(sig, frame):
    print('\nArrêt...')
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    print('PiDebugger v0.1')
    print('Initialisation...')
    
    # Initialiser USB Gadget
    gadget = USBGadget()
    try:
        tty = gadget.setup()
        print(f'USB Gadget: {tty}')
    except Exception as e:
        print(f'Warning: USB Gadget non disponible: {e}')
        tty = None
    
    # Initialiser console série
    console = None
    if tty:
        console = SerialConsole(tty)
        if console.connect():
            console.start_reading()
            print('Console série active')
    
    # Initialiser UI
    ui = CircularUI()
    
    # Enregistrer les écrans
    ui.register_screen('clock', ClockScreen)
    ui.register_screen('dashboard', DashboardScreen)
    
    # Démarrer sur l'horloge
    ui.switch_screen('clock')
    
    print('Démarrage interface...')
    
    try:
        ui.run()
    finally:
        if console:
            console.disconnect()
        gadget.teardown()
        print('Arrêt propre')


if __name__ == '__main__':
    main()
```

## 📋 Phase 9 : Service systemd

### 📌 9.1 Créer le service

```bash
sudo nano /etc/systemd/system/pidebugger.service
```

```ini
[Unit]
Description=PiDebugger Interface
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/pi/pidebugger
ExecStart=/usr/bin/python3 /home/pi/pidebugger/main.py
Restart=on-failure
RestartSec=5
Environment=SDL_FBDEV=/dev/fb0
Environment=DISPLAY=:0

[Install]
WantedBy=multi-user.target
```

### 📌 9.2 Activer le service

```bash
sudo systemctl daemon-reload
sudo systemctl enable pidebugger
sudo systemctl start pidebugger

# Vérifier le statut
sudo systemctl status pidebugger

# Voir les logs
journalctl -u pidebugger -f
```

## 📋 Phase 10 : Contrôle alimentation USB cible

### 📌 10.1 Architecture USB OTG Power

Le Pi Zero W peut alimenter les cibles EspressoBin/MochaBin via son port USB OTG en mode host avec contrôle VBUS.

```
┌─────────────────┐      USB Cable       ┌──────────────────┐
│   Pi Zero W     │◄────────────────────►│   EspressoBin    │
│                 │                       │                  │
│  USB OTG Port   │    +5V (500mA-2A)    │  USB-C / Debug   │
│  (dwc2 driver)  │────────────────────►│  Port            │
│                 │                       │                  │
│  GPIO Control   │    VBUS Enable       │  Powered via     │
│  (optional)     │────────────────────►│  USB             │
└─────────────────┘                       └──────────────────┘
```

### 📌 10.2 Configuration kernel pour USB Host

```bash
# /boot/config.txt
dtoverlay=dwc2,dr_mode=host

# Pour le mode dual (gadget + host switchable)
dtoverlay=dwc2,dr_mode=otg
```

### 📌 10.3 Module de contrôle alimentation (`power/usb_power.py`)

```python
#!/usr/bin/env python3
"""
Contrôle alimentation USB pour cibles SoC.
Supporte EspressoBin (5V USB-C) et MochaBin (12V barrel - via relay).
"""

import subprocess
import time
from pathlib import Path
from dataclasses import dataclass
from enum import Enum
from typing import Optional
import threading


class PowerState(Enum):
    OFF = 'off'
    ON = 'on'
    STANDBY = 'standby'
    FAULT = 'fault'


class TargetPlatform(Enum):
    ESPRESSOBIN = 'espressobin'
    ESPRESSOBIN_V7 = 'espressobin-v7'
    ESPRESSOBIN_ULTRA = 'espressobin-ultra'
    MOCHABIN = 'mochabin'


@dataclass
class PowerConfig:
    """Configuration alimentation par plateforme."""
    platform: TargetPlatform
    voltage: float  # Volts
    max_current: float  # Ampères
    usb_powered: bool  # True si alimentable via USB
    connector: str
    boot_delay: float  # Délai après power-on avant boot


PLATFORM_CONFIGS = {
    TargetPlatform.ESPRESSOBIN: PowerConfig(
        platform=TargetPlatform.ESPRESSOBIN,
        voltage=5.0,
        max_current=2.0,
        usb_powered=True,
        connector='USB-C or Barrel 5V',
        boot_delay=0.5,
    ),
    TargetPlatform.ESPRESSOBIN_V7: PowerConfig(
        platform=TargetPlatform.ESPRESSOBIN_V7,
        voltage=5.0,
        max_current=2.0,
        usb_powered=True,
        connector='USB-C',
        boot_delay=0.5,
    ),
    TargetPlatform.ESPRESSOBIN_ULTRA: PowerConfig(
        platform=TargetPlatform.ESPRESSOBIN_ULTRA,
        voltage=12.0,
        max_current=5.0,
        usb_powered=False,  # Nécessite 12V externe
        connector='Barrel 5.5x2.1mm',
        boot_delay=1.0,
    ),
    TargetPlatform.MOCHABIN: PowerConfig(
        platform=TargetPlatform.MOCHABIN,
        voltage=12.0,
        max_current=3.0,
        usb_powered=False,  # Nécessite 12V externe
        connector='Barrel 5.5x2.1mm',
        boot_delay=1.0,
    ),
}


class USBPowerController:
    """
    Contrôleur d'alimentation USB pour le Pi Zero.
    
    Modes supportés:
    1. USB Host direct (5V via VBUS) - pour EspressoBin
    2. GPIO relay control - pour alimentations 12V externes
    3. USB PD negotiation (future) - pour USB-C PD
    """
    
    VBUS_GPIO = 4  # GPIO pour contrôle VBUS externe (optionnel)
    RELAY_GPIO = 17  # GPIO pour relais 12V (optionnel)
    
    USB_HOST_PATH = Path('/sys/bus/usb/devices')
    DWC2_PATH = Path('/sys/devices/platform/soc/20980000.usb')
    
    def __init__(self, platform: TargetPlatform = TargetPlatform.ESPRESSOBIN):
        self.platform = platform
        self.config = PLATFORM_CONFIGS[platform]
        self.state = PowerState.OFF
        self.current_ma = 0
        self.voltage_v = 0
        self.uptime_seconds = 0
        self._monitor_thread: Optional[threading.Thread] = None
        self._monitoring = False
    
    def set_platform(self, platform: TargetPlatform):
        """Change la plateforme cible."""
        if self.state == PowerState.ON:
            raise RuntimeError("Cannot change platform while power is ON")
        self.platform = platform
        self.config = PLATFORM_CONFIGS[platform]
    
    def power_on(self) -> bool:
        """Active l'alimentation de la cible."""
        if self.state == PowerState.ON:
            return True
        
        try:
            if self.config.usb_powered:
                # Alimentation via USB VBUS
                success = self._enable_usb_host_power()
            else:
                # Alimentation via relais externe
                success = self._enable_relay_power()
            
            if success:
                self.state = PowerState.ON
                self._start_monitoring()
                
                # Attendre le délai de boot
                time.sleep(self.config.boot_delay)
                
            return success
            
        except Exception as e:
            print(f"Power on error: {e}")
            self.state = PowerState.FAULT
            return False
    
    def power_off(self) -> bool:
        """Coupe l'alimentation de la cible."""
        self._stop_monitoring()
        
        try:
            if self.config.usb_powered:
                success = self._disable_usb_host_power()
            else:
                success = self._disable_relay_power()
            
            if success:
                self.state = PowerState.OFF
                self.current_ma = 0
                self.voltage_v = 0
                self.uptime_seconds = 0
                
            return success
            
        except Exception as e:
            print(f"Power off error: {e}")
            return False
    
    def power_cycle(self, delay: float = 2.0) -> bool:
        """Effectue un cycle power off/on."""
        if not self.power_off():
            return False
        
        time.sleep(delay)
        return self.power_on()
    
    def _enable_usb_host_power(self) -> bool:
        """Active le mode USB host avec VBUS."""
        # Méthode 1: Via sysfs si disponible
        mode_path = self.DWC2_PATH / 'mode'
        if mode_path.exists():
            try:
                mode_path.write_text('host')
                return True
            except:
                pass
        
        # Méthode 2: Via modprobe
        try:
            subprocess.run(
                ['modprobe', 'dwc2', 'dr_mode=host'],
                check=True, capture_output=True
            )
            return True
        except:
            pass
        
        # Méthode 3: GPIO direct pour VBUS
        return self._gpio_set(self.VBUS_GPIO, True)
    
    def _disable_usb_host_power(self) -> bool:
        """Désactive le VBUS USB."""
        # Repasser en mode gadget
        mode_path = self.DWC2_PATH / 'mode'
        if mode_path.exists():
            try:
                mode_path.write_text('peripheral')
            except:
                pass
        
        return self._gpio_set(self.VBUS_GPIO, False)
    
    def _enable_relay_power(self) -> bool:
        """Active le relais pour alimentation 12V."""
        return self._gpio_set(self.RELAY_GPIO, True)
    
    def _disable_relay_power(self) -> bool:
        """Désactive le relais 12V."""
        return self._gpio_set(self.RELAY_GPIO, False)
    
    def _gpio_set(self, gpio: int, value: bool) -> bool:
        """Configure un GPIO."""
        gpio_path = Path(f'/sys/class/gpio/gpio{gpio}')
        
        try:
            # Exporter le GPIO si nécessaire
            if not gpio_path.exists():
                Path('/sys/class/gpio/export').write_text(str(gpio))
                time.sleep(0.1)
            
            # Configurer en sortie
            (gpio_path / 'direction').write_text('out')
            
            # Définir la valeur
            (gpio_path / 'value').write_text('1' if value else '0')
            
            return True
        except Exception as e:
            print(f"GPIO {gpio} error: {e}")
            return False
    
    def _start_monitoring(self):
        """Démarre le monitoring de consommation."""
        self._monitoring = True
        self._monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self._monitor_thread.start()
    
    def _stop_monitoring(self):
        """Arrête le monitoring."""
        self._monitoring = False
        if self._monitor_thread:
            self._monitor_thread.join(timeout=1)
    
    def _monitor_loop(self):
        """Boucle de monitoring."""
        start_time = time.time()
        
        while self._monitoring:
            self.uptime_seconds = int(time.time() - start_time)
            
            # Lire la consommation USB si disponible
            # (nécessite un INA219 ou similaire pour mesure réelle)
            # Ici on simule pour la démo
            if self.state == PowerState.ON:
                self.voltage_v = self.config.voltage * (0.98 + 0.02 * (time.time() % 1))
                self.current_ma = 500 + 300 * (time.time() % 2)  # Simulation
            
            time.sleep(1)
    
    def get_status(self) -> dict:
        """Retourne le status actuel."""
        return {
            'platform': self.platform.value,
            'state': self.state.value,
            'voltage_v': round(self.voltage_v, 2),
            'current_ma': int(self.current_ma),
            'power_w': round(self.voltage_v * self.current_ma / 1000, 2),
            'uptime_s': self.uptime_seconds,
            'config': {
                'max_voltage': self.config.voltage,
                'max_current': self.config.max_current,
                'connector': self.config.connector,
                'usb_powered': self.config.usb_powered,
            }
        }


class PowerSequencer:
    """
    Séquenceur pour les opérations power complexes.
    Gère les séquences de boot recovery, flash, etc.
    """
    
    def __init__(self, power: USBPowerController):
        self.power = power
    
    def boot_to_uboot(self, timeout: float = 10.0) -> bool:
        """
        Séquence pour atteindre le prompt U-Boot.
        Power cycle + envoi break pour stopper autoboot.
        """
        # Power cycle
        self.power.power_off()
        time.sleep(1)
        self.power.power_on()
        
        # Attendre et envoyer break
        # (nécessite la console série)
        return True
    
    def recovery_mode(self) -> bool:
        """
        Met la cible en mode recovery (UART boot).
        Pour EspressoBin: maintenir le bouton reset pendant power-on.
        """
        self.power.power_off()
        time.sleep(0.5)
        
        # Signal de recovery (plateforme spécifique)
        # ...
        
        self.power.power_on()
        return True
    
    def flash_sequence(self) -> bool:
        """
        Séquence complète de flash:
        1. Power off
        2. Power on en mode recovery
        3. Upload firmware via UART
        4. Reset normal
        """
        pass


# Test standalone
if __name__ == '__main__':
    controller = USBPowerController(TargetPlatform.ESPRESSOBIN)
    
    print(f"Platform: {controller.platform.value}")
    print(f"Config: {controller.config}")
    
    print("\nPowering on...")
    if controller.power_on():
        print("Power ON successful")
        
        for i in range(5):
            time.sleep(1)
            status = controller.get_status()
            print(f"  {status['voltage_v']}V @ {status['current_ma']}mA = {status['power_w']}W")
        
        print("\nPowering off...")
        controller.power_off()
        print("Power OFF")
    else:
        print("Power ON failed")
```

### 📌 10.4 Écran Power Control (`ui/screens/power.py`)

```python
#!/usr/bin/env python3
"""Écran de contrôle alimentation USB."""

import pygame
import math
from ui.core import Screen, COLORS, CENTER, RADIUS
from power.usb_power import USBPowerController, TargetPlatform, PowerState


class PowerScreen(Screen):
    """Interface de contrôle alimentation."""
    
    PLATFORM_NAMES = {
        TargetPlatform.ESPRESSOBIN: 'EspressoBin',
        TargetPlatform.ESPRESSOBIN_V7: 'EspressoBin V7',
        TargetPlatform.ESPRESSOBIN_ULTRA: 'Espresso Ultra',
        TargetPlatform.MOCHABIN: 'MochaBin',
    }
    
    def __init__(self, ui):
        super().__init__(ui)
        self.controller = USBPowerController()
        self.platforms = list(TargetPlatform)
        self.platform_index = 0
        self.button_pressed = False
    
    def draw(self, surface):
        # Titre
        title = self.ui.fonts['medium'].render('USB Power Control', True, (255, 87, 34))
        title_rect = title.get_rect(center=(CENTER, 35))
        surface.blit(title, title_rect)
        
        # Sélecteur de plateforme
        platform = self.platforms[self.platform_index]
        platform_name = self.PLATFORM_NAMES[platform]
        
        pygame.draw.rect(surface, COLORS['bgLight'], 
                        (CENTER - 80, 55, 160, 30), border_radius=6)
        pygame.draw.rect(surface, COLORS['border'], 
                        (CENTER - 80, 55, 160, 30), 2, border_radius=6)
        
        plat_text = self.ui.fonts['medium'].render(platform_name, True, COLORS['text'])
        plat_rect = plat_text.get_rect(center=(CENTER, 70))
        surface.blit(plat_text, plat_rect)
        
        # Flèches navigation
        arrow_left = self.ui.fonts['medium'].render('◀', True, COLORS['textDim'])
        arrow_right = self.ui.fonts['medium'].render('▶', True, COLORS['textDim'])
        surface.blit(arrow_left, (CENTER - 95, 62))
        surface.blit(arrow_right, (CENTER + 82, 62))
        
        # Gros bouton power
        status = self.controller.get_status()
        is_on = status['state'] == 'on'
        
        btn_radius = 70
        btn_color = COLORS['secondary'] if is_on else COLORS['danger']
        
        # Cercle externe (progress si on)
        pygame.draw.circle(surface, COLORS['bgLight'], CENTER, btn_radius + 10, 0)
        pygame.draw.circle(surface, COLORS['border'], CENTER, btn_radius + 10, 2)
        
        if is_on:
            # Arc de progression
            rect = pygame.Rect(CENTER - btn_radius - 5, CENTER - btn_radius - 5,
                              (btn_radius + 5) * 2, (btn_radius + 5) * 2)
            pygame.draw.arc(surface, btn_color, rect, 
                           math.radians(-135), math.radians(135), 6)
        
        # Cercle bouton
        pygame.draw.circle(surface, (*btn_color[:3], 50), CENTER, btn_radius)
        
        # Icône power
        icon_color = btn_color
        # Ligne verticale
        pygame.draw.line(surface, icon_color, 
                        (CENTER, CENTER - 25), (CENTER, CENTER + 5), 6)
        # Arc
        pygame.draw.arc(surface, icon_color,
                       (CENTER - 25, CENTER - 15, 50, 50),
                       math.radians(40), math.radians(140), 6)
        
        # Label état
        state_text = 'POWER ON' if is_on else 'POWER OFF'
        state_label = self.ui.fonts['medium'].render(state_text, True, btn_color)
        state_rect = state_label.get_rect(center=(CENTER, CENTER + 60))
        surface.blit(state_label, state_rect)
        
        # Stats
        stats_y = CENTER + 100
        
        # Voltage
        v_label = self.ui.fonts['small'].render('VOLTAGE', True, COLORS['textDim'])
        surface.blit(v_label, (60, stats_y))
        v_value = f"{status['voltage_v']:.2f}V" if is_on else '--'
        v_text = self.ui.fonts['medium'].render(v_value, True, 
                 COLORS['secondary'] if is_on else COLORS['textDim'])
        surface.blit(v_text, (60, stats_y + 18))
        
        # Current
        c_label = self.ui.fonts['small'].render('CURRENT', True, COLORS['textDim'])
        c_rect = c_label.get_rect(center=(CENTER, stats_y))
        surface.blit(c_label, c_rect)
        c_value = f"{status['current_ma']}mA" if is_on else '--'
        c_text = self.ui.fonts['medium'].render(c_value, True,
                 COLORS['warning'] if is_on else COLORS['textDim'])
        c_rect = c_text.get_rect(center=(CENTER, stats_y + 18))
        surface.blit(c_text, c_rect)
        
        # Uptime
        u_label = self.ui.fonts['small'].render('UPTIME', True, COLORS['textDim'])
        surface.blit(u_label, (SCREEN_SIZE - 120, stats_y))
        if is_on:
            mins = status['uptime_s'] // 60
            secs = status['uptime_s'] % 60
            u_value = f"{mins}:{secs:02d}"
        else:
            u_value = '--'
        u_text = self.ui.fonts['medium'].render(u_value, True,
                 COLORS['primary'] if is_on else COLORS['textDim'])
        surface.blit(u_text, (SCREEN_SIZE - 120, stats_y + 18))
        
        # Info connecteur
        config = status['config']
        info = f"{config['connector']} • Max {config['max_voltage']}V/{config['max_current']}A"
        info_text = self.ui.fonts['small'].render(info, True, COLORS['textDim'])
        info_rect = info_text.get_rect(center=(CENTER, stats_y + 55))
        surface.blit(info_text, info_rect)
    
    def on_touch(self, pos):
        x, y = pos
        
        # Bouton power (centre)
        dist = math.sqrt((x - CENTER) ** 2 + (y - CENTER) ** 2)
        if dist < 80:
            self._toggle_power()
            return
        
        # Sélecteur plateforme
        if 55 < y < 85:
            if x < CENTER - 40:
                self.platform_index = (self.platform_index - 1) % len(self.platforms)
                self._update_platform()
            elif x > CENTER + 40:
                self.platform_index = (self.platform_index + 1) % len(self.platforms)
                self._update_platform()
    
    def _toggle_power(self):
        """Bascule l'alimentation."""
        status = self.controller.get_status()
        if status['state'] == 'on':
            self.controller.power_off()
        else:
            self.controller.power_on()
    
    def _update_platform(self):
        """Met à jour la plateforme sélectionnée."""
        if self.controller.state != PowerState.ON:
            platform = self.platforms[self.platform_index]
            self.controller.set_platform(platform)
```

### 📌 10.5 Schéma de câblage USB Power

```
Pour EspressoBin (5V USB):
═══════════════════════════

Pi Zero W                    EspressoBin
┌─────────┐                  ┌─────────┐
│         │   USB Cable      │         │
│ USB OTG ├──────────────────┤ USB-C   │
│  (data) │   D+/D-          │ (debug) │
│         │                  │         │
│  VBUS   ├──────────────────┤ VBUS    │
│  (5V)   │   5V @ 2A max    │ (power) │
│         │                  │         │
│   GND   ├──────────────────┤ GND     │
└─────────┘                  └─────────┘


Pour MochaBin (12V externe avec relay):
═══════════════════════════════════════

Pi Zero W                    Relay Module              MochaBin
┌─────────┐                  ┌─────────┐              ┌─────────┐
│         │                  │         │   12V PSU   │         │
│ GPIO 17 ├──────────────────┤ IN      │◄────────────┤ Barrel  │
│         │                  │         │             │ Jack    │
│   3.3V  ├──────────────────┤ VCC     │             │         │
│         │                  │         │             │         │
│   GND   ├──────────────────┤ GND     │             │         │
│         │                  │         │             │         │
│ USB OTG ├──────────────────┼─────────┼─────────────┤ USB-C   │
│  (data) │   D+/D- only     │         │  (debug)    │ (debug) │
└─────────┘                  └─────────┘             └─────────┘
```

## 📋 Phase 11 : Moniteur série temps réel

### 📌 10.1 Écran Serial Monitor (`ui/screens/serial_monitor.py`)

```python
#!/usr/bin/env python3
"""
Moniteur série temps réel avec scroll fluide et coloration syntaxique.
Optimisé pour écran circulaire 480x480.
"""

import pygame
import math
import re
import threading
from collections import deque
from datetime import datetime
from ui.core import Screen, COLORS, CENTER, RADIUS


class LineType:
    """Types de lignes pour coloration."""
    NORMAL = 'normal'
    UBOOT = 'uboot'
    KERNEL = 'kernel'
    ERROR = 'error'
    WARNING = 'warning'
    PROMPT = 'prompt'
    TIMESTAMP = 'timestamp'
    SPI = 'spi'
    UEFI = 'uefi'


class SerialLine:
    """Représente une ligne de la console."""
    __slots__ = ['text', 'type', 'timestamp', 'raw']
    
    def __init__(self, text: str, line_type: str = LineType.NORMAL):
        self.text = text[:60]  # Tronquer pour l'écran rond
        self.raw = text
        self.type = line_type
        self.timestamp = datetime.now()


class SerialBuffer:
    """Buffer circulaire thread-safe avec classification."""
    
    def __init__(self, maxlen: int = 2000):
        self.lines = deque(maxlen=maxlen)
        self.lock = threading.Lock()
        self.new_data = threading.Event()
        
        # Patterns de classification
        self.patterns = [
            (re.compile(r'^(=>|[A-Za-z0-9_-]+>)\s*'), LineType.PROMPT),
            (re.compile(r'U-Boot|SPL|TPL', re.I), LineType.UBOOT),
            (re.compile(r'Linux version|kernel:|initramfs', re.I), LineType.KERNEL),
            (re.compile(r'error|fail|fatal', re.I), LineType.ERROR),
            (re.compile(r'warn|caution', re.I), LineType.WARNING),
            (re.compile(r'WTMI|BootROM|SPI|SPINOR', re.I), LineType.SPI),
            (re.compile(r'UEFI|EFI|TianoCore|EDK', re.I), LineType.UEFI),
            (re.compile(r'^\[\s*\d+\.\d+\]'), LineType.TIMESTAMP),
        ]
    
    def classify(self, text: str) -> str:
        """Classifie une ligne de texte."""
        for pattern, line_type in self.patterns:
            if pattern.search(text):
                return line_type
        return LineType.NORMAL
    
    def append(self, text: str):
        """Ajoute une ligne."""
        line_type = self.classify(text)
        line = SerialLine(text, line_type)
        
        with self.lock:
            self.lines.append(line)
        self.new_data.set()
    
    def get_visible(self, start: int, count: int) -> list:
        """Retourne les lignes visibles."""
        with self.lock:
            lines = list(self.lines)
        
        total = len(lines)
        if start < 0:
            start = max(0, total + start)
        
        end = min(start + count, total)
        return lines[start:end], total
    
    def get_last(self, count: int) -> list:
        """Retourne les dernières lignes."""
        with self.lock:
            return list(self.lines)[-count:]


class SerialMonitorScreen(Screen):
    """Écran moniteur série avec scroll temps réel."""
    
    # Couleurs par type de ligne
    LINE_COLORS = {
        LineType.NORMAL: (200, 200, 200),
        LineType.UBOOT: (100, 200, 255),      # Bleu clair
        LineType.KERNEL: (150, 255, 150),      # Vert clair
        LineType.ERROR: (255, 100, 100),       # Rouge
        LineType.WARNING: (255, 200, 100),     # Orange
        LineType.PROMPT: (255, 255, 100),      # Jaune
        LineType.TIMESTAMP: (150, 150, 150),   # Gris
        LineType.SPI: (255, 150, 255),         # Magenta
        LineType.UEFI: (100, 255, 255),        # Cyan
    }
    
    def __init__(self, ui):
        super().__init__(ui)
        
        self.buffer = SerialBuffer()
        self.scroll_offset = 0
        self.auto_scroll = True
        self.paused = False
        
        # Dimensions zone d'affichage (cercle inscrit)
        self.display_radius = RADIUS - 40
        self.line_height = 16
        self.max_visible_lines = 20
        
        # Zone de texte (rectangle inscrit dans le cercle)
        self.text_width = int(self.display_radius * 1.4)
        self.text_left = CENTER[0] - self.text_width // 2
        
        # Font monospace
        try:
            self.mono_font = pygame.font.Font(
                '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 12
            )
        except:
            self.mono_font = pygame.font.SysFont('monospace', 12)
        
        # Input buffer
        self.input_text = ''
        self.input_active = False
        
        # Touch zones
        self.scroll_touch_start = None
        self.last_touch_y = 0
        
        # Stats
        self.bytes_received = 0
        self.lines_received = 0
    
    def on_enter(self):
        """Appelé quand l'écran devient actif."""
        self.auto_scroll = True
    
    def feed_data(self, data: str):
        """Reçoit des données du port série."""
        self.bytes_received += len(data)
        
        for line in data.split('\n'):
            line = line.strip('\r')
            if line:
                self.buffer.append(line)
                self.lines_received += 1
    
    def draw(self, surface):
        # Header circulaire
        self._draw_header(surface)
        
        # Zone de log
        self._draw_log_area(surface)
        
        # Scrollbar
        self._draw_scrollbar(surface)
        
        # Status bar
        self._draw_status(surface)
        
        # Input zone
        if self.input_active:
            self._draw_input(surface)
    
    def _draw_header(self, surface):
        """Dessine l'en-tête."""
        # Titre
        title = self.ui.fonts['medium'].render('Serial Monitor', True, COLORS['primary'])
        title_rect = title.get_rect(center=(CENTER[0], 35))
        surface.blit(title, title_rect)
        
        # Indicateurs
        # Auto-scroll
        auto_color = COLORS['secondary'] if self.auto_scroll else COLORS['text_dim']
        pygame.draw.circle(surface, auto_color, (CENTER[0] - 80, 55), 5)
        auto_text = self.ui.fonts['small'].render('AUTO', True, auto_color)
        surface.blit(auto_text, (CENTER[0] - 72, 48))
        
        # Pause
        pause_color = COLORS['warning'] if self.paused else COLORS['text_dim']
        pygame.draw.circle(surface, pause_color, (CENTER[0] + 50, 55), 5)
        pause_text = self.ui.fonts['small'].render('PAUSE', True, pause_color)
        surface.blit(pause_text, (CENTER[0] + 58, 48))
    
    def _draw_log_area(self, surface):
        """Dessine la zone de log avec scroll."""
        # Fond semi-transparent
        log_rect = pygame.Rect(
            self.text_left - 10,
            70,
            self.text_width + 20,
            320
        )
        
        # Masque arrondi pour la zone de log
        log_surface = pygame.Surface((log_rect.width, log_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(log_surface, (20, 22, 26, 230), 
                        (0, 0, log_rect.width, log_rect.height), 
                        border_radius=10)
        surface.blit(log_surface, log_rect.topleft)
        
        # Obtenir les lignes visibles
        if self.auto_scroll:
            lines = self.buffer.get_last(self.max_visible_lines)
        else:
            lines, total = self.buffer.get_visible(
                total - self.max_visible_lines - self.scroll_offset,
                self.max_visible_lines
            )
        
        # Dessiner les lignes
        y = 75
        for line in lines:
            # Vérifier si la ligne est dans le cercle visible
            if y > 70 and y < 385:
                color = self.LINE_COLORS.get(line.type, self.LINE_COLORS[LineType.NORMAL])
                
                # Tronquer le texte si nécessaire
                display_text = line.text
                text_surface = self.mono_font.render(display_text, True, color)
                
                # Clip horizontal
                clip_rect = pygame.Rect(0, 0, self.text_width, self.line_height)
                surface.blit(text_surface, (self.text_left, y), clip_rect)
            
            y += self.line_height
    
    def _draw_scrollbar(self, surface):
        """Dessine la scrollbar verticale."""
        _, total = self.buffer.get_visible(0, 1)
        
        if total <= self.max_visible_lines:
            return
        
        # Position de la scrollbar (arc sur le côté droit)
        bar_height = 250
        bar_top = 95
        
        visible_ratio = self.max_visible_lines / total
        thumb_height = max(20, int(bar_height * visible_ratio))
        
        if self.auto_scroll:
            thumb_pos = bar_height - thumb_height
        else:
            scroll_ratio = self.scroll_offset / (total - self.max_visible_lines)
            thumb_pos = int((bar_height - thumb_height) * (1 - scroll_ratio))
        
        # Track
        pygame.draw.line(surface, COLORS['border'], 
                        (CENTER[0] + 170, bar_top),
                        (CENTER[0] + 170, bar_top + bar_height), 2)
        
        # Thumb
        pygame.draw.line(surface, COLORS['primary'],
                        (CENTER[0] + 170, bar_top + thumb_pos),
                        (CENTER[0] + 170, bar_top + thumb_pos + thumb_height), 6)
    
    def _draw_status(self, surface):
        """Dessine la barre de status."""
        status_y = RADIUS * 2 - 60
        
        # Compteurs
        stats = f"RX: {self.bytes_received:,} B | {self.lines_received} lines"
        stats_text = self.ui.fonts['small'].render(stats, True, COLORS['text_dim'])
        stats_rect = stats_text.get_rect(center=(CENTER[0], status_y))
        surface.blit(stats_text, stats_rect)
        
        # Boutons tactiles
        btn_y = RADIUS * 2 - 35
        
        # Bouton Clear
        pygame.draw.circle(surface, COLORS['bg_light'], (CENTER[0] - 60, btn_y), 20)
        pygame.draw.circle(surface, COLORS['border'], (CENTER[0] - 60, btn_y), 20, 2)
        clr = self.ui.fonts['small'].render('CLR', True, COLORS['text'])
        clr_rect = clr.get_rect(center=(CENTER[0] - 60, btn_y))
        surface.blit(clr, clr_rect)
        
        # Bouton Send
        pygame.draw.circle(surface, COLORS['primary'], (CENTER[0] + 60, btn_y), 20)
        snd = self.ui.fonts['small'].render('SND', True, COLORS['text'])
        snd_rect = snd.get_rect(center=(CENTER[0] + 60, btn_y))
        surface.blit(snd, snd_rect)
    
    def _draw_input(self, surface):
        """Dessine la zone de saisie."""
        input_rect = pygame.Rect(self.text_left, 395, self.text_width, 25)
        pygame.draw.rect(surface, COLORS['bg_light'], input_rect, border_radius=5)
        pygame.draw.rect(surface, COLORS['primary'], input_rect, 2, border_radius=5)
        
        # Texte saisi
        input_display = '> ' + self.input_text + '_'
        input_surface = self.mono_font.render(input_display, True, COLORS['text'])
        surface.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))
    
    def on_touch(self, pos):
        """Gère les touches."""
        x, y = pos
        
        # Zone header - toggle auto-scroll
        if 45 < y < 65:
            if CENTER[0] - 90 < x < CENTER[0] - 40:
                self.auto_scroll = not self.auto_scroll
                return
            elif CENTER[0] + 40 < x < CENTER[0] + 100:
                self.paused = not self.paused
                return
        
        # Zone boutons bas
        btn_y = RADIUS * 2 - 35
        if btn_y - 25 < y < btn_y + 25:
            # Clear
            if abs(x - (CENTER[0] - 60)) < 25:
                self.buffer.lines.clear()
                self.bytes_received = 0
                self.lines_received = 0
                return
            # Send
            elif abs(x - (CENTER[0] + 60)) < 25:
                self.input_active = not self.input_active
                return
        
        # Zone log - début scroll
        if 70 < y < 390:
            self.scroll_touch_start = y
            self.last_touch_y = y
            self.auto_scroll = False
    
    def on_touch_move(self, pos):
        """Gère le déplacement tactile (scroll)."""
        if self.scroll_touch_start is not None:
            delta = self.last_touch_y - pos[1]
            self.last_touch_y = pos[1]
            
            # Convertir en lignes
            lines_delta = delta / self.line_height
            self.scroll_offset = max(0, self.scroll_offset + int(lines_delta))
    
    def on_touch_end(self, pos):
        """Fin du touch."""
        self.scroll_touch_start = None
    
    def on_key(self, key, char):
        """Gère la saisie clavier."""
        if not self.input_active:
            return
        
        if key == pygame.K_RETURN:
            # Envoyer la commande
            if hasattr(self, 'serial_console') and self.serial_console:
                self.serial_console.send(self.input_text + '\n')
            self.input_text = ''
        elif key == pygame.K_BACKSPACE:
            self.input_text = self.input_text[:-1]
        elif char and ord(char) >= 32:
            self.input_text += char
    
    def send_break(self):
        """Envoie un signal BREAK."""
        if hasattr(self, 'serial_console') and self.serial_console:
            self.serial_console.send_break()
```

### 📌 10.2 Widget de visualisation flux (`ui/widgets/stream_view.py`)

```python
#!/usr/bin/env python3
"""Widget de visualisation du flux série en temps réel."""

import pygame
import math
from collections import deque


class StreamView:
    """Visualisation graphique du débit série."""
    
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.samples = deque(maxlen=100)
        self.max_value = 1000  # bytes/sec
        
    def add_sample(self, bytes_per_sec: int):
        """Ajoute un échantillon de débit."""
        self.samples.append(min(bytes_per_sec, self.max_value))
        
        # Ajuster l'échelle automatiquement
        if bytes_per_sec > self.max_value * 0.8:
            self.max_value = int(bytes_per_sec * 1.5)
    
    def draw(self, surface, color=(0, 149, 218)):
        """Dessine le graphique."""
        if len(self.samples) < 2:
            return
        
        # Fond
        pygame.draw.rect(surface, (30, 32, 36), self.rect, border_radius=5)
        
        # Points du graphique
        points = []
        sample_width = self.rect.width / (len(self.samples) - 1)
        
        for i, sample in enumerate(self.samples):
            x = self.rect.x + i * sample_width
            y = self.rect.bottom - (sample / self.max_value) * self.rect.height
            points.append((x, y))
        
        # Ligne du graphique
        if len(points) >= 2:
            pygame.draw.lines(surface, color, False, points, 2)
        
        # Remplissage sous la courbe
        if len(points) >= 2:
            fill_points = points + [
                (self.rect.right, self.rect.bottom),
                (self.rect.x, self.rect.bottom)
            ]
            fill_surface = pygame.Surface(
                (self.rect.width, self.rect.height), pygame.SRCALPHA
            )
            adjusted_points = [
                (p[0] - self.rect.x, p[1] - self.rect.y) 
                for p in fill_points
            ]
            pygame.draw.polygon(fill_surface, (*color, 50), adjusted_points)
            surface.blit(fill_surface, self.rect.topleft)
```

## 📋 Phase 11 : USB Mass Storage Gadget

### 📌 11.1 Configuration composite gadget (`serial/gadget_composite.py`)

```python
#!/usr/bin/env python3
"""
USB Gadget composite : Serial + Mass Storage
Permet d'exposer une image disque contenant les fichiers d'installation.
"""

import os
import subprocess
from pathlib import Path
from typing import Optional


class CompositeGadget:
    """Gadget USB composite avec serial et stockage de masse."""
    
    GADGET_PATH = Path('/sys/kernel/config/usb_gadget/pidebugger')
    STORAGE_IMAGE = Path('/home/pi/pidebugger/storage/armbian_files.img')
    STORAGE_MOUNT = Path('/home/pi/pidebugger/storage/mount')
    
    def __init__(self):
        self.configured = False
        self.serial_tty = None
    
    def create_storage_image(self, size_mb: int = 512):
        """Crée l'image disque pour le stockage de masse."""
        
        self.STORAGE_IMAGE.parent.mkdir(parents=True, exist_ok=True)
        self.STORAGE_MOUNT.mkdir(parents=True, exist_ok=True)
        
        if not self.STORAGE_IMAGE.exists():
            print(f'Création image {size_mb}MB...')
            
            # Créer fichier sparse
            subprocess.run([
                'dd', 'if=/dev/zero', f'of={self.STORAGE_IMAGE}',
                'bs=1M', f'count={size_mb}'
            ], check=True)
            
            # Formater en FAT32
            subprocess.run([
                'mkfs.vfat', '-F', '32', '-n', 'PIDEBUGGER',
                str(self.STORAGE_IMAGE)
            ], check=True)
            
            print('Image créée et formatée')
        
        return self.STORAGE_IMAGE
    
    def mount_storage(self) -> Path:
        """Monte l'image de stockage pour accès local."""
        if not self._is_mounted():
            subprocess.run([
                'mount', '-o', 'loop',
                str(self.STORAGE_IMAGE),
                str(self.STORAGE_MOUNT)
            ], check=True)
        return self.STORAGE_MOUNT
    
    def unmount_storage(self):
        """Démonte le stockage."""
        if self._is_mounted():
            subprocess.run(['umount', str(self.STORAGE_MOUNT)], check=True)
    
    def _is_mounted(self) -> bool:
        """Vérifie si le stockage est monté."""
        result = subprocess.run(
            ['mountpoint', '-q', str(self.STORAGE_MOUNT)],
            capture_output=True
        )
        return result.returncode == 0
    
    def setup(self) -> str:
        """Configure le gadget composite."""
        
        # Charger module
        subprocess.run(['modprobe', 'libcomposite'], check=True)
        
        gadget = self.GADGET_PATH
        gadget.mkdir(exist_ok=True)
        
        # === IDs USB ===
        (gadget / 'idVendor').write_text('0x1d6b')   # Linux Foundation
        (gadget / 'idProduct').write_text('0x0104') # Composite Gadget
        (gadget / 'bcdDevice').write_text('0x0100')
        (gadget / 'bcdUSB').write_text('0x0200')
        (gadget / 'bDeviceClass').write_text('0xEF')    # Misc
        (gadget / 'bDeviceSubClass').write_text('0x02')
        (gadget / 'bDeviceProtocol').write_text('0x01') # IAD
        
        # === Strings ===
        strings = gadget / 'strings/0x409'
        strings.mkdir(parents=True, exist_ok=True)
        (strings / 'serialnumber').write_text('PIDEBUG001')
        (strings / 'manufacturer').write_text('PiDebugger')
        (strings / 'product').write_text('Debug Console + Storage')
        
        # === Configuration ===
        config = gadget / 'configs/c.1'
        config.mkdir(parents=True, exist_ok=True)
        (config / 'MaxPower').write_text('250')
        
        config_strings = config / 'strings/0x409'
        config_strings.mkdir(parents=True, exist_ok=True)
        (config_strings / 'configuration').write_text('Serial + Mass Storage')
        
        # === Fonction ACM (Serial) ===
        acm = gadget / 'functions/acm.usb0'
        acm.mkdir(exist_ok=True)
        
        # === Fonction Mass Storage ===
        mass = gadget / 'functions/mass_storage.usb0'
        mass.mkdir(exist_ok=True)
        
        # Configurer le LUN
        lun = mass / 'lun.0'
        lun.mkdir(exist_ok=True)
        
        # S'assurer que l'image existe
        self.create_storage_image()
        
        # Démonter si monté localement
        self.unmount_storage()
        
        (lun / 'file').write_text(str(self.STORAGE_IMAGE))
        (lun / 'removable').write_text('1')
        (lun / 'ro').write_text('0')  # Read-write
        (lun / 'cdrom').write_text('0')
        
        # === Lier les fonctions ===
        acm_link = config / 'acm.usb0'
        if not acm_link.exists():
            acm_link.symlink_to(acm)
        
        mass_link = config / 'mass_storage.usb0'
        if not mass_link.exists():
            mass_link.symlink_to(mass)
        
        # === Activer ===
        udc = list(Path('/sys/class/udc').iterdir())[0].name
        (gadget / 'UDC').write_text(udc)
        
        self.configured = True
        self.serial_tty = '/dev/ttyGS0'
        
        return self.serial_tty
    
    def teardown(self):
        """Désactive le gadget."""
        gadget = self.GADGET_PATH
        
        if not gadget.exists():
            return
        
        try:
            (gadget / 'UDC').write_text('')
        except:
            pass
        
        # Supprimer liens
        config = gadget / 'configs/c.1'
        for link in config.glob('*.usb*'):
            try:
                link.unlink()
            except:
                pass
        
        # Supprimer dans l'ordre
        dirs_to_remove = [
            'functions/mass_storage.usb0/lun.0',
            'functions/mass_storage.usb0',
            'functions/acm.usb0',
            'configs/c.1/strings/0x409',
            'configs/c.1',
            'strings/0x409',
            ''
        ]
        
        for d in dirs_to_remove:
            try:
                (gadget / d).rmdir()
            except:
                pass
        
        self.configured = False


class StorageManager:
    """Gestionnaire du contenu du stockage de masse."""
    
    def __init__(self, gadget: CompositeGadget):
        self.gadget = gadget
        self.structure = {
            'armbian': {
                'espressobin': [],
                'mochabin': [],
                'espressobin-ultra': [],
            },
            'uboot': {
                'espressobin': [],
                'mochabin': [],
            },
            'scripts': [],
            'configs': [],
        }
    
    def initialize_structure(self):
        """Crée la structure de dossiers sur le stockage."""
        mount = self.gadget.mount_storage()
        
        # Créer arborescence
        for category, content in self.structure.items():
            cat_path = mount / category
            cat_path.mkdir(exist_ok=True)
            
            if isinstance(content, dict):
                for subcat in content:
                    (cat_path / subcat).mkdir(exist_ok=True)
        
        # Créer README
        readme = mount / 'README.txt'
        readme.write_text("""PiDebugger Storage
==================

Structure:
- armbian/          Images Armbian par plateforme
  - espressobin/    EspressoBin v5/v7
  - mochabin/       MochaBin
  - espressobin-ultra/
  
- uboot/            Binaires U-Boot et flash tools
  - espressobin/    
  - mochabin/       
  
- scripts/          Scripts d'installation automatique
- configs/          Fichiers de configuration (env, dtb)

Utilisation:
1. Copier les images dans les dossiers appropriés
2. Le PiDebugger détectera automatiquement les fichiers
3. Utiliser l'interface pour flasher/installer
""")
        
        self.gadget.unmount_storage()
    
    def list_files(self, category: str = None) -> dict:
        """Liste les fichiers disponibles."""
        mount = self.gadget.mount_storage()
        
        result = {}
        
        try:
            if category:
                cat_path = mount / category
                if cat_path.is_dir():
                    result[category] = self._scan_dir(cat_path)
            else:
                for cat in self.structure:
                    cat_path = mount / cat
                    if cat_path.is_dir():
                        result[cat] = self._scan_dir(cat_path)
        finally:
            self.gadget.unmount_storage()
        
        return result
    
    def _scan_dir(self, path: Path) -> dict:
        """Scanne récursivement un dossier."""
        result = {}
        
        for item in path.iterdir():
            if item.is_dir():
                result[item.name] = self._scan_dir(item)
            else:
                if item.name not in result:
                    result['_files'] = []
                result.setdefault('_files', []).append({
                    'name': item.name,
                    'size': item.stat().st_size,
                })
        
        return result
```

### 📌 11.2 Gestionnaire Armbian/U-Boot (`storage/firmware_manager.py`)

```python
#!/usr/bin/env python3
"""
Gestionnaire des firmwares pour EspressoBin, MochaBin et Ultra.
Gère mvebu64boot, flash-image.bin, et installations Armbian.
"""

import os
import re
import hashlib
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, List
from enum import Enum


class Platform(Enum):
    ESPRESSOBIN_V5 = 'espressobin-v5'
    ESPRESSOBIN_V7 = 'espressobin-v7'
    ESPRESSOBIN_ULTRA = 'espressobin-ultra'
    MOCHABIN = 'mochabin'


class MemoryConfig(Enum):
    DDR3_1GB_1CS = '1g-1cs'
    DDR3_2GB_2CS = '2g-2cs'
    DDR4_4GB = '4g-ddr4'
    DDR4_8GB = '8g-ddr4'


@dataclass
class FirmwareInfo:
    """Information sur un firmware."""
    name: str
    platform: Platform
    version: str
    path: Path
    size: int
    sha256: Optional[str] = None
    memory_config: Optional[MemoryConfig] = None
    description: str = ''


class MvebuBootManager:
    """
    Gestionnaire pour mvebu64boot (MochaBin) et équivalent EspressoBin.
    
    Structure flash Marvell Armada:
    - SPI NOR: 0x000000 - 0x200000 (2MB)
      - 0x000000: WTMI (Trusted firmware)
      - 0x020000: U-Boot
      - 0x1F0000: U-Boot env
    """
    
    FLASH_LAYOUT = {
        Platform.MOCHABIN: {
            'wtmi_offset': 0x000000,
            'uboot_offset': 0x020000,
            'env_offset': 0x1F0000,
            'total_size': 0x200000,
        },
        Platform.ESPRESSOBIN_V7: {
            'wtmi_offset': 0x000000,
            'uboot_offset': 0x020000,
            'env_offset': 0x1F0000,
            'total_size': 0x200000,
        },
        Platform.ESPRESSOBIN_ULTRA: {
            'wtmi_offset': 0x000000,
            'uboot_offset': 0x020000,
            'env_offset': 0x3F0000,
            'total_size': 0x400000,  # 4MB SPI
        },
    }
    
    def __init__(self, storage_path: Path):
        self.storage_path = storage_path
        self.uboot_path = storage_path / 'uboot'
        self.firmwares: List[FirmwareInfo] = []
    
    def scan_firmwares(self) -> List[FirmwareInfo]:
        """Scanne les firmwares disponibles."""
        self.firmwares = []
        
        for platform in Platform:
            platform_path = self.uboot_path / platform.value.split('-')[0]
            if not platform_path.exists():
                continue
            
            for fw_file in platform_path.glob('*.bin'):
                info = self._parse_firmware(fw_file, platform)
                if info:
                    self.firmwares.append(info)
        
        return self.firmwares
    
    def _parse_firmware(self, path: Path, platform: Platform) -> Optional[FirmwareInfo]:
        """Parse le nom d'un firmware pour extraire les infos."""
        name = path.stem
        
        # Patterns de nom de fichier
        # flash-image-espressobin-v7-2g-2cs-2000_800.bin
        # u-boot-mochabin-ddr4-4g.bin
        
        patterns = [
            r'flash-image-(?P<plat>\w+)-(?P<ver>v\d+)-(?P<mem>\d+g-\d+cs)',
            r'u-boot-(?P<plat>\w+)-(?P<mem>ddr\d+-\d+g)',
            r'(?P<plat>espressobin|mochabin).*(?P<mem>\d+g)',
        ]
        
        version = 'unknown'
        mem_config = None
        
        for pattern in patterns:
            m = re.search(pattern, name, re.I)
            if m:
                groups = m.groupdict()
                if 'ver' in groups:
                    version = groups['ver']
                if 'mem' in groups:
                    mem_str = groups['mem'].lower()
                    for mc in MemoryConfig:
                        if mc.value in mem_str or mem_str in mc.value:
                            mem_config = mc
                            break
                break
        
        return FirmwareInfo(
            name=name,
            platform=platform,
            version=version,
            path=path,
            size=path.stat().st_size,
            sha256=self._compute_hash(path),
            memory_config=mem_config,
        )
    
    def _compute_hash(self, path: Path) -> str:
        """Calcule le SHA256 d'un fichier."""
        sha256 = hashlib.sha256()
        with open(path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                sha256.update(chunk)
        return sha256.hexdigest()[:16]
    
    def get_flash_commands(self, firmware: FirmwareInfo) -> List[str]:
        """Génère les commandes U-Boot pour flasher le firmware."""
        layout = self.FLASH_LAYOUT.get(firmware.platform)
        if not layout:
            return []
        
        filename = firmware.path.name
        
        commands = [
            f'# Flash {firmware.name} sur {firmware.platform.value}',
            '',
            '# Méthode USB:',
            'usb start',
            f'load usb 0:1 $loadaddr {filename}',
            f'sf probe',
            f'sf erase 0 {hex(layout["total_size"])}',
            f'sf write $loadaddr 0 $filesize',
            '',
            '# Méthode TFTP:',
            'setenv serverip 192.168.1.1',
            'setenv ipaddr 192.168.1.100',
            f'tftp $loadaddr {filename}',
            f'sf probe',
            f'sf erase 0 {hex(layout["total_size"])}',
            f'sf write $loadaddr 0 $filesize',
            '',
            '# Vérification:',
            'sf probe',
            f'sf read $loadaddr 0 0x100',
            'md $loadaddr 0x10',
        ]
        
        return commands
    
    def get_recovery_commands(self, platform: Platform) -> List[str]:
        """Commandes de recovery via UART/XMODEM."""
        commands = [
            f'# Recovery {platform.value} via UART',
            '',
            '# 1. Connecter UART (115200 8N1)',
            '# 2. Mettre la carte sous tension',
            '# 3. Envoyer pattern de boot escape',
            '',
        ]
        
        if platform in [Platform.MOCHABIN, Platform.ESPRESSOBIN_ULTRA]:
            commands.extend([
                '# MochaBin/Ultra - mvebu64boot:',
                '# - Utiliser mvebu64boot pour upload WTMI+U-Boot',
                '# - Commande: mvebu64boot -t -b flash-image.bin /dev/ttyUSB0',
            ])
        else:
            commands.extend([
                '# EspressoBin - WTP download:',
                '# - Utiliser WtpDownload ou uart-download.py',
                '# - Patterns escape: 0xBB 0x11 0x22 0x33...',
            ])
        
        return commands


class ArmbianManager:
    """Gestionnaire des images Armbian."""
    
    SUPPORTED_IMAGES = {
        Platform.ESPRESSOBIN_V7: [
            'Armbian_*_Espressobin_*.img*',
        ],
        Platform.MOCHABIN: [
            'Armbian_*_Mochabin_*.img*',
        ],
        Platform.ESPRESSOBIN_ULTRA: [
            'Armbian_*_Espressobin-ultra_*.img*',
        ],
    }
    
    def __init__(self, storage_path: Path):
        self.storage_path = storage_path
        self.armbian_path = storage_path / 'armbian'
        self.images: List[FirmwareInfo] = []
    
    def scan_images(self) -> List[FirmwareInfo]:
        """Scanne les images Armbian disponibles."""
        self.images = []
        
        for platform in Platform:
            plat_name = platform.value.split('-')[0]
            platform_path = self.armbian_path / plat_name
            
            if not platform_path.exists():
                continue
            
            for img_file in platform_path.glob('*.img*'):
                info = self._parse_image(img_file, platform)
                if info:
                    self.images.append(info)
        
        return self.images
    
    def _parse_image(self, path: Path, platform: Platform) -> Optional[FirmwareInfo]:
        """Parse une image Armbian."""
        name = path.stem
        
        # Armbian_24.11_Espressobin_bookworm_current_6.6.38.img
        m = re.search(r'Armbian_(\d+\.\d+)_\w+_(\w+)_(\w+)_(\d+\.\d+)', name)
        
        version = 'unknown'
        description = ''
        
        if m:
            version = m.group(1)
            release = m.group(2)
            branch = m.group(3)
            kernel = m.group(4)
            description = f'{release} {branch} kernel {kernel}'
        
        return FirmwareInfo(
            name=name,
            platform=platform,
            version=version,
            path=path,
            size=path.stat().st_size,
            description=description,
        )
    
    def get_install_commands(self, image: FirmwareInfo, target_dev: str = 'mmc') -> List[str]:
        """Génère les commandes d'installation."""
        commands = [
            f'# Installation Armbian {image.version}',
            f'# Image: {image.name}',
            f'# Plateforme: {image.platform.value}',
            '',
        ]
        
        if image.path.suffix == '.xz':
            commands.extend([
                '# Image compressée XZ',
                f'xzcat {image.path.name} | dd of=/dev/{target_dev} bs=4M status=progress',
            ])
        elif image.path.suffix == '.gz':
            commands.extend([
                '# Image compressée GZ', 
                f'zcat {image.path.name} | dd of=/dev/{target_dev} bs=4M status=progress',
            ])
        else:
            commands.extend([
                '# Image raw',
                f'dd if={image.path.name} of=/dev/{target_dev} bs=4M status=progress',
            ])
        
        commands.extend([
            '',
            '# Post-installation:',
            'sync',
            f'partprobe /dev/{target_dev}',
            f'mount /dev/{target_dev}p1 /mnt',
            'ls /mnt/',
        ])
        
        return commands
```

## 📋 Phase 12 : Analyseur SPI Boot

### 📌 12.1 Parser SPI/WTMI (`analyzers/spi_boot.py`)

```python
#!/usr/bin/env python3
"""
Analyseur de séquence boot SPI pour Marvell Armada.
Parse les messages WTMI, BootROM et initialisation early boot.
"""

import re
from dataclasses import dataclass, field
from typing import Optional, List
from enum import Enum
from datetime import datetime


class BootStage(Enum):
    BOOTROM = 'bootrom'
    WTMI = 'wtmi'
    ATF_BL1 = 'atf_bl1'
    ATF_BL2 = 'atf_bl2'
    ATF_BL31 = 'atf_bl31'
    UBOOT_SPL = 'uboot_spl'
    UBOOT = 'uboot'
    KERNEL = 'kernel'
    UNKNOWN = 'unknown'


class BootSource(Enum):
    SPI = 'spi'
    EMMC = 'emmc'
    SD = 'sd'
    UART = 'uart'
    SATA = 'sata'
    UNKNOWN = 'unknown'


@dataclass
class BootEvent:
    """Événement de boot."""
    timestamp: datetime
    stage: BootStage
    message: str
    raw_line: str
    level: str = 'info'  # info, warning, error
    data: dict = field(default_factory=dict)


@dataclass
class HardwareInfo:
    """Informations matérielles détectées."""
    cpu: Optional[str] = None
    cpu_freq: Optional[int] = None
    ddr_type: Optional[str] = None
    ddr_size: Optional[str] = None
    ddr_freq: Optional[int] = None
    board: Optional[str] = None
    boot_source: BootSource = BootSource.UNKNOWN
    chip_revision: Optional[str] = None
    efuse: Optional[str] = None


class SPIBootAnalyzer:
    """Analyseur de séquence boot SPI Marvell."""
    
    def __init__(self):
        self.events: List[BootEvent] = []
        self.hardware = HardwareInfo()
        self.current_stage = BootStage.UNKNOWN
        self.start_time: Optional[datetime] = None
        
        # Patterns de détection
        self.stage_patterns = {
            BootStage.BOOTROM: [
                re.compile(r'BootROM', re.I),
                re.compile(r'Boot\s*ROM\s*:\s*Image', re.I),
            ],
            BootStage.WTMI: [
                re.compile(r'WTMI', re.I),
                re.compile(r'SVC REV:', re.I),
                re.compile(r'NOTICE:\s*Booting', re.I),
            ],
            BootStage.ATF_BL1: [
                re.compile(r'BL1:\s', re.I),
            ],
            BootStage.ATF_BL2: [
                re.compile(r'BL2:\s', re.I),
            ],
            BootStage.ATF_BL31: [
                re.compile(r'BL31:\s', re.I),
            ],
            BootStage.UBOOT_SPL: [
                re.compile(r'U-Boot SPL', re.I),
            ],
            BootStage.UBOOT: [
                re.compile(r'^U-Boot \d', re.I),
            ],
            BootStage.KERNEL: [
                re.compile(r'Linux version', re.I),
                re.compile(r'Booting Linux', re.I),
            ],
        }
        
        # Patterns d'extraction hardware
        self.hw_patterns = {
            'cpu': re.compile(r'CPU:\s*(.+)|SoC:\s*(.+)', re.I),
            'cpu_freq': re.compile(r'CPU.*?(\d+)\s*MHz', re.I),
            'ddr_type': re.compile(r'(DDR[34][A-Z]*)', re.I),
            'ddr_size': re.compile(r'DRAM:\s*(\d+\s*[GMK]i?B)', re.I),
            'ddr_freq': re.compile(r'DDR.*?(\d+)\s*MHz', re.I),
            'board': re.compile(r'Board:\s*(.+)|Model:\s*(.+)', re.I),
            'boot_source': re.compile(r'Boot\s*(?:device|source):\s*(\w+)', re.I),
            'chip_rev': re.compile(r'(?:Chip|SoC)\s*(?:rev|revision)[:\s]*(\w+)', re.I),
        }
        
        # Patterns d'erreur
        self.error_patterns = [
            re.compile(r'error|fail|fatal|panic|abort', re.I),
            re.compile(r'DDR\s*init.*fail', re.I),
            re.compile(r'SPI.*fail', re.I),
            re.compile(r'timeout', re.I),
        ]
        
        self.warning_patterns = [
            re.compile(r'warn|caution', re.I),
            re.compile(r'retry', re.I),
        ]
    
    def feed(self, line: str) -> Optional[BootEvent]:
        """Analyse une ligne et retourne un événement si pertinent."""
        if not self.start_time:
            self.start_time = datetime.now()
        
        line = line.strip()
        if not line:
            return None
        
        # Détecter le stage
        new_stage = self._detect_stage(line)
        if new_stage != BootStage.UNKNOWN:
            self.current_stage = new_stage
        
        # Détecter le niveau
        level = 'info'
        for pattern in self.error_patterns:
            if pattern.search(line):
                level = 'error'
                break
        if level == 'info':
            for pattern in self.warning_patterns:
                if pattern.search(line):
                    level = 'warning'
                    break
        
        # Extraire hardware info
        self._extract_hardware(line)
        
        # Créer événement
        event = BootEvent(
            timestamp=datetime.now(),
            stage=self.current_stage,
            message=self._clean_message(line),
            raw_line=line,
            level=level,
        )
        
        self.events.append(event)
        return event
    
    def _detect_stage(self, line: str) -> BootStage:
        """Détecte le stage de boot actuel."""
        for stage, patterns in self.stage_patterns.items():
            for pattern in patterns:
                if pattern.search(line):
                    return stage
        return BootStage.UNKNOWN
    
    def _extract_hardware(self, line: str):
        """Extrait les infos hardware."""
        for key, pattern in self.hw_patterns.items():
            m = pattern.search(line)
            if m:
                value = next((g for g in m.groups() if g), None)
                if value:
                    value = value.strip()
                    
                    if key == 'boot_source':
                        for bs in BootSource:
                            if bs.value in value.lower():
                                self.hardware.boot_source = bs
                                break
                    elif key == 'cpu_freq':
                        self.hardware.cpu_freq = int(value)
                    elif key == 'ddr_freq':
                        self.hardware.ddr_freq = int(value)
                    elif key == 'cpu':
                        self.hardware.cpu = value
                    elif key == 'ddr_type':
                        self.hardware.ddr_type = value
                    elif key == 'ddr_size':
                        self.hardware.ddr_size = value
                    elif key == 'board':
                        self.hardware.board = value
                    elif key == 'chip_rev':
                        self.hardware.chip_revision = value
    
    def _clean_message(self, line: str) -> str:
        """Nettoie un message pour affichage."""
        # Supprimer timestamps type [0.000000]
        line = re.sub(r'^\[\s*\d+\.\d+\]\s*', '', line)
        # Supprimer préfixes NOTICE: WARNING: etc
        line = re.sub(r'^(NOTICE|WARNING|ERROR|INFO):\s*', '', line)
        return line[:80]  # Tronquer
    
    def get_timeline(self) -> List[dict]:
        """Retourne une timeline des événements."""
        if not self.events:
            return []
        
        timeline = []
        stage_events = {}
        
        for event in self.events:
            stage = event.stage.value
            if stage not in stage_events:
                stage_events[stage] = {
                    'stage': stage,
                    'start': event.timestamp,
                    'end': event.timestamp,
                    'count': 0,
                    'errors': 0,
                    'warnings': 0,
                }
            
            stage_events[stage]['end'] = event.timestamp
            stage_events[stage]['count'] += 1
            
            if event.level == 'error':
                stage_events[stage]['errors'] += 1
            elif event.level == 'warning':
                stage_events[stage]['warnings'] += 1
        
        # Calculer durées
        for stage_data in stage_events.values():
            duration = (stage_data['end'] - stage_data['start']).total_seconds()
            stage_data['duration_ms'] = int(duration * 1000)
            timeline.append(stage_data)
        
        return sorted(timeline, key=lambda x: x['start'])
    
    def get_summary(self) -> dict:
        """Retourne un résumé de l'analyse."""
        timeline = self.get_timeline()
        
        total_duration = 0
        if self.events:
            total_duration = (
                self.events[-1].timestamp - self.events[0].timestamp
            ).total_seconds()
        
        return {
            'hardware': {
                'cpu': self.hardware.cpu,
                'cpu_freq_mhz': self.hardware.cpu_freq,
                'ddr': f'{self.hardware.ddr_type} {self.hardware.ddr_size}',
                'ddr_freq_mhz': self.hardware.ddr_freq,
                'board': self.hardware.board,
                'boot_source': self.hardware.boot_source.value,
            },
            'boot': {
                'total_duration_s': round(total_duration, 2),
                'stages': len(timeline),
                'total_events': len(self.events),
                'errors': sum(1 for e in self.events if e.level == 'error'),
                'warnings': sum(1 for e in self.events if e.level == 'warning'),
            },
            'timeline': timeline,
        }
    
    def detect_platform(self) -> Optional[str]:
        """Tente de détecter la plateforme."""
        board = (self.hardware.board or '').lower()
        
        if 'mochabin' in board:
            return 'mochabin'
        elif 'espressobin' in board:
            if 'ultra' in board:
                return 'espressobin-ultra'
            return 'espressobin'
        elif 'armada' in board:
            return 'armada-generic'
        
        # Détection par patterns dans les logs
        all_text = ' '.join(e.raw_line for e in self.events[:50])
        
        if 'CN9130' in all_text or 'cn9130' in all_text:
            return 'mochabin'
        elif 'A3720' in all_text or 'a3720' in all_text:
            return 'espressobin'
        
        return None
```

### 📌 12.2 Écran Boot Analyzer (`ui/screens/boot_analyzer.py`)

```python
#!/usr/bin/env python3
"""Écran d'analyse de boot avec timeline visuelle."""

import pygame
import math
from datetime import datetime
from ui.core import Screen, COLORS, CENTER, RADIUS
from analyzers.spi_boot import SPIBootAnalyzer, BootStage


class BootAnalyzerScreen(Screen):
    """Visualisation de la séquence de boot."""
    
    STAGE_COLORS = {
        BootStage.BOOTROM: (200, 100, 100),
        BootStage.WTMI: (255, 150, 100),
        BootStage.ATF_BL1: (255, 200, 100),
        BootStage.ATF_BL2: (200, 255, 100),
        BootStage.ATF_BL31: (100, 255, 150),
        BootStage.UBOOT_SPL: (100, 200, 255),
        BootStage.UBOOT: (100, 150, 255),
        BootStage.KERNEL: (150, 100, 255),
        BootStage.UNKNOWN: (128, 128, 128),
    }
    
    def __init__(self, ui):
        super().__init__(ui)
        self.analyzer = SPIBootAnalyzer()
        self.selected_stage = None
        self.view_mode = 'timeline'  # timeline, details, hardware
    
    def feed_line(self, line: str):
        """Reçoit une ligne de la console."""
        self.analyzer.feed(line)
    
    def draw(self, surface):
        if self.view_mode == 'timeline':
            self._draw_timeline(surface)
        elif self.view_mode == 'details':
            self._draw_details(surface)
        elif self.view_mode == 'hardware':
            self._draw_hardware(surface)
        
        # Navigation
        self._draw_nav(surface)
    
    def _draw_timeline(self, surface):
        """Dessine la timeline circulaire."""
        # Titre
        title = self.ui.fonts['medium'].render('Boot Timeline', True, COLORS['primary'])
        title_rect = title.get_rect(center=(CENTER[0], 35))
        surface.blit(title, title_rect)
        
        timeline = self.analyzer.get_timeline()
        
        if not timeline:
            # Pas de données
            msg = self.ui.fonts['medium'].render('En attente...', True, COLORS['text_dim'])
            msg_rect = msg.get_rect(center=CENTER)
            surface.blit(msg, msg_rect)
            return
        
        # Calculer les angles pour chaque stage
        total_duration = sum(s['duration_ms'] for s in timeline) or 1
        
        # Timeline circulaire
        timeline_radius = RADIUS - 80
        start_angle = -90
        
        for i, stage_data in enumerate(timeline):
            stage = BootStage(stage_data['stage'])
            duration_ratio = stage_data['duration_ms'] / total_duration
            sweep_angle = max(10, duration_ratio * 360)  # Min 10 degrés
            
            color = self.STAGE_COLORS.get(stage, (128, 128, 128))
            
            # Arc pour ce stage
            rect = pygame.Rect(
                CENTER[0] - timeline_radius,
                CENTER[1] - timeline_radius,
                timeline_radius * 2,
                timeline_radius * 2
            )
            
            start_rad = math.radians(start_angle)
            end_rad = math.radians(start_angle + sweep_angle)
            
            # Dessiner l'arc (approximation avec lignes)
            points = []
            for angle in range(int(start_angle), int(start_angle + sweep_angle) + 1, 2):
                rad = math.radians(angle)
                x = CENTER[0] + timeline_radius * math.cos(rad)
                y = CENTER[1] + timeline_radius * math.sin(rad)
                points.append((x, y))
            
            if len(points) >= 2:
                pygame.draw.lines(surface, color, False, points, 15)
            
            # Label au milieu de l'arc
            mid_angle = math.radians(start_angle + sweep_angle / 2)
            label_r = timeline_radius - 40
            lx = CENTER[0] + label_r * math.cos(mid_angle)
            ly = CENTER[1] + label_r * math.sin(mid_angle)
            
            # Nom court du stage
            short_name = stage.value[:6].upper()
            label = self.ui.fonts['small'].render(short_name, True, color)
            label_rect = label.get_rect(center=(lx, ly))
            surface.blit(label, label_rect)
            
            start_angle += sweep_angle
        
        # Centre - résumé
        summary = self.analyzer.get_summary()
        
        duration_text = f"{summary['boot']['total_duration_s']}s"
        dur_surf = self.ui.fonts['xlarge'].render(duration_text, True, COLORS['text'])
        dur_rect = dur_surf.get_rect(center=(CENTER[0], CENTER[1] - 20))
        surface.blit(dur_surf, dur_rect)
        
        boot_label = self.ui.fonts['small'].render('Boot time', True, COLORS['text_dim'])
        boot_rect = boot_label.get_rect(center=(CENTER[0], CENTER[1] + 20))
        surface.blit(boot_label, boot_rect)
        
        # Erreurs/warnings
        if summary['boot']['errors'] > 0:
            err = self.ui.fonts['small'].render(
                f"⚠ {summary['boot']['errors']} errors", 
                True, COLORS['danger']
            )
            err_rect = err.get_rect(center=(CENTER[0], CENTER[1] + 50))
            surface.blit(err, err_rect)
    
    def _draw_hardware(self, surface):
        """Dessine les infos hardware."""
        title = self.ui.fonts['medium'].render('Hardware Info', True, COLORS['primary'])
        title_rect = title.get_rect(center=(CENTER[0], 35))
        surface.blit(title, title_rect)
        
        hw = self.analyzer.hardware
        
        info_lines = [
            ('CPU', hw.cpu or 'Unknown'),
            ('Freq', f'{hw.cpu_freq} MHz' if hw.cpu_freq else 'Unknown'),
            ('RAM', f'{hw.ddr_type} {hw.ddr_size}' if hw.ddr_size else 'Unknown'),
            ('DDR', f'{hw.ddr_freq} MHz' if hw.ddr_freq else 'Unknown'),
            ('Board', hw.board or 'Unknown'),
            ('Boot', hw.boot_source.value),
        ]
        
        y = 80
        for label, value in info_lines:
            # Label
            lbl = self.ui.fonts['small'].render(label + ':', True, COLORS['text_dim'])
            surface.blit(lbl, (CENTER[0] - 100, y))
            
            # Value
            val = self.ui.fonts['medium'].render(value[:20], True, COLORS['text'])
            surface.blit(val, (CENTER[0] - 30, y - 2))
            
            y += 35
        
        # Platform détectée
        platform = self.analyzer.detect_platform()
        if platform:
            plat_text = self.ui.fonts['large'].render(
                platform.upper(), True, COLORS['primary']
            )
            plat_rect = plat_text.get_rect(center=(CENTER[0], RADIUS * 2 - 80))
            surface.blit(plat_text, plat_rect)
    
    def _draw_details(self, surface):
        """Dessine les derniers événements."""
        title = self.ui.fonts['medium'].render('Boot Events', True, COLORS['primary'])
        title_rect = title.get_rect(center=(CENTER[0], 35))
        surface.blit(title, title_rect)
        
        # Derniers événements
        events = self.analyzer.events[-15:]
        
        y = 65
        for event in events:
            color = COLORS['text']
            if event.level == 'error':
                color = COLORS['danger']
            elif event.level == 'warning':
                color = COLORS['warning']
            
            # Stage tag
            stage_color = self.STAGE_COLORS.get(event.stage, (128, 128, 128))
            pygame.draw.rect(surface, stage_color, (50, y, 4, 18))
            
            # Message
            msg = self.ui.fonts['small'].render(
                event.message[:45], True, color
            )
            surface.blit(msg, (60, y + 2))
            
            y += 22
    
    def _draw_nav(self, surface):
        """Dessine les boutons de navigation."""
        btn_y = RADIUS * 2 - 35
        modes = ['timeline', 'hardware', 'details']
        
        for i, mode in enumerate(modes):
            x = CENTER[0] - 70 + i * 70
            
            is_active = self.view_mode == mode
            color = COLORS['primary'] if is_active else COLORS['bg_light']
            
            pygame.draw.circle(surface, color, (x, btn_y), 25)
            pygame.draw.circle(surface, COLORS['border'], (x, btn_y), 25, 2)
            
            label = mode[:4].upper()
            text = self.ui.fonts['small'].render(label, True, COLORS['text'])
            text_rect = text.get_rect(center=(x, btn_y))
            surface.blit(text, text_rect)
    
    def on_touch(self, pos):
        """Gère les touches."""
        x, y = pos
        btn_y = RADIUS * 2 - 35
        
        if btn_y - 30 < y < btn_y + 30:
            modes = ['timeline', 'hardware', 'details']
            for i, mode in enumerate(modes):
                btn_x = CENTER[0] - 70 + i * 70
                if abs(x - btn_x) < 30:
                    self.view_mode = mode
                    return
    
    def reset(self):
        """Réinitialise l'analyseur."""
        self.analyzer = SPIBootAnalyzer()
```

## 📋 Phase 13 : Démo interactive

### 📌 13.1 Fonctionnalités de la démo

La démo interactive HTML/React inclut toutes les fonctionnalités :

| Écran | Emoji | Fonctionnalités |
|-------|-------|-----------------|
| 🏭 Factory Boot | 🍓 | Séquence boot Pi Zero avec status progressifs |
| 🕐 Clock | 🕐 | Horloge analogique + mini-status bar |
| 📊 Dashboard | 🔧 | Menu radial + mini-dashboards Master/Target |
| 💻 Serial Monitor | 💻 | Logs colorés + status bar + stats RX |
| 📈 Boot Timeline | 🚀 | Arcs colorés par stage + infos hardware |
| 🔋 Power Control | 🔋 | Bouton ON/OFF + voltage/current/uptime |
| 📁 Files | 💿 | Explorateur arborescence USB storage |

### 📌 13.2 Mini-Dashboards dans la démo

Chaque écran affiche les status Master/Target :

```javascript
// Status Master (Pi Zero)
const master = {
  power: true,      // 🔋 Alimentation Pi
  gadget: true,     // 🔗 USB Gadget composite actif
  tty: true,        // 📟 /dev/ttyGS0 disponible
  storage: true,    // 💿 Mass Storage monté
  wifi: true,       // 📶 WiFi connecté
  temp: 48,         // 🌡️ Température CPU
};

// Status Target (SoC cible)
const target = {
  power: false,     // 🔋 Alimentation cible
  usb: false,       // 🔌 Connexion USB
  serial: false,    // 📡 Liaison UART
  platform: '☕ ESPRESSOBin',  // Plateforme détectée
  booting: false,   // 🔄 Boot en cours
  ready: false,     // ✅ Système prêt
};
```

### 📌 13.3 Intégration dans Hexo

Il y a plusieurs méthodes pour intégrer la démo interactive dans un article Hexo :

#### Méthode 1 : iframe (recommandé)

Placez le fichier `pidebugger-demo.html` dans le dossier `source/demos/` de votre projet Hexo, puis utilisez un iframe :

```markdown
---
title: PiDebugger - Outil portable de debug SoC
date: 2025-01-15
---

## Démonstration interactive

<div style="display: flex; justify-content: center; margin: 30px 0;">
  <iframe 
    src="/demos/pidebugger-demo.html" 
    width="450" 
    height="680" 
    frameborder="0"
    style="border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  </iframe>
</div>
```

#### Méthode 2 : Tag Hexo personnalisé

Créez un tag personnalisé dans `scripts/pidebugger-tag.js` :

```javascript
// scripts/pidebugger-tag.js
hexo.extend.tag.register('pidebugger_demo', function(args) {
  return `
    <div class="pidebugger-container" style="display:flex;justify-content:center;margin:30px 0;">
      <iframe 
        src="/demos/pidebugger-demo.html" 
        width="450" 
        height="680" 
        frameborder="0"
        loading="lazy"
        style="border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,0.3);background:#0a0b0d;">
      </iframe>
    </div>
  `;
});
```

Puis dans votre article :

```markdown
{% pidebugger_demo %}
```

#### Méthode 3 : Embed direct (pour thèmes supportant le JS inline)

Si votre thème Hexo supporte le JavaScript inline, vous pouvez inclure directement le code dans un fichier `.ejs` ou utiliser le plugin `hexo-filter-inline-html`.

### 📌 13.2 Structure des fichiers Hexo

```
your-hexo-blog/
├── source/
│   ├── _posts/
│   │   └── pidebugger-guide.md      # Article principal
│   └── demos/
│       └── pidebugger-demo.html     # Démo interactive
├── scripts/
│   └── pidebugger-tag.js            # Tag personnalisé (optionnel)
└── themes/
    └── your-theme/
```

### 📌 13.3 Exemple d'article complet

```markdown
---
title: PiDebugger - Swiss Army Knife pour Debug SoC ARM
date: 2025-01-15
tags:
  - raspberry-pi
  - embedded
  - debug
  - espressobin
categories:
  - Hardware
  - Projets
cover: /images/pidebugger-cover.jpg
---

# PiDebugger

Un outil portable basé sur **Raspberry Pi Zero W** et écran **HyperPixel 2.1" Round** 
pour le debug, monitoring et installation de plateformes SoC ARM.

## Démonstration Live

Testez l'interface directement dans votre navigateur :

<div style="display: flex; justify-content: center; margin: 30px 0;">
  <iframe 
    src="/demos/pidebugger-demo.html" 
    width="450" 
    height="680" 
    frameborder="0"
    style="border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  </iframe>
</div>

> **Instructions** : Cliquez sur l'horloge pour accéder au dashboard. 
> Sélectionnez **UART** pour voir une simulation de boot EspressoBin.

## Plateformes supportées

| Plateforme | SoC | RAM | Boot |
|------------|-----|-----|------|
| EspressoBin V5 | Armada 3720 | 1GB DDR3 | SPI |
| EspressoBin V7 | Armada 3720 | 1-2GB DDR3 | SPI |
| MochaBin | CN9130 | 4-8GB DDR4 | SPI |
| EspressoBin Ultra | CN9130 | 4GB DDR4 | SPI |

<!-- Suite de l'article... -->
```

### 📌 13.4 CSS additionnel pour le thème

Ajoutez ces styles dans votre fichier CSS de thème pour un meilleur rendu :

```css
/* Style pour la démo PiDebugger */
.pidebugger-container {
  display: flex;
  justify-content: center;
  margin: 30px 0;
  padding: 20px;
  background: linear-gradient(135deg, #1a1c22 0%, #0a0b0d 100%);
  border-radius: 16px;
}

.pidebugger-container iframe {
  border: none;
  border-radius: 12px;
  box-shadow: 
    0 4px 20px rgba(0, 0, 0, 0.4),
    0 0 40px rgba(0, 149, 218, 0.1);
}

/* Mode sombre automatique */
@media (prefers-color-scheme: dark) {
  .pidebugger-container {
    background: transparent;
  }
}

/* Responsive */
@media (max-width: 500px) {
  .pidebugger-container iframe {
    width: 100%;
    max-width: 380px;
    height: 600px;
  }
}
```

## 🔗 Ressources

| Emoji | Ressource | Lien |
|-------|-----------|------|
| 🔲 | HyperPixel 2.1" | [shop.pimoroni.com](https://shop.pimoroni.com/products/hyperpixel-2-1-round) |
| 🔌 | USB Gadget API | [kernel.org](https://www.kernel.org/doc/html/latest/usb/gadget.html) |
| 🥾 | U-Boot docs | [u-boot.readthedocs.io](https://u-boot.readthedocs.io/) |
| ☕ | EspressoBin wiki | [wiki.espressobin.net](http://wiki.espressobin.net/) |
| 🍫 | MochaBin docs | [developer.solid-run.com](https://developer.solid-run.com/knowledge-base/mochabin-getting-started/) |

## 🎯 Plateformes cibles supportées

| Emoji | Plateforme | SoC | RAM | Boot | USB Power |
|-------|------------|-----|-----|------|-----------|
| ☕ | EspressoBin V5 | Armada 3720 | 1GB DDR3 | SPI | ✅ 5V/2A |
| ☕ | EspressoBin V7 | Armada 3720 | 1-2GB DDR3 | SPI | ✅ 5V/2A |
| ⚡ | EspressoBin Ultra | CN9130 | 4GB DDR4 | SPI | ❌ 12V ext |
| 🍫 | MochaBin | CN9130 | 4-8GB DDR4 | SPI | ❌ 12V ext |

## ✅ Checklist des fonctionnalités

### 🟢 Implémenté (v2.1)

#### Interface & Navigation
- [x] 🕐 Interface horloge circulaire avec status bar
- [x] 📊 Dashboard avec menu radial à emojis (9 items)
- [x] 📊 Mini-dashboards Master/Target centrés sur tous les écrans
- [x] 🎮 Gestures tactiles (swipe ←→↑↓, pinch in/out, long press 600ms)
- [x] 🔔 Notifications sonores Web Audio API (click, success, boot, notify, power)
- [x] 🎨 4 Thèmes (🌙 Dark, ☀️ Light, ⬛ OLED, 🍓 Berry)
- [x] 📱 Interface responsive (adapte à toutes tailles d'écran)

#### Hardware & USB
- [x] 🔗 Indicateurs USB Gadget (🔗 Gadget, 📟 TTY, 💿 Storage)
- [x] 🎯 Indicateurs Target (🔋 Power, 🔌 USB, 📡 Serial)
- [x] 🔌 USB Gadget composite (ACM + Mass Storage 512MB)
- [x] 🏭 Mode Factory Boot avec séquence progressive Pi Zero W
- [x] ⏭️ Bouton SKIP pour passer le boot

#### Multi-Target Support (v2.1)
- [x] ☕ ESPRESSObin V7 (Armada 3720, 2×A53 @ 1.0GHz)
- [x] 🚀 ESPRESSObin Ultra (Armada 3720 + PoE, 2×A53 @ 1.2GHz)
- [x] 🍫 MOCHAbin (Armada 7040, 4×A72 @ 1.4GHz, 10G SFP+)
- [x] 🔌 Sheeva64 (Armada 3720, plug computer form factor)
- [x] 🔄 Sélection dynamique du target dans Power Screen
- [x] 📊 Séquences de boot spécifiques par target

#### Serial & Boot Analysis
- [x] 💻 Moniteur série temps réel avec coloration syntaxique
- [x] 🚀 Analyseur de boot multi-stages (🔒→🔑→🛡️→📦→🥾→🐧→👤)
- [x] 📈 Timeline circulaire avec emojis par stage
- [x] 🛡️ Parser ARM Trusted Firmware (BL1, BL2, BL31, PSCI, FIP)
- [x] 🔑 Support WTMI (Cortex-M3) pour Armada 3720
- [x] ⏸️ Pause/Resume du flux série
- [x] 🧹 Clear buffer série

#### Power & Monitoring
- [x] 🔋 Contrôle alimentation USB cibles avec stats V/A/temps
- [x] 📊 Graphiques temps réel voltage/courant (30 points, 500ms)
- [x] ⚡ Affichage puissance calculée (W)
- [x] 🌡️ Monitoring température CPU en temps réel
- [x] 📶 Indicateur force signal WiFi (%)

#### Network & Transfers
- [x] 🌐 Écran configuration réseau (IP, Gateway, DHCP)
- [x] 📶 WiFi scan avec liste réseaux disponibles
- [x] 🔐 Authentification WiFi WPA2/WPA3 avec clavier virtuel 40 touches
- [x] 📡 Serveur TFTP intégré (port 69)
- [x] 📤 Transfert XMODEM-CRC pour recovery UART (128B packets)
- [x] 🛡️ UEFI Shell interactif (6 commandes: help, ver, map, ls, reset, memmap)

#### Files & Storage
- [x] 📁 Explorateur fichiers USB Storage avec icônes
- [x] 💾 Export logs vers USB (/logs/)

### 🟡 À venir
- [ ] 📱 Mode portrait/paysage auto-rotate
- [ ] 🔄 OTA firmware update Pi Zero W
- [ ] 📊 Export timeline JSON/CSV
- [ ] 🔒 Mode kiosk / verrouillage écran
- [ ] 🔌 Support INA219 réel (I2C) pour mesures V/A
- [ ] 🎯 Multi-targets simultanés
- [ ] 📝 Enregistrement macros commandes
- [ ] 🔍 Recherche dans logs série

## 📋 Résumé des emojis utilisés

### 🎨 Thèmes disponibles

| Emoji | Thème | Background | Primary | Description |
|-------|-------|------------|---------|-------------|
| 🌙 | Dark | #181a1f | #0095da | Thème sombre par défaut |
| ☀️ | Light | #f5f5f5 | #1976d2 | Thème clair |
| ⬛ | OLED | #000000 | #00bcd4 | Noir pur pour écrans OLED |
| 🍓 | Berry | #1a0a10 | #c51a4a | Thème Raspberry Pi |

### 🌐 Configuration réseau

L'écran Network propose 3 onglets :

| Onglet | Emoji | Fonctions |
|--------|-------|-----------|
| Status | 🌐 | IP, Gateway, SSID, DHCP status |
| WiFi | 📶 | Scan réseaux, connexion, signal % |
| TFTP | 📡 | Serveur TFTP port 69, root dir |

### 📡 Serveur TFTP intégré

```bash
# Configuration U-Boot pour boot TFTP
setenv serverip 192.168.1.42
setenv ipaddr 192.168.1.100
tftp 0x5000000 flash-image.bin
sf update 0x5000000 0x0 $filesize
```

### ⌨️ Clavier virtuel

Le clavier virtuel permet d'envoyer des commandes UART :

```
┌───────────────────────────────────────┐
│ > help_                               │
├───────────────────────────────────────┤
│ [1][2][3][4][5][6][7][8][9][0]       │
│ [q][w][e][r][t][y][u][i][o][p]       │
│ [a][s][d][f][g][h][j][k][l][◀️]      │
│ [z][x][c][v][b][n][m][.][−][📤]      │
└───────────────────────────────────────┘
```

Commandes U-Boot courantes :
- `help` - Liste des commandes
- `printenv` - Variables d'environnement
- `boot` - Démarrer le kernel
- `reset` - Redémarrer

### 🌡️ Monitoring système

| Indicateur | Emoji | Plage | Alerte |
|------------|-------|-------|--------|
| CPU Temp | 🌡️ | 35-85°C | >70°C orange, >80°C rouge |
| WiFi Signal | 📶 | 0-100% | <30% orange, <15% rouge |
| Voltage | ⚡ | 4.8-5.2V | <4.8V orange |
| Current | 〰️ | 0-2A | >1.8A orange |

### 💾 Export des logs

Les logs sont exportés vers `/logs/` sur le stockage USB :

```
/mnt/usb/PIDEBUGGER/
├── logs/
│   ├── serial_2024-12-08.log      # Logs série
│   ├── boot_analysis_001.json     # Timeline JSON
│   └── system_2024-12-08.log      # Logs système
└── ...
```

Format du fichier log :
```
[2024-12-08 14:32:15] 🥾 U-Boot 2024.01-armbian
[2024-12-08 14:32:15] ☕ ESPRESSOBin V7
[2024-12-08 14:32:16] ⚡ Armada 3720 @ 1000 MHz
...
```

## 📤 Transfert XMODEM

L'écran XMODEM permet d'envoyer des fichiers via le protocole XMODEM-CRC :

### Caractéristiques

| Paramètre | Valeur |
|-----------|--------|
| Protocol | XMODEM-CRC |
| Packet size | 128 bytes |
| Checksum | CRC-16 |
| Start char | SOH (0x01) |
| End char | EOT (0x04) |

### Séquence de transfert

```
┌─────────────────────────────────────┐
│  1. Idle: Ready to send             │
│  2. Wait: Waiting for NAK from target │
│  3. Transfer: Sending packets       │
│  4. Complete: Transfer done         │
└─────────────────────────────────────┘
```

### Commandes côté target

```bash
# U-Boot
loady 0x5000000           # Receive via YMODEM
loadx 0x5000000           # Receive via XMODEM

# Linux
rx /tmp/firmware.bin      # Receive file
```

## 🛡️ UEFI Shell Commands

L'écran UEFI Shell permet d'exécuter des commandes UEFI standard :

### Commandes disponibles

| Catégorie | Commandes |
|-----------|-----------|
| General | `help`, `ver` |
| Device | `map`, `devices`, `drivers` |
| File | `ls`, `cd`, `cp`, `rm`, `type` |
| Boot | `bcfg`, `boot`, `exit` |
| System | `reset`, `memmap`, `dmpstore` |

### Exemple d'utilisation

```
Shell> map
Mapping table:
  FS0: Alias HD0b
  BLK0: Alias USB0

Shell> ls FS0:\
Directory of FS0:\
  EFI          <DIR>
  startup.nsh  1,234
  
Shell> bcfg boot dump
```

## 🛡️ Parser ARM Trusted Firmware

Le parser ATF détecte automatiquement les stages de boot ARM Trusted Firmware :

### Stages détectés

| Stage | Description | Pattern |
|-------|-------------|---------|
| BL1 | Boot Loader Stage 1 | `/BL1[:\s]/i` |
| BL2 | Boot Loader Stage 2 | `/BL2[:\s]/i` |
| BL31 | EL3 Runtime (Secure) | `/BL31[:\s]/i` |
| BL32 | Secure Payload (OP-TEE) | `/BL32[:\s]/i` |
| BL33 | Non-secure (U-Boot) | `/BL33[:\s]/i` |
| PSCI | Power State Coordination | `/PSCI/i` |
| SMCCC | SMC Calling Convention | `/SMCCC/i` |
| FIP | Firmware Image Package | `/FIP[:\s]/i` |

### Affichage dans Boot Analyzer

L'onglet "ATF" affiche les stages détectés avec indicateur visuel :
- ✅ Stage détecté dans les logs
- ○ Stage non détecté

## 🔐 Authentification WiFi WPA2/WPA3

L'écran WiFi Auth permet de se connecter aux réseaux sécurisés :

### Caractéristiques

- Clavier virtuel complet (a-z, 0-9, symboles)
- Sélection WPA2 / WPA3
- Masquage mot de passe (• • •)
- Validation min 8 caractères
- Animation de connexion

### Flux de connexion

```
1. Scan réseaux disponibles
2. Sélection réseau sécurisé
3. Écran d'authentification
4. Saisie mot de passe (clavier virtuel)
5. Sélection WPA2/WPA3
6. Connexion
7. Notification succès
```

## 📊 Graphiques temps réel

L'écran Power Control affiche des graphiques en temps réel :

### Voltage Graph
- Plage: 4.5V - 5.5V
- Historique: 30 points
- Update: 500ms
- Couleur: vert (secondary)

### Current Graph
- Plage: 0A - 2A
- Historique: 30 points
- Update: 500ms
- Couleur: orange (warning)

### Calcul puissance
```
Power (W) = Voltage (V) × Current (A)
```

## 🎮 Gestures tactiles

### Gestures supportées

| Gesture | Action |
|---------|--------|
| Swipe ← | Écran précédent |
| Swipe → | Écran suivant |
| Swipe ↑ | Retour Dashboard |
| Swipe ↓ | (réservé) |
| Pinch in | Notification "Pinch in" |
| Pinch out | Notification "Pinch out" |
| Long press | Notification "Long press" |

### Paramètres de détection

```javascript
// Swipe
minDistance: 50px
maxTime: 300ms

// Pinch
scaleThreshold: 0.2 (20%)

// Long press
duration: 600ms
```

## 🔔 Notifications sonores

### Sons disponibles

| Type | Fréquence | Durée | Usage |
|------|-----------|-------|-------|
| click | 800 Hz | 50ms | Boutons |
| success | 880 Hz | 150ms | Succès |
| boot | 440 Hz | 100ms | Boot stages |
| notify | 660 Hz | 80ms | Notifications |
| power | 150 Hz | 300ms | Power toggle |

### Implémentation Web Audio API

```javascript
const playSound = (type) => {
  const ctx = new AudioContext();
  const osc = ctx.createOscillator();
  const gain = ctx.createGain();
  osc.connect(gain);
  gain.connect(ctx.destination);
  osc.frequency.setValueAtTime(freq, ctx.currentTime);
  gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
  osc.start();
  osc.stop(ctx.currentTime + duration);
};
```

### Toggle Sound

Le son peut être activé/désactivé dans Settings :
- 🔔 Sound ON
- 🔇 Sound OFF

### Interface principale
| Emoji | Usage | Description |
|-------|-------|-------------|
| 🔧 | Titre | PiDebugger |
| 🕐 | Menu | Horloge |
| 💻 | Menu | Terminal UART |
| 🚀 | Menu | Boot Analyzer |
| 🔋 | Menu | Power Control |
| 📁 | Menu | File Browser |
| ⚙️ | Menu | Configuration |

### Status indicators
| Emoji | Usage | Description |
|-------|-------|-------------|
| 🟢 | Status | ON / Actif |
| 🔴 | Status | OFF / Inactif |
| 🟡 | Status | Standby |
| 🔄 | Status | Loading / En cours |
| ✅ | Status | OK / Succès |
| ❌ | Status | Erreur |

### Hardware Master
| Emoji | Usage | Description |
|-------|-------|-------------|
| 🍓 | Master | Raspberry Pi |
| 🔗 | Master | USB Gadget |
| 📟 | Master | TTY Serial |
| 💿 | Master | Mass Storage |
| 📶 | Master | WiFi |
| 🌡️ | Master | Température |

### Hardware Target
| Emoji | Usage | Description |
|-------|-------|-------------|
| 🎯 | Target | Cible SoC |
| 🔋 | Target | Power |
| 🔌 | Target | USB |
| 📡 | Target | Serial UART |
| ☕ | Target | ESPRESSObin V7 |
| 🚀 | Target | ESPRESSObin Ultra |
| 🍫 | Target | MOCHAbin |
| 🔌 | Target | Sheeva64 |

### Boot stages
| Emoji | Stage | Description |
|-------|-------|-------------|
| 🔒 | BootROM | ROM boot initial |
| 🔑 | WTMI | Marvell Trusted FW |
| 🛡️ | ATF | ARM Trusted FW |
| 📦 | SPL | Secondary Loader |
| 🥾 | U-Boot | Bootloader |
| 🐧 | Kernel | Linux |
| 👤 | Login | User prompt |

---

## 📜 Licence

MIT License - Libre d'utilisation et modification.

---

> 🔧 **PiDebugger v2.1** - *Multi-Target ARM Debugger* 
> 
> Made with ❤️ for the embedded community
>
> 🍓 Pi Zero W | 🔲 HyperPixel 480×480 | ☕ ESPRESSObin | 🚀 Ultra | 🍫 MOCHAbin | 🔌 Sheeva64
