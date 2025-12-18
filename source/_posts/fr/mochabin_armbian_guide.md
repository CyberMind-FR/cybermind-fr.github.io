---
title: 🚀 Implémenter le MOCHAbin de GlobalScale dans Armbian
date: 2025-12-04 18:45:00
tags:
- MOCHAbin
- armbian
- GlobalScale
- Marvell
- Armada 7040
- Build
categories:
- Tutoriels
- Embedded Systems
- Development
---
# 🚀 Implémenter le MOCHAbin de GlobalScale dans Armbian

## 📖 Introduction

Le **MOCHAbin** de GlobalScale Technologies est une carte de développement basée sur le SoC Marvell Armada 7040 (quad-core ARM Cortex-A72 @ 1.4GHz). C'est l'évolution de l'ESPRESSObin avec des capacités réseau avancées : WiFi 6, 5G, et connectivité Multi-Gigabit.

Ce guide explique comment ajouter le support du MOCHAbin dans le framework de build Armbian.

<!-- more -->

## 🎯 Spécifications du MOCHAbin

### 💻 Caractéristiques matérielles

| Composant | Spécification |
|-----------|---------------|
| 🔧 SoC | Marvell Armada 7040 |
| ⚡ CPU | 4x ARM Cortex-A72 @ 1.4 GHz |
| 💾 RAM | 4GB ou 8GB DDR4 |
| 🌐 Réseau | 4x GbE + 1x WAN PoE |
| 📡 SFP | 1x SFP + 1x SFP+ (10GbE) |
| 💿 Stockage | M.2 SATA + SATA + eMMC |
| 📶 Sans fil | WiFi 6 (802.11ax) + Bluetooth 5 |
| 📱 Cellulaire | Support 4G/5G via M.2 |
| 🔌 Expansion | PCIe + Mini-PCIe |

## 🔍 État actuel du support

### ✅ Support Mainline Linux

Le support du MOCHAbin a été intégré dans le kernel Linux mainline avec le fichier Device Tree `armada-7040-mochabin.dts`.

### ⚠️ Support Armbian

Actuellement, le MOCHAbin n'est **pas officiellement supporté** par Armbian. Il existe une discussion sur le forum Armbian pour ajouter le support du MOCHAbin, mais aucune configuration officielle n'est disponible.

## 🛠️ Étapes pour ajouter le MOCHAbin à Armbian

### 1️⃣ Prérequis

```bash
# 📥 Cloner le repository Armbian
git clone https://github.com/armbian/build.git
cd build

# 📦 Installer les dépendances
sudo apt-get update
sudo apt-get install -y git
```

### 2️⃣ Créer la configuration de la carte

Créez le fichier de configuration pour le MOCHAbin :

```bash
# 📝 Créer le fichier de configuration
nano config/boards/mochabin.conf
```

**Contenu du fichier `mochabin.conf` :**

```bash
# MOCHAbin by GlobalScale Technologies
# Marvell Armada 7040 based board

BOARD_NAME="GlobalScale MOCHAbin"
BOARDFAMILY="mvebu64"
BOARD_MAINTAINER="votre-github-id"
BOOTCONFIG="mvebu_mochabin-88f7040_defconfig"
KERNEL_TARGET="current,edge"
FULL_DESKTOP="no"
BOOT_LOGO="desktop"

# Device Tree
BOOT_FDT_FILE="marvell/armada-7040-mochabin.dtb"

# Serial console
SERIALCON="ttyS0:115200n8"

# Modules
MODULES="ahci mv_xor mvneta mvpp2"
MODULES_CURRENT="ahci mv_xor mvneta mvpp2"

# Packages
PACKAGE_LIST_BOARD="ethtool"

# Support 4GB and 8GB variants
BOARD_FIRMWARE_INSTALL="-full"
```

### 3️⃣ Vérifier le Device Tree

Le Device Tree du MOCHAbin doit être présent dans le kernel Linux :

```bash
# 🔍 Vérifier la présence du DTS dans le kernel
ls -la cache/sources/linux-mainline/*/arch/arm64/boot/dts/marvell/ | grep mochabin

# Devrait afficher :
# armada-7040-mochabin.dts
```

### 4️⃣ Configuration U-Boot (optionnel)

Si U-Boot nécessite une configuration spécifique :

```bash
# 📝 Créer un patch U-Boot si nécessaire
mkdir -p patch/u-boot/u-boot-mvebu64/

# Ajouter les configurations U-Boot spécifiques au MOCHAbin
```

### 5️⃣ Ajouter la famille de carte (si nécessaire)

Si la famille `mvebu64` n'existe pas encore, créez-la :

```bash
# 📂 Vérifier l'existence de la famille
ls config/sources/families/

# 📝 Si nécessaire, créer mvebu64.conf
nano config/sources/families/mvebu64.conf
```

**Contenu de `mvebu64.conf` :**

```bash
# Marvell MVEBU 64-bit family
ARCH=arm64
BOOTSCRIPT="boot-mvebu.cmd:boot.cmd"
BOOTENV_FILE="mvebu.txt"
UBOOT_TARGET_MAP=";;flash-image.bin u-boot.bin"
BOOTDELAY=3
BOOTBRANCH='tag:v2024.01'
ATFSOURCE='https://github.com/ARM-software/arm-trusted-firmware'
ATFDIR='arm-trusted-firmware'
ATFBRANCH='tag:v2.10'
ATF_PLAT="a70x0"
ATF_TARGET_MAP='USE_COHERENT_MEM=0 LOG_LEVEL=20 CLOCKSPRESET=CPU_1400_DDR_800 DDR_TOPOLOGY=2 BOOTDEV=SPINOR PARTNUM=0 BL33=$UBOOT_PATH/u-boot.bin all fip;;build/a70x0/release/flash-image.bin'
KERNELSOURCE='https://github.com/torvalds/linux'
KERNELBRANCH='branch:linux-6.6.y'
LINUXFAMILY=mvebu64
```

### 6️⃣ Compilation

Lancez la compilation pour le MOCHAbin :

```bash
# 🚀 Compilation interactive
./compile.sh

# Ou directement en ligne de commande :
./compile.sh \
  BOARD=mochabin \
  BRANCH=current \
  RELEASE=noble \
  BUILD_MINIMAL=yes \
  BUILD_DESKTOP=no \
  KERNEL_CONFIGURE=no \
  TMPDIR=/tmp/armbian-build
```

### 7️⃣ Options de compilation avancées

```bash
# 🔧 Avec configuration du kernel
./compile.sh \
  BOARD=mochabin \
  BRANCH=edge \
  RELEASE=bookworm \
  KERNEL_CONFIGURE=yes

# 📦 Build desktop
./compile.sh \
  BOARD=mochabin \
  BRANCH=current \
  RELEASE=noble \
  BUILD_DESKTOP=yes \
  DESKTOP_ENVIRONMENT=xfce

# 🐛 Mode debug
./compile.sh \
  BOARD=mochabin \
  BRANCH=current \
  RELEASE=noble \
  BUILD_MINIMAL=yes \
  CLEAN_LEVEL="" \
  KERNEL_ONLY=no \
  INSTALL_HEADERS=yes
```

## 📋 Configuration Device Tree spécifique

### 🔧 Personnalisation du DTS

Si vous devez modifier le Device Tree pour des besoins spécifiques :

```bash
# 📁 Créer un overlay personnalisé
mkdir -p patch/kernel/mvebu64-current/
nano patch/kernel/mvebu64-current/mochabin-custom.patch
```

Exemple de patch pour activer des fonctionnalités :

```diff
--- a/arch/arm64/boot/dts/marvell/armada-7040-mochabin.dts
+++ b/arch/arm64/boot/dts/marvell/armada-7040-mochabin.dts
@@ -XX,X +XX,X @@
 
+// Ajoutez vos modifications ici
+&spi0 {
+    status = "okay";
+};
```

## 🌐 Configuration réseau

### 📡 Configuration des interfaces Ethernet

Le MOCHAbin dispose de plusieurs interfaces réseau qui doivent être configurées :

```bash
# 📝 Configuration réseau dans /etc/network/interfaces
auto eth0
iface eth0 inet dhcp

auto eth1
iface eth1 inet static
    address 192.168.1.1
    netmask 255.255.255.0

# Configuration du switch intégré
auto lan1 lan2 lan3 lan4
```

### 🔧 Configuration SFP/SFP+

```bash
# 📦 Installer les outils réseau
apt-get install ethtool sfputil

# 🔍 Vérifier les interfaces SFP
ethtool -m eth2  # SFP
ethtool -m eth3  # SFP+ (10GbE)
```

## 🚨 Problèmes courants et solutions

### ❌ Erreur : Device Tree non trouvé

```bash
# Solution : Vérifier le chemin du DTB
# Dans mochabin.conf :
BOOT_FDT_FILE="marvell/armada-7040-mochabin.dtb"

# Ou forcer la compilation du DTB
KERNEL_CONFIGURE=yes
```

### ❌ Erreur : U-Boot ne démarre pas

```bash
# Solution : Utiliser l'outil mvebu64boot pour le recovery
git clone https://github.com/pali/mvebu64boot
cd mvebu64boot
make

# Boot via UART
./mvebu64boot -t -b u-boot.bin /dev/ttyUSB0
```

### ❌ Erreur : Interfaces réseau non détectées

```bash
# Solution : Vérifier les modules kernel
modprobe mvpp2
modprobe mvneta

# Ajouter à la configuration
MODULES_CURRENT="mvpp2 mvneta mv_xor ahci"
```

## 📦 Création d'une Pull Request

### 🎯 Contribuer au projet Armbian

Une fois votre configuration testée et fonctionnelle :

```bash
# 1️⃣ Fork le repository Armbian sur GitHub

# 2️⃣ Créer une branche
git checkout -b add-mochabin-support

# 3️⃣ Ajouter vos fichiers
git add config/boards/mochabin.conf
git add config/sources/families/mvebu64.conf  # Si créé

# 4️⃣ Commit
git commit -m "Add GlobalScale MOCHAbin board support

- Add board configuration for MOCHAbin
- Based on Marvell Armada 7040 SoC
- Support for 4GB and 8GB RAM variants
- Multi-gigabit networking support
- Tested with kernel 6.6.x"

# 5️⃣ Push
git push origin add-mochabin-support

# 6️⃣ Créer la Pull Request sur GitHub
```

### 📋 Checklist pour la PR

- ✅ Configuration de la carte testée et fonctionnelle
- ✅ Device Tree présent dans le kernel mainline
- ✅ Documentation ajoutée
- ✅ Support pour multiples variantes (4GB/8GB)
- ✅ Maintainer déclaré avec GitHub ID
- ✅ Tests effectués sur matériel réel
- ✅ Screenshots / logs de boot fournis

## 🔗 Ressources complémentaires

### 📚 Documentation

- 📖 [Documentation Armbian - Ajouter une carte](https://docs.armbian.com/Developer-Guide_Adding-Board-Family/)
- 📖 [Board Configuration Reference](https://github.com/armbian/build/tree/main/config/boards)
- 📖 [Armbian Build Options](https://docs.armbian.com/Developer-Guide_Build-Options/)

### 🌐 Liens utiles

- 🏠 [Site GlobalScale MOCHAbin](https://globalscaletechnologies.com/product/mochabin/)
- 🐙 [Linux Kernel - MOCHAbin DTS](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/arch/arm64/boot/dts/marvell/armada-7040-mochabin.dts)
- 💬 [Forum Armbian - MOCHAbin](https://forum.armbian.com/topic/24705-can-we-get-a-mochabin-5g-sub-board/)
- 📘 [MOCHAbin Wiki](http://www.espressobin.net/mochabin_wiki/)
- 🔧 [UEFI Boot for MOCHAbin](https://lukegb.com/posts/2023-08-08-uefi-boot-for-mochabin/)

### 🛠️ Outils de développement

```bash
# 📥 mvebu64boot - Recovery tool
git clone https://github.com/pali/mvebu64boot

# 📥 U-Boot MOCHAbin
git clone https://github.com/u-boot/u-boot
# Voir: configs/mvebu_mochabin-88f7040_defconfig

# 📥 ARM Trusted Firmware
git clone https://github.com/ARM-software/arm-trusted-firmware
```

## 💡 Cas d'usage du MOCHAbin

### 🏠 Applications

- 🌐 **Routeur/Firewall performant** : 10GbE + 5G/LTE
- 🔒 **VPN Gateway** : OpenVPN, WireGuard
- 📦 **NAS distribué** : Cubbit, NextCloud
- 🐳 **Plateforme Docker** : Container hosting
- 📡 **Point d'accès WiFi 6** : AP Controller
- 🔍 **IDS/IPS** : Suricata, Snort
- 📊 **Network Monitoring** : PRTG, Zabbix

### ⚡ Performances réseau

```bash
# Test de bande passante 10GbE
iperf3 -c server_ip -t 60

# Résultats typiques :
# SFP+  (10GbE) : ~9.5 Gbps
# SFP   (1GbE)  : ~940 Mbps
# RJ45  (1GbE)  : ~940 Mbps
```

## 🎯 Conclusion

L'ajout du support MOCHAbin dans Armbian permet de bénéficier :

- ✅ **Écosystème Armbian** : Mises à jour, outils, communauté
- ✅ **Kernel récent** : Support mainline Linux
- ✅ **Personnalisation** : Build framework flexible
- ✅ **Support communautaire** : Forums, documentation
- ✅ **Images optimisées** : Pour serveur ou desktop

Le MOCHAbin est une excellente plateforme pour les applications réseau avancées, et son intégration dans Armbian facilite grandement son déploiement et sa maintenance.

---

## 📝 Exemple de session de build

```bash
# 📜 Session complète de build
mkdir ~/armbian-mochabin
cd ~/armbian-mochabin

# 1️⃣ Clone
git clone https://github.com/armbian/build.git
cd build

# 2️⃣ Configuration
# Créer mochabin.conf comme décrit ci-dessus

# 3️⃣ Build
./compile.sh \
  BOARD=mochabin \
  BRANCH=current \
  RELEASE=noble \
  BUILD_MINIMAL=yes \
  KERNEL_CONFIGURE=no \
  TMPDIR=/tmp/armbian-build

# 4️⃣ Résultat
ls -lh output/images/
# Armbian_XX.XX.X_Mochabin_noble_current_X.X.XX.img.xz

# 5️⃣ Flash
sudo dd if=output/images/Armbian_*.img of=/dev/sdX bs=4M status=progress
sync
```

---
# 💾 Flasher Armbian depuis U-Boot sur MOCHAbin

## 📋 Méthodes disponibles

1. **TFTP** - Flasher via réseau (recommandé)
2. **USB** - Flasher depuis clé USB
3. **UART** - Flasher via console série (lent)

## 🌐 Méthode 1 : Flash via TFTP (Recommandé)

### Prérequis

**Sur votre PC Linux :**

```bash
# 1. Installer serveur TFTP
sudo apt-get install tftpd-hpa

# 2. Configurer TFTP
sudo nano /etc/default/tftpd-hpa
```

**Contenu de `/etc/default/tftpd-hpa` :**
```
TFTP_USERNAME="tftp"
TFTP_DIRECTORY="/srv/tftp"
TFTP_ADDRESS="0.0.0.0:69"
TFTP_OPTIONS="--secure"
```

```bash
# 3. Créer le répertoire et copier l'image
sudo mkdir -p /srv/tftp
sudo chmod 777 /srv/tftp

# 4. Copier votre image (décompressée)
cd output/images/
unxz Armbian_*.img.xz
sudo cp Armbian_*.img /srv/tftp/armbian-mochabin.img

# 5. Redémarrer TFTP
sudo systemctl restart tftpd-hpa
sudo systemctl status tftpd-hpa

# 6. Configurer une IP statique sur votre PC
sudo ip addr add 192.168.1.10/24 dev eth0
```

### Depuis U-Boot

```bash
# Console série
sudo screen /dev/ttyUSB0 115200

# Démarrez le MOCHAbin et interrompez le boot
Hit any key to stop autoboot:
Marvell>>

# 1. Configurer le réseau sur le MOCHAbin
setenv ipaddr 192.168.1.100
setenv serverip 192.168.1.10
setenv netmask 255.255.255.0

# 2. Tester la connexion
ping ${serverip}
# Vous devriez voir : host 192.168.1.10 is alive

# 3. Télécharger l'image en RAM
# ATTENTION : Vérifiez que vous avez assez de RAM
tftp 0x10000000 armbian-mochabin.img

# Cela va prendre plusieurs minutes...
# Vous verrez la progression : 
# #############################

# 4. Flasher sur eMMC (mmcblk1)
mmc dev 1
mmc write 0x10000000 0 0x200000

# OU Flasher sur SD card (mmcblk0)
mmc dev 0
mmc write 0x10000000 0 0x200000

# 5. Redémarrer
reset
```

### Notes importantes pour TFTP

```bash
# Calcul de la taille en blocs
# Si votre image fait 2GB :
# 2GB = 2048MB = 2097152KB = 2147483648 bytes
# En blocs de 512 bytes : 2147483648 / 512 = 4194304 blocs (0x400000)

# Pour une image de 4GB :
# Blocs = 8388608 (0x800000)

# Vérifier la taille de votre image :
ls -lh /srv/tftp/armbian-mochabin.img
# Exemple : 1.8G -> utilisez 0x380000 blocs
```

## 💿 Méthode 2 : Flash via USB

### Prérequis

**Préparer une clé USB :**

```bash
# 1. Formater la clé en ext2 (U-Boot le supporte bien)
sudo mkfs.ext2 /dev/sdc1

# 2. Monter et copier l'image
sudo mount /dev/sdc1 /mnt
sudo cp output/images/Armbian_*.img /mnt/armbian.img
sudo umount /mnt

# 3. Éjecter
sudo eject /dev/sdc
```

### Depuis U-Boot

```bash
Marvell>>

# 1. Démarrer le port USB
usb start

# Sortie attendue :
# scanning bus 0 for devices... 2 USB Device(s) found
#        scanning usb for storage devices... 1 Storage Device(s) found

# 2. Lister les périphériques USB
usb storage

# 3. Lister les partitions
usb part

# 4. Vérifier que l'image est présente
ext2ls usb 0:1 /
# Vous devriez voir : armbian.img

# 5. Obtenir la taille du fichier
ext2size usb 0:1 /armbian.img

# 6. Charger l'image en mémoire
ext2load usb 0:1 0x10000000 /armbian.img

# 7. Flasher sur eMMC
mmc dev 1
mmc write 0x10000000 0 0x200000

# 8. Redémarrer
reset
```

## 🔌 Méthode 3 : Flash via UART (mvebu64boot)

### Prérequis

**Sur votre PC :**

```bash
# 1. Installer mvebu64boot
git clone https://github.com/pali/mvebu64boot
cd mvebu64boot
make

# 2. Copier dans PATH (optionnel)
sudo cp mvebu64boot /usr/local/bin/
```

### Utilisation

```bash
# 1. Éteignez le MOCHAbin

# 2. Préparer votre image bootloader
# Vous avez besoin du fichier flash-image.bin depuis votre build

# 3. Lancer mvebu64boot
./mvebu64boot -t -b /path/to/flash-image.bin /dev/ttyUSB0

# Sortie :
# Sending boot pattern...

# 4. MAINTENANT allumez le MOCHAbin
# Le transfert va démarrer automatiquement

# 5. Attendez que le transfert se termine
# BootROM is ready for image file transfer
# [============================] 100%

# 6. Le MOCHAbin va démarrer avec l'image envoyée
```

**Note :** Cette méthode flash uniquement le bootloader, pas l'image complète.

## 🔧 Méthode 4 : Flash partiel (Boot + Rootfs)

### Flash en deux étapes

#### Étape 1 : Flash le bootloader

```bash
Marvell>>

# Via TFTP
tftp 0x10000000 u-boot-mochabin.bin

# Flasher dans SPI NOR (si disponible)
sf probe
sf erase 0 0x400000
sf write 0x10000000 0 ${filesize}

# OU dans MMC boot partition
mmc dev 0
mmc write 0x10000000 0 0x800
```

#### Étape 2 : Flash le rootfs

```bash
Marvell>>

# Charger l'image rootfs
tftp 0x10000000 rootfs.ext4

# Flasher sur la partition principale
mmc dev 0
mmc write 0x10000000 0x10000 0x1F0000
```

## 📦 Méthode 5 : Flash par parties (pour grosses images)

Si votre image est trop grosse pour la RAM :

```bash
Marvell>>

# Configuration réseau
setenv ipaddr 192.168.1.100
setenv serverip 192.168.1.10

# Effacer la destination d'abord
mmc dev 0
mmc erase 0 0x800000

# Flash par blocs de 128MB
# Partie 1
tftp 0x10000000 armbian-mochabin.img.part1
mmc write 0x10000000 0 0x100000

# Partie 2
tftp 0x10000000 armbian-mochabin.img.part2
mmc write 0x10000000 0x100000 0x100000

# Partie 3
tftp 0x10000000 armbian-mochabin.img.part3
mmc write 0x10000000 0x200000 0x100000

# etc...
```

**Préparer les parties sur le PC :**

```bash
# Découper l'image en morceaux de 128MB
split -b 128M armbian-mochabin.img armbian-mochabin.img.part

# Copier dans TFTP
sudo cp armbian-mochabin.img.part* /srv/tftp/
```

## 🔍 Vérifications après flash

### Vérifier l'intégrité

```bash
Marvell>>

# 1. Lire les premiers blocs
mmc dev 0
mmc read 0x10000000 0 100

# 2. Afficher le contenu (doit contenir des données)
md 0x10000000

# 3. Vérifier la table de partitions
mmc part

# Sortie attendue :
# Partition Map for MMC device 0  --   Partition Type: DOS
# 
# Part    Start Sector    Num Sectors     UUID            Type
#   1     8192            7634944         00000000-01     83
```

### Premier boot après flash

```bash
Marvell>>

# Redémarrer
reset

# OU forcer le boot depuis MMC
mmc dev 0
run bootcmd

# Si ça ne démarre pas automatiquement, boot manuel :
mmc dev 0
ext4load mmc 0:1 0x02080000 /boot/Image
ext4load mmc 0:1 0x01000000 /boot/dtb/marvell/armada-7040-mochabin.dtb
ext4load mmc 0:1 0x06000000 /boot/uInitrd
setenv bootargs "console=ttyS0,115200 root=/dev/mmcblk0p1 rootwait rw"
booti 0x02080000 0x06000000 0x01000000
```

## 🚨 Dépannage

### Erreur : "TFTP timeout"

```bash
# Vérifier la connexion réseau
ping ${serverip}

# Vérifier le service TFTP sur le PC
sudo systemctl status tftpd-hpa

# Vérifier le firewall
sudo ufw allow 69/udp

# Tester TFTP depuis le PC
tftp 192.168.1.10
tftp> get test.txt
```

### Erreur : "MMC: no card present"

```bash
# Réinitialiser le MMC
mmc rescan

# Lister les périphériques MMC
mmc list

# Essayer l'autre MMC
mmc dev 1
mmc info
```

### Erreur : "USB device not found"

```bash
# Réinitialiser USB
usb reset

# Scanner à nouveau
usb start

# Vérifier les ports USB
usb tree
```

### Mémoire insuffisante

```bash
# Vérifier la mémoire disponible
bdinfo

# Utiliser une adresse plus haute
# Au lieu de 0x10000000, essayez :
tftp 0x20000000 armbian-mochabin.img

# Ou flasher par parties (voir Méthode 5)
```

## 📊 Script automatique de flash TFTP

### Créer un script U-Boot

```bash
# Sur le PC, créez flash-tftp.txt

# === flash-tftp.txt ===
setenv ipaddr 192.168.1.100
setenv serverip 192.168.1.10
setenv netmask 255.255.255.0
echo "Testing network..."
ping ${serverip}
echo "Downloading image..."
tftp 0x10000000 armbian-mochabin.img
echo "Erasing MMC..."
mmc dev 0
mmc erase 0 0x800000
echo "Writing to MMC..."
mmc write 0x10000000 0 0x400000
echo "Done! Rebooting..."
reset
```

### Utiliser le script

```bash
# Depuis U-Boot, vous pouvez copier-coller ligne par ligne
# OU utiliser 'source' si le script est sur USB/MMC
```

## 🎯 Résumé - Commandes Flash rapide TFTP

```bash
# === SUR LE PC ===
# Installer et configurer TFTP
sudo apt-get install tftpd-hpa
sudo mkdir -p /srv/tftp
sudo cp armbian.img /srv/tftp/
sudo systemctl restart tftpd-hpa
sudo ip addr add 192.168.1.10/24 dev eth0

# === SUR U-BOOT ===
# Configuration réseau
setenv ipaddr 192.168.1.100
setenv serverip 192.168.1.10
ping ${serverip}

# Flash sur SD
tftp 0x10000000 armbian.img
mmc dev 0
mmc write 0x10000000 0 0x400000
reset

# Flash sur eMMC
tftp 0x10000000 armbian.img
mmc dev 1
mmc write 0x10000000 0 0x400000
reset
```

## 💡 Conseils

### ✅ Bonnes pratiques

- 🔒 **Sauvegardez** toujours avant de flasher
- 🧪 **Testez** d'abord sur SD avant eMMC
- 📊 **Vérifiez** la taille de l'image vs RAM disponible
- 🌐 **Utilisez** un câble Ethernet de qualité
- ⚡ **Assurez-vous** que l'alimentation est stable

### ⚠️ Précautions

- ❌ Ne débranchez JAMAIS pendant le flash
- ❌ Ne flashez pas sur le mauvais périphérique
- ❌ N'utilisez pas `0x0` comme adresse de destination MMC
- ❌ Ne flashez pas moins de blocs que nécessaire

### 📏 Calcul des blocs

```bash
# Formule : blocs = taille_fichier / 512

# Exemples :
# 1GB   = 1073741824 bytes / 512 = 2097152 blocs = 0x200000
# 2GB   = 2147483648 bytes / 512 = 4194304 blocs = 0x400000
# 4GB   = 4294967296 bytes / 512 = 8388608 blocs = 0x800000
# 8GB   = 8589934592 bytes / 512 = 16777216 blocs = 0x1000000

# Pour calculer depuis U-Boot (après tftp) :
# La variable ${filesize} contient la taille en bytes (hex)
printenv filesize
# Calculer : filesize / 0x200 = nombre de blocs
```

## 🔗 Ressources

- [U-Boot TFTP Documentation](https://u-boot.readthedocs.io/en/latest/usage/cmd/tftp.html)
- [mvebu64boot GitHub](https://github.com/pali/mvebu64boot)
- [U-Boot MMC Commands](https://u-boot.readthedocs.io/en/latest/usage/cmd/mmc.html)

---
# 🔧 Démarrer le MOCHAbin depuis U-Boot

## 🎯 Accéder à U-Boot

### 1️⃣ Connexion console série

```bash
# Connectez le câble microUSB du MOCHAbin à votre PC
# Identifiez le port série
ls /dev/ttyUSB*

# Connectez-vous avec screen ou minicom
sudo screen /dev/ttyUSB0 115200

# OU avec minicom
sudo minicom -D /dev/ttyUSB0 -b 115200
```

### 2️⃣ Interrompre le démarrage automatique

1. **Allumez** le MOCHAbin
2. **Appuyez sur n'importe quelle touche** dès que vous voyez :
   ```
   Hit any key to stop autoboot: 3
   ```
3. Vous obtenez le prompt U-Boot :
   ```
   Marvell>>
   ```

## 📋 Boot depuis carte SD/eMMC

### Démarrage automatique (déjà configuré)

Si votre image Armbian est flashée correctement, U-Boot devrait démarrer automatiquement avec :

```
Marvell>> run bootcmd
```

### Démarrage manuel depuis carte SD (mmcblk0)

```bash
# Prompt U-Boot
Marvell>>

# 1. Initialiser la carte SD
mmc dev 0
mmc info

# 2. Lister les partitions
mmc part

# 3. Définir les adresses de chargement
setenv kernel_addr_r 0x02080000
setenv fdt_addr_r 0x01000000
setenv ramdisk_addr_r 0x06000000

# 4. Charger le kernel
ext4load mmc 0:1 ${kernel_addr_r} /boot/Image

# 5. Charger le Device Tree
ext4load mmc 0:1 ${fdt_addr_r} /boot/dtb/marvell/armada-7040-mochabin.dtb

# 6. Charger l'initramfs
ext4load mmc 0:1 ${ramdisk_addr_r} /boot/uInitrd

# 7. Définir les arguments de boot
setenv bootargs "console=ttyS0,115200 root=/dev/mmcblk0p1 rootwait rootfstype=ext4 rw"

# 8. Démarrer
booti ${kernel_addr_r} ${ramdisk_addr_r} ${fdt_addr_r}
```

### Démarrage depuis eMMC (mmcblk1)

```bash
Marvell>>

# Sélectionner l'eMMC
mmc dev 1
mmc info

# Puis même procédure que pour SD
ext4load mmc 1:1 ${kernel_addr_r} /boot/Image
ext4load mmc 1:1 ${fdt_addr_r} /boot/dtb/marvell/armada-7040-mochabin.dtb
ext4load mmc 1:1 ${ramdisk_addr_r} /boot/uInitrd
setenv bootargs "console=ttyS0,115200 root=/dev/mmcblk1p1 rootwait rootfstype=ext4 rw"
booti ${kernel_addr_r} ${ramdisk_addr_r} ${fdt_addr_r}
```

## 💾 Boot depuis SATA/M.2 SSD

```bash
Marvell>>

# 1. Scanner les périphériques SCSI/SATA
scsi scan

# 2. Lister les périphériques
scsi device

# 3. Charger depuis SATA (device 0)
ext4load scsi 0:1 ${kernel_addr_r} /boot/Image
ext4load scsi 0:1 ${fdt_addr_r} /boot/dtb/marvell/armada-7040-mochabin.dtb
ext4load scsi 0:1 ${ramdisk_addr_r} /boot/uInitrd

# 4. Arguments de boot
setenv bootargs "console=ttyS0,115200 root=/dev/sda1 rootwait rootfstype=ext4 rw"

# 5. Démarrer
booti ${kernel_addr_r} ${ramdisk_addr_r} ${fdt_addr_r}
```

## 🌐 Boot via réseau (TFTP)

### Prérequis
- Serveur TFTP configuré sur votre réseau
- Fichiers de boot disponibles sur le serveur TFTP

```bash
Marvell>>

# 1. Configurer le réseau
setenv ipaddr 192.168.1.100
setenv serverip 192.168.1.10
setenv netmask 255.255.255.0
setenv gatewayip 192.168.1.1

# 2. Tester la connexion
ping ${serverip}

# 3. Charger le kernel via TFTP
tftp ${kernel_addr_r} Image

# 4. Charger le Device Tree
tftp ${fdt_addr_r} armada-7040-mochabin.dtb

# 5. Charger l'initramfs
tftp ${ramdisk_addr_r} uInitrd

# 6. Arguments de boot (NFS root exemple)
setenv bootargs "console=ttyS0,115200 root=/dev/nfs nfsroot=192.168.1.10:/nfs/rootfs,v3 ip=dhcp"

# 7. Démarrer
booti ${kernel_addr_r} ${ramdisk_addr_r} ${fdt_addr_r}
```

## 🔍 Commandes U-Boot utiles

### Informations système

```bash
# Version U-Boot
version

# Informations sur le SoC
bdinfo

# Variables d'environnement
printenv

# Afficher une variable spécifique
printenv bootcmd
printenv bootargs
```

### Gestion de la mémoire

```bash
# Informations mémoire
mmc list
mmc dev 0
mmc info
mmc part

# SATA/SCSI
scsi scan
scsi info
scsi part
```

### Gestion du réseau

```bash
# Afficher les interfaces réseau
net list

# Configuration IP
setenv ipaddr 192.168.1.100
setenv netmask 255.255.255.0
setenv gatewayip 192.168.1.1

# Test réseau
ping 192.168.1.1
dhcp
```

### Gestion des fichiers

```bash
# Lister les fichiers (ext4)
ext4ls mmc 0:1 /boot
ext4ls mmc 0:1 /boot/dtb/marvell

# Taille d'un fichier
ext4size mmc 0:1 /boot/Image

# Charger un fichier
ext4load mmc 0:1 ${kernel_addr_r} /boot/Image
```

## 💾 Sauvegarder la configuration U-Boot

### Créer un script de boot personnalisé

```bash
Marvell>>

# 1. Définir les variables
setenv bootdelay 3
setenv baudrate 115200

# 2. Créer un script de boot complet
setenv bootcmd_mmc 'mmc dev 0; ext4load mmc 0:1 ${kernel_addr_r} /boot/Image; ext4load mmc 0:1 ${fdt_addr_r} /boot/dtb/marvell/armada-7040-mochabin.dtb; ext4load mmc 0:1 ${ramdisk_addr_r} /boot/uInitrd; setenv bootargs console=ttyS0,115200 root=/dev/mmcblk0p1 rootwait rootfstype=ext4 rw; booti ${kernel_addr_r} ${ramdisk_addr_r} ${fdt_addr_r}'

# 3. Définir comme boot par défaut
setenv bootcmd 'run bootcmd_mmc'

# 4. Sauvegarder dans SPI Flash
saveenv
```

### Restaurer les paramètres par défaut

```bash
Marvell>>

# Effacer l'environnement
env default -a

# Sauvegarder
saveenv

# Redémarrer
reset
```

## 🔧 Dépannage depuis U-Boot

### Vérifier que les fichiers existent

```bash
Marvell>>

# Vérifier la partition boot
ext4ls mmc 0:1 /boot

# Devrait afficher :
# Image                  (kernel)
# uInitrd               (initramfs)
# boot.scr              (boot script)
# armbianEnv.txt        (variables)
# dtb/                  (device trees)

# Vérifier le Device Tree
ext4ls mmc 0:1 /boot/dtb/marvell
# Devrait contenir : armada-7040-mochabin.dtb
```

### Vérifier les adresses mémoire

```bash
Marvell>>

# Afficher la mémoire disponible
bdinfo

# Vérifier les adresses ne se chevauchent pas
printenv kernel_addr_r    # 0x02080000
printenv fdt_addr_r       # 0x01000000
printenv ramdisk_addr_r   # 0x06000000
```

### Tester le Device Tree

```bash
Marvell>>

# Charger et vérifier le DTB
ext4load mmc 0:1 ${fdt_addr_r} /boot/dtb/marvell/armada-7040-mochabin.dtb
fdt addr ${fdt_addr_r}
fdt print /

# Vérifier le modèle
fdt print /model
```

### Boot en mode debug

```bash
Marvell>>

# Ajouter des paramètres de debug
setenv bootargs "console=ttyS0,115200 root=/dev/mmcblk0p1 rootwait rootfstype=ext4 rw debug ignore_loglevel earlyprintk"

# Démarrer
booti ${kernel_addr_r} ${ramdisk_addr_r} ${fdt_addr_r}
```

## 🔄 Mettre à jour U-Boot depuis Linux

Une fois le système démarré, vous pouvez mettre à jour U-Boot :

```bash
# Depuis le système Linux démarré

# 1. Sauvegarder l'ancien U-Boot
sudo dd if=/dev/mmcblk0 of=/root/backup-uboot.img bs=1M count=4

# 2. Copier le nouveau U-Boot (depuis votre build)
# Le fichier est dans : output/debs/linux-u-boot-mochabin-current_*.deb

# 3. Extraire le .deb
dpkg-deb -x linux-u-boot-mochabin-current_*.deb /tmp/uboot

# 4. Trouver le fichier u-boot
find /tmp/uboot -name "u-boot*"

# 5. Flasher (ATTENTION !)
sudo dd if=/tmp/uboot/usr/lib/linux-u-boot-*/u-boot.bin of=/dev/mmcblk0 bs=512 seek=1 conv=notrunc

# 6. Synchroniser
sudo sync

# 7. Redémarrer
sudo reboot
```

## 📊 Script de boot automatique complet

Créez un fichier `boot.cmd` optimisé :

```bash
# boot.cmd pour MOCHAbin
# Compiler avec : mkimage -C none -A arm -T script -d boot.cmd boot.scr

# Configuration réseau (optionnel)
setenv autoload no
setenv ethaddr 00:50:43:01:02:03

# Adresses mémoire
setenv kernel_addr_r 0x02080000
setenv fdt_addr_r 0x01000000
setenv ramdisk_addr_r 0x06000000

# Device Tree
setenv fdtfile marvell/armada-7040-mochabin.dtb

# Source de boot (SD card par défaut)
setenv bootdev mmc
setenv bootpart 0:1

# Arguments de boot
setenv bootargs console=ttyS0,115200 root=/dev/mmcblk0p1 rootwait rootfstype=ext4 rw quiet loglevel=1

# Commandes de chargement
setenv load_kernel 'ext4load ${bootdev} ${bootpart} ${kernel_addr_r} /boot/Image'
setenv load_fdt 'ext4load ${bootdev} ${bootpart} ${fdt_addr_r} /boot/dtb/${fdtfile}'
setenv load_initrd 'ext4load ${bootdev} ${bootpart} ${ramdisk_addr_r} /boot/uInitrd'

# Commande de boot
setenv bootcmd 'run load_kernel; run load_fdt; run load_initrd; booti ${kernel_addr_r} ${ramdisk_addr_r} ${fdt_addr_r}'

# Sauvegarder
saveenv

# Démarrer
run bootcmd
```

**Compiler le script :**
```bash
mkimage -C none -A arm64 -T script -d boot.cmd boot.scr
```

## 🎯 Résumé - Commandes essentielles

```bash
# Accéder à U-Boot
# Appuyez sur une touche au démarrage

# Boot rapide depuis SD
mmc dev 0
ext4load mmc 0:1 0x02080000 /boot/Image
ext4load mmc 0:1 0x01000000 /boot/dtb/marvell/armada-7040-mochabin.dtb
ext4load mmc 0:1 0x06000000 /boot/uInitrd
setenv bootargs "console=ttyS0,115200 root=/dev/mmcblk0p1 rootwait rw"
booti 0x02080000 0x06000000 0x01000000

# Boot automatique
run bootcmd

# Sauvegarder config
saveenv

# Redémarrer
reset
```

## 🔗 Ressources

- [U-Boot Documentation](https://docs.u-boot.org/)
- [U-Boot Command Reference](https://u-boot.readthedocs.io/)
- [Armada SoC Boot Process](https://www.kernel.org/doc/html/latest/arm/marvell.html)
- [MOCHAbin U-Boot Config](https://github.com/u-boot/u-boot/tree/master/configs)

---

**Note importante** : Toutes ces commandes sont exécutées depuis le prompt U-Boot (`Marvell>>`), pas depuis le système Linux !
**Note importante** : Flasher via U-Boot efface toutes les données ! Sauvegardez d'abord !

**Tags:** #MOCHAbin #Armbian #Marvell #Armada7040 #GlobalScale #Networking #Build

**Catégories:** Tutoriels, Développement, Systèmes Embarqués, Réseau
