---
title: "LuCI Netdata Dashboard : Monitoring système temps réel pour OpenWrt"
date: 2025-12-19
author: Gandalf
tags: [netdata, openwrt, luci, monitoring, open-source, dashboard]
categories: [Projets, Monitoring]
image: /images/netdata-dashboard-hero.png
description: "Présentation de luci-app-netdata-dashboard, une interface de monitoring système moderne et responsive inspirée de Netdata pour OpenWrt."
---

# LuCI Netdata Dashboard : Votre routeur sous surveillance

Le monitoring système est essentiel pour tout administrateur réseau. Mais sur un routeur OpenWrt avec ses ressources limitées, les solutions classiques comme **Netdata** (qui nécessite ~200MB de RAM) ou **Prometheus + Grafana** sont tout simplement hors de portée.

J'ai donc développé **luci-app-netdata-dashboard**, un dashboard léger directement intégré à LuCI qui offre une expérience de monitoring moderne sans compromettre les performances de votre routeur.

<div class="demo-banner">
🎮 <strong>Démo interactive disponible :</strong> <a href="https://cybermind.fr/apps/netdata-dashboard/">Essayez le dashboard</a>
</div>

## Le problème : Pas de monitoring visuel léger sur OpenWrt

OpenWrt dispose bien de quelques outils :
- **luci-app-statistics** : collectd + graphiques, mais configuration complexe
- **vnStat** : statistiques réseau uniquement
- **htop** : terminal only

Ce qui manque cruellement : une interface **web moderne** avec des **métriques temps réel** qui tourne sur un routeur avec 128MB de RAM.

## La solution : Un dashboard natif inspiré de Netdata

**luci-app-netdata-dashboard** apporte l'expérience utilisateur de Netdata sur OpenWrt :

![Dashboard Preview](/images/netdata-dashboard-overview.png)

### Métriques couvertes

#### ⚡ CPU
- Utilisation globale en pourcentage
- Jauge animée avec historique sparkline
- Load average (1/5/15 minutes)
- Fréquence si disponible

#### 🧠 Mémoire
- Barre empilée : used / buffers / cached / free
- Valeurs absolues et pourcentages
- Swap si configuré

#### 💾 Disques
- Usage par point de montage
- Barres de progression colorées (vert → orange → rouge)
- Support multi-filesystem

#### 🌐 Réseau
- Trafic RX/TX total et par interface
- État des liens (up/down)
- Compteurs de paquets et erreurs
- Connection tracking (conntrack)

#### 🌡️ Températures
- Lecture des thermal zones
- Capteurs hwmon
- Code couleur selon la température

#### ⚙️ Processus
- Comptage par état (running, sleeping)
- Liste des processus avec PID, user, commande
- Consommation mémoire par processus

## Architecture technique

Le dashboard est 100% natif LuCI — pas de dépendance externe :

```
┌─────────────────────────────────────────────────────────┐
│                    LuCI JavaScript                       │
│              (realtime.js, system.js, etc.)             │
└───────────────────────────┬─────────────────────────────┘
                            │ ubus RPC
                            ▼
┌─────────────────────────────────────────────────────────┐
│                    RPCD Backend                          │
│               /usr/libexec/rpcd/netdata                 │
└───────────────────────────┬─────────────────────────────┘
                            │ reads
                            ▼
┌─────────────────────────────────────────────────────────┐
│                   Linux /proc & /sys                     │
│     /proc/stat, /proc/meminfo, /sys/class/thermal       │
└─────────────────────────────────────────────────────────┘
```

### Backend léger en Shell

Le script RPCD (`/usr/libexec/rpcd/netdata`) lit directement les fichiers du kernel :
- `/proc/stat` pour le CPU
- `/proc/meminfo` pour la RAM
- `/proc/net/dev` pour le réseau
- `/sys/class/thermal` pour les températures

Aucun daemon en arrière-plan, aucune base de données — les métriques sont collectées à la demande.

### Frontend JavaScript moderne

Les vues utilisent le framework LuCI client-side avec :
- **Jauges SVG** animées
- **Sparklines** pour l'historique récent
- **Barres empilées** pour la mémoire
- **Polling automatique** toutes les 2 secondes

## Design : Dark theme pour monitoring

Le thème s'inspire de GitHub et des interfaces de monitoring professionnelles :

| Élément | Couleur |
|---------|---------|
| Background | `#0d1117` |
| Cards | `#161b22` |
| Accent vert | `#3fb950` |
| Accent bleu | `#58a6ff` |
| Warning | `#d29922` |
| Danger | `#f85149` |

Le design est **full responsive** pour consultation sur mobile.

## Installation

### Prérequis

- OpenWrt 21.02+
- LuCI installé
- ~50KB d'espace disque

### Depuis les sources

```bash
cd ~/openwrt/feeds/luci/applications/
git clone https://github.com/gkerma/luci-app-netdata-dashboard.git

cd ~/openwrt
./scripts/feeds update -a && ./scripts/feeds install -a
make menuconfig  # LuCI > Applications > luci-app-netdata-dashboard
make package/luci-app-netdata-dashboard/compile V=s
```

### Installation manuelle

```bash
scp luci-app-netdata-dashboard_*.ipk root@router:/tmp/
ssh root@router "opkg install /tmp/luci-app-netdata-dashboard_*.ipk"
/etc/init.d/rpcd restart
```

### Accès

Après installation : **Status → Netdata Dashboard**

## Comparaison avec les alternatives

| Solution | RAM | Stockage | Config | Temps réel |
|----------|-----|----------|--------|------------|
| Netdata complet | ~200MB | ~100MB | Moyenne | ✅ |
| luci-app-statistics | ~30MB | ~20MB | Complexe | ❌ |
| **Ce dashboard** | **< 1MB** | **50KB** | **Zéro** | ✅ |

## Démo interactive

Testez l'interface avant d'installer :

👉 **[https://cybermind.fr/apps/netdata-dashboard/](https://cybermind.fr/apps/netdata-dashboard/)**

## Roadmap

- [x] Vue temps réel avec jauges
- [x] Détails système
- [x] Statistiques réseau
- [x] Moniteur de processus
- [ ] Historique sur 24h (optionnel, stockage flash)
- [ ] Alertes configurables
- [ ] Export des métriques
- [ ] Mode kiosk pour affichage dédié

## Contribuer

Projet open-source sous licence Apache-2.0 :

**GitHub** : [github.com/gkerma/luci-app-netdata-dashboard](https://github.com/gkerma/luci-app-netdata-dashboard)

## Conclusion

Avec **luci-app-netdata-dashboard**, le monitoring de votre routeur OpenWrt devient enfin **visuel et instantané**. Plus besoin de SSH pour vérifier la charge CPU ou l'état de la mémoire — tout est accessible en un coup d'œil depuis votre navigateur.

Le dashboard prouve qu'on peut avoir une interface moderne sans sacrifier les performances sur du matériel embarqué.

---

*Vous utilisez quel outil de monitoring sur vos routeurs ? Partagez dans les commentaires !*

<style>
.demo-banner {
    background: linear-gradient(135deg, #161b22, #21262d);
    border: 1px solid #3fb950;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 24px 0;
    font-size: 16px;
}
.demo-banner a {
    color: #3fb950;
    font-weight: 600;
}
</style>
