---
title: 🚀 Compiler Armbian pour ESPRESSObin - Guide Complet
date: 2025-12-04 17:30:00
tags:
- armbian
- ESPRESSObin
- Linux
- Compilation
- ARM
categories:
- Tutoriels
- Embedded Systems
---
# 🚀 Compiler Armbian pour ESPRESSObin - Guide Complet

## 📖 Introduction

Ce guide détaille la compilation d'une image Armbian personnalisée pour la carte **ESPRESSObin**, en résolvant les problèmes courants de montage de partitions qui peuvent bloquer le processus de build.

<!-- more -->

## 🎯 Objectif

Créer une image Armbian fonctionnelle pour ESPRESSObin avec :
- 🐧 Ubuntu Noble (24.04)
- 🔧 Kernel Linux 6.12.60
- ⚡ Configuration optimisée

## 🔧 Prérequis

### 💻 Configuration système requise

- **OS** : Linux (Ubuntu/Debian recommandé)
- **RAM** : Minimum 8 GB
- **Espace disque** : ~50 GB libre
- **Connexion** : Internet stable

### 📦 Paquets nécessaires

```bash
sudo apt-get update
sudo apt-get install -y git
```

## 🚨 Problème rencontré : Erreur de montage

### ❌ Message d'erreur

```
[💥] error! Directory /media/reepost/ZAND/ARMBIAN/build/.tmp 
is mounted with the 'noexec' and/or 'nodev' options
```

### 🔍 Analyse

Le système de build Armbian détecte que le répertoire temporaire est monté avec des options de sécurité (`nosuid`, `nodev`, `noexec`) qui empêchent l'exécution de fichiers nécessaires à la compilation.

## ✅ Solution étape par étape

### 1️⃣ Préparation de l'environnement

```bash
# 📁 Création du répertoire de travail
mkdir ARMBIAN
cd ARMBIAN/

# 📥 Clone du repository officiel Armbian
git clone https://github.com/armbian/build.git
cd build
```

### 2️⃣ Résolution du problème de montage

**Option A : Remonter la partition**

```bash
# 🔧 Remontage avec les permissions nécessaires
sudo mount -o remount,exec,dev /dev/sdb1
```

**Option B : Utiliser un répertoire temporaire alternatif** ⭐ *Recommandé*

```bash
# 📂 Création d'un répertoire temporaire
mkdir -p ~/armbian-tmp

# 🔄 Configuration de la variable d'environnement
export TMPDIR=~/armbian-tmp
```

### 3️⃣ Lancement de la compilation

```bash
# 🚀 Compilation avec répertoire temporaire personnalisé
./compile.sh TMPDIR=/tmp/armbian-build
```

### 4️⃣ Configuration interactive

L'interface de compilation vous demandera :

1. **🎯 Target board** : Sélectionnez `ESPRESSObin`
2. **🔧 Kernel version** : Choisissez `current` (6.12.x)
3. **🐧 Distribution** : Sélectionnez `Ubuntu Noble` (24.04)
4. **📦 Build type** : Image complète ou minimale

## 🎊 Résultat de la compilation

### ✨ Image générée

```bash
# 📍 Vérification de l'image créée
ls output/images/

# 📦 Fichier généré :
Armbian-unofficial_26.02.0-trunk_Espressobin_noble_current_6.12.60.img
```

### 📊 Détails de l'image

| Propriété | Valeur |
|-----------|--------|
| 📛 Nom | Armbian-unofficial_26.02.0-trunk |
| 💻 Plateforme | ESPRESSObin |
| 🐧 Distribution | Ubuntu Noble 24.04 |
| 🔧 Kernel | Linux 6.12.60 |
| 📦 Type | current (stable) |
| ⚠️ Statut | unofficial/trunk |

## 💾 Installation de l'image

### 🔥 Flasher sur carte SD

**Avec Balena Etcher :**

```bash
# 📥 Installation de Balena Etcher
wget https://github.com/balena-io/etcher/releases/download/v1.18.11/balenaEtcher-1.18.11-x64.AppImage
chmod +x balenaEtcher-*.AppImage
./balenaEtcher-*.AppImage
```

**Avec dd (ligne de commande) :**

```bash
# ⚠️ ATTENTION : Vérifiez bien le périphérique cible !
sudo dd if=output/images/Armbian-*.img of=/dev/sdX bs=4M status=progress
sudo sync
```

### 🔌 Premier démarrage

1. **💾 Insérez** la carte SD dans l'ESPRESSObin
2. **🔌 Connectez** l'alimentation et le câble réseau
3. **⚡ Démarrez** la carte
4. **🔐 Connexion par défaut** :
   - Username : `root`
   - Password : `1234`
5. **⚙️ Configuration initiale** : Suivez les instructions à l'écran

## 🛠️ Dépannage

### ❌ Erreur : "No space left on device"

```bash
# 🧹 Nettoyage des fichiers temporaires
./compile.sh clean
```

### ❌ Erreur : "Permission denied"

```bash
# 🔑 Vérification des permissions
sudo chown -R $USER:$USER ~/armbian-tmp
```

### ❌ Build échoue pendant la compilation

```bash
# 🔄 Réessayer avec mode verbeux
./compile.sh TMPDIR=/tmp/armbian-build BUILD_DESKTOP=no KERNEL_CONFIGURE=no
```

## 📚 Ressources complémentaires

### 🔗 Liens utiles

- 📖 [Documentation officielle Armbian](https://docs.armbian.com/)
- 💬 [Forum Armbian - ESPRESSObin](https://forum.armbian.com/topic/42473-espressobin-completely-set-aside/)
- 🐙 [Repository GitHub Armbian](https://github.com/armbian/build)
- 📘 [Wiki ESPRESSObin](http://wiki.espressobin.net/)

### 🎓 Commandes avancées

```bash
# 🔧 Compilation avec configuration personnalisée
./compile.sh \
  BOARD=espressobin \
  BRANCH=current \
  RELEASE=noble \
  BUILD_MINIMAL=no \
  KERNEL_CONFIGURE=no \
  TMPDIR=/tmp/armbian-build

# 📦 Compilation du kernel uniquement
./compile.sh KERNEL_ONLY=yes

# 🖥️ Compilation avec interface desktop
./compile.sh BUILD_DESKTOP=yes DESKTOP_ENVIRONMENT=xfce
```

## 💡 Conseils et bonnes pratiques

### ✅ À faire

- 🔄 Toujours utiliser la dernière version du repository
- 💾 Prévoir suffisamment d'espace disque (50+ GB)
- 🌐 Utiliser une connexion Internet stable
- 📝 Noter les paramètres de compilation utilisés
- 🔐 Changer le mot de passe root au premier démarrage

### ❌ À éviter

- 🚫 Ne pas compiler en tant que root
- ⚠️ Ne pas interrompre la compilation
- 💾 Ne pas utiliser une partition avec `noexec`
- 🔌 Ne pas débrancher pendant le flash

## 📈 Performances ESPRESSObin

### 🎯 Spécifications matérielles

| Composant | Spécification |
|-----------|---------------|
| 🔧 CPU | Marvell Armada 3700 (ARM Cortex-A53) |
| ⚡ Fréquence | Dual-core 1.2 GHz |
| 💾 RAM | 512MB / 1GB / 2GB DDR3 |
| 🌐 Réseau | 3x Gigabit Ethernet |
| 💿 Stockage | microSD + SATA + eMMC |

### 📊 Cas d'usage

- 🏠 Serveur domestique
- 🌐 Routeur / Firewall
- 📡 Point d'accès WiFi
- 🔒 VPN Gateway
- 📦 NAS léger
- 🐳 Plateforme Docker

## 🎯 Conclusion

Vous avez maintenant une image Armbian personnalisée pour votre ESPRESSObin ! Ce guide vous a permis de :

- ✅ Compiler Armbian depuis les sources
- ✅ Résoudre les problèmes de montage
- ✅ Créer une image bootable
- ✅ Comprendre le processus de build

N'hésitez pas à expérimenter avec différentes configurations et à partager vos résultats sur le forum Armbian !

---

## 📝 Historique des commandes

```bash
# 📜 Historique complet de la session
872  mkdir ARMBIAN
873  cd ARMBIAN/
874  git clone https://github.com/armbian/build.git;cd build;./compile.sh
875  sudo mount -o remount,exec,dev /dev/sdb1
876  mkdir -p ~/armbian-tmp
877  export TMPDIR=~/armbian-tmp
878  ./compile.sh TMPDIR=/tmp/armbian-build
879  ls
880  ls output/images/Armbian-unofficial_26.02.0-trunk_Espressobin_noble_current_6.12.60.img
881  history
```
---
**Tags:** #Armbian #ESPRESSObin #Linux #ARM #Compilation #Ubuntu #Embedded
