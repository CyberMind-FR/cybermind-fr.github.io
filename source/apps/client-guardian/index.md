---
title: "Client Guardian - Network Access Control for OpenWrt"
date: 2024-12-20
layout: app
app:
  name: Client Guardian
  version: 1.0.0
  category: Security
  license: Apache-2.0
  repo: https://github.com/gkerma/luci-app-client-guardian
  demo: /demos/client-guardian
  icon: 🛡️
  color: "#ef4444"
---

<style>
.cg-hero {
  background: linear-gradient(135deg, #0f0a0a 0%, #1a1212 50%, #0f0a0a 100%);
  padding: 60px 20px;
  text-align: center;
  border-radius: 20px;
  margin-bottom: 40px;
  position: relative;
  overflow: hidden;
}

.cg-hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #ef4444, #dc2626, #b91c1c);
}

.cg-hero-badge {
  display: inline-block;
  padding: 6px 16px;
  background: rgba(239, 68, 68, 0.15);
  color: #ef4444;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
  margin-bottom: 20px;
  border: 1px solid rgba(239, 68, 68, 0.3);
}

.cg-hero-title {
  font-size: 48px;
  font-weight: 800;
  color: #fafafa;
  margin-bottom: 16px;
}

.cg-hero-title span {
  background: linear-gradient(135deg, #ef4444, #dc2626);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.cg-hero-desc {
  font-size: 20px;
  color: #b8a8a8;
  max-width: 700px;
  margin: 0 auto 30px;
  line-height: 1.6;
}

.cg-hero-actions {
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
  background: linear-gradient(135deg, #ef4444, #dc2626);
  color: white;
  border: none;
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 30px rgba(239, 68, 68, 0.4);
}

.btn-secondary {
  background: #251a1a;
  color: #fafafa;
  border: 1px solid #3d2828;
}

.btn-secondary:hover {
  border-color: #ef4444;
}

.cg-section {
  margin: 60px 0;
}

.cg-section-title {
  font-size: 28px;
  font-weight: 700;
  color: #fafafa;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.cg-section-desc {
  font-size: 16px;
  color: #b8a8a8;
  margin-bottom: 30px;
}

.cg-zones-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 16px;
}

.cg-zone-card {
  background: #1a1212;
  border: 1px solid #3d2828;
  border-radius: 12px;
  padding: 20px;
  text-align: center;
  transition: all 0.3s;
  position: relative;
  overflow: hidden;
}

.cg-zone-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--zone-color);
}

.cg-zone-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}

.cg-zone-icon {
  font-size: 32px;
  margin-bottom: 10px;
}

.cg-zone-name {
  font-size: 15px;
  font-weight: 700;
  color: #fafafa;
  margin-bottom: 4px;
}

.cg-zone-desc {
  font-size: 11px;
  color: #8a7575;
}

.cg-features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}

.cg-feature-card {
  background: #1a1212;
  border: 1px solid #3d2828;
  border-radius: 12px;
  padding: 24px;
}

.cg-feature-icon {
  font-size: 32px;
  margin-bottom: 12px;
}

.cg-feature-title {
  font-size: 16px;
  font-weight: 600;
  color: #fafafa;
  margin-bottom: 8px;
}

.cg-feature-desc {
  font-size: 13px;
  color: #b8a8a8;
  line-height: 1.5;
}

.cg-workflow {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
  margin: 30px 0;
}

.cg-workflow-step {
  background: #1a1212;
  border: 1px solid #3d2828;
  border-radius: 12px;
  padding: 20px;
  text-align: center;
  min-width: 140px;
}

.cg-workflow-step.highlight {
  border-color: #ef4444;
  background: rgba(239, 68, 68, 0.1);
}

.cg-workflow-icon {
  font-size: 28px;
  margin-bottom: 8px;
}

.cg-workflow-text {
  font-size: 12px;
  color: #b8a8a8;
}

.cg-workflow-arrow {
  font-size: 24px;
  color: #3d2828;
}

.cg-demo-frame {
  border: 1px solid #3d2828;
  border-radius: 16px;
  overflow: hidden;
  background: #0f0a0a;
}

.cg-demo-frame iframe {
  width: 100%;
  height: 700px;
  border: none;
}

.cg-install-code {
  background: #0f0a0a;
  border: 1px solid #3d2828;
  border-radius: 12px;
  padding: 20px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
  overflow-x: auto;
  color: #b8a8a8;
}

.cg-install-code .comment { color: #8a7575; }
.cg-install-code .command { color: #ef4444; }

.cg-comparison-table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

.cg-comparison-table th,
.cg-comparison-table td {
  padding: 12px 16px;
  border: 1px solid #3d2828;
  text-align: left;
}

.cg-comparison-table th {
  background: #251a1a;
  font-weight: 600;
  color: #fafafa;
}

.cg-comparison-table td {
  background: #1a1212;
  color: #b8a8a8;
}

.cg-comparison-table tr:hover td {
  background: #251a1a;
}

.cg-resources {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 16px;
}

.cg-resource-link {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 20px;
  background: #1a1212;
  border: 1px solid #3d2828;
  border-radius: 10px;
  text-decoration: none;
  color: #fafafa;
  transition: all 0.2s;
}

.cg-resource-link:hover {
  border-color: #ef4444;
  background: #251a1a;
}

.cg-resource-icon {
  font-size: 24px;
}
</style>

<!-- Hero Section -->
<div class="cg-hero">
  <div class="cg-hero-badge">🛡️ Network Access Control for OpenWrt</div>
  <h1 class="cg-hero-title">Client <span>Guardian</span></h1>
  <p class="cg-hero-desc">
    Contrôle d'accès réseau avec quarantaine automatique, portail captif nouvelle génération, 
    contrôle parental et alertes SMS/Email en temps réel.
  </p>
  <div class="cg-hero-actions">
    <a href="https://github.com/gkerma/luci-app-client-guardian" class="btn btn-primary" target="_blank">
      ⬇️ Télécharger
    </a>
    <a href="#demo" class="btn btn-secondary">
      🎮 Voir la Démo
    </a>
  </div>
</div>

<!-- Workflow -->
<div class="cg-section">
  <h2 class="cg-section-title">⚡ Quarantaine par Défaut</h2>
  <p class="cg-section-desc">Tout nouveau client est automatiquement isolé jusqu'à approbation explicite.</p>
  
  <div class="cg-workflow">
    <div class="cg-workflow-step">
      <div class="cg-workflow-icon">📱</div>
      <div class="cg-workflow-text">Nouvel appareil<br>se connecte</div>
    </div>
    <div class="cg-workflow-arrow">→</div>
    <div class="cg-workflow-step highlight">
      <div class="cg-workflow-icon">⏳</div>
      <div class="cg-workflow-text">Quarantaine<br>automatique</div>
    </div>
    <div class="cg-workflow-arrow">→</div>
    <div class="cg-workflow-step">
      <div class="cg-workflow-icon">🔔</div>
      <div class="cg-workflow-text">Alerte<br>SMS/Email</div>
    </div>
    <div class="cg-workflow-arrow">→</div>
    <div class="cg-workflow-step">
      <div class="cg-workflow-icon">👤</div>
      <div class="cg-workflow-text">Admin<br>décide</div>
    </div>
    <div class="cg-workflow-arrow">→</div>
    <div class="cg-workflow-step">
      <div class="cg-workflow-icon">✅</div>
      <div class="cg-workflow-text">Approuver<br>ou Bannir</div>
    </div>
  </div>
</div>

<!-- Zones -->
<div class="cg-section">
  <h2 class="cg-section-title">🏠 Six Zones de Sécurité</h2>
  <p class="cg-section-desc">Assignez chaque client à une zone avec des permissions spécifiques.</p>
  
  <div class="cg-zones-grid">
    <div class="cg-zone-card" style="--zone-color: #22c55e;">
      <div class="cg-zone-icon">🏠</div>
      <div class="cg-zone-name">LAN Privé</div>
      <div class="cg-zone-desc">Confiance totale</div>
    </div>
    <div class="cg-zone-card" style="--zone-color: #f59e0b;">
      <div class="cg-zone-icon">🔧</div>
      <div class="cg-zone-name">IoT</div>
      <div class="cg-zone-desc">Objets isolés</div>
    </div>
    <div class="cg-zone-card" style="--zone-color: #06b6d4;">
      <div class="cg-zone-icon">👶</div>
      <div class="cg-zone-name">Enfants</div>
      <div class="cg-zone-desc">Accès filtré</div>
    </div>
    <div class="cg-zone-card" style="--zone-color: #8b5cf6;">
      <div class="cg-zone-icon">👥</div>
      <div class="cg-zone-name">Invités</div>
      <div class="cg-zone-desc">Accès limité</div>
    </div>
    <div class="cg-zone-card" style="--zone-color: #ef4444;">
      <div class="cg-zone-icon">⏳</div>
      <div class="cg-zone-name">Quarantaine</div>
      <div class="cg-zone-desc">Non approuvés</div>
    </div>
    <div class="cg-zone-card" style="--zone-color: #6b7280;">
      <div class="cg-zone-icon">🚫</div>
      <div class="cg-zone-name">Bloqué</div>
      <div class="cg-zone-desc">Bannis</div>
    </div>
  </div>
</div>

<!-- Features -->
<div class="cg-section">
  <h2 class="cg-section-title">✨ Fonctionnalités</h2>
  
  <div class="cg-features-grid">
    <div class="cg-feature-card">
      <div class="cg-feature-icon">🔍</div>
      <h4 class="cg-feature-title">Surveillance Temps Réel</h4>
      <p class="cg-feature-desc">Détection automatique des clients par MAC et hostname DHCP. Statut en ligne/offline, trafic RX/TX.</p>
    </div>
    <div class="cg-feature-card">
      <div class="cg-feature-icon">🚪</div>
      <h4 class="cg-feature-title">Portail Captif</h4>
      <p class="cg-feature-desc">Interface moderne personnalisable. Authentification, inscription, CGU, durée de session.</p>
    </div>
    <div class="cg-feature-card">
      <div class="cg-feature-icon">👨‍👩‍👧‍👦</div>
      <h4 class="cg-feature-title">Contrôle Parental</h4>
      <p class="cg-feature-desc">Plages horaires, filtrage de contenu, SafeSearch forcé, quotas de temps, listes blanches/noires.</p>
    </div>
    <div class="cg-feature-card">
      <div class="cg-feature-icon">🔔</div>
      <h4 class="cg-feature-title">Alertes SMS & Email</h4>
      <p class="cg-feature-desc">Notifications instantanées : nouveau client, tentative banni, quota dépassé, activité suspecte.</p>
    </div>
    <div class="cg-feature-card">
      <div class="cg-feature-icon">🔒</div>
      <h4 class="cg-feature-title">Isolation IoT</h4>
      <p class="cg-feature-desc">Vos objets connectés n'ont plus accès à votre réseau local ni aux autres appareils.</p>
    </div>
    <div class="cg-feature-card">
      <div class="cg-feature-icon">📊</div>
      <h4 class="cg-feature-title">Logs Complets</h4>
      <p class="cg-feature-desc">Journal de toutes les connexions, actions admin, alertes. Filtres et export CSV.</p>
    </div>
  </div>
</div>

<!-- Demo -->
<div class="cg-section" id="demo">
  <h2 class="cg-section-title">🎮 Démo Interactive</h2>
  <p class="cg-section-desc">Explorez l'interface complète sans installation.</p>
  
  <div class="cg-demo-frame">
    <iframe src="/demos/client-guardian/index.html" loading="lazy"></iframe>
  </div>
</div>

<!-- Comparison -->
<div class="cg-section">
  <h2 class="cg-section-title">📊 Comparaison des Zones</h2>
  
  <table class="cg-comparison-table">
    <thead>
      <tr>
        <th>Zone</th>
        <th>Internet</th>
        <th>Local</th>
        <th>Inter-client</th>
        <th>Portail</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><strong>🏠 LAN Privé</strong></td><td>✅</td><td>✅</td><td>✅</td><td>❌</td></tr>
      <tr><td><strong>🔧 IoT</strong></td><td>✅</td><td>❌</td><td>❌</td><td>❌</td></tr>
      <tr><td><strong>👶 Enfants</strong></td><td>✅ Filtré</td><td>✅</td><td>✅</td><td>❌</td></tr>
      <tr><td><strong>👥 Invités</strong></td><td>✅ Limité</td><td>❌</td><td>❌</td><td>✅</td></tr>
      <tr><td><strong>⏳ Quarantaine</strong></td><td>❌</td><td>❌</td><td>❌</td><td>✅ Only</td></tr>
      <tr><td><strong>🚫 Bloqué</strong></td><td>❌</td><td>❌</td><td>❌</td><td>❌</td></tr>
    </tbody>
  </table>
</div>

<!-- Installation -->
<div class="cg-section">
  <h2 class="cg-section-title">📦 Installation</h2>
  
  <div class="cg-install-code">
    <span class="comment"># Prérequis</span><br>
    <span class="command">opkg update</span><br>
    <span class="command">opkg install luci-base rpcd dnsmasq-full iptables</span><br><br>
    <span class="comment"># Cloner et installer</span><br>
    <span class="command">git clone https://github.com/gkerma/luci-app-client-guardian.git</span><br>
    <span class="command">cd luci-app-client-guardian</span><br>
    <span class="command">make install</span><br><br>
    <span class="comment"># Redémarrer</span><br>
    <span class="command">/etc/init.d/rpcd restart</span>
  </div>
</div>

<!-- Resources -->
<div class="cg-section">
  <h2 class="cg-section-title">🔗 Ressources</h2>
  
  <div class="cg-resources">
    <a href="https://github.com/gkerma/luci-app-client-guardian" class="cg-resource-link" target="_blank">
      <span class="cg-resource-icon">📦</span>
      <div>
        <strong>GitHub Repository</strong>
        <div style="font-size:12px;color:#8a7575">Code source et issues</div>
      </div>
    </a>
    <a href="https://openwrt.org/docs/start" class="cg-resource-link" target="_blank">
      <span class="cg-resource-icon">📚</span>
      <div>
        <strong>OpenWrt Documentation</strong>
        <div style="font-size:12px;color:#8a7575">Guide officiel</div>
      </div>
    </a>
    <a href="/dashboards" class="cg-resource-link">
      <span class="cg-resource-icon">🎛️</span>
      <div>
        <strong>Autres Dashboards</strong>
        <div style="font-size:12px;color:#8a7575">CrowdSec, Netdata, WireGuard...</div>
      </div>
    </a>
  </div>
</div>

---

<div style="text-align: center; margin-top: 40px; padding: 20px; background: #1a1212; border-radius: 12px;">
  <p style="color: #8a7575; font-size: 14px;">
    Créé par <a href="https://cybermind.fr" style="color: #ef4444;">Gandalf @ CyberMind.fr</a><br>
    Licence Apache-2.0
  </p>
</div>
