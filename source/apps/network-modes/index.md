---
title: "Network Modes Dashboard - Multi-Mode Configuration for OpenWrt"
date: 2024-12-20
layout: app
app:
  name: Network Modes Dashboard
  version: 1.0.0
  category: Network
  license: Apache-2.0
  repo: https://github.com/gkerma/luci-app-network-modes
  demo: /demos/network-modes
  icon: ⚙️
  color: "#f97316"
---

<style>
.nm-hero {
  background: linear-gradient(135deg, #0c0a09 0%, #1c1917 50%, #0c0a09 100%);
  padding: 60px 20px;
  text-align: center;
  border-radius: 20px;
  margin-bottom: 40px;
  position: relative;
  overflow: hidden;
}

.nm-hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #f97316, #f59e0b, #eab308);
}

.nm-hero-badge {
  display: inline-block;
  padding: 6px 16px;
  background: rgba(249, 115, 22, 0.15);
  color: #f97316;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
  margin-bottom: 20px;
  border: 1px solid rgba(249, 115, 22, 0.3);
}

.nm-hero-title {
  font-size: 48px;
  font-weight: 800;
  color: #fafaf9;
  margin-bottom: 16px;
}

.nm-hero-title span {
  background: linear-gradient(135deg, #f97316, #f59e0b, #eab308);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.nm-hero-desc {
  font-size: 20px;
  color: #a8a29e;
  max-width: 700px;
  margin: 0 auto 30px;
  line-height: 1.6;
}

.nm-hero-actions {
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
  background: linear-gradient(135deg, #f97316, #f59e0b);
  color: white;
  border: none;
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 30px rgba(249, 115, 22, 0.4);
}

.btn-secondary {
  background: #292524;
  color: #fafaf9;
  border: 1px solid #44403c;
}

.btn-secondary:hover {
  border-color: #f97316;
}

.nm-modes {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin: 40px 0;
}

.nm-mode-card {
  background: #1c1917;
  border: 1px solid #44403c;
  border-radius: 16px;
  padding: 28px;
  text-align: left;
  transition: all 0.3s;
  position: relative;
  overflow: hidden;
}

.nm-mode-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: var(--mode-color);
  opacity: 0;
  transition: opacity 0.3s;
}

.nm-mode-card:hover::before {
  opacity: 1;
}

.nm-mode-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(0,0,0,0.4);
  border-color: var(--mode-color);
}

.nm-mode-card.sniffer { --mode-color: #8b5cf6; }
.nm-mode-card.accesspoint { --mode-color: #06b6d4; }
.nm-mode-card.relay { --mode-color: #10b981; }
.nm-mode-card.router { --mode-color: #f97316; }

.nm-mode-icon {
  width: 60px;
  height: 60px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 30px;
  margin-bottom: 20px;
  background: rgba(255,255,255,0.05);
  border: 1px solid #44403c;
}

.nm-mode-card:hover .nm-mode-icon {
  background: var(--mode-color);
  border-color: var(--mode-color);
}

.nm-mode-title {
  font-size: 20px;
  font-weight: 700;
  color: #fafaf9;
  margin-bottom: 8px;
}

.nm-mode-desc {
  font-size: 14px;
  color: #a8a29e;
  margin-bottom: 16px;
  line-height: 1.6;
}

.nm-mode-features {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.nm-mode-feature {
  padding: 4px 12px;
  background: #292524;
  border-radius: 20px;
  font-size: 11px;
  color: #a8a29e;
}

.nm-section {
  margin: 60px 0;
}

.nm-section-title {
  font-size: 28px;
  font-weight: 700;
  color: #fafaf9;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.nm-section-desc {
  font-size: 16px;
  color: #a8a29e;
  margin-bottom: 30px;
}

.nm-demo-frame {
  border: 1px solid #44403c;
  border-radius: 16px;
  overflow: hidden;
  background: #0c0a09;
}

.nm-demo-frame iframe {
  width: 100%;
  height: 700px;
  border: none;
}

.nm-install-code {
  background: #0c0a09;
  border: 1px solid #44403c;
  border-radius: 12px;
  padding: 20px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 14px;
  overflow-x: auto;
  color: #a8a29e;
}

.nm-install-code .comment { color: #78716c; }
.nm-install-code .command { color: #f97316; }

.nm-features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.nm-feature-card {
  background: #1c1917;
  border: 1px solid #44403c;
  border-radius: 12px;
  padding: 24px;
}

.nm-feature-icon {
  font-size: 32px;
  margin-bottom: 12px;
}

.nm-feature-title {
  font-size: 16px;
  font-weight: 600;
  color: #fafaf9;
  margin-bottom: 8px;
}

.nm-feature-desc {
  font-size: 13px;
  color: #a8a29e;
  line-height: 1.5;
}

.nm-comparison-table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

.nm-comparison-table th,
.nm-comparison-table td {
  padding: 14px 16px;
  border: 1px solid #44403c;
  text-align: left;
}

.nm-comparison-table th {
  background: #292524;
  font-weight: 600;
  color: #fafaf9;
}

.nm-comparison-table td {
  background: #1c1917;
  color: #a8a29e;
}

.nm-comparison-table tr:hover td {
  background: #292524;
}

.nm-resources {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 16px;
}

.nm-resource-link {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 20px;
  background: #1c1917;
  border: 1px solid #44403c;
  border-radius: 10px;
  text-decoration: none;
  color: #fafaf9;
  transition: all 0.2s;
}

.nm-resource-link:hover {
  border-color: #f97316;
  background: #292524;
}

.nm-resource-icon {
  font-size: 24px;
}
</style>

<!-- Hero Section -->
<div class="nm-hero">
  <div class="nm-hero-badge">⚙️ LuCI Dashboard for OpenWrt</div>
  <h1 class="nm-hero-title">Network <span>Modes</span></h1>
  <p class="nm-hero-desc">
    Basculez instantanément entre Sniffer, Access Point, Relay et Router. 
    Configuration multi-mode simplifiée pour OpenWrt.
  </p>
  <div class="nm-hero-actions">
    <a href="https://github.com/gkerma/luci-app-network-modes" class="btn btn-primary" target="_blank">
      ⬇️ Télécharger
    </a>
    <a href="#demo" class="btn btn-secondary">
      🎮 Voir la Démo
    </a>
  </div>
</div>

<!-- Modes Grid -->
<div class="nm-section">
  <h2 class="nm-section-title">🎯 Quatre Modes, Un Dashboard</h2>
  <p class="nm-section-desc">Chaque mode est optimisé pour un usage spécifique avec les meilleures pratiques intégrées.</p>
  
  <div class="nm-modes">
    <div class="nm-mode-card sniffer">
      <div class="nm-mode-icon">🔍</div>
      <h3 class="nm-mode-title">Sniffer / Passthrough</h3>
      <p class="nm-mode-desc">Pont Ethernet transparent sans IP pour l'analyse passive du trafic avec Netifyd.</p>
      <div class="nm-mode-features">
        <span class="nm-mode-feature">No IP</span>
        <span class="nm-mode-feature">Promiscuous</span>
        <span class="nm-mode-feature">Netifyd</span>
        <span class="nm-mode-feature">Bridge</span>
      </div>
    </div>
    
    <div class="nm-mode-card accesspoint">
      <div class="nm-mode-icon">📶</div>
      <h3 class="nm-mode-title">Access Point</h3>
      <p class="nm-mode-desc">Point d'accès WiFi haute performance avec 802.11r/k/v et band steering.</p>
      <div class="nm-mode-features">
        <span class="nm-mode-feature">802.11r Roaming</span>
        <span class="nm-mode-feature">Band Steering</span>
        <span class="nm-mode-feature">Beamforming</span>
      </div>
    </div>
    
    <div class="nm-mode-card relay">
      <div class="nm-mode-icon">🔄</div>
      <h3 class="nm-mode-title">Relay / Extender</h3>
      <p class="nm-mode-desc">Extension réseau avec relayd et tunnel WireGuard optimisé.</p>
      <div class="nm-mode-features">
        <span class="nm-mode-feature">Relayd</span>
        <span class="nm-mode-feature">WireGuard</span>
        <span class="nm-mode-feature">MTU Opt</span>
        <span class="nm-mode-feature">MSS Clamp</span>
      </div>
    </div>
    
    <div class="nm-mode-card router">
      <div class="nm-mode-icon">🌐</div>
      <h3 class="nm-mode-title">Router</h3>
      <p class="nm-mode-desc">Routeur complet avec WAN, NAT, firewall, proxy et reverse proxy HTTPS.</p>
      <div class="nm-mode-features">
        <span class="nm-mode-feature">NAT</span>
        <span class="nm-mode-feature">Firewall</span>
        <span class="nm-mode-feature">Squid</span>
        <span class="nm-mode-feature">Nginx</span>
        <span class="nm-mode-feature">Let's Encrypt</span>
      </div>
    </div>
  </div>
</div>

<!-- Features -->
<div class="nm-section">
  <h2 class="nm-section-title">✨ Fonctionnalités</h2>
  
  <div class="nm-features-grid">
    <div class="nm-feature-card">
      <div class="nm-feature-icon">🎛️</div>
      <h4 class="nm-feature-title">Changement en Un Clic</h4>
      <p class="nm-feature-desc">Basculez entre les modes instantanément avec sauvegarde automatique de la configuration.</p>
    </div>
    <div class="nm-feature-card">
      <div class="nm-feature-icon">📊</div>
      <h4 class="nm-feature-title">Status Temps Réel</h4>
      <p class="nm-feature-desc">Visualisez l'état des interfaces réseau et des services en temps réel.</p>
    </div>
    <div class="nm-feature-card">
      <div class="nm-feature-icon">🔐</div>
      <h4 class="nm-feature-title">Configuration Sécurisée</h4>
      <p class="nm-feature-desc">Backup automatique avant chaque changement, rollback facile en cas de problème.</p>
    </div>
    <div class="nm-feature-card">
      <div class="nm-feature-icon">🌐</div>
      <h4 class="nm-feature-title">Reverse Proxy HTTPS</h4>
      <p class="nm-feature-desc">Exposez plusieurs services via Nginx/HAProxy avec Let's Encrypt automatique.</p>
    </div>
    <div class="nm-feature-card">
      <div class="nm-feature-icon">📶</div>
      <h4 class="nm-feature-title">WiFi Optimisé</h4>
      <p class="nm-feature-desc">802.11r/k/v pour le roaming, band steering, beamforming et airtime fairness.</p>
    </div>
    <div class="nm-feature-card">
      <div class="nm-feature-icon">🔄</div>
      <h4 class="nm-feature-title">WireGuard Intégré</h4>
      <p class="nm-feature-desc">Tunnel VPN optimisé avec MTU auto-adjustment et MSS clamping.</p>
    </div>
  </div>
</div>

<!-- Demo -->
<div class="nm-section" id="demo">
  <h2 class="nm-section-title">🎮 Démo Interactive</h2>
  <p class="nm-section-desc">Explorez l'interface sans installation. Cliquez sur les modes pour voir les options.</p>
  
  <div class="nm-demo-frame">
    <iframe src="/demos/network-modes/index.html" loading="lazy"></iframe>
  </div>
</div>

<!-- Comparison Table -->
<div class="nm-section">
  <h2 class="nm-section-title">📊 Comparaison des Modes</h2>
  
  <table class="nm-comparison-table">
    <thead>
      <tr>
        <th>Caractéristique</th>
        <th>🔍 Sniffer</th>
        <th>📶 Access Point</th>
        <th>🔄 Relay</th>
        <th>🌐 Router</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Adresse IP</strong></td>
        <td>Aucune</td>
        <td>DHCP Client</td>
        <td>Statique</td>
        <td>Statique</td>
      </tr>
      <tr>
        <td><strong>NAT</strong></td>
        <td>❌</td>
        <td>❌</td>
        <td>❌</td>
        <td>✅</td>
      </tr>
      <tr>
        <td><strong>Firewall</strong></td>
        <td>❌</td>
        <td>❌</td>
        <td>Minimal</td>
        <td>✅ Complet</td>
      </tr>
      <tr>
        <td><strong>DHCP Server</strong></td>
        <td>❌</td>
        <td>❌</td>
        <td>Optionnel</td>
        <td>✅</td>
      </tr>
      <tr>
        <td><strong>WiFi</strong></td>
        <td>❌</td>
        <td>✅ AP Optimisé</td>
        <td>✅ Client</td>
        <td>✅ AP</td>
      </tr>
      <tr>
        <td><strong>WireGuard</strong></td>
        <td>❌</td>
        <td>❌</td>
        <td>✅ Tunnel</td>
        <td>✅ Server</td>
      </tr>
      <tr>
        <td><strong>Proxy</strong></td>
        <td>❌</td>
        <td>❌</td>
        <td>❌</td>
        <td>✅ Squid</td>
      </tr>
      <tr>
        <td><strong>Reverse Proxy</strong></td>
        <td>❌</td>
        <td>❌</td>
        <td>❌</td>
        <td>✅ Nginx</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- Installation -->
<div class="nm-section">
  <h2 class="nm-section-title">📦 Installation</h2>
  
  <div class="nm-install-code">
    <span class="comment"># Cloner le repository</span><br>
    <span class="command">git clone https://github.com/gkerma/luci-app-network-modes.git</span><br><br>
    <span class="comment"># Installer les dépendances par mode</span><br>
    <span class="command">opkg install netifyd                    # Sniffer</span><br>
    <span class="command">opkg install hostapd-openssl            # Access Point</span><br>
    <span class="command">opkg install relayd wireguard-tools     # Relay</span><br>
    <span class="command">opkg install squid nginx-ssl acme       # Router</span><br><br>
    <span class="comment"># Installer le package</span><br>
    <span class="command">cd luci-app-network-modes</span><br>
    <span class="command">make install</span><br>
    <span class="command">/etc/init.d/rpcd restart</span>
  </div>
</div>

<!-- Resources -->
<div class="nm-section">
  <h2 class="nm-section-title">🔗 Ressources</h2>
  
  <div class="nm-resources">
    <a href="https://github.com/gkerma/luci-app-network-modes" class="nm-resource-link" target="_blank">
      <span class="nm-resource-icon">📦</span>
      <div>
        <strong>GitHub Repository</strong>
        <div style="font-size:12px;color:#78716c">Code source et issues</div>
      </div>
    </a>
    <a href="https://openwrt.org/docs/start" class="nm-resource-link" target="_blank">
      <span class="nm-resource-icon">📚</span>
      <div>
        <strong>OpenWrt Documentation</strong>
        <div style="font-size:12px;color:#78716c">Guide officiel</div>
      </div>
    </a>
    <a href="/dashboards" class="nm-resource-link">
      <span class="nm-resource-icon">🎛️</span>
      <div>
        <strong>Autres Dashboards</strong>
        <div style="font-size:12px;color:#78716c">CrowdSec, Netdata, Netifyd, WireGuard</div>
      </div>
    </a>
  </div>
</div>

---

<div style="text-align: center; margin-top: 40px; padding: 20px; background: #1c1917; border-radius: 12px;">
  <p style="color: #78716c; font-size: 14px;">
    Créé par <a href="https://cybermind.fr" style="color: #f97316;">Gandalf @ CyberMind.fr</a><br>
    Licence Apache-2.0
  </p>
</div>
