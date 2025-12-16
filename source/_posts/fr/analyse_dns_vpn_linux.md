---
title: Fiches - Analyse du Problème de Résolution DNS sous Linux avec VPN
lang: fr
date: 2025-11-07 13:30:00
author: 🧙 -- Gandalf (from "The Conjurers")
tags: 
- Reseau
- Analyse
- Mood
- Informatique
- contribute
categories: Network
##publish: true
private: false
hidden: false

---
# 🧠 Analyse du Problème de Résolution DNS sous Linux avec VPN

## 📝 Résumé
Un problème a été identifié concernant la résolution DNS sur un système Linux utilisant un VPN basé sur WireGuard (NordVPN). Le fichier `/etc/resolv.conf` est écrasé à chaque connexion VPN, modifiant notamment le champ `search domain`.

---<!-- more -->

## 🔍 Diagnostic

### ✅ Symptômes
- Résolution DNS incorrecte ou incomplète après connexion au VPN.
- Le champ `search` de `/etc/resolv.conf` change automatiquement.
- Redémarrer `systemd-resolved` restaure temporairement un bon fonctionnement.

### 🧪 Tests effectués
- Vérification du contenu de `/etc/resolv.conf` ✅
- Utilisation de `journalctl -u systemd-resolved` pour consulter les logs 🔍
- Tentative de modification de `/etc/systemd/resolved.conf` sans succès 🔒
- Confirmation que NordVPN avec WireGuard est responsable de la modification ❗

---

## 🛠 Solutions explorées

### ⚙️ Redémarrage de systemd-resolved
```bash
sudo systemctl restart systemd-resolved
```
✔️ Efficace temporairement après connexion VPN

---

### 📦 Emplacement des fichiers de config
- Les fichiers `nordlynx` générés par NordVPN ne sont pas visibles ni éditables directement via `~/.config/nordvpn` ❌
- L’usage de hooks post-connexion VPN semble être la meilleure piste pour automatiser le rétablissement de la config DNS 🔁

---

## 💡 Solution recommandée

### 🧩 Script de post-connexion

Créer un petit script personnalisé :
```bash
#!/bin/bash
sudo systemctl restart systemd-resolved
```

À exécuter **après** chaque connexion VPN, ou via un hook automatique si le client VPN le permet.

---

## 🚀 Étapes suivantes

1. 🔎 Vérifier si NordVPN propose un mécanisme de hook ou de script post-connexion.
2. 🧰 Automatiser le redémarrage de `systemd-resolved` si nécessaire.
3. ✅ Tester la solution sur plusieurs connexions VPN pour s’assurer de la stabilité.

---

## 🧭 Conclusion

Ce comportement est typique des VPNs qui prennent le contrôle total du DNS. En contournant cette prise de contrôle par des scripts ou des redémarrages ciblés de service, on peut restaurer une résolution DNS fonctionnelle sans perdre les bénéfices du VPN.
