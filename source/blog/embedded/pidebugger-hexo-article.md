---
title: PiDebugger v2.1 - Multi-Target ARM Debugger
date: 2025-12-09 12:54:00
tags:
  - raspberry-pi
  - embedded
  - debug
  - espressobin
  - mochabin
  - sheeva64
  - marvell
  - armada
  - armbian
categories:
  - Hardware
  - Projets DIY
cover: /images/pidebugger-cover.jpg
excerpt: Outil portable basé sur Pi Zero W et écran HyperPixel 480×480 pour debugger, monitorer et flasher des plateformes ARM Marvell (ESPRESSObin, MOCHAbin, Sheeva64).
---

# PiDebugger v2.1

Un **couteau suisse portable** pour le debug de plateformes SoC ARM Marvell/Globalscale, basé sur Raspberry Pi Zero W et écran tactile rond HyperPixel 2.1" (480×480 @ 60fps).
<!-- more -->
## 🎯 Targets Supportés

| Target | SoC | CPU | Réseau |
|--------|-----|-----|--------|
| ☕ **ESPRESSObin V7** | Armada 3720 | 2×A53 @ 1.0GHz | 3×GbE |
| 🚀 **ESPRESSObin Ultra** | Armada 3720 | 2×A53 @ 1.2GHz | WAN+4LAN PoE |
| 🍫 **MOCHAbin** | Armada 7040 | 4×A72 @ 1.4GHz | 10G SFP+ |
| 🔌 **Sheeva64** | Armada 3720 | 2×A53 @ 1.2GHz | 2×GbE |

## ✨ Fonctionnalités

- **12 écrans interactifs** : Clock, Dashboard, Serial, Boot, Power, Files, Network, XMODEM, UEFI, WiFi Auth, Settings
- **Moniteur série temps réel** avec coloration syntaxique et parser ATF
- **Analyseur de boot** : BootROM → WTMI → ATF → U-Boot → Linux
- **USB Gadget composite** : Serial + Mass Storage 512MB
- **Transfert XMODEM-CRC** pour recovery via UART
- **4 thèmes** : Dark, Light, OLED, Berry
- **Gestures tactiles** : swipe, pinch, long press
- **Interface responsive** adaptée à toutes tailles

## 🖥️ Démonstration Interactive

Testez l'interface directement dans votre navigateur. Cliquez sur l'horloge pour commencer !

<div class="pidebugger-demo-container">
  <iframe 
    src="/projects/DEMO.HTML" 
    width="500" 
    height="520" 
    frameborder="0"
    loading="lazy"
    title="PiDebugger v2.1 Demo"
    style="border-radius: 50%; box-shadow: 0 4px 30px rgba(0,0,0,0.5); background: #000;">
  </iframe>
</div>

<style>
.pidebugger-demo-container {
  display: flex;
  justify-content: center;
  margin: 40px 0;
  padding: 30px;
  background: linear-gradient(135deg, #1a1c22 0%, #0a0b0d 100%);
  border-radius: 20px;
}
@media (max-width: 520px) {
  .pidebugger-demo-container iframe {
    width: 100%;
    max-width: 380px;
    height: 400px;
  }
}
</style>

> **Navigation** :
> 1. Cliquez sur l'horloge → Dashboard
> 2. **UART** : Simulation boot ESPRESSObin avec logs colorés
> 3. **BOOT** : Timeline circulaire + Hardware info + ATF stages
> 4. **PWR** : Sélection target + graphiques V/A temps réel
> 5. **NET** : Status/WiFi/TFTP avec auth WPA2
> 6. **XMOD** : Transfert fichiers XMODEM-CRC
> 7. **UEFI** : Shell interactif
> 8. **Swipe** gauche/droite pour naviguer entre écrans

---

## 🔧 Matériel

| Composant | Modèle | Rôle |
|-----------|--------|------|
| SBC | Raspberry Pi Zero W | Master USB Gadget + WiFi |
| Écran | HyperPixel 2.1" Round | Interface tactile 480×480 |
| Stockage | microSD 16GB+ | OS + logs |
| Câble | USB micro → USB-A | Connexion gadget vers cible |

### Plateformes cibles supportées

| Plateforme | SoC | RAM | Interface Boot |
|------------|-----|-----|----------------|
| **EspressoBin V5** | Armada 3720 | 1GB DDR3 | SPI NOR |
| **EspressoBin V7** | Armada 3720 | 1-2GB DDR3 | SPI NOR |
| **EspressoBin Ultra** | CN9130 | 4GB DDR4 | SPI NOR |
| **MochaBin** | CN9130 | 4-8GB DDR4 | SPI NOR |

---

## 📊 Couches de boot analysées

Le PiDebugger parse et colore automatiquement les différentes étapes du boot :

```
┌─────────────────────────────────────────────────────────────┐
│  BootROM      │ Vérification checksum, init minimale       │
├───────────────┼─────────────────────────────────────────────┤
│  WTMI         │ Marvell Trusted Firmware, init DDR         │
├───────────────┼─────────────────────────────────────────────┤
│  ATF BL1/2/31 │ ARM Trusted Firmware, secure boot          │
├───────────────┼─────────────────────────────────────────────┤
│  U-Boot SPL   │ Secondary Program Loader                   │
├───────────────┼─────────────────────────────────────────────┤
│  U-Boot       │ Bootloader principal, autoboot             │
├───────────────┼─────────────────────────────────────────────┤
│  Linux Kernel │ Démarrage système, drivers, systemd        │
└─────────────────────────────────────────────────────────────┘
```

### Coloration syntaxique

| Couleur | Stage | Exemple |
|---------|-------|---------|
| 🟣 Magenta | SPI/WTMI | `WTMI: System started` |
| 🔵 Cyan | ATF/UEFI | `BL31: ARM Trusted Firmware` |
| 🔵 Bleu | U-Boot | `U-Boot 2024.01-armbian` |
| 🟢 Vert | Kernel | `Linux version 6.6.38` |
| 🔴 Rouge | Erreurs | `Error: DDR init failed` |
| 🟠 Orange | Warnings | `Warning: timeout` |

---

## 💾 USB Mass Storage

Le PiDebugger expose un stockage USB de 512MB (configurable) contenant :

```
PIDEBUGGER/
├── armbian/
│   ├── espressobin/
│   │   └── Armbian_24.11_Espressobin_bookworm.img.xz
│   ├── mochabin/
│   │   └── Armbian_24.11_Mochabin_bookworm.img.xz
│   └── espressobin-ultra/
│
├── uboot/
│   ├── espressobin/
│   │   └── flash-image-espressobin-v7-2g-2cs.bin
│   └── mochabin/
│       └── flash-image-mochabin-ddr4.bin
│
├── scripts/
│   ├── install-armbian.sh
│   └── flash-uboot.sh
│
└── README.txt
```

La cible SoC voit ce stockage comme une clé USB standard, permettant le boot et l'installation directe.

---

## 🚀 Installation rapide

### 1. Préparer la carte SD

```bash
# Télécharger Raspberry Pi OS Lite
wget https://downloads.raspberrypi.com/raspios_lite_armhf/images/...

# Flasher
sudo dd if=raspios-lite.img of=/dev/sdX bs=4M status=progress

# Activer SSH
touch /boot/ssh
```

### 2. Installer les drivers HyperPixel

```bash
git clone https://github.com/pimoroni/hyperpixel2r
cd hyperpixel2r
sudo ./install.sh
sudo reboot
```

### 3. Déployer PiDebugger

```bash
git clone https://github.com/votre-repo/pidebugger
cd pidebugger
pip install -r requirements.txt
sudo python3 main.py
```

---

## 📖 Documentation complète

La documentation technique détaillée (2800+ lignes) couvre :

- [Phase 1-3](/docs/pidebugger/setup) : Installation système
- [Phase 4-5](/docs/pidebugger/ui) : Interface circulaire Pygame
- [Phase 6-8](/docs/pidebugger/gadget) : USB Gadget et Serial
- [Phase 9-12](/docs/pidebugger/analyzers) : Parsers boot et timeline
- [Phase 13](/docs/pidebugger/integration) : Intégration Hexo

---

## 🔗 Ressources

- [Pimoroni HyperPixel 2.1" Round](https://shop.pimoroni.com/products/hyperpixel-2-1-round)
- [EspressoBin Wiki](http://wiki.espressobin.net/)
- [MochaBin Documentation](https://developer.solid-run.com/knowledge-base/mochabin-getting-started/)
- [Armbian Downloads](https://www.armbian.com/download/)
- [U-Boot Documentation](https://u-boot.readthedocs.io/)

---

## 📝 Licence

MIT License - Libre d'utilisation et modification.

---

*Projet créé avec ❤️ pour la communauté embedded ARM.*
