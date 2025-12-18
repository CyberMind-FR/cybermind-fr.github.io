---
title: ARM64 — EspressoBin — UEFI + eMMC Complete Guide (2022 → 2025) 🚀
lang: fr
date: 2025-11-05 20:12:00
tags: 
- ARM
- Aramada
- NAS
- CLOUD
- SECUBOX
- FAST BACK
- contribute
categories: Cyber
##publish: true
private: false
hidden: false
---
  
# ⚙️ EspressoBin — UEFI + eMMC Complete Guide (2022 → 2025) 🚀
**📘 Projet :** OMNI SUITE | Cyber / Embedded Labs  
**🧠 Auteur :** KuBoX Studio @ CyberMind # KERMA’s project  
**📅 Période couverte :** 2022 → 2025  
**💻 Plateformes :** EspressoBin v5 / v7 / Ultra — ARM64 (Marvell Armada 3720)  

---

## 🏁 Introduction  
Ce guide fusionne l’ensemble des expérimentations **UEFI Boot (CyberMind, 2022)** et **OpenWrt eMMC (KuBoX Studio, 2024)** sur les cartes **Globalscale EspressoBin**.  
Il couvre l’installation, la configuration et le démarrage d’OS ARM64 via **U‑Boot / Tow‑Boot / UEFI**, avec un focus sur la version **v7 eMMC**.

---<!-- more -->

## 🧱 1️⃣ Hardware Overview  

| Version | SoC | Mémoire | Stockage | Interfaces principales |
|----------|------|----------|-----------|------------------------|
| **EspressoBin v5** | Armada 3720 | DDR3 1‑2 GB | µSD / SATA | 3× GbE, 1× USB3, 1× SATA, UART |
| **EspressoBin v7 (eMMC)** | Armada 3720 Rev.7 | DDR3L 2 GB | eMMC 8/16 GB, µSD | 3× GbE, 2× USB3, SATA, UART, mini‑PCIe |
| **EspressoBin Ultra** | Armada 3720 + DDR4 | DDR4 4 GB | eMMC + SATA + NVMe | 3× GbE, 2× USB3, SATA, M.2 NVMe |

### 🔩 Ports principaux
```
     ┌──────────────────────────┐
     │        EspressoBin        │
     │ ┌───────┐  ┌──────────┐  │
     │ │  USB3 │  │   USB2   │  │
     │ └───────┘  └──────────┘  │
     │ ┌───────────────┐         │
     │ │   SATA Port   │         │
     │ └───────────────┘         │
     │ [ETH0] [ETH1] [ETH2]      │  → 3× Gigabit Ethernet
     │                           │
     │  ○ UART / Console (micro‑USB)  
     │  ○ microSD slot  
     │  ○ eMMC (on‑board v7+)  
     │  ○ 12 V DC IN (centre +)  
     └──────────────────────────┘
```

---

## ⚡ 2️⃣ Power & Console Setup  

🔋 **Alimentation :** 12 V / 2 A (centre positif).  
🧷 **Console série :** via micro‑USB ou header UART 3‑pins (115200 8N1).  
💻 **Outils :**  
- Linux/macOS → `screen /dev/ttyUSB0 115200`  
- Windows → *PuTTY* (115200 8N1, No Flow Control)  

### 🔍 Vérifications initiales
Dans la console :
```bash
version
mmc list
usb reset
```
Assure‑toi que les périphériques USB et MMC sont correctement détectés avant de flasher ou booter.

---

## 🧩 3️⃣ UEFI Boot Setup (CyberMind, 2022)  

Basé sur les travaux originaux de **CyberMind** (EspressoBin UEFI Boot Notes).

### 🧠 Objectif
Configurer et valider le **boot UEFI** sur les cartes **EspressoBin ARM64** à partir d’U‑Boot.  
Compatible avec **Debian**, **IPFire**, **OPNsense**, **FreeBSD**, et **OpenBSD**.

### ⚙️ Configuration U‑Boot
```bash
setenv fdt_name 'dtb/marvell/armada-3720-espressobin.dtb'
setenv image_name 'EFI/BOOT/bootaa64.efi'
setenv kernel_addr_r 0x5000000
setenv fdt_addr_r 0x4f00000
saveenv
```

### 💾 Préparer un support de boot (USB / eMMC / SD)
```bash
sudo wipefs -a /dev/sdX
sudo sgdisk --zap-all /dev/sdX
sudo sgdisk -n1:0:+512M -t1:EF00 -c1:"EFI System" /dev/sdX
sudo mkfs.vfat -F32 -n EFI /dev/sdX1
```
Copie :  
```
/EFI/BOOT/BOOTAA64.EFI
/dtb/marvell/armada-3720-espressobin.dtb
```

### 🧪 Test IPFire 🔥
```bash
usb reset
load usb 0:2 $kernel_addr_r /efi/boot/bootaa64.efi
load usb 0:1 $fdt_addr_r /dtb-5.10.50-ipfire/marvell/armada-3720-espressobin-v7-emmc.dtb
bootefi $kernel_addr_r $fdt_addr_r
```
✅ **Résultat :** Boot Linux LTS OK – USB3 fonctionnel / USB2 non.

### 🧪 Test OPNsense 🧠
```bash
mmc dev 0
fatload mmc 0:1 $kernel_addr_r EFI/BOOT/bootaa64.efi
fatload mmc 0:1 $fdt_addr_r dtb/marvell/armada-3720-espressobin.dtb
bootefi $kernel_addr_r $fdt_addr_r
```
✅ **Résultat :** Boot FreeBSD / OPNsense EFI OK.

---

## 💾 4️⃣ OpenWrt v7 eMMC Build & Flash (KuBoX Studio, 2024)  

Inspiré du guide technique eMMC v7 EBIN.

### 🧱 Construction de l’image OpenWrt
```bash
make PACKAGES="luci luci-ssl openssh-server openssh-client fstools e2fsprogs resize2fs qosify ..." ROOTFS_PARTSIZE="3500" EXTRA_IMAGE_NAME="-GK2@TEST-2408111-003" image PROFILE=globalscale_espressobin-v7-emmc
```

### 💾 Flash vers eMMC via U‑Boot
```console
usb reset
ls usb 0
load usb 0:1 $kernel_addr_r EBIN/openwrt-23.05.4-EBINv7EMMC.img.gz
mmc dev 1 0
gzwrite mmc 1 $kernel_addr_r $filesize
mmc rescan
reset
```

### 🚀 Démarrage automatique OpenWrt eMMC
```console
setenv bootowrt 'mmc dev 1; ext4load mmc 1:1 $kernel_addr_r $image_name; ext4load mmc 1:1 $fdt_addr_r $fdt_name; setenv bootargs $console root=/dev/mmcblk1p2 rw rootwait net.ifnames=0 biosdevname=0; booti $kernel_addr_r - $fdt_addr_r'
setenv bootcmd 'run bootowrt'
setenv fdt_name 'armada-3720-espressobin-v7-emmc.dtb'
setenv image_name 'Image'
saveenv
reset
```

---

## 🌳 5️⃣ DTB & Compatibility Matrix

| 🧱 Carte | 🧬 DTB recommandé | 💿 OS testé | ⚙️ Statut |
|----------|------------------|-------------|-----------|
| EspressoBin v7 eMMC | armada-3720-espressobin-v7-emmc.dtb | IPFire | ✅ OK |
| EspressoBin v5 | armada-3720-espressobin.dtb | OPNsense / FreeBSD | ✅ OK |
| EspressoBin Ultra | armada-3720-espressobin-ultra.dtb | Debian / OpenWrt | ⚙️ En test |

> 💡 Les DTB doivent correspondre à la révision matérielle exacte.

---

## 🧰 6️⃣ Troubleshooting & Commands

| ⚠️ Problème | 💡 Cause | 🧩 Solution |
|--------------|----------|-------------|
| `Bad gz header` sur `gzwrite` | Image corrompue | Re‑copier l’image sur la clé USB et recharger |
| `Unknown MMC device` | Mauvais index | Utiliser `mmc list` pour vérifier (0 = SD / 1 = eMMC) |
| Boot bloqué | Mauvais chemins | Vérifier `$image_name`, `$fdt_name`, `ext4load` |
| Kernel panic root | Mauvais `root=/dev/mmcblkXpY` | Adapter selon la détection Linux |
| LuCI absent | Paquets manquants | Rebuild ImageBuilder avec modules luci |

---

## 🧩 7️⃣ OS Compatibility Table (2022 → 2025)

| 🖥️ OS / Distribution | 💿 UEFI | 💾 eMMC | 🌐 Réseau | 🧱 Statut |
|----------------------|---------|---------|-----------|-----------|
| **Debian 12 (Bookworm)** | ✅ Oui | ✅ Oui | ✅ OK | 🟢 Stable |
| **OpenWrt 23.05.4 (mvebu)** | ✅ Oui | ✅ Oui | ✅ OK | 🟢 Stable |
| **IPFire 2.27 (LTS)** | ✅ Oui | ⚙️ Partiel | ✅ OK (USB3) | 🟡 Fonctionnel |
| **OPNsense / FreeBSD 13+** | ✅ Oui | ⚙️ Partiel | ⚠️ à configurer | 🟡 Boot EFI OK |
| **Armbian 24.x (Debian/Ubuntu)** | ✅ Oui | ✅ Oui | ✅ OK | 🟢 Recommandé |
| **OpenBSD 7.x ARM64** | ⚙️ Expérimental | ❌ Non | ⚙️ Limitée | 🔴 Non stable |

---

## 🧾 8️⃣ Credits & References

**✍️ Rédaction & Tests :** KuBoX Studio @ CyberMind — KERMA’s Project  
**📅 2022 → 2025 :** CyberMind, KuBoX Studio, OpenWrt Labs  
**🔗 Sources :**
- CyberMind — EspressoBin UEFI Boot Notes (2022)  
- OpenWrt 23.05.4 ImageBuilder – mvebu‑cortexa53 (2024)  
- KuBoX Studio / OMNI SUITE 2025 Internal Docs  

---
