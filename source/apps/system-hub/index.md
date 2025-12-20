---
title: "System Hub - Central Control for OpenWrt"
date: 2024-12-20
layout: app
app:
  name: System Hub
  version: 1.0.0
  category: Administration
  license: Apache-2.0
  repo: https://github.com/gkerma/luci-app-system-hub
  demo: /demos/system-hub
  icon: 🎛️
  color: "#6366f1"
image: /images/system-hub-hero.png
---

<style>
.sh-hero {
  background: linear-gradient(135deg, #0a0a0f 0%, #12121a 50%, #0a0a0f 100%);
  padding: 60px 20px;
  text-align: center;
  border-radius: 20px;
  margin-bottom: 40px;
  position: relative;
  overflow: hidden;
}

.sh-hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #6366f1, #8b5cf6, #a855f7);
}

.sh-hero-badge {
  display: inline-block;
  padding: 6px 16px;
  background: rgba(99, 102, 241, 0.15);
  color: #6366f1;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
  margin-bottom: 20px;
  border: 1px solid rgba(99, 102, 241, 0.3);
}

.sh-hero-title {
  font-size: 48px;
  font-weight: 800;
  color: #fafafa;
  margin-bottom: 16px;
}

.sh-hero-title span {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.sh-hero-desc {
  font-size: 20px;
  color: #a0a0b0;
  max-width: 700px;
  margin: 0 auto 30px;
  line-height: 1.6;
}

.sh-hero-actions {
  display: flex;
  gap: 16px;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 14px 28px;
  border-radius: 10px;
  font-size: 15px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.3s;
}

.btn-primary {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: white;
  border: none;
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 30px rgba(99, 102, 241, 0.4);
}

.btn-secondary {
  background: #1a1a24;
  color: #fafafa;
  border: 1px solid #2a2a3a;
}

.btn-secondary:hover {
  border-color: #6366f1;
}

.sh-section {
  margin: 60px 0;
}

.sh-section-title {
  font-size: 28px;
  font-weight: 700;
  color: #fafafa;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.sh-section-desc {
  font-size: 16px;
  color: #a0a0b0;
  margin-bottom: 30px;
}

.sh-features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}

.sh-feature-card {
  background: #12121a;
  border: 1px solid #2a2a3a;
  border-radius: 12px;
  padding: 24px;
  transition: all 0.3s;
}

.sh-feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.4);
  border-color: #6366f1;
}

.sh-feature-icon {
  font-size: 32px;
  margin-bottom: 12px;
}

.sh-feature-title {
  font-size: 16px;
  font-weight: 600;
  color: #fafafa;
  margin-bottom: 8px;
}

.sh-feature-desc {
  font-size: 13px;
  color: #a0a0b0;
  line-height: 1.5;
}

.sh-components-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 14px;
}

.sh-component-card {
  background: #12121a;
  border: 1px solid #2a2a3a;
  border-radius: 12px;
  padding: 20px;
  text-align: center;
  position: relative;
  overflow: hidden;
  transition: all 0.3s;
}

.sh-component-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--comp-color);
}

.sh-component-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.4);
}

.sh-component-card.planned {
  opacity: 0.6;
  border-style: dashed;
}

.sh-component-icon { font-size: 28px; margin-bottom: 8px; }
.sh-component-name { font-size: 13px; font-weight: 700; color: #fafafa; }
.sh-component-status { font-size: 10px; color: #a0a0b0; }

.sh-health-demo {
  background: #12121a;
  border: 1px solid #2a2a3a;
  border-radius: 16px;
  padding: 30px;
  text-align: center;
}

.sh-health-score {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background: rgba(34, 197, 94, 0.15);
  border: 6px solid #22c55e;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 20px;
  font-size: 42px;
  font-weight: 800;
  font-family: 'JetBrains Mono', monospace;
  color: #22c55e;
}

.sh-health-label {
  font-size: 20px;
  font-weight: 700;
  color: #fafafa;
  margin-bottom: 8px;
}

.sh-health-time {
  font-size: 13px;
  color: #707080;
}

.sh-metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 12px;
  margin-top: 24px;
}

.sh-metric {
  background: #1a1a24;
  border-radius: 10px;
  padding: 14px;
}

.sh-metric-label {
  font-size: 11px;
  color: #707080;
  margin-bottom: 4px;
}

.sh-metric-value {
  font-family: 'JetBrains Mono', monospace;
  font-size: 18px;
  font-weight: 700;
}

.sh-metric-value.ok { color: #22c55e; }
.sh-metric-value.warning { color: #f59e0b; }
.sh-metric-value.critical { color: #ef4444; }

.sh-metric-bar {
  height: 4px;
  background: #0a0a0f;
  border-radius: 2px;
  margin-top: 8px;
  overflow: hidden;
}

.sh-metric-fill {
  height: 100%;
  border-radius: 2px;
}

.sh-metric-fill.ok { background: #22c55e; }
.sh-metric-fill.warning { background: #f59e0b; }
.sh-metric-fill.critical { background: #ef4444; }

.sh-remote-card {
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.05));
  border: 1px solid rgba(99, 102, 241, 0.3);
  border-radius: 16px;
  padding: 30px;
  display: flex;
  align-items: center;
  gap: 24px;
  flex-wrap: wrap;
}

.sh-remote-icon {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 40px;
}

.sh-remote-id {
  font-family: 'JetBrains Mono', monospace;
  font-size: 32px;
  font-weight: 800;
  letter-spacing: 3px;
  color: #fafafa;
}

.sh-remote-label {
  font-size: 13px;
  color: #707080;
}

.sh-demo-frame {
  border: 1px solid #2a2a3a;
  border-radius: 16px;
  overflow: hidden;
  background: #0a0a0f;
}

.sh-demo-frame iframe {
  width: 100%;
  height: 700px;
  border: none;
}

.sh-install-code {
  background: #0a0a0f;
  border: 1px solid #2a2a3a;
  border-radius: 12px;
  padding: 20px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
  overflow-x: auto;
  color: #a0a0b0;
}

.sh-install-code .comment { color: #707080; }
.sh-install-code .command { color: #6366f1; }

.sh-roadmap-timeline {
  position: relative;
  padding-left: 30px;
}

.sh-roadmap-timeline::before {
  content: '';
  position: absolute;
  left: 10px;
  top: 0;
  bottom: 0;
  width: 2px;
  background: linear-gradient(180deg, #6366f1, #8b5cf6);
}

.sh-roadmap-item {
  position: relative;
  padding: 16px 0;
}

.sh-roadmap-item::before {
  content: '';
  position: absolute;
  left: -24px;
  top: 22px;
  width: 12px;
  height: 12px;
  background: #6366f1;
  border-radius: 50%;
  border: 3px solid #12121a;
}

.sh-roadmap-quarter {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  color: #6366f1;
  margin-bottom: 8px;
}

.sh-roadmap-components {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.sh-roadmap-chip {
  padding: 6px 12px;
  background: #1a1a24;
  border: 1px solid #2a2a3a;
  border-radius: 8px;
  font-size: 12px;
  color: #a0a0b0;
}

.sh-resources {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 16px;
}

.sh-resource-link {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 20px;
  background: #12121a;
  border: 1px solid #2a2a3a;
  border-radius: 10px;
  text-decoration: none;
  color: #fafafa;
  transition: all 0.2s;
}

.sh-resource-link:hover {
  border-color: #6366f1;
  background: #1a1a24;
}

.sh-resource-icon { font-size: 24px; }

@media (max-width: 768px) {
  .sh-hero-title { font-size: 32px; }
  .sh-remote-card { flex-direction: column; text-align: center; }
}
</style>

<!-- Hero Section -->
<div class="sh-hero">
  <div class="sh-hero-badge">🎛️ Central Control for OpenWrt</div>
  <h1 class="sh-hero-title">System <span>Hub</span></h1>
  <p class="sh-hero-desc">
    Centre de contrôle unifié avec gestion des composants, rapports de santé automatisés,
    assistance remote RustDesk et collecte de diagnostics.
  </p>
  <div class="sh-hero-actions">
    <a href="https://github.com/gkerma/luci-app-system-hub" class="btn btn-primary" target="_blank">
      ⬇️ Télécharger
    </a>
    <a href="#demo" class="btn btn-secondary">
      🎮 Voir la Démo
    </a>
  </div>
</div>

<!-- Features -->
<div class="sh-section">
  <h2 class="sh-section-title">✨ Fonctionnalités</h2>
  
  <div class="sh-features-grid">
    <div class="sh-feature-card">
      <div class="sh-feature-icon">🧩</div>
      <h4 class="sh-feature-title">Gestion des Composants</h4>
      <p class="sh-feature-desc">Vue unifiée de tous vos dashboards et services. Start, Stop, Restart en un clic.</p>
    </div>
    <div class="sh-feature-card">
      <div class="sh-feature-icon">💚</div>
      <h4 class="sh-feature-title">Rapports de Santé</h4>
      <p class="sh-feature-desc">Score global 0-100, métriques détaillées, seuils configurables, recommandations.</p>
    </div>
    <div class="sh-feature-card">
      <div class="sh-feature-icon">🖥️</div>
      <h4 class="sh-feature-title">Assistance RustDesk</h4>
      <p class="sh-feature-desc">Support à distance sécurisé avec ID unique, approbation requise et timeout.</p>
    </div>
    <div class="sh-feature-card">
      <div class="sh-feature-icon">🔍</div>
      <h4 class="sh-feature-title">Diagnostics</h4>
      <p class="sh-feature-desc">Collecte automatisée des logs, configs et infos réseau. Anonymisation incluse.</p>
    </div>
    <div class="sh-feature-card">
      <div class="sh-feature-icon">📋</div>
      <h4 class="sh-feature-title">Logs Unifiés</h4>
      <p class="sh-feature-desc">Agrégation de tous les logs composants avec filtres et export CSV.</p>
    </div>
    <div class="sh-feature-card">
      <div class="sh-feature-icon">📅</div>
      <h4 class="sh-feature-title">Automatisation</h4>
      <p class="sh-feature-desc">Tâches planifiées : health check, backup, nettoyage logs automatiques.</p>
    </div>
  </div>
</div>

<!-- Components -->
<div class="sh-section">
  <h2 class="sh-section-title">🧩 Composants Supportés</h2>
  <p class="sh-section-desc">Gérez tous vos dashboards depuis une interface unique.</p>
  
  <div class="sh-components-grid">
    <div class="sh-component-card" style="--comp-color: #22c55e;">
      <div class="sh-component-icon">🛡️</div>
      <div class="sh-component-name">CrowdSec</div>
      <div class="sh-component-status">Cybersécurité</div>
    </div>
    <div class="sh-component-card" style="--comp-color: #00ab44;">
      <div class="sh-component-icon">📊</div>
      <div class="sh-component-name">Netdata</div>
      <div class="sh-component-status">Monitoring</div>
    </div>
    <div class="sh-component-card" style="--comp-color: #8b5cf6;">
      <div class="sh-component-icon">🔍</div>
      <div class="sh-component-name">Netifyd</div>
      <div class="sh-component-status">DPI</div>
    </div>
    <div class="sh-component-card" style="--comp-color: #88171a;">
      <div class="sh-component-icon">🔒</div>
      <div class="sh-component-name">WireGuard</div>
      <div class="sh-component-status">VPN</div>
    </div>
    <div class="sh-component-card" style="--comp-color: #f97316;">
      <div class="sh-component-icon">🔀</div>
      <div class="sh-component-name">Network Modes</div>
      <div class="sh-component-status">Multi-mode</div>
    </div>
    <div class="sh-component-card" style="--comp-color: #ef4444;">
      <div class="sh-component-icon">🛡️</div>
      <div class="sh-component-name">Client Guardian</div>
      <div class="sh-component-status">NAC</div>
    </div>
    <div class="sh-component-card planned" style="--comp-color: #68bc71;">
      <div class="sh-component-icon">🚫</div>
      <div class="sh-component-name">AdGuard</div>
      <div class="sh-component-status">Q1 2025</div>
    </div>
    <div class="sh-component-card planned" style="--comp-color: #0ea5e9;">
      <div class="sh-component-icon">🌐</div>
      <div class="sh-component-name">Tailscale</div>
      <div class="sh-component-status">Q1 2025</div>
    </div>
  </div>
</div>

<!-- Health Demo -->
<div class="sh-section">
  <h2 class="sh-section-title">💚 Rapports de Santé</h2>
  
  <div class="sh-health-demo">
    <div class="sh-health-score">92</div>
    <div class="sh-health-label">Système en Bonne Santé</div>
    <div class="sh-health-time">Dernière vérification: il y a 5 minutes</div>
    
    <div class="sh-metrics-grid">
      <div class="sh-metric">
        <div class="sh-metric-label">🔲 CPU</div>
        <div class="sh-metric-value ok">23%</div>
        <div class="sh-metric-bar"><div class="sh-metric-fill ok" style="width: 23%"></div></div>
      </div>
      <div class="sh-metric">
        <div class="sh-metric-label">💾 RAM</div>
        <div class="sh-metric-value ok">58%</div>
        <div class="sh-metric-bar"><div class="sh-metric-fill ok" style="width: 58%"></div></div>
      </div>
      <div class="sh-metric">
        <div class="sh-metric-label">💿 Disque</div>
        <div class="sh-metric-value warning">76%</div>
        <div class="sh-metric-bar"><div class="sh-metric-fill warning" style="width: 76%"></div></div>
      </div>
      <div class="sh-metric">
        <div class="sh-metric-label">🌡️ Temp</div>
        <div class="sh-metric-value ok">52°C</div>
        <div class="sh-metric-bar"><div class="sh-metric-fill ok" style="width: 52%"></div></div>
      </div>
    </div>
  </div>
</div>

<!-- Remote -->
<div class="sh-section">
  <h2 class="sh-section-title">🖥️ Assistance Remote RustDesk</h2>
  
  <div class="sh-remote-card">
    <div class="sh-remote-icon">🖥️</div>
    <div>
      <div class="sh-remote-id">847 293 156</div>
      <div class="sh-remote-label">ID RustDesk — Partagez ce code avec le support pour une assistance à distance sécurisée</div>
    </div>
    <a href="#" class="btn btn-primary" style="margin-left: auto;">🚀 Démarrer Session</a>
  </div>
</div>

<!-- Demo -->
<div class="sh-section" id="demo">
  <h2 class="sh-section-title">🎮 Démo Interactive</h2>
  <p class="sh-section-desc">Explorez l'interface complète sans installation.</p>
  
  <div class="sh-demo-frame">
    <iframe src="/demos/system-hub/index.html" loading="lazy"></iframe>
  </div>
</div>

<!-- Roadmap -->
<div class="sh-section">
  <h2 class="sh-section-title">🗓️ Roadmap</h2>
  
  <div class="sh-roadmap-timeline">
    <div class="sh-roadmap-item">
      <div class="sh-roadmap-quarter">Q1 2025</div>
      <div class="sh-roadmap-components">
        <span class="sh-roadmap-chip">🚫 AdGuard Home</span>
        <span class="sh-roadmap-chip">📈 Prometheus</span>
        <span class="sh-roadmap-chip">🌐 Tailscale</span>
      </div>
    </div>
    <div class="sh-roadmap-item">
      <div class="sh-roadmap-quarter">Q2 2025</div>
      <div class="sh-roadmap-components">
        <span class="sh-roadmap-chip">📉 Grafana</span>
        <span class="sh-roadmap-chip">🏠 Home Assistant</span>
        <span class="sh-roadmap-chip">📶 ntopng</span>
      </div>
    </div>
    <div class="sh-roadmap-item">
      <div class="sh-roadmap-quarter">Q3 2025</div>
      <div class="sh-roadmap-components">
        <span class="sh-roadmap-chip">📱 App Mobile</span>
        <span class="sh-roadmap-chip">🔗 API REST</span>
        <span class="sh-roadmap-chip">🌍 Multi-routeurs</span>
      </div>
    </div>
  </div>
</div>

<!-- Installation -->
<div class="sh-section">
  <h2 class="sh-section-title">📦 Installation</h2>
  
  <div class="sh-install-code">
    <span class="comment"># Prérequis</span><br>
    <span class="command">opkg update</span><br>
    <span class="command">opkg install luci-base rpcd</span><br><br>
    <span class="comment"># RustDesk (optionnel)</span><br>
    <span class="command">opkg install rustdesk</span><br><br>
    <span class="comment"># Cloner et installer</span><br>
    <span class="command">git clone https://github.com/gkerma/luci-app-system-hub.git</span><br>
    <span class="command">cd luci-app-system-hub && make install</span><br><br>
    <span class="comment"># Redémarrer</span><br>
    <span class="command">/etc/init.d/rpcd restart</span>
  </div>
</div>

<!-- Resources -->
<div class="sh-section">
  <h2 class="sh-section-title">🔗 Ressources</h2>
  
  <div class="sh-resources">
    <a href="https://github.com/gkerma/luci-app-system-hub" class="sh-resource-link" target="_blank">
      <span class="sh-resource-icon">📦</span>
      <div>
        <strong>GitHub Repository</strong>
        <div style="font-size:12px;color:#707080">Code source et issues</div>
      </div>
    </a>
    <a href="https://rustdesk.com" class="sh-resource-link" target="_blank">
      <span class="sh-resource-icon">🖥️</span>
      <div>
        <strong>RustDesk</strong>
        <div style="font-size:12px;color:#707080">Remote desktop open source</div>
      </div>
    </a>
    <a href="/dashboards" class="sh-resource-link">
      <span class="sh-resource-icon">🎛️</span>
      <div>
        <strong>Autres Dashboards</strong>
        <div style="font-size:12px;color:#707080">CrowdSec, Netdata, Client Guardian...</div>
      </div>
    </a>
  </div>
</div>

---

<div style="text-align: center; margin-top: 40px; padding: 20px; background: #12121a; border-radius: 12px;">
  <p style="color: #707080; font-size: 14px;">
    Créé par <a href="https://cybermind.fr" style="color: #6366f1;">Gandalf @ CyberMind.fr</a><br>
    Licence Apache-2.0
  </p>
</div>
