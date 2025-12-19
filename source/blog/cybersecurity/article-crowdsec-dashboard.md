---
title: "LuCI CrowdSec Dashboard : Surveillance de sécurité en temps réel pour OpenWrt"
date: 2025-12-19 17:22:00
author: Gandalf
tags: [crowdsec, openwrt, luci, cybersecurity, open-source, dashboard]
categories: [Projets, Sécurité]
image: /images/crowdsec-dashboard-hero.png
description: "Présentation de luci-app-crowdsec-dashboard, une interface de surveillance moderne et responsive pour monitorer CrowdSec directement depuis votre routeur OpenWrt."
---

# LuCI CrowdSec Dashboard : La sécurité de votre réseau en un coup d'œil

Après plusieurs années à utiliser [CrowdSec](https://crowdsec.net/) sur mes routeurs OpenWrt, j'ai ressenti le besoin d'avoir une **interface visuelle** pour surveiller l'activité de sécurité sans avoir à me connecter en SSH et taper des commandes `cscli`. C'est ainsi qu'est né **luci-app-crowdsec-dashboard**.

<div class="demo-banner">
🎮 <strong>Démo interactive disponible :</strong> <a href="https://cybermind.fr/apps/crowdsec-dashboard/">Essayez le dashboard</a>
</div>

## Le problème : CrowdSec sans dashboard sur OpenWrt

CrowdSec est un excellent IPS collaboratif open-source, mais ses options de visualisation posent problème sur les routeurs embarqués :

- **Metabase** nécessite Docker et ~2GB de RAM — incompatible avec la plupart des routeurs
- La commande `cscli dashboard` est **dépréciée** depuis la version 1.7.0
- La **Console CrowdSec** cloud est pratique mais nécessite une connexion externe
- L'interface **luci-app-crowdsec-firewall-bouncer** existante ne fait que configurer le bouncer

Résultat : pour voir ce qui se passe, il faut systématiquement passer par le terminal :

```bash
cscli decisions list
cscli alerts list
cscli metrics
```

## La solution : Un dashboard natif LuCI

J'ai développé **luci-app-crowdsec-dashboard**, un package OpenWrt qui ajoute une interface complète directement dans LuCI :

![Dashboard Overview](/images/crowdsec-dashboard-overview.png)

### Fonctionnalités principales

#### 📊 Vue d'ensemble (Overview)

- **Statistiques en temps réel** : bans actifs, alertes 24h, bouncers connectés
- **Top scénarios** : visualisation des attaques les plus fréquentes
- **Top pays** : répartition géographique des menaces avec drapeaux
- **Timeline des alertes** : fil d'activité des dernières détections
- **Tableau des décisions** : liste des IP bannies avec actions rapides

#### 🚫 Gestion des décisions

- Recherche et filtrage par IP, scénario, pays
- Tri multi-colonnes
- **Actions bulk** : débannir plusieurs IP en une fois
- **Ajout manuel** : bannir une IP avec durée et raison personnalisées
- Export des données

#### ⚠️ Historique des alertes

- Consultation de toutes les alertes passées
- Statistiques agrégées par scénario
- Possibilité de bannir directement depuis une alerte
- Pagination pour les gros volumes

#### 📈 Métriques détaillées

- État des **bouncers** enregistrés
- **Machines** connectées à la LAPI
- **Hub status** : collections, parsers, scénarios installés
- Métriques **Prometheus** brutes (acquisition, buckets, etc.)

## Architecture technique

Le dashboard utilise l'architecture standard LuCI avec quelques spécificités :

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   LuCI Views    │────▶│   RPCD Backend  │────▶│     cscli       │
│   (JavaScript)  │     │   (Shell script)│     │   (CrowdSec)    │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                       │
        ▼                       ▼
┌─────────────────┐     ┌─────────────────┐
│   ubus RPC      │     │   JSON output   │
│   (WebSocket)   │     │   (-o json)     │
└─────────────────┘     └─────────────────┘
```

### Backend RPCD

Le cœur du système est un script shell (`/usr/libexec/rpcd/crowdsec`) qui expose les commandes `cscli` via ubus :

```bash
# Exemple d'appel interne
cscli decisions list -o json
cscli alerts list -o json --limit 50
cscli metrics -o json
```

Les méthodes exposées :
- `decisions` / `alerts` / `metrics` — Lecture des données
- `bouncers` / `machines` / `hub` — État des composants
- `status` — Santé des services
- `ban` / `unban` — Actions sur les IP

### Frontend JavaScript

Les vues utilisent le framework LuCI client-side avec :
- **Polling automatique** toutes les 30-60 secondes
- **Rendu dynamique** sans rechargement de page
- **Gestion d'état** locale pour filtres et tri

## Design : Un thème cybersecurity industriel

J'ai voulu créer une interface qui **respire la sécurité** sans tomber dans le cliché du "hacker movie". Le thème s'inspire des dashboards de SOC (Security Operations Center) :

- **Palette sombre** avec fond #0a0e14 pour réduire la fatigue visuelle
- **Accent vert cyan** (#00d4aa) pour les éléments positifs
- **Rouge corail** (#ff6b6b) pour les alertes et bans
- **Typographie monospace** (JetBrains Mono) pour les données techniques
- **Animations subtiles** : shimmer sur les barres, pulse sur les statuts

```css
:root {
    --cs-bg-primary: #0a0e14;
    --cs-accent-green: #00d4aa;
    --cs-accent-red: #ff6b6b;
    --cs-font-mono: 'JetBrains Mono', monospace;
}
```

Le design est **full responsive** : utilisable sur desktop, tablette, et même smartphone pour un check rapide.

## Installation

### Depuis les sources

```bash
# Cloner dans l'environnement de build OpenWrt
cd ~/openwrt/feeds/luci/applications/
git clone https://github.com/gkerma/luci-app-crowdsec-dashboard.git

# Compiler
cd ~/openwrt
./scripts/feeds update -a && ./scripts/feeds install -a
make menuconfig  # LuCI > Applications > luci-app-crowdsec-dashboard
make package/luci-app-crowdsec-dashboard/compile V=s
```

### Installation manuelle

```bash
# Transférer le .ipk sur le routeur
scp luci-app-crowdsec-dashboard_*.ipk root@router:/tmp/

# Installer
opkg install /tmp/luci-app-crowdsec-dashboard_*.ipk
/etc/init.d/rpcd restart
/etc/init.d/uhttpd restart
```

### Prérequis

- OpenWrt 21.02+
- CrowdSec Security Engine (`crowdsec`)
- CrowdSec Firewall Bouncer (recommandé)
- LuCI

## Démo interactive

Avant d'installer sur votre routeur, vous pouvez **tester l'interface** avec des données simulées :

👉 **[https://cybermind.fr/apps/crowdsec-dashboard/](https://cybermind.fr/apps/crowdsec-dashboard/)**

La démo inclut :
- Navigation entre les 4 vues
- Données fictives mais réalistes
- Toutes les interactions (recherche, tri, modales)
- Responsive design

## Retours et contributions

Le projet est open-source sous licence Apache-2.0. Les contributions sont bienvenues :

- 🐛 **Issues** : Signaler un bug ou suggérer une amélioration
- 🔀 **Pull Requests** : Code, traductions, documentation
- ⭐ **Star** : Si le projet vous est utile !

**Repository GitHub** : [github.com/gkerma/luci-app-crowdsec-dashboard](https://github.com/gkerma/luci-app-crowdsec-dashboard)

## Conclusion

Avec **luci-app-crowdsec-dashboard**, la surveillance de CrowdSec sur OpenWrt devient enfin **visuelle et accessible**. Plus besoin de terminal pour vérifier si votre routeur fait bien son travail de protection.

Le dashboard ne remplace pas la puissance de `cscli` pour les opérations avancées, mais il offre une **fenêtre instantanée** sur la santé sécuritaire de votre réseau — exactement ce dont on a besoin au quotidien.

---

*Vous utilisez CrowdSec sur OpenWrt ? Partagez votre configuration dans les commentaires !*

<style>
.demo-banner {
    background: linear-gradient(135deg, #151b23, #1a2231);
    border: 1px solid #00d4aa;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 24px 0;
    font-size: 16px;
}
.demo-banner a {
    color: #00d4aa;
    font-weight: 600;
}
</style>
