---
title: ARM64 — MOCHABIN — EMMC / UEFI Tow-Boot GUIDE
lang: fr
date: 2025-11-05 20:00:00
tags: 
- ARM
- Aramada
- NAS
- CLOUD
- SECUBOX
- FAST BACK
- contribute
category: cybersecurity
##publish: true
private: false
hidden: false
---
 # ⚙️ MOCHABIN — EMMC / UEFI Tow-Boot GUIDE 🚀  
**📅 Créé le :** 10 octobre 2025  
**💻 Matériel testé :** Mochabin (Armada 7040 – MVEBU ARM64)  
**🔗 Référence :** [Luke Granger-Brown — UEFI Boot for Mochabin](https://lukegb.com/posts/2023-08-08-uefi-boot-for-mochabin/)  

---

## 🧭 Objectif 🎯  
Configurer et démarrer un système **UEFI Tow-Boot** sur **eMMC, SSD ou USB** pour Mochabin.  
Le but : disposer d’un environnement **UEFI propre**, capable de démarrer **Debian, OpenWrt ou toute image ARM64** via GPT + ESP.

---<!-- more -->

## 🧩 1️⃣ Préparation de la carte et environnement  

⚡ Chargement Tow-Boot :
```bash
mvebu64boot -t -b result/binaries/Tow-Boot.spi.bin /dev/ttyUSB0
```

🔧 Réglage des adresses MAC dans U-Boot :
```bash
setenv ethaddr  F0:AD:4E:27:88:99
setenv eth1addr F0:AD:4E:27:88:9A
setenv eth2addr F0:AD:4E:27:88:9B
saveenv
```

✅ Environnement sauvegardé dans la flash SPI (`/dev/mtdblock2`).

---

## 🧠 2️⃣ Diagnostic initial 🔍  
Si Tow-Boot affiche :
```
No EFI system partition
EFI boot manager: Cannot load any image
```

👉 Cela signifie qu’il ne trouve **aucune partition FAT32 GPT** contenant un fichier `EFI/BOOT/BOOTAA64.EFI`.

---

## 💾 3️⃣ Créer la table GPT + partition EFI  
Sur ton **disque cible** (`/dev/mmcblk0` pour eMMC, `/dev/sda` pour SSD SATA) :

```bash
sudo wipefs -a /dev/sdX
sudo sgdisk --zap-all /dev/sdX

# 🧱 Créer 2 partitions :
# 1️⃣ ESP FAT32 (512 MiB)
# 2️⃣ Rootfs Linux (reste du disque)
sudo sgdisk -n1:0:+512M -t1:EF00 -c1:"EFI System" /dev/sdX
sudo sgdisk -n2:0:0      -t2:8300 -c2:"rootfs"     /dev/sdX

sudo mkfs.vfat -F32 -n EFI /dev/sdX1
sudo mkfs.ext4 -L rootfs   /dev/sdX2
```

💡 *Astuce :* utilise `lsblk -f` pour vérifier les étiquettes avant de démonter.

---

## 🗂️ 4️⃣ Créer l’arborescence EFI  
Monte la partition EFI :
```bash
sudo mkdir -p /mnt/esp
sudo mount /dev/sdX1 /mnt/esp
sudo mkdir -p /mnt/esp/EFI/BOOT
```

📂 Place ton bootloader ici :
```
/mnt/esp/EFI/BOOT/BOOTAA64.EFI
```

💡 *Le nom exact `BOOTAA64.EFI` est obligatoire pour l’amorçage UEFI ARM64.*

---

## 🧰 5️⃣ Choisir ton bootloader  

### 🅐 GRUB (Debian/Ubuntu ARM64) 🐧
```bash
apt install grub-efi-arm64
grub-install --target=arm64-efi --efi-directory=/mnt/esp --bootloader-id=debian
```

### 🅑 systemd-boot ⚙️  
```bash
cp /usr/lib/systemd/boot/efi/systemd-bootaa64.efi /mnt/esp/EFI/BOOT/BOOTAA64.EFI
```

📝 Crée `/mnt/esp/loader/entries/mochabin.conf` :
```
title Mochabin Debian
linux /boot/Image
initrd /boot/initrd.img
options root=PARTUUID=<UUID>-02 rw rootwait net.ifnames=0 biosdevname=0
```

---

## 🌳 6️⃣ Ajouter le DTB (Device Tree)  
📦 Copie le fichier DTB à jour :
```
/boot/dtb/marvell/armada-7040-mochabin.dtb
```
🧠 *Tow-Boot et UEFI l’utiliseront automatiquement avec ton kernel ARM64.*

---

## 🔄 7️⃣ Premier boot Tow-Boot  

🧭 Menu Tow-Boot :
```
Boot from eMMC
Boot from USB
Boot from (scsi0)  # pour SSD SATA
```

### ⚠️ Erreurs courantes
| 🚨 Message | ❓ Cause | 🛠️ Solution |
|-------------|----------|-------------|
| No EFI system partition | ESP manquante / mal formatée | Recrée `/dev/sdX1` FAT32 + `BOOTAA64.EFI` |
| No partition table – scsi 0 | Pas de GPT sur le disque | Refaire `sgdisk` |
| 0 Storage Device(s) | Clé USB exFAT ou non reconnue | Utiliser FAT32 ou EXT2 |

---

## 🌐 8️⃣ Réseau Tow-Boot  
Définir les adresses MAC une seule fois :
```bash
setenv ethaddr  F0:AD:4E:27:88:99
setenv eth1addr F0:AD:4E:27:88:9A
setenv eth2addr F0:AD:4E:27:88:9B
saveenv
```

🌍 *Les ports LAN ne sont pas actifs au boot : utiliser WAN pour PXE/HTTP boot.*

---

## 🧩 9️⃣ Compatibilité et firmware  
- 🧠 Tow-Boot SPI persiste sur la flash interne  
- 🧾 `/dev/mtdblock2` contient l’environnement (`fw_env.config`)  
- 🧬 Les kernels récents (≥ 6.6) améliorent eMMC & PCIe Mochabin  

---

## 🔧 Rappel BootFlow
```
[ BootROM ] → [ Tow-Boot SPI ] → [ UEFI / BOOTAA64.EFI ] → [ Kernel + DTB + RootFS ]
```

---

## 🧰 Commandes utiles 💡  
Afficher les variables Tow-Boot :
```
fw_printenv
```
Modifier :
```
fw_setenv bootcmd ...
```
Retour menu Tow-Boot :
```
run menucmd
```

---

## ✅ Résumé  
| 🧱 Élément | 📋 Valeur |
|-------------|------------|
| Bootloader | Tow-Boot 2022.07 SPI |
| Support | eMMC / SSD SATA / USB |
| Partition table | GPT |
| ESP | FAT32 – 512 MiB |
| Boot file | `/EFI/BOOT/BOOTAA64.EFI` |
| DTB | `armada-7040-mochabin.dtb` |
| OS supportés | Debian / OpenWrt / Ubuntu / Armbian |
| Réseau | mvpp2-{0,1,2} (eth0/1/2) |
| Console série | `ttyS0,115200` |

---

## 🧾 Crédits ✍️  
**Rédaction et validation : KuBoX Studio @ CyberMind # KERMA’s project (2025)**  
Basé sur le travail original de **Luke Granger-Brown**  
> _“UEFI Boot for Mochabin”_ → https://lukegb.com/posts/2023-08-08-uefi-boot-for-mochabin/

