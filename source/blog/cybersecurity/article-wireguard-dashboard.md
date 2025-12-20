---
title: "LuCI WireGuard Dashboard : Monitoring VPN moderne pour OpenWrt"
date: 2024-12-19
author: Gandalf
tags: [wireguard, openwrt, luci, vpn, dashboard, security, tunnel]
categories: [Projets, Réseau, Sécurité]
image: /images/wireguard-dashboard-hero.png
description: "Dashboard moderne pour visualiser vos tunnels WireGuard sur OpenWrt : interfaces, peers, trafic et configuration en temps réel."
---

# WireGuard Dashboard : Visualisez vos tunnels VPN

WireGuard est devenu **le** protocole VPN de référence : rapide, sécurisé, simple. Mais sur OpenWrt, le monitoring reste rudimentaire — quelques commandes `wg show` dans un terminal.

J'ai créé **luci-app-wireguard-dashboard** pour apporter une interface moderne et intuitive à la surveillance de vos tunnels WireGuard.

<div class="demo-banner">
🔐 <strong>Démo interactive :</strong> <a href="https://cybermind.fr/apps/wireguard-dashboard/">Essayez le dashboard</a>
</div>

## Pourquoi WireGuard ?

| Protocole | Lignes de code | Performance | Audit |
|-----------|---------------|-------------|-------|
| OpenVPN | ~100,000 | Moyenne | Complexe |
| IPsec | ~400,000 | Variable | Très complexe |
| **WireGuard** | **~4,000** | **Excellente** | **Facile** |

WireGuard est intégré au noyau Linux depuis 5.6, avec un support natif dans OpenWrt depuis la version 21.02.

## Fonctionnalités du dashboard

### 🌐 Vue Status

![Status Overview](/images/wireguard-dashboard-status.png)

- **Interfaces actives** : Nombre de tunnels configurés
- **Peers totaux** : Nombre de pairs configurés
- **Peers connectés** : Handshakes récents (< 3 min)
- **Trafic total** : RX/TX cumulés

Chaque interface affiche :
- Clé publique (tronquée)
- Port d'écoute
- Adresse IP du tunnel
- MTU et état

### 👥 Vue Peers

Liste détaillée de tous les pairs avec :
- **Statut en temps réel** : Active (🟢), Idle (🟡), Inactive (⚪)
- **Endpoint** : IP:port du pair distant (ou "roaming")
- **Allowed IPs** : Réseaux routés via ce pair
- **Last handshake** : Dernier échange cryptographique
- **Trafic** : RX/TX par pair
- **PSK** : Indicateur de clé pré-partagée

### 📊 Vue Traffic

Statistiques de bande passante :
- Totaux par interface
- Barres de progression RX/TX
- Répartition par pair
- Pourcentages visuels

### ⚙️ Vue Configuration

Affichage de la configuration au format WireGuard :
- Syntaxe colorée `[Interface]` et `[Peer]`
- Clés publiques (jamais les privées !)
- Visualisation du tunnel

## Architecture technique

```
┌─────────────────────────────────────────────────────────┐
│                    LuCI Dashboard                        │
│          (status.js, peers.js, traffic.js)              │
└───────────────────────────┬─────────────────────────────┘
                            │ ubus RPC
                            ▼
┌─────────────────────────────────────────────────────────┐
│                    RPCD Backend                          │
│           /usr/libexec/rpcd/wireguard-dashboard         │
└───────────────────────────┬─────────────────────────────┘
                            │ executes
                            ▼
┌─────────────────────────────────────────────────────────┐
│                      wg show                             │
│                  WireGuard CLI Tool                      │
└───────────────────────────┬─────────────────────────────┘
                            │ interacts with
                            ▼
┌─────────────────────────────────────────────────────────┐
│                WireGuard Kernel Module                   │
│                  Encrypted Tunnels                       │
└─────────────────────────────────────────────────────────┘
```

Le backend utilise `wg show` pour lire les informations en temps réel :
- `wg show interfaces` : liste des interfaces
- `wg show <iface> peers` : liste des pairs
- `wg show <iface> transfer` : trafic par pair
- `wg show <iface> latest-handshakes` : dernier handshake

## Design : Thème VPN Tunnel

Interface inspirée des outils de monitoring réseau professionnel :

| Élément | Couleur |
|---------|---------|
| Background | `#030712` (noir profond) |
| Cards | `#0f172a` (slate) |
| Accent principal | `#06b6d4` (cyan) |
| Accent secondaire | `#0ea5e9` (bleu) |
| Tunnel gradient | cyan → bleu → indigo |
| Active | `#10b981` (vert) |
| Idle | `#f59e0b` (orange) |

Animations fluides pour les indicateurs de statut et le flux du tunnel.

## Installation

### Prérequis

```bash
# Installer WireGuard
opkg update
opkg install kmod-wireguard wireguard-tools

# Optionnel : support LuCI natif
opkg install luci-proto-wireguard
```

### Installer le dashboard

```bash
# Depuis les sources OpenWrt
cd ~/openwrt/feeds/luci/applications/
git clone https://github.com/gkerma/luci-app-wireguard-dashboard.git

./scripts/feeds update -a && ./scripts/feeds install -a
make package/luci-app-wireguard-dashboard/compile V=s
```

### Installation manuelle

```bash
scp luci-app-wireguard-dashboard_*.ipk root@router:/tmp/
ssh root@router "opkg install /tmp/luci-app-wireguard-dashboard_*.ipk"
/etc/init.d/rpcd restart
```

### Accès

**VPN → WireGuard Dashboard**

## Indicateurs de statut des peers

| Indicateur | Signification |
|------------|---------------|
| 🟢 **Active** | Handshake < 3 minutes |
| 🟡 **Idle** | Handshake 3-10 minutes |
| ⚪ **Inactive** | Handshake > 10 min ou jamais |

Un handshake WireGuard a lieu :
- À l'établissement de la connexion
- Toutes les 2 minutes en cas de trafic
- Lors d'un keepalive si configuré

## Sécurité

Le dashboard respecte les bonnes pratiques de sécurité :

✅ **Les clés privées ne sont JAMAIS exposées**
✅ Lecture seule (pas de modification de config)
✅ Accès via ACL rpcd (utilisateurs authentifiés)
✅ Pas de stockage de données sensibles

## Cas d'usage

### 🏠 Accès distant à la maison
Surveillez les connexions de vos appareils mobiles à votre routeur.

### 🏢 Site-to-site entreprise
Visualisez l'état des tunnels entre sites distants.

### 🔒 VPN client
Vérifiez la connexion à votre fournisseur VPN.

## Démo interactive

Testez l'interface complète avec des données simulées :

👉 **[https://cybermind.fr/apps/wireguard-dashboard/](https://cybermind.fr/apps/wireguard-dashboard/)**

## Roadmap

- [x] Vue Status avec interfaces et peers
- [x] Vue Peers avec détails complets
- [x] Vue Traffic avec statistiques
- [x] Vue Configuration avec syntaxe colorée
- [ ] Graphiques historiques (24h/7j)
- [ ] Alertes sur déconnexion de peers
- [ ] Génération de QR codes pour mobile
- [ ] Export de configuration
- [ ] Gestion des peers (ajout/suppression)

## Contribuer

Projet open-source sous licence Apache-2.0 :

**GitHub** : [github.com/gkerma/luci-app-wireguard-dashboard](https://github.com/gkerma/luci-app-wireguard-dashboard)

## Conclusion

Avec **luci-app-wireguard-dashboard**, vos tunnels VPN deviennent enfin visibles. Plus besoin de SSH et de commandes cryptiques — un simple coup d'œil dans LuCI suffit pour vérifier l'état de votre infrastructure VPN.

---

*Vous utilisez WireGuard sur OpenWrt ? Partagez votre configuration dans les commentaires !*

<style>
.demo-banner {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    border: 1px solid #06b6d4;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 24px 0;
    font-size: 16px;
}
.demo-banner a {
    color: #06b6d4;
    font-weight: 600;
}
</style>
