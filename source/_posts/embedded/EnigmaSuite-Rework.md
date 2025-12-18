---
title: EnigmaSuite — Rework complet pour OpenWrt 19.07
category: embedded
date: 2025-12-02 14:30:00
tags:
- openwrt
- EnigmaSuite
- ARM
- EspressoBin
- EnigmaBox
---
# EnigmaSuite — Rework complet pour OpenWrt 19.07

Ce document présente la version **entièrement retravaillée** d’EnigmaSuite pour **OpenWrt 19.07**, basée sur la version *v19.07.7*.
<!-- more -->
> ⚠️ **Statut : expérimental — “Use it at your own risk”**  
> ⚠️ **Mention d’origine : “CONFIDENTIAL and PRIVATE — For your eyes only!”**  
> (Cette mention est reproduite ici uniquement à des fins documentaires.)

---
```
https://github.com/CyberMind-FR/enigmasuite-openwrt
```
---
```
[Build PC]
   |
   | git clone / feeds update
   v
[OpenWrt 19.07 tree]
   |
   | make menuconfig -> make
   v
[bin/targets/.../images]
   |  ┌────────────┬──────────────┐
   |  │ kernel.img │ rootfs.ext4  │  (sysupgrade.img)
   |  └────────────┴──────────────┘
   |
   | scp / tftp
   v
[U-Boot on EspressoBin]
   |
   | tftp 0x8000000 kernel.img
   | tftp 0x9000000 rootfs.ext4
   | sf probe ; sf erase ; sf write
   v
[Flash (kernel + rootfs)]
   |
   v
[Reboot -> OpenWrt starts]
   └─> init -> mount rootfs -> EnigmaSuite services up
```
## Résumé de l’état du projet

- **Rework interne complet** basé sur *OpenWrt v19.07.7*  
- **Fonctionnel sur Cortex-A53** (testé en juin 2021)  
- Testé sur **MVEBU ARMADA 37xx ESPRESSOBIN** (carte de GlobalScale Technologies)

---

## 🎯 Comment compiler EnigmaSuite pour OpenWrt 19.07

### 1. Cloner OpenWrt

```sh
git clone https://github.com/openwrt/openwrt.git
cd openwrt
git checkout v19.07.7
```

### 2. Créer le fichier feeds.conf

Créer ou éditer feeds.conf pour y mettre :
```
src-git enigmabox https://github.com/CyberMind-FR/enigmasuite-openwrt.git;openwrt-19.07
src-git packages https://git.openwrt.org/feed/packages.git;openwrt-19.07
src-git luci https://git.openwrt.org/project/luci.git;openwrt-19.07
src-git routing https://git.openwrt.org/feed/routing.git;openwrt-19.07
src-git telephony https://git.openwrt.org/feed/telephony.git;openwrt-19.07
```
### 3. Activer le feed Enigmabox
```
echo "CONFIG_FEED_enigmabox=y" >> .config
```

### 4. Mise à jour & installation des feeds
```
./scripts/feeds update -a
./scripts/feeds install -a
```

### 5. Génération de la configuration
```
make defconfig
```
### 6. Compilation

Compiler le toolchain puis la cible :
```
make toolchain/compile
make target/compile
```

ou version raccourcie :
```
make {toolchain,target}/compile
```
## 🔥 Flash final

Une fois l’image générée :

Flashez le firmware sur votre appareil comme d’habitude…


(méthode dépendante du bootloader et du matériel — ex. u-boot + tftp + ext4 pour EspressoBin)

## ⚠️ Avertissements d’origine
```
Use it at your own risk...
Still in development phase...

CONFIDENTIAL and PRIVATE!
For your eyes only!
```

Ces indications font partie du texte original et sont conservées à titre informatif.

# 📐 Schéma ASCII — Build & Flash EnigmaSuite (OpenWrt 19.07)
```
                           ┌──────────────────────────────┐
                           │     Poste de Build (PC)       │
                           │  GNU/Linux / toolchain GCC    │
                           └──────────────┬───────────────┘
                                          │
                                          │ git clone + feeds
                                          ▼
                    ┌────────────────────────────────────────────┐
                    │        Arbre OpenWrt v19.07.7               │
                    │   (source officielle + feed EnigmaSuite)    │
                    └──────────────┬──────────────────────────────┘
                                   │
                                   │ make defconfig
                                   │ feeds update/install
                                   ▼
                    ┌────────────────────────────────────────────┐
                    │         Configuration OpenWrt               │
                    │  .config = sélection des paquets + options  │
                    └──────────────┬──────────────────────────────┘
                                   │
                                   │ make toolchain/compile
                                   │
                                   ▼
                    ┌────────────────────────────────────────────┐
                    │           Build Toolchain GCC               │
                    │  (cross-compile ARM Cortex-A53 / ARMADA)    │
                    └──────────────┬──────────────────────────────┘
                                   │
                                   │ make target/compile
                                   ▼
                    ┌────────────────────────────────────────────┐
                    │      Compilation du Target / Packages       │
                    │  - Kernel (uImage)                          │
                    │  - RootFS (ext4 + overlay)                  │
                    │  - Paquets EnigmaSuite                      │
                    └──────────────┬──────────────────────────────┘
                                   │
                                   │ génération image sysupgrade
                                   ▼
                    ┌────────────────────────────────────────────┐
                    │     Dossier ./bin/targets/.../images        │
                    │  - openwrt-*-kernel.bin                      │
                    │  - openwrt-*-rootfs.ext4                     │
                    │  - openwrt-*-sysupgrade.img                  │
                    └──────────────┬──────────────────────────────┘
                                   │
                                   │ transfert par tftp / scp
                                   ▼
              ┌───────────────────────────────────────────────────────────┐
              │             Carte ARM — ESPRESSOBIN                        │
              │      ARMADA 3720 / Cortex-A53 / U-Boot                    │
              └──────────────┬────────────────────────────────────────────┘
                             │
                             │ U-Boot : load image depuis TFTP
                             ▼
             ┌────────────────────────────────────────────────────────────┐
             │                    U-Boot (bootloader)                     │
             │  > tftp 0x8000000 openwrt-kernel.bin                       │
             │  > tftp 0x9000000 openwrt-rootfs.ext4                      │
             │  > sf probe ; sf write ; etc.                              │
             └──────────────┬────────────────────────────────────────────┘
                            │
                            │ Flashage partitions :
                            │ - kernel partition (16MB env.)  
                            │ - rootfs ext4 (3600MB env.)
                            ▼
             ┌────────────────────────────────────────────────────────────┐
             │                     Mémoire Flash / eMMC                   │
             │  ┌─────────────────────────┬──────────────────────────┐    │
             │  │  Kernel (uImage)        │   RootFS ext4 + overlay  │    │
             │  └─────────────────────────┴──────────────────────────┘    │
             └──────────────┬────────────────────────────────────────────┘
                            │
                            │ reboot
                            ▼
             ┌────────────────────────────────────────────────────────────┐
             │                         Boot OpenWrt                        │
             │   kernel → init → mount rootfs → start services             │
             │   + démarrage EnigmaSuite (web/mail/cloud/etc.)             │
             └────────────────────────────────────────────────────────────┘
```
## 2) Schéma réseau (flux LAN ↔ services ↔ EnigmaSuite)
```
                            Internet
                               |
                           (WAN/L3)
                               |
                       [Router / Firewall]
                       /       |        \
                      /        |         \
                (LAN) /    (DMZ) |      (Mgmt)
                    /           |         \
           +-------+-----+   +--+---+   +--+---+
           | Switch / VLAN|   |Espresso|  |Admin|
           | (LAN: 192.168.1.0/24) |Bin   |Host |
           +---+---+---+---+   +--+---+   +--+---+
               |   |   |           |          |
  Devices ---> PC  NAS Phone     eth0      eth1 (Mgmt)
               |               (OpenWrt)   (Serial/SSH)
               |                  |
        Browser -> 80/443 -> Web UI (EnigmaSuite)
                              |
            ------------------+-------------------
            |        |         |         |       |
         HTTP(S)  SMTP/IMAP  DB(5432)  S3 API  Cron/jobs
            |        |         |         |       |
          nginx   postfix/dovecot  postgresql  minio  task runner
```
## 3) Layout partitions / mémoire (EspressoBin — exemple typique SPI flash + eMMC)
```
SPI Flash (small, holds bootloader + env)
------------------------------------------------
offset 0x00000000  size 512KB   --> U-Boot SPL + U-Boot
offset 0x00080000  size 64KB    --> U-Boot env (env)
offset 0x00090000  size 448KB   --> reserved / bootloader extras

eMMC / NAND / SPI-NOR (rootfs + data)
------------------------------------------------
partition 1:  kernel        offset 0x00100000  size 16MB   -> uImage / fitImage
partition 2:  rootfs        offset 0x01100000  size 4096MB -> ext4 / squashfs + overlay
partition 3:  data          offset 0x41100000  size rest   -> /overlay, persistent data (configs, DB)
partition 4:  recovery      optional               -> recovery image / fallback

Example mtd layout (U-Boot env style):
mtdparts=spi0.0:512k(u-boot),64k(u-boot-env),448k(reserved),16m(kernel),-(rootfs)

Typical mount points after boot:
- / (root)  -> mounted from rootfs (ext4 or squashfs + overlay)
- /overlay  -> writable overlay on top of read-only root
- /boot     -> kernel image (if separate, sometimes not mounted)
- /data     -> persistent app data, DBs, uploads (on separate partition)
```
