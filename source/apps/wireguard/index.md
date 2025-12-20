---
title: "WireGuard Dashboard pour OpenWrt"
description: "Dashboard moderne pour visualiser vos tunnels WireGuard sur OpenWrt : interfaces, peers, trafic et configuration en temps réel."
layout: app
date: 2026-01-01
updated: 2026-01-01
author: Gandalf
app:
  name: luci-app-wireguard-dashboard
  version: 1.0.0
  license: Apache-2.0
  repo: https://github.com/gkerma/luci-app-wireguard-dashboard
  demo: true
image: /images/wireguard-dashboard-hero.png
embed_url: "/apps//wireguard/demo.html"
featured: true
github: https://github.com/gkerma/luci-app-wireguard-dashboard
---


<div class="app-hero">
  <div class="app-hero-content">
    <div class="app-badge">🔐 Secure VPN</div>
    <h1>WireGuard Dashboard</h1>
    <p class="app-tagline">VPN Monitoring pour OpenWrt</p>
    <p class="app-description">
      Visualisez vos tunnels VPN en temps réel : interfaces actives, peers connectés, 
      trafic et handshakes. Une interface moderne pour le protocole VPN le plus 
      rapide et sécurisé.
    </p>
    <div class="app-actions">
      <a href="#demo" class="btn btn-primary">🎮 Essayer la démo</a>
      <a href="https://github.com/gkerma/luci-app-wireguard-dashboard" class="btn btn-secondary" target="_blank">
        <svg viewBox="0 0 16 16" width="16" height="16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
        GitHub
      </a>
    </div>
  </div>
  <div class="app-hero-image">
    <img src="/images/wireguard-dashboard-hero.png" alt="WireGuard Dashboard Preview">
  </div>
</div>

---

## 🎯 Pourquoi WireGuard ?

| Protocole | Lignes de code | Performance | Sécurité |
|-----------|---------------|-------------|----------|
| OpenVPN | ~100,000 | Moyenne | Bonne |
| IPsec | ~400,000 | Variable | Complexe |
| **WireGuard** | **~4,000** | **Excellente** | **État de l'art** |

WireGuard utilise des primitives cryptographiques modernes (ChaCha20, Curve25519, BLAKE2s) et est intégré au noyau Linux depuis 5.6.

---

## ✨ Fonctionnalités

<div class="features-grid">
  <div class="feature-card">
    <div class="feature-icon">🌐</div>
    <h3>Interfaces</h3>
    <p>Liste des tunnels actifs avec clé publique, port, adresse IP et état.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">👥</div>
    <h3>Peers</h3>
    <p>Statut en temps réel, endpoint, allowed IPs, dernier handshake.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">📊</div>
    <h3>Traffic</h3>
    <p>Statistiques RX/TX par peer et par interface avec barres de progression.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">⚙️</div>
    <h3>Configuration</h3>
    <p>Affichage de la config au format WireGuard avec syntaxe colorée.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🔒</div>
    <h3>Sécurité</h3>
    <p>Clés privées jamais exposées. Lecture seule via RPCD authentifié.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🚀</div>
    <h3>Temps réel</h3>
    <p>Mise à jour automatique des handshakes et du trafic.</p>
  </div>
</div>

---

## 🎮 Démo interactive {#demo}

<p class="demo-intro">
  Explorez l'interface avec des données simulées. Interfaces, peers, trafic — 
  tout fonctionne comme sur un vrai routeur avec WireGuard.
</p>

<div class="demo-container">
  <div class="demo-toolbar">
    <span class="demo-badge">🔐 Mode démo — VPN simulé</span>
    <a href="/apps/wireguard-dashboard/demo.html" target="_blank" class="btn btn-sm">Ouvrir en plein écran ↗</a>
  </div>
  <iframe 
    src="/apps/wireguard-dashboard/demo.html" 
    width="100%" 
    height="700" 
    frameborder="0"
    style="border-radius: 8px; border: 1px solid #334155;">
  </iframe>
</div>

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    LuCI Dashboard                        │
│          (status.js, peers.js, traffic.js)              │
└───────────────────────────┬─────────────────────────────┘
                            │ ubus RPC (JSON)
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
│                  kmod-wireguard                          │
└─────────────────────────────────────────────────────────┘
```

Le backend utilise `wg show` pour interroger le module kernel en temps réel.

---

## 📦 Installation

### Prérequis

- OpenWrt 21.02 ou supérieur
- **WireGuard** installé et configuré
- LuCI (interface web OpenWrt)

```bash
# Installer WireGuard
opkg update
opkg install kmod-wireguard wireguard-tools

# Optionnel : support LuCI natif
opkg install luci-proto-wireguard
```

### Depuis les sources

```bash
# Dans votre environnement de build OpenWrt
cd ~/openwrt/feeds/luci/applications/
git clone https://github.com/gkerma/luci-app-wireguard-dashboard.git

# Mettre à jour les feeds et compiler
cd ~/openwrt
./scripts/feeds update -a && ./scripts/feeds install -a
make menuconfig  # LuCI > Applications > luci-app-wireguard-dashboard
make package/luci-app-wireguard-dashboard/compile V=s
```

### Installation manuelle du .ipk

```bash
# Transférer le package sur votre routeur
scp luci-app-wireguard-dashboard_1.0.0-1_all.ipk root@192.168.1.1:/tmp/

# Se connecter et installer
ssh root@192.168.1.1
opkg install /tmp/luci-app-wireguard-dashboard_1.0.0-1_all.ipk

# Redémarrer les services
/etc/init.d/rpcd restart
```

### Accès au dashboard

Après installation : **VPN → WireGuard Dashboard**

---

## 🎨 Design

Thème VPN Tunnel avec gradient cyan/bleu :

| Élément | Valeur |
|---------|--------|
| Background | `#030712` (noir profond) |
| Cards | `#0f172a` (slate) |
| Tunnel gradient | cyan → bleu → indigo |
| Active | `#10b981` (vert) |
| Idle | `#f59e0b` (orange) |
| Inactive | `#64748b` (gris) |
| Typographie données | JetBrains Mono |
| Typographie UI | Inter |

**Animations fluides** pour les indicateurs de statut et le flux du tunnel.

---

## 📊 Indicateurs de statut

| Indicateur | Signification | Handshake |
|------------|---------------|-----------|
| 🟢 **Active** | Communication récente | < 3 min |
| 🟡 **Idle** | Inactif temporaire | 3-10 min |
| ⚪ **Inactive** | Déconnecté | > 10 min |

---

## 📋 Roadmap

- [x] Vue Status avec interfaces et peers
- [x] Vue Peers avec détails complets
- [x] Vue Traffic avec statistiques
- [x] Vue Configuration avec syntaxe colorée
- [ ] Graphiques historiques (24h/7j)
- [ ] Alertes sur déconnexion
- [ ] Génération de QR codes
- [ ] Export de configuration
- [ ] Gestion des peers (ajout/suppression)

---

## 🤝 Contribuer

Le projet est open-source sous licence **Apache-2.0**. Les contributions sont bienvenues !

<div class="contribute-options">
  <a href="https://github.com/gkerma/luci-app-wireguard-dashboard/issues" class="contribute-card">
    <span class="contribute-icon">🐛</span>
    <span class="contribute-title">Signaler un bug</span>
  </a>
  <a href="https://github.com/gkerma/luci-app-wireguard-dashboard/pulls" class="contribute-card">
    <span class="contribute-icon">🔀</span>
    <span class="contribute-title">Pull Request</span>
  </a>
  <a href="https://github.com/gkerma/luci-app-wireguard-dashboard" class="contribute-card">
    <span class="contribute-icon">⭐</span>
    <span class="contribute-title">Star le projet</span>
  </a>
</div>

---

## 📚 Ressources

- [WireGuard Official](https://www.wireguard.com/)
- [OpenWrt Wiki - WireGuard](https://openwrt.org/docs/guide-user/services/vpn/wireguard/start)
- [WireGuard White Paper](https://www.wireguard.com/papers/wireguard.pdf)
- [Article de blog : Présentation du dashboard](/blog/2024/12/luci-wireguard-dashboard/)

---

<div class="app-footer">
  <p>
    Développé par <a href="https://cybermind.fr">Gandalf @ CyberMind.fr</a><br>
    <small>Consultant Cybersécurité • Passionné de VPN et Tunnels sécurisés</small><br>
    <small style="color: #64748b">WireGuard® is a registered trademark of Jason A. Donenfeld.</small>
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
  background: linear-gradient(135deg, #06b6d420, #0ea5e920);
  border: 1px solid #06b6d440;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  color: #06b6d4;
  margin-bottom: 16px;
}

.app-hero h1 {
  font-size: 48px;
  margin: 0 0 12px 0;
  background: linear-gradient(135deg, #f8fafc, #94a3b8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.app-tagline {
  font-size: 20px;
  color: #94a3b8;
  margin: 0 0 16px 0;
}

.app-description {
  font-size: 16px;
  line-height: 1.7;
  color: #64748b;
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
  background: linear-gradient(135deg, #06b6d4, #0ea5e9);
  color: white;
}

.btn-primary:hover {
  box-shadow: 0 0 25px rgba(6, 182, 212, 0.4);
}

.btn-secondary {
  background: #1e293b;
  color: #f8fafc;
  border: 1px solid #334155;
}

.btn-secondary:hover { border-color: #06b6d4; }

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
  background: linear-gradient(145deg, #0f172a, #030712);
  border: 1px solid #334155;
  border-radius: 12px;
  padding: 24px;
  transition: all 0.3s;
}

.feature-card:hover {
  border-color: #06b6d440;
  transform: translateY(-4px);
}

.feature-icon {
  font-size: 32px;
  margin-bottom: 12px;
}

.feature-card h3 {
  font-size: 18px;
  margin: 0 0 8px 0;
  color: #f8fafc;
}

.feature-card p {
  font-size: 14px;
  color: #94a3b8;
  margin: 0;
  line-height: 1.6;
}

/* Demo */
.demo-intro {
  text-align: center;
  color: #94a3b8;
  margin-bottom: 24px;
}

.demo-container {
  background: #030712;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid #334155;
}

.demo-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  background: #0f172a;
  border-bottom: 1px solid #334155;
}

.demo-badge {
  font-size: 13px;
  color: #06b6d4;
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
  background: #0f172a;
  border: 1px solid #334155;
  border-radius: 12px;
  text-decoration: none;
  transition: all 0.2s;
}

.contribute-card:hover {
  border-color: #06b6d4;
  transform: translateY(-2px);
}

.contribute-icon { font-size: 28px; }

.contribute-title {
  font-size: 14px;
  font-weight: 600;
  color: #f8fafc;
}

/* Footer */
.app-footer {
  text-align: center;
  padding: 40px 0;
  margin-top: 40px;
  border-top: 1px solid #334155;
  color: #64748b;
}

.app-footer a { color: #06b6d4; }
</style>
