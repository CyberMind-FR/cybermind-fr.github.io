---
title: "Erreur de compilation Armbian (/tmp)"
date: 2025-12-04 7:25:00
tags:
  - armbian
categories:
  - contrib
---

# 🚨 Erreur de montage Armbian - Options noexec/nodev
<!-- more -->

Cette erreur se produit car le système de build Armbian a détecté que votre répertoire temporaire est monté avec les options `nosuid` et `nodev`, mais il vérifie également `noexec`. Le processus de build nécessite la capacité d'exécuter des fichiers dans le répertoire temporaire.

## 🔧 Solutions

### ✅ Option 1 : Remonter la partition avec les bonnes options

Remontez `/dev/sdb1` avec les options nécessaires :
```bash
sudo mount -o remount,exec,dev /dev/sdb1
```

### 🎯 Option 2 : Utiliser un répertoire temporaire différent

Faites pointer Armbian vers un répertoire sur un système de fichiers sans ces restrictions (comme votre système de fichiers racine) :
```bash
# 📁 Créer un répertoire temporaire dans /tmp ou votre home
mkdir -p ~/armbian-tmp

# 🔄 Définir la variable d'environnement avant de builder
export TMPDIR=~/armbian-tmp

# 🚀 Ou le spécifier directement dans la commande de build
./compile.sh TMPDIR=/tmp/armbian-build
```

### ⚙️ Option 3 : Modifier fstab pour des changements permanents

Si vous devez modifier définitivement les options de montage pour `/dev/sdb1` :

1. 📝 Éditez `/etc/fstab` :
```bash
   sudo nano /etc/fstab
```

2. 🔍 Trouvez la ligne pour `/dev/sdb1` et supprimez `noexec` et `nodev` des options, ou changez-les en `exec,dev`

3. 🔄 Remontez :
```bash
   sudo mount -o remount /media/reepost/ZAND
```

### 🛠️ Option 4 : Changer l'emplacement du répertoire de build

Modifiez la configuration du build Armbian pour utiliser un emplacement différent :
```bash
./compile.sh BUILD_TMPDIR=/tmp/armbian-build
```

## 💡 Recommandation

**⭐ L'option 2 est la plus rapide et la plus sûre** - utilisez simplement un répertoire temporaire sur votre système de fichiers racine où l'exécution est autorisée.

## 📋 Détails de l'erreur

- **💾 Partition concernée** : `/dev/sdb1`
- **📍 Point de montage** : `/media/reepost/ZAND/ARMBIAN/build/.tmp`
- **⚠️ Options actuelles** : `rw,nosuid,nodev,relatime,errors=remount-ro`
- **❌ Code d'erreur** : 43
