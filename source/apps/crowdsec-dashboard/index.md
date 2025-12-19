---
title: "CrowdSec Dashboard pour OpenWrt"
description: "Dashboard de sécurité moderne et responsive pour surveiller CrowdSec directement depuis LuCI sur votre routeur OpenWrt."
layout: app
date: 2025-12-19
updated: 2025-12-19
author: Gandalf
app:
  name: luci-app-crowdsec-dashboard
  version: 1.0.0
  license: Apache-2.0
  repo: https://github.com/gkerma/luci-app-crowdsec-dashboard
  demo: true
tags: [crowdsec, openwrt, luci, security, dashboard, open-source]
image: /images/crowdsec-dashboard-hero.png
---

<div class="app-hero">
  <div class="app-hero-content">
    <div class="app-badge">🛡️ Open Source</div>
    <h1>CrowdSec Dashboard</h1>
    <p class="app-tagline">Surveillance de sécurité en temps réel pour OpenWrt</p>
    <p class="app-description">
      Une interface moderne et responsive pour monitorer votre protection CrowdSec 
      directement depuis LuCI. Visualisez les bans, alertes et métriques sans quitter 
      votre navigateur.
    </p>
    <div class="app-actions">
      <a href="#demo" class="btn btn-primary">🎮 Essayer la démo</a>
      <a href="https://github.com/gkerma/luci-app-crowdsec-dashboard" class="btn btn-secondary" target="_blank">
        <svg viewBox="0 0 16 16" width="16" height="16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
        GitHub
      </a>
    </div>
  </div>
  <div class="app-hero-image">
    <img src="/images/crowdsec-dashboard-hero.png" alt="CrowdSec Dashboard Preview">
  </div>
</div>

---

## ✨ Fonctionnalités

<div class="features-grid">
  <div class="feature-card">
    <div class="feature-icon">📊</div>
    <h3>Vue d'ensemble</h3>
    <p>Statistiques temps réel : bans actifs, alertes 24h, bouncers. Graphiques des top scénarios et pays d'origine des attaques.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🚫</div>
    <h3>Gestion des décisions</h3>
    <p>Recherche, filtrage et tri des IP bannies. Actions bulk pour débannir plusieurs IP. Ajout manuel de bans avec durée personnalisée.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">⚠️</div>
    <h3>Historique des alertes</h3>
    <p>Consultation complète des alertes passées avec statistiques agrégées par scénario. Bannissement direct depuis une alerte.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">📈</div>
    <h3>Métriques détaillées</h3>
    <p>État des bouncers et machines, hub status (collections, parsers, scénarios), métriques Prometheus brutes.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">🔄</div>
    <h3>Auto-refresh</h3>
    <p>Les données se mettent à jour automatiquement toutes les 30 secondes. Pas besoin de rafraîchir manuellement.</p>
  </div>
  
  <div class="feature-card">
    <div class="feature-icon">📱</div>
    <h3>Responsive</h3>
    <p>Interface adaptée desktop, tablette et mobile. Vérifiez la sécurité de votre réseau depuis n'importe où.</p>
  </div>
</div>

---

## 🎮 Démo interactive {#demo}

<p class="demo-intro">
  Testez l'interface avec des données simulées. Toutes les fonctionnalités sont actives : 
  navigation, recherche, tri, modales d'ajout de ban, etc.
</p>

<div class="demo-container">
  <div class="demo-toolbar">
    <span class="demo-badge">💡 Mode démo — Données fictives</span>
    <a href="/apps/crowdsec-dashboard/demo.html" target="_blank" class="btn btn-sm">Ouvrir en plein écran ↗</a>
  </div>
  <iframe 
    src="/apps/crowdsec-dashboard/demo.html" 
    width="100%" 
    height="700" 
    frameborder="0"
    style="border-radius: 8px; border: 1px solid #2a3444;">
  </iframe>
</div>

---

## 📦 Installation

### Prérequis

- OpenWrt 21.02 ou supérieur
- CrowdSec Security Engine installé
- LuCI (interface web OpenWrt)

```bash
# Installer CrowdSec si ce n'est pas déjà fait
opkg update
opkg install crowdsec crowdsec-firewall-bouncer
```

### Depuis les sources (recommandé)

```bash
# Dans votre environnement de build OpenWrt
cd ~/openwrt/feeds/luci/applications/
git clone https://github.com/gkerma/luci-app-crowdsec-dashboard.git

# Mettre à jour les feeds et compiler
cd ~/openwrt
./scripts/feeds update -a && ./scripts/feeds install -a
make menuconfig  # Sélectionner LuCI > Applications > luci-app-crowdsec-dashboard
make package/luci-app-crowdsec-dashboard/compile V=s
```

### Installation manuelle du .ipk

```bash
# Transférer le package sur votre routeur
scp luci-app-crowdsec-dashboard_1.0.0-1_all.ipk root@192.168.1.1:/tmp/

# Se connecter et installer
ssh root@192.168.1.1
opkg install /tmp/luci-app-crowdsec-dashboard_1.0.0-1_all.ipk

# Redémarrer les services
/etc/init.d/rpcd restart
/etc/init.d/uhttpd restart
```

### Accès au dashboard

Après installation, le dashboard est accessible dans LuCI :

**Services → CrowdSec Dashboard**

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Navigateur Web                          │
│                    (LuCI JavaScript)                         │
└─────────────────────────┬───────────────────────────────────┘
                          │ ubus RPC (WebSocket)
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                       rpcd daemon                            │
│              /usr/libexec/rpcd/crowdsec                      │
└─────────────────────────┬───────────────────────────────────┘
                          │ Shell exec
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    cscli (CrowdSec CLI)                      │
│         decisions | alerts | metrics | bouncers              │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  CrowdSec Local API                          │
│                    (SQLite / REST)                           │
└─────────────────────────────────────────────────────────────┘
```

Le dashboard n'accède pas directement à la base CrowdSec. Il utilise `cscli` via un backend RPCD, 
ce qui garantit la compatibilité avec toutes les versions de CrowdSec et respecte les permissions système.

---

## 🎨 Design

Le thème s'inspire des dashboards de SOC (Security Operations Center) avec une esthétique **cybersecurity industrielle** :

| Élément | Valeur |
|---------|--------|
| Background | `#0a0e14` (noir profond) |
| Accent principal | `#00d4aa` (cyan/vert) |
| Alertes/Danger | `#ff6b6b` (rouge corail) |
| Warning | `#ffa94d` (orange) |
| Typographie données | JetBrains Mono |
| Typographie UI | Inter |

Le design est optimisé pour :
- Réduire la fatigue visuelle (thème sombre)
- Hiérarchiser l'information (couleurs sémantiques)
- Fonctionner sur tous les écrans (responsive)

---

## 📋 Roadmap

- [x] Vue Overview avec stats et graphiques
- [x] Gestion complète des décisions
- [x] Historique des alertes
- [x] Métriques et status hub
- [ ] Export CSV/JSON des données
- [ ] Notifications push (Telegram, email)
- [ ] Graphiques temporels (évolution sur 7j/30j)
- [ ] Intégration Console CrowdSec
- [ ] Thème clair optionnel
- [ ] Traductions (FR, DE, ES)

---

## 🤝 Contribuer

Le projet est open-source sous licence **Apache-2.0**. Les contributions sont bienvenues !

<div class="contribute-options">
  <a href="https://github.com/gkerma/luci-app-crowdsec-dashboard/issues" class="contribute-card">
    <span class="contribute-icon">🐛</span>
    <span class="contribute-title">Signaler un bug</span>
  </a>
  <a href="https://github.com/gkerma/luci-app-crowdsec-dashboard/pulls" class="contribute-card">
    <span class="contribute-icon">🔀</span>
    <span class="contribute-title">Pull Request</span>
  </a>
  <a href="https://github.com/gkerma/luci-app-crowdsec-dashboard" class="contribute-card">
    <span class="contribute-icon">⭐</span>
    <span class="contribute-title">Star le projet</span>
  </a>
</div>

---

## 📚 Ressources

- [Documentation CrowdSec](https://docs.crowdsec.net/)
- [Wiki OpenWrt - CrowdSec](https://openwrt.org/docs/guide-user/services/crowdsec)
- [Article de blog : Présentation du dashboard](/blog/2024/12/luci-crowdsec-dashboard/)
- [CrowdSec Hub - Collections et scénarios](https://hub.crowdsec.net/)

---

<div class="app-footer">
  <p>
    Développé par <a href="https://cybermind.fr">Gandalf @ CyberMind.fr</a><br>
    <small>CrowdSec Ambassador • Consultant Cybersécurité</small>
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
  .app-hero {
    grid-template-columns: 1fr;
  }
}

.app-badge {
  display: inline-block;
  padding: 6px 12px;
  background: linear-gradient(135deg, #00d4aa20, #4dabf720);
  border: 1px solid #00d4aa40;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  color: #00d4aa;
  margin-bottom: 16px;
}

.app-hero h1 {
  font-size: 48px;
  margin: 0 0 12px 0;
  background: linear-gradient(135deg, #e6edf3, #8b949e);
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
  background: #00d4aa;
  color: #0a0e14;
}

.btn-primary:hover {
  background: #00e6b8;
  box-shadow: 0 0 20px #00d4aa40;
}

.btn-secondary {
  background: #1e2632;
  color: #e6edf3;
  border: 1px solid #2a3444;
}

.btn-secondary:hover {
  border-color: #00d4aa;
}

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
  background: linear-gradient(145deg, #151b23, #1a2231);
  border: 1px solid #2a3444;
  border-radius: 12px;
  padding: 24px;
  transition: all 0.3s;
}

.feature-card:hover {
  border-color: #00d4aa40;
  transform: translateY(-4px);
}

.feature-icon {
  font-size: 32px;
  margin-bottom: 12px;
}

.feature-card h3 {
  font-size: 18px;
  margin: 0 0 8px 0;
  color: #e6edf3;
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
  background: #0a0e14;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid #2a3444;
}

.demo-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  background: #151b23;
  border-bottom: 1px solid #2a3444;
}

.demo-badge {
  font-size: 13px;
  color: #ffa94d;
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
  background: #151b23;
  border: 1px solid #2a3444;
  border-radius: 12px;
  text-decoration: none;
  transition: all 0.2s;
}

.contribute-card:hover {
  border-color: #00d4aa;
  transform: translateY(-2px);
}

.contribute-icon {
  font-size: 28px;
}

.contribute-title {
  font-size: 14px;
  font-weight: 600;
  color: #e6edf3;
}

/* Footer */
.app-footer {
  text-align: center;
  padding: 40px 0;
  margin-top: 40px;
  border-top: 1px solid #2a3444;
  color: #6e7681;
}

.app-footer a {
  color: #00d4aa;
}
</style>
