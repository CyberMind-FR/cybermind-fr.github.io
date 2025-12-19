---
title: "Netifyd Dashboard pour OpenWrt"
description: "Dashboard de Network Intelligence avec Deep Packet Inspection pour visualiser applications, protocoles et appareils sur votre réseau OpenWrt."
layout: app
date: 2024-12-19
updated: 2024-12-19
author: Gandalf
app:
  name: luci-app-netifyd-dashboard
  version: 1.0.0
  license: Apache-2.0
  repo: https://github.com/gkerma/luci-app-netifyd-dashboard
  demo: true
tags: [netifyd, openwrt, luci, dpi, network-intelligence, dashboard, security]
image: /images/netifyd-dashboard-hero.png
---

<div class="app-hero">
  <div class="app-hero-content">
    <div class="app-badge">🔍 Deep Packet Inspection</div>
    <h1>Netifyd Dashboard</h1>
    <p class="app-tagline">Network Intelligence pour OpenWrt</p>
    <p class="app-description">
      Visualisez en temps réel les applications, protocoles et appareils 
      sur votre réseau grâce au Deep Packet Inspection. Identifiez Netflix, 
      YouTube, Zoom et 1000+ applications au-delà des simples ports.
    </p>
    <div class="app-actions">
      <a href="#demo" class="btn btn-primary">🎮 Essayer la démo</a>
      <a href="https://github.com/gkerma/luci-app-netifyd-dashboard" class="btn btn-secondary" target="_blank">
        <svg viewBox="0 0 16 16" width="16" height="16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
        GitHub
      </a>
    </div>
  </div>
  <div class="app-hero-image">
    <img src="/images/netifyd-dashboard-hero.png" alt="Netifyd Dashboard Preview">
  </div>
</div>

---

## 🎯 Pourquoi le Deep Packet Inspection ?

Sans DPI, tout le trafic HTTPS est indiscernable :

| Port 443 classique | Avec Netifyd DPI |
|-------------------|------------------|
| HTTPS | 🎬 Netflix |
| HTTPS | 📺 YouTube |
| HTTPS | 📹 Zoom |
| HTTPS | 💬 Discord |
| HTTPS | 🎮 Steam |

Netifyd identifie **300+ protocoles** et **1000+ applications** en analysant le contenu des paquets, pas seulement les ports.

---

## ✨ Fonctionnalités

<div class="features-grid">
  <div class="feature-card">
    <div class="feature-icon">🔄</div>
    <h3>Flux réseau</h3>
    <p>Connexions actives en temps réel avec source, destination, application et catégorie.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">📱</div>
    <h3>Applications</h3>
    <p>Détection automatique : Netflix, YouTube, Zoom, Teams, Discord, Steam, Spotify...</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">💻</div>
    <h3>Appareils</h3>
    <p>Découverte automatique avec identification du fabricant et hostname DHCP.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">📊</div>
    <h3>Protocoles</h3>
    <p>Distribution TCP/UDP/QUIC avec graphiques donut interactifs.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🏷️</div>
    <h3>Catégories</h3>
    <p>Classification automatique : Streaming, VoIP, Social, Gaming, Network...</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">📈</div>
    <h3>Bande passante</h3>
    <p>Trafic RX/TX par application avec pourcentages et barres de progression.</p>
  </div>
</div>

---

## 🎮 Démo interactive {#demo}

<p class="demo-intro">
  Explorez l'interface avec des données simulées. Flux réseau, applications détectées, 
  appareils découverts — tout fonctionne comme sur un vrai routeur avec Netifyd.
</p>

<div class="demo-container">
  <div class="demo-toolbar">
    <span class="demo-badge">🔍 Mode démo — DPI simulé</span>
    <a href="/apps/netifyd-dashboard/demo.html" target="_blank" class="btn btn-sm">Ouvrir en plein écran ↗</a>
  </div>
  <iframe 
    src="/apps/netifyd-dashboard/demo.html" 
    width="100%" 
    height="700" 
    frameborder="0"
    style="border-radius: 8px; border: 1px solid #374151;">
  </iframe>
</div>

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    LuCI Dashboard                        │
│         (overview.js, flows.js, applications.js)        │
└───────────────────────────┬─────────────────────────────┘
                            │ ubus RPC (JSON)
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
│           /var/run/netifyd/status.json                  │
└───────────────────────────┬─────────────────────────────┘
                            │ inspects
                            ▼
┌─────────────────────────────────────────────────────────┐
│                   Network Interfaces                     │
│                 br-lan, eth0, wlan0...                  │
└─────────────────────────────────────────────────────────┘
```

Le dashboard **ne fait aucune inspection** — il visualise les données produites par le daemon Netifyd.

---

## 📦 Installation

### Prérequis

- OpenWrt 21.02 ou supérieur
- **Netifyd** installé et actif
- LuCI (interface web OpenWrt)

```bash
# Installer Netifyd
opkg update
opkg install netifyd

# Activer et démarrer
/etc/init.d/netifyd enable
/etc/init.d/netifyd start
```

### Depuis les sources

```bash
# Dans votre environnement de build OpenWrt
cd ~/openwrt/feeds/luci/applications/
git clone https://github.com/gkerma/luci-app-netifyd-dashboard.git

# Mettre à jour les feeds et compiler
cd ~/openwrt
./scripts/feeds update -a && ./scripts/feeds install -a
make menuconfig  # LuCI > Applications > luci-app-netifyd-dashboard
make package/luci-app-netifyd-dashboard/compile V=s
```

### Installation manuelle du .ipk

```bash
# Transférer le package sur votre routeur
scp luci-app-netifyd-dashboard_1.0.0-1_all.ipk root@192.168.1.1:/tmp/

# Se connecter et installer
ssh root@192.168.1.1
opkg install /tmp/luci-app-netifyd-dashboard_1.0.0-1_all.ipk

# Redémarrer les services
/etc/init.d/rpcd restart
```

### Accès au dashboard

Après installation : **Status → Netifyd Dashboard**

---

## 🎨 Design

Thème Network Intelligence inspiré des outils de SOC :

| Élément | Valeur |
|---------|--------|
| Background | `#0a0f1a` (noir profond) |
| Cards | `#111827` |
| Accent principal | `#8b5cf6` (violet) |
| Accent secondaire | `#3b82f6` (bleu) |
| Streaming | `#ec4899` (rose) |
| VoIP | `#10b981` (vert) |
| Network | `#f59e0b` (orange) |
| Typographie données | JetBrains Mono |
| Typographie UI | Inter |

**Catégories colorées** pour identifier rapidement le type de trafic.

---

## 📊 Vues disponibles

### Overview
Vue principale avec quick stats, distribution des protocoles (donut), top applications par bande passante.

### Flows
Table des connexions actives avec protocole, source/destination, application détectée, catégorie et trafic.

### Applications
Liste des applications détectées avec nombre de flux, trafic total et pourcentage.

### Devices
Grille des appareils découverts avec hostname, fabricant, IP, MAC et interface.

---

## 🔧 Configuration Netifyd

Fichier `/etc/netifyd.conf` :

```ini
# Interfaces à surveiller
[capture]
interface = br-lan
interface = eth0.2

# Activer le suivi des flux
[flow]
enable = yes
hash_buckets = 1999

# Format de sortie
[output]
json = yes
```

---

## 📋 Roadmap

- [x] Vue Overview avec stats et graphiques donut
- [x] Vue Flows avec table temps réel
- [x] Vue Applications avec tri par trafic
- [x] Vue Devices avec découverte automatique
- [ ] Historique 24h/7j (stockage SQLite optionnel)
- [ ] Alertes sur applications spécifiques
- [ ] Intégration firewall (blocage d'applications)
- [ ] Export CSV/JSON des données
- [ ] Graphiques temporels
- [ ] Mode kiosk pour affichage dédié

---

## 🤝 Contribuer

Le projet est open-source sous licence **Apache-2.0**. Les contributions sont bienvenues !

<div class="contribute-options">
  <a href="https://github.com/gkerma/luci-app-netifyd-dashboard/issues" class="contribute-card">
    <span class="contribute-icon">🐛</span>
    <span class="contribute-title">Signaler un bug</span>
  </a>
  <a href="https://github.com/gkerma/luci-app-netifyd-dashboard/pulls" class="contribute-card">
    <span class="contribute-icon">🔀</span>
    <span class="contribute-title">Pull Request</span>
  </a>
  <a href="https://github.com/gkerma/luci-app-netifyd-dashboard" class="contribute-card">
    <span class="contribute-icon">⭐</span>
    <span class="contribute-title">Star le projet</span>
  </a>
</div>

---

## 📚 Ressources

- [Documentation Netifyd](https://www.netify.ai/developer/netify-agent)
- [OpenWrt Wiki - Netifyd](https://openwrt.org/docs/guide-user/services/network_monitoring/netifyd)
- [Netify DPI Signatures](https://gitlab.com/netify.ai/public/netify-agent)
- [Article de blog : Présentation du dashboard](/blog/cybersecurity/luci-netifyd-dashboard/)

---

<div class="app-footer">
  <p>
    Développé par <a href="https://cybermind.fr">Gandalf @ CyberMind.fr</a><br>
    <small>Consultant Cybersécurité • Passionné de Network Intelligence</small>
  </p>
</div>

<style>
/* App Hero */
.app-hero {
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: 40px;
  align-items: center;
  margin: 40px 0;
}

@media (max-width: 900px) {
  .app-hero { grid-template-columns: 1fr; }
}

.app-badge {
  display: inline-block;
  padding: 6px 12px;
  background: linear-gradient(135deg, #8b5cf620, #3b82f620);
  border: 1px solid #8b5cf640;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  color: #8b5cf6;
  margin-bottom: 16px;
}

.app-hero h1 {
  font-size: 48px;
  margin: 0 0 12px 0;
  background: linear-gradient(135deg, #f9fafb, #9ca3af);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.app-tagline {
  font-size: 20px;
  color: #9ca3af;
  margin: 0 0 16px 0;
}

.app-description {
  font-size: 16px;
  line-height: 1.7;
  color: #6b7280;
  margin-bottom: 24px;
}

.app-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s;
}

.btn-primary {
  background: #8b5cf6;
  color: white;
}

.btn-primary:hover {
  background: #a78bfa;
  box-shadow: 0 0 20px #8b5cf640;
}

.btn-secondary {
  background: #1f2937;
  color: #f9fafb;
  border: 1px solid #374151;
}

.btn-secondary:hover { border-color: #8b5cf6; }

.btn-sm {
  padding: 6px 12px;
  font-size: 13px;
}

.app-hero-image img {
  width: 100%;
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.4);
}

/* Features Grid */
.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin: 32px 0;
}

.feature-card {
  background: linear-gradient(145deg, #111827, #0a0f1a);
  border: 1px solid #374151;
  border-radius: 12px;
  padding: 24px;
  transition: all 0.3s;
}

.feature-card:hover {
  border-color: #8b5cf640;
  transform: translateY(-4px);
}

.feature-icon {
  font-size: 32px;
  margin-bottom: 12px;
}

.feature-card h3 {
  font-size: 18px;
  margin: 0 0 8px 0;
  color: #f9fafb;
}

.feature-card p {
  font-size: 14px;
  color: #9ca3af;
  margin: 0;
  line-height: 1.6;
}

/* Demo */
.demo-intro {
  text-align: center;
  color: #9ca3af;
  margin-bottom: 24px;
}

.demo-container {
  background: #0a0f1a;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid #374151;
}

.demo-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  background: #111827;
  border-bottom: 1px solid #374151;
}

.demo-badge {
  font-size: 13px;
  color: #8b5cf6;
}

/* Contribute */
.contribute-options {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  justify-content: center;
  margin: 24px 0;
}

.contribute-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 24px 32px;
  background: #111827;
  border: 1px solid #374151;
  border-radius: 12px;
  text-decoration: none;
  transition: all 0.2s;
}

.contribute-card:hover {
  border-color: #8b5cf6;
  transform: translateY(-2px);
}

.contribute-icon { font-size: 28px; }

.contribute-title {
  font-size: 14px;
  font-weight: 600;
  color: #f9fafb;
}

/* Footer */
.app-footer {
  text-align: center;
  padding: 40px 0;
  margin-top: 40px;
  border-top: 1px solid #374151;
  color: #6b7280;
}

.app-footer a { color: #8b5cf6; }
</style>
