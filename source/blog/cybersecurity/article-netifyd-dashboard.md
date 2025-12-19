---
title: "LuCI Netifyd Dashboard : Deep Packet Inspection pour OpenWrt"
date: 2025-12-19
author: Gandalf
tags: [netifyd, openwrt, luci, dpi, network-intelligence, dashboard, security]
categories: [Projets, Réseau]
image: /images/netifyd-dashboard-hero.png
description: "Dashboard de Network Intelligence avec Deep Packet Inspection pour visualiser applications, protocoles et appareils sur votre réseau OpenWrt."
---

# Netifyd Dashboard : Voyez ce qui transite sur votre réseau

Savez-vous vraiment ce qui passe sur votre réseau ? Quelles applications consomment votre bande passante ? Quels appareils communiquent avec l'extérieur ?

**Netifyd** est un moteur de Deep Packet Inspection (DPI) open-source capable d'identifier plus de 300 protocoles et 1000+ applications. J'ai créé **luci-app-netifyd-dashboard** pour visualiser ces données directement dans LuCI.

<div class="demo-banner">
🔍 <strong>Démo interactive :</strong> <a href="https://cybermind.fr/apps/netifyd-dashboard/">Essayez le dashboard</a>
</div>

## Qu'est-ce que le Deep Packet Inspection ?

Le DPI analyse le contenu des paquets réseau pour identifier les applications, au-delà des simples ports. Par exemple :

| Port 443 classique | Avec DPI |
|-------------------|----------|
| HTTPS | Netflix |
| HTTPS | YouTube |
| HTTPS | Zoom |
| HTTPS | Microsoft Teams |

Sans DPI, tout le trafic HTTPS est indiscernable. Avec Netifyd, vous savez exactement quelle application utilise votre connexion.

## Fonctionnalités du dashboard

### 📊 Vue d'ensemble

![Overview](/images/netifyd-dashboard-overview.png)

- **Flows actifs** : Nombre de connexions en temps réel
- **Applications détectées** : Identifiées par le moteur DPI
- **Appareils** : Découverte automatique sur le réseau
- **Bande passante** : Totaux RX/TX
- **Distribution des protocoles** : Graphique donut TCP/UDP/QUIC

### 🔄 Flux réseau

Table des connexions actives avec :
- IP source/destination et ports
- Application détectée (YouTube, Netflix, Zoom...)
- Catégorie (Streaming, VoIP, Social, Gaming...)
- Trafic en temps réel

### 📱 Applications

Classement des applications par consommation :
- Pourcentage du trafic total
- Nombre de flux par application
- Catégorisation automatique
- Icônes reconnaissables

### 💻 Appareils

Découverte automatique des appareils :
- Identification du fabricant (OUI MAC)
- Résolution des hostnames (DHCP)
- Interface de connexion
- Dernière activité

## Architecture technique

```
┌─────────────────────────────────────────────────────────┐
│                    LuCI Dashboard                        │
│          (overview.js, flows.js, devices.js)            │
└───────────────────────────┬─────────────────────────────┘
                            │ ubus RPC
                            ▼
┌─────────────────────────────────────────────────────────┐
│                    RPCD Backend                          │
│            /usr/libexec/rpcd/netifyd-dashboard          │
└───────────────────────────┬─────────────────────────────┘
                            │ reads
                            ▼
┌─────────────────────────────────────────────────────────┐
│                     Netifyd Agent                        │
│              Deep Packet Inspection Engine               │
└───────────────────────────┬─────────────────────────────┘
                            │ inspects
                            ▼
┌─────────────────────────────────────────────────────────┐
│                   Network Interfaces                     │
│                 br-lan, eth0, wlan0...                  │
└─────────────────────────────────────────────────────────┘
```

Le dashboard ne fait **aucune inspection lui-même** — il consomme les données produites par le daemon Netifyd qui tourne en arrière-plan.

## Design : Thème Network Intelligence

Interface inspirée des outils de SOC et d'analyse réseau :

| Élément | Couleur |
|---------|---------|
| Background | `#0a0f1a` (noir profond) |
| Accent principal | `#8b5cf6` (violet) |
| Accent secondaire | `#3b82f6` (bleu) |
| Streaming | `#ec4899` (rose) |
| VoIP | `#10b981` (vert) |
| Network | `#f59e0b` (orange) |

Les catégories sont colorées pour identifier rapidement le type de trafic.

## Installation

### Prérequis

```bash
# Installer Netifyd
opkg update
opkg install netifyd

# Activer et démarrer
/etc/init.d/netifyd enable
/etc/init.d/netifyd start
```

### Installer le dashboard

```bash
# Depuis les sources OpenWrt
cd ~/openwrt/feeds/luci/applications/
git clone https://github.com/gkerma/luci-app-netifyd-dashboard.git

./scripts/feeds update -a && ./scripts/feeds install -a
make package/luci-app-netifyd-dashboard/compile V=s
```

### Installation manuelle

```bash
scp luci-app-netifyd-dashboard_*.ipk root@router:/tmp/
ssh root@router "opkg install /tmp/luci-app-netifyd-dashboard_*.ipk"
/etc/init.d/rpcd restart
```

### Accès

**Status → Netifyd Dashboard**

## Cas d'usage

### 🏠 Réseau domestique
- Identifier les gros consommateurs de bande passante
- Détecter les appareils inconnus
- Surveiller l'activité des enfants (streaming, gaming)

### 🏢 PME / Bureau
- Audit de l'utilisation du réseau
- Détection d'applications non autorisées
- Planification de capacité

### 🔒 Sécurité
- Détecter les tunnels suspects
- Identifier les connexions P2P
- Repérer les communications vers des IP suspectes

## Comparaison avec ntopng

| Fonctionnalité | ntopng | Ce dashboard |
|----------------|--------|--------------|
| DPI | ✅ nDPI | ✅ Netifyd |
| RAM | ~500 MB | < 50 MB |
| Interface | Web séparée | Intégré LuCI |
| Licence | GPLv3 (limitations) | Apache-2.0 |
| Base de données | Redis/InfluxDB | Aucune |

Pour un routeur avec ressources limitées, ce dashboard offre l'essentiel sans le poids.

## Démo interactive

Testez l'interface complète avec des données simulées :

👉 **[https://cybermind.fr/apps/netifyd-dashboard/](https://cybermind.fr/apps/netifyd-dashboard/)**

## Roadmap

- [x] Vue Overview avec stats et graphiques
- [x] Table des flux en temps réel
- [x] Liste des applications détectées
- [x] Découverte des appareils
- [ ] Historique sur 24h/7j
- [ ] Alertes sur applications spécifiques
- [ ] Blocage d'applications (intégration firewall)
- [ ] Export des données
- [ ] Graphiques temporels

## Contribuer

Projet open-source sous licence Apache-2.0 :

**GitHub** : [github.com/gkerma/luci-app-netifyd-dashboard](https://github.com/gkerma/luci-app-netifyd-dashboard)

## Conclusion

Avec **luci-app-netifyd-dashboard**, la visibilité réseau devient accessible à tous. Plus besoin d'outils complexes ou coûteux pour savoir ce qui transite sur votre réseau — le DPI est maintenant à portée de clic dans LuCI.

---

*Vous utilisez déjà Netifyd ou un autre outil DPI ? Partagez votre expérience dans les commentaires !*

<style>
.demo-banner {
    background: linear-gradient(135deg, #111827, #1f2937);
    border: 1px solid #8b5cf6;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 24px 0;
    font-size: 16px;
}
.demo-banner a {
    color: #8b5cf6;
    font-weight: 600;
}
</style>
