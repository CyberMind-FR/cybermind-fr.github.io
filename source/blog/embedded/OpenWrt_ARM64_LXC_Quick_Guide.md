---
title: OpenWrt ARM64 — LXC QUICK GUIDE
lang: fr
date: 2021-06-07 10:00:00
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
  
  # ⚙️ OpenWrt ARM64 — LXC QUICK GUIDE  
**Tested on:** EspressoBin / EspressoBin Ultra (MVEBU ARM64)  
**Base version:** OpenWrt 21.02-RC  
**Goal:** Run lightweight Debian containers (LXC) inside OpenWrt

---<!-- more -->

## 1️⃣ Prérequis & outils
```bash
opkg update
opkg install xz tar gnupg
opkg install kmod-ikconfig kmod-veth
opkg install cgroupfs-mount cgroup-tools
```

---

## 2️⃣ Installation de LXC et LuCI
```bash
opkg install liblxc luci-app-lxc lxc lxc-attach lxc-auto lxc-autostart lxc-cgroup lxc-checkconfig lxc-common lxc-config lxc-console lxc-copy lxc-create lxc-destroy lxc-device lxc-execute lxc-freeze lxc-hooks lxc-info lxc-init lxc-ls lxc-monitor lxc-snapshot lxc-start lxc-stop lxc-templates lxc-top lxc-unfreeze lxc-unprivileged lxc-unshare lxc-user-nic lxc-usernsexec lxc-wait rpcd-mod-lxc
```

---

## 3️⃣ Vérification du noyau
```bash
lxc-checkconfig
```
✅ Vérifie que les namespaces et les cgroups sont activés.  
Les erreurs sur `CONFIG_NF_NAT_IPV4/6` peuvent être ignorées si NAT géré par OpenWrt.

---

## 4️⃣ Création d’un conteneur Debian Buster (ARM64)
Si GPG keyserver inaccessible :
```bash
opkg install gnupg2-utils gnupg2-dirmngr
```
Puis :
```bash
DOWNLOAD_KEYSERVER="pgp.mit.edu" lxc-create --name myLMS --template download -- --dist debian --release buster --arch arm64
```
ou sans validation :
```bash
lxc-create --name myLMS --template download -- --dist debian --release buster --arch arm64 --no-validate
```

---

## 5️⃣ Démarrage du conteneur
```bash
lxc-start -n myLMS
lxc-ls -f
```
Si erreur liée à **cgroups v1**, commente la section legacy :
```bash
nano /usr/share/lxc/config/common.conf
#lxc.cgroup.devices.deny = a
#lxc.cgroup.devices.allow = c 10:229 rwm
```
Puis relance :
```bash
lxc-start -n myLMS
```

---

## 6️⃣ Configuration réseau du conteneur
```bash
nano /srv/lxc/myLMS/config
```
Ajoute :
```
lxc.net.0.type = veth
lxc.net.0.link = br-lan
lxc.net.0.flags = up
lxc.net.0.hwaddr = 00:FF:DD:BB:CC:01
```
Démarre :
```bash
lxc-start -n myLMS
lxc-ls -f
```
> ✅ Exemple IP : `192.168.1.188`

---

## 7️⃣ Post-installation Debian
```bash
lxc-attach -n myLMS
adduser admin
apt install sudo ssh -y
addgroup admin sudo
exit
```
Accès SSH :
```bash
ssh admin@192.168.1.188
```

---

## 8️⃣ Autostart au boot
```bash
uci add lxc-auto container
uci set lxc-auto.@container[-1].name=myLMS
uci set lxc-auto.@container[-1].timeout=30
uci commit lxc-auto
```

---

## 9️⃣ Installer LMS (Logitech Media Server)
```bash
sudo apt update
sudo apt install wget libio-socket-ssl-perl -y
wget http://downloads.slimdevices.com/LogitechMediaServer_v8.1.1/logitechmediaserver_8.1.1_all.deb
sudo dpkg -i logitechmediaserver_8.1.1_all.deb
```

### 💻 Accès Web :
```
http://192.168.1.188:9000/
ou
http://mylms.local:9000/
```

---

## ✅ Résumé final
| Élément | Valeur |
|----------|--------|
| Base OS | OpenWrt 21.02-RC ARM64 |
| Container | Debian Buster |
| IP par défaut | DHCP via `br-lan` |
| Démarrage auto | via `lxc-auto` |
| Exemple App | Logitech Media Server |
| WebUI | http://<IP>:9000 |
| SSH | admin@<IP> |

---

## 🧾 Crédits
**Guide adapté et testé sur EspressoBin / EspressoBin Ultra — KuBoX Studio @ CyberMind # KERMA’s project (2025)**  
