---
title: "Netdata Dashboard pour OpenWrt"
description: "Dashboard de monitoring système temps réel inspiré de Netdata, directement intégré à LuCI pour surveiller votre routeur OpenWrt."
layout: app
date: 2025-12-19
updated: 2025-12-19
author: Gandalf
app:
  name: luci-app-netdata-dashboard
  version: 1.0.0
  license: Apache-2.0
  repo: https://github.com/gkerma/luci-app-netdata-dashboard
  demo: true
tags: [netdata, openwrt, luci, monitoring, dashboard, open-source, system]
cover: /images/netdata-dashboard-hero.png
embed_url: "/apps/netdata-dashboard/demo.html"
---

<div class="app-hero">
  <div class="app-hero-content">
    <div class="app-badge">📊 Open Source</div>
    <h1>Netdata Dashboard</h1>
    <p class="app-tagline">Monitoring système temps réel pour OpenWrt</p>
    <p class="app-description">
      Une interface de monitoring moderne et légère inspirée de Netdata, 
      directement intégrée à LuCI. Surveillez CPU, mémoire, réseau, disques 
      et processus sans compromettre les performances de votre routeur.
    </p>
    <div class="app-actions">
      <a href="#demo" class="btn btn-primary">🎮 Essayer la démo</a>
      <a href="https://github.com/gkerma/luci-app-netdata-dashboard" class="btn btn-secondary" target="_blank">
        <svg viewBox="0 0 16 16" width="16" height="16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
        GitHub
      </a>
    </div>
  </div>
  <div class="app-hero-image">
    <img src="/images/netdata-dashboard-hero.png" alt="Netdata Dashboard Preview">
  </div>
</div>

---

## 🎯 Pourquoi ce dashboard ?

| Solution | RAM requise | Stockage | Configuration |
|----------|-------------|----------|---------------|
| **Netdata complet** | ~200 MB | ~100 MB | Moyenne |
| luci-app-statistics | ~30 MB | ~20 MB | Complexe |
| **Ce dashboard** | **< 1 MB** | **50 KB** | **Zéro** |

Sur un routeur avec 128 MB de RAM, le monitoring classique n'est pas une option. Ce dashboard offre l'expérience Netdata sans le poids.

---

## ✨ Fonctionnalités

<div class="features-grid">
  <div class="feature-card">
    <div class="feature-icon">⚡</div>
    <h3>CPU</h3>
    <p>Jauge animée, sparkline historique, load average 1/5/15 min, fréquence CPU si disponible.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🧠</div>
    <h3>Mémoire</h3>
    <p>Barre empilée (used/buffers/cached/free), pourcentages, détails swap.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">💾</div>
    <h3>Disques</h3>
    <p>Usage par point de montage avec barres colorées et statistiques I/O.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🌐</div>
    <h3>Réseau</h3>
    <p>Trafic RX/TX par interface, état des liens, connection tracking.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🌡️</div>
    <h3>Températures</h3>
    <p>Lecture des thermal zones et capteurs hwmon avec code couleur.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">⚙️</div>
    <h3>Processus</h3>
    <p>Liste complète avec PID, user, commande, mémoire et état.</p>
  </div>
</div>

---

## 🎮 Démo interactive {#demo}

<p class="demo-intro">
  Testez l'interface avec des données simulées. Navigation, jauges animées, 
  sparklines temps réel — tout fonctionne comme sur un vrai routeur.
</p>

<div class="demo-container">
  <div class="demo-toolbar">
    <span class="demo-badge">💡 Mode démo — Données simulées</span>
    <a href="/apps/netdata-dashboard/demo.html" target="_blank" class="btn btn-sm">Ouvrir en plein écran ↗</a>
  </div>
  <iframe 
    src="/apps/netdata-dashboard/demo.html" 
    width="100%" 
    height="700" 
    frameborder="0"
    style="border-radius: 8px; border: 1px solid #30363d;">
  </iframe>
</div>

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    LuCI JavaScript                       │
│              (realtime.js, system.js, etc.)             │
└───────────────────────────┬─────────────────────────────┘
                            │ ubus RPC (JSON)
                            ▼
┌─────────────────────────────────────────────────────────┐
│                    RPCD Backend                          │
│               /usr/libexec/rpcd/netdata                 │
└───────────────────────────┬─────────────────────────────┘
                            │ reads
                            ▼
┌─────────────────────────────────────────────────────────┐
│                   Linux /proc & /sys                     │
│     /proc/stat  /proc/meminfo  /sys/class/thermal       │
└─────────────────────────────────────────────────────────┘
```

**Aucun daemon** en arrière-plan, **aucune base de données** — les métriques sont collectées à la demande via des scripts shell légers.

---

## 📦 Installation

### Prérequis

- OpenWrt 21.02 ou supérieur
- LuCI (interface web OpenWrt)
- ~50 KB d'espace disque

### Depuis les sources

```bash
# Dans votre environnement de build OpenWrt
cd ~/openwrt/feeds/luci/applications/
git clone https://github.com/gkerma/luci-app-netdata-dashboard.git

# Mettre à jour les feeds et compiler
cd ~/openwrt
./scripts/feeds update -a && ./scripts/feeds install -a
make menuconfig  # LuCI > Applications > luci-app-netdata-dashboard
make package/luci-app-netdata-dashboard/compile V=s
```

### Installation manuelle du .ipk

```bash
# Transférer le package sur votre routeur
scp luci-app-netdata-dashboard_1.0.0-1_all.ipk root@192.168.1.1:/tmp/

# Se connecter et installer
ssh root@192.168.1.1
opkg install /tmp/luci-app-netdata-dashboard_1.0.0-1_all.ipk

# Redémarrer les services
/etc/init.d/rpcd restart
```

### Accès au dashboard

Après installation, le dashboard est accessible dans LuCI :

**Status → Netdata Dashboard**

---

## 🎨 Design

Thème sombre inspiré des interfaces de monitoring professionnelles :

| Élément | Valeur |
|---------|--------|
| Background | `#0d1117` (noir GitHub) |
| Cards | `#161b22` |
| Accent principal | `#3fb950` (vert) |
| Accent secondaire | `#58a6ff` (bleu) |
| Warning | `#d29922` (orange) |
| Danger | `#f85149` (rouge) |
| Typographie données | JetBrains Mono |
| Typographie UI | Inter |

Interface **100% responsive** pour consultation sur mobile et tablette.

---

## 📊 Vues disponibles

### Real-time
Vue principale avec quick stats, jauges CPU/mémoire animées, sparklines historiques, trafic réseau et usage disque.

### System
Informations système détaillées : hostname, modèle, kernel, architecture, uptime avec compteur, températures.

### Network
Liste des interfaces avec état, IP, vitesse, compteurs RX/TX, connection tracking.

### Processes
Comptage par état, liste des processus avec tri, top consommateurs mémoire.

---

## 📋 Roadmap

- [x] Vue Real-time avec jauges et sparklines
- [x] Vue System avec uptime et températures
- [x] Vue Network avec statistiques interfaces
- [x] Vue Processes avec liste et tri
- [ ] Historique 24h (stockage flash optionnel)
- [ ] Alertes configurables (seuils CPU/RAM/temp)
- [ ] Export CSV/JSON des métriques
- [ ] Mode kiosk pour affichage dédié
- [ ] Graphiques temporels (7j/30j)
- [ ] Intégration MQTT pour push metrics

---

## 🤝 Contribuer

Le projet est open-source sous licence **Apache-2.0**. Les contributions sont bienvenues !

<div class="contribute-options">
  <a href="https://github.com/gkerma/luci-app-netdata-dashboard/issues" class="contribute-card">
    <span class="contribute-icon">🐛</span>
    <span class="contribute-title">Signaler un bug</span>
  </a>
  <a href="https://github.com/gkerma/luci-app-netdata-dashboard/pulls" class="contribute-card">
    <span class="contribute-icon">🔀</span>
    <span class="contribute-title">Pull Request</span>
  </a>
  <a href="https://github.com/gkerma/luci-app-netdata-dashboard" class="contribute-card">
    <span class="contribute-icon">⭐</span>
    <span class="contribute-title">Star le projet</span>
  </a>
</div>

---

## 📚 Ressources

- [Documentation OpenWrt](https://openwrt.org/docs/start)
- [Wiki LuCI Development](https://openwrt.org/docs/guide-developer/luci)
- [Netdata (inspiration)](https://netdata.cloud/)
- [Article de blog : Présentation du dashboard](/blog/2024/12/luci-netdata-dashboard/)

---

<div class="app-footer">
  <p>
    Développé par <a href="https://cybermind.fr">Gandalf @ CyberMind.fr</a><br>
    <small>Consultant Cybersécurité • Passionné d'embarqué</small>
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
  background: linear-gradient(135deg, #3fb95020, #58a6ff20);
  border: 1px solid #3fb95040;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  color: #3fb950;
  margin-bottom: 16px;
}

.app-hero h1 {
  font-size: 48px;
  margin: 0 0 12px 0;
  background: linear-gradient(135deg, #f0f6fc, #8b949e);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.app-tagline {
  font-size: 20px;
  color: #8b949e;
  margin: 0 0 16px 0;
}

.app-description {
  font-size: 16px;
  line-height: 1.7;
  color: #6e7681;
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
  background: #3fb950;
  color: #0d1117;
}

.btn-primary:hover {
  background: #56d364;
  box-shadow: 0 0 20px #3fb95040;
}

.btn-secondary {
  background: #21262d;
  color: #f0f6fc;
  border: 1px solid #30363d;
}

.btn-secondary:hover { border-color: #3fb950; }

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
  background: linear-gradient(145deg, #161b22, #1a2231);
  border: 1px solid #30363d;
  border-radius: 12px;
  padding: 24px;
  transition: all 0.3s;
}

.feature-card:hover {
  border-color: #3fb95040;
  transform: translateY(-4px);
}

.feature-icon {
  font-size: 32px;
  margin-bottom: 12px;
}

.feature-card h3 {
  font-size: 18px;
  margin: 0 0 8px 0;
  color: #f0f6fc;
}

.feature-card p {
  font-size: 14px;
  color: #8b949e;
  margin: 0;
  line-height: 1.6;
}

/* Demo */
.demo-intro {
  text-align: center;
  color: #8b949e;
  margin-bottom: 24px;
}

.demo-container {
  background: #0d1117;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid #30363d;
}

.demo-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  background: #161b22;
  border-bottom: 1px solid #30363d;
}

.demo-badge {
  font-size: 13px;
  color: #d29922;
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
  background: #161b22;
  border: 1px solid #30363d;
  border-radius: 12px;
  text-decoration: none;
  transition: all 0.2s;
}

.contribute-card:hover {
  border-color: #3fb950;
  transform: translateY(-2px);
}

.contribute-icon { font-size: 28px; }

.contribute-title {
  font-size: 14px;
  font-weight: 600;
  color: #f0f6fc;
}

/* Footer */
.app-footer {
  text-align: center;
  padding: 40px 0;
  margin-top: 40px;
  border-top: 1px solid #30363d;
  color: #6e7681;
}

.app-footer a { color: #3fb950; }
</style>
