---
title: "System Hub : Le Centre de Contrôle Unifié pour OpenWrt"
date: 2024-12-20
categories: [OpenWrt, LuCI, Administration, Remote]
tags: [openwrt, luci, dashboard, rustdesk, monitoring, administration, remote-assistance]
author: Gandalf
image: /images/system-hub-hero.png
description: "Un méta-dashboard centralisé pour OpenWrt avec gestion des composants, rapports de santé, assistance remote RustDesk et collecte de diagnostics."
---

# System Hub : Votre Tour de Contrôle OpenWrt

Avec la multiplication des dashboards et composants sur nos routeurs OpenWrt, il devient difficile de garder une vue d'ensemble. **System Hub** répond à ce besoin en offrant un centre de contrôle unifié pour administrer, diagnostiquer et maintenir votre infrastructure.

## 🎯 Le Problème

Après avoir installé CrowdSec, Netdata, Netifyd, WireGuard et d'autres dashboards, on se retrouve avec :

- **Multiples interfaces** à surveiller individuellement
- **Pas de vue globale** de l'état du système
- **Difficulté à diagnostiquer** les problèmes
- **Support à distance compliqué** sans outils adaptés
- **Logs dispersés** dans différents fichiers
- **Pas de health check** automatisé

## 💡 La Solution : System Hub

System Hub centralise tout en un seul point :

```
┌─────────────────────────────────────────────────────────────┐
│                      SYSTEM HUB                              │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  Score: 92/100  |  6 Composants  |  5 Running  |  1⚠️ │  │
│  └───────────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│  CrowdSec ✅  │  Netdata ✅  │  Netifyd ✅  │  WireGuard ✅ │
├─────────────────────────────────────────────────────────────┤
│  Client Guardian ⚠️        │  Network Modes ✅              │
├─────────────────────────────────────────────────────────────┤
│  🖥️ RustDesk ID: 847 293 156  │  📊 Health: Healthy         │
└─────────────────────────────────────────────────────────────┘
```

## 🧩 Gestion Centralisée des Composants

### Vue Unifiée

Tous vos dashboards et services en un coup d'œil :

| Composant | Status | Actions |
|-----------|--------|---------|
| 🛡️ CrowdSec | ✅ Running | Start · Stop · Restart |
| 📊 Netdata | ✅ Running | Start · Stop · Restart |
| 🔍 Netifyd | ✅ Running | Start · Stop · Restart |
| 🔒 WireGuard | ✅ Running | Start · Stop · Restart |
| 🛡️ Client Guardian | ⚠️ Stopped | **Start** · Stop · Restart |
| 🔀 Network Modes | ✅ Running | Start · Stop · Restart |

### Catégorisation Intelligente

Les composants sont organisés par fonction :

- **🔒 Sécurité** : CrowdSec, Client Guardian, AdGuard
- **📊 Monitoring** : Netdata, Prometheus, Grafana
- **🌐 Réseau** : Netifyd, Network Modes, ntopng
- **🔐 VPN** : WireGuard, Tailscale
- **🏠 Automation** : Home Assistant

### Roadmap Intégrée

Visualisez les composants planifiés :

```
🗓️ ROADMAP 2025

Q1 ─────────────────────────────────
    🚫 AdGuard Home      DNS Filtering
    📈 Prometheus        Metrics & Alerting
    🌐 Tailscale         Mesh VPN

Q2 ─────────────────────────────────
    📉 Grafana           Visualization
    🏠 Home Assistant    Automation
    📶 ntopng            Traffic Analysis
```

## 💚 Rapports de Santé Automatisés

### Score Global

Un indicateur unique de 0 à 100 :

- **80-100** : 💚 Healthy - Tout fonctionne bien
- **50-79** : 🟡 Warning - Attention requise
- **0-49** : 🔴 Critical - Action immédiate nécessaire

### Métriques Surveillées

| Métrique | Warning | Critical | Actuel |
|----------|---------|----------|--------|
| 🔲 CPU | 80% | 95% | **23%** ✅ |
| 💾 RAM | 80% | 95% | **58%** ✅ |
| 💿 Disque | 80% | 95% | **76%** ⚠️ |
| 🌡️ Température | 70°C | 85°C | **52°C** ✅ |
| 🌐 WAN | - | Down | **Up** ✅ |
| ⚙️ Services | - | < 100% | **12/12** ✅ |

### Recommandations Automatiques

System Hub analyse l'état et suggère des actions :

```
⚠️ RECOMMANDATION

Le stockage atteint 76% de capacité.

Actions suggérées :
• Nettoyer /tmp et /var/log
• Supprimer les anciens backups
• Désinstaller les packages inutilisés

Commande : opkg list-installed | wc -l
```

### Génération de Rapports

Créez des rapports détaillés :

- **📋 JSON** : Pour analyse automatisée
- **📄 PDF** : Pour documentation/audit
- **📧 Email** : Envoi programmé quotidien/hebdo

## 🖥️ Assistance Remote avec RustDesk

### Pourquoi RustDesk ?

- **Open Source** : Pas de dépendance cloud propriétaire
- **Auto-hébergeable** : Votre propre serveur relay
- **Sécurisé** : Chiffrement E2E
- **Multi-plateforme** : Windows, Mac, Linux, Mobile

### Intégration System Hub

```
┌─────────────────────────────────────────────┐
│  🖥️  RUSTDESK - ASSISTANCE REMOTE           │
├─────────────────────────────────────────────┤
│                                             │
│     ID: 847 293 156                         │
│     ─────────────────                       │
│     Communiquez ce code au support          │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │  🚀 Démarrer Session                 │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  ☑️ Approbation requise                     │
│  ☑️ Notification de connexion              │
│  ☐ Accès sans surveillance                 │
│                                             │
└─────────────────────────────────────────────┘
```

### Sécurité Remote

- **Approbation explicite** pour chaque connexion
- **Timeout de session** (1h par défaut)
- **Notification SMS/Email** à chaque connexion
- **Historique** des sessions

## 🔍 Collecte de Diagnostics

### Ce qui est collecté

| Catégorie | Contenu |
|-----------|---------|
| **📋 Logs** | syslog, dmesg, logs composants |
| **⚙️ Config** | network, wireless, firewall, dhcp |
| **🌐 Réseau** | interfaces, routes, ARP, connexions |
| **💻 Hardware** | CPU, mémoire, stockage, température |
| **📦 Packages** | Liste des packages installés |

### Anonymisation

Les données sensibles sont automatiquement masquées :

```bash
# Avant anonymisation
option key 'abc123secret'
option password 'mysupersecretpass'

# Après anonymisation
option key '*****'
option password '*****'
```

### Workflow Support

1. **Générer** l'archive diagnostic
2. **Télécharger** ou **envoyer** au support
3. Le support analyse avec les données
4. Session RustDesk si intervention nécessaire

## 📋 Logs Unifiés

### Agrégation Multi-Sources

Tous les logs en un seul endroit :

```
2024-12-20 15:45:23 | system      | INFO  | Health check: Score 92
2024-12-20 15:44:12 | crowdsec    | INFO  | Blocked IP 192.168.1.254
2024-12-20 15:42:00 | client-gdn  | WARN  | New unknown client
2024-12-20 15:40:30 | netifyd     | INFO  | Netflix detected
2024-12-20 15:35:00 | system      | WARN  | Disk usage 76%
2024-12-20 15:15:30 | adguard     | ERROR | Failed to start
```

### Filtres Puissants

- **Par source** : system, crowdsec, netifyd, etc.
- **Par niveau** : info, warning, error
- **Par texte** : recherche libre
- **Par date** : plage temporelle

### Export

- **CSV** pour Excel/Google Sheets
- **JSON** pour scripts/API
- **Syslog forward** vers serveur externe

## 📅 Automatisation

### Tâches Planifiées

| Tâche | Fréquence | Description |
|-------|-----------|-------------|
| Health Check | 1h | Vérification complète |
| Rapport Santé | 6h quotidien | Email au admin |
| Backup Config | Dimanche 3h | Sauvegarde UCI |
| Nettoyage Logs | Quotidien 4h | Supprimer > 30j |

### Alertes

Notification automatique en cas de :

- 🔴 Score santé < 50
- 🟡 Composant stopped
- ⚠️ Disque > 90%
- 🌡️ Température > 80°C

## 🔧 Installation

```bash
# Prérequis
opkg update
opkg install luci-base rpcd

# RustDesk (optionnel)
opkg install rustdesk

# Installation
git clone https://github.com/gkerma/luci-app-system-hub.git
cd luci-app-system-hub
make install

# Redémarrer
/etc/init.d/rpcd restart
```

## 🎨 Interface Utilisateur

### Thème Indigo

- **Couleur principale** : Gradient indigo (#6366f1 → #8b5cf6)
- **Dark mode** : Fond sombre professionnel
- **Typography** : Inter pour l'UI, JetBrains Mono pour les données
- **Responsive** : Adapté mobile/tablette

### Navigation

```
Services → System Hub
    ├── Overview        (vue d'ensemble)
    ├── Composants      (gestion services)
    ├── Santé           (health reports)
    ├── Assistance      (RustDesk)
    ├── Diagnostics     (collecte données)
    ├── Logs            (logs unifiés)
    └── Paramètres      (configuration)
```

## 🔗 Ressources

- **GitHub** : [github.com/gkerma/luci-app-system-hub](https://github.com/gkerma/luci-app-system-hub)
- **Démo** : [cybermind.fr/demos/system-hub](https://cybermind.fr/demos/system-hub)
- **RustDesk** : [rustdesk.com](https://rustdesk.com)

## 🎬 Conclusion

**System Hub** transforme l'administration OpenWrt en une expérience unifiée et professionnelle. Plus besoin de jongler entre multiples interfaces : tout est centralisé, monitoré et accessible.

Avec l'intégration RustDesk, le support à distance devient simple et sécurisé. Les diagnostics automatisés réduisent le temps de résolution des problèmes.

> *"La complexité est l'ennemi de l'exécution."* — Tony Robbins

System Hub simplifie la complexité pour vous permettre de vous concentrer sur l'essentiel.

---

*Dashboard créé par [Gandalf @ CyberMind.fr](https://cybermind.fr) - Licence Apache-2.0*
