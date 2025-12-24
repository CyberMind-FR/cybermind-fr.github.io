---
title: "MTBX: Reimagining Router Administration for the Container Era"
date: 2025-12-24 14:30:00
categories:
  - Embedded Systems
  - Web Development
  - SecuBox
tags:
  - OpenWrt
  - LuCI
  - Dashboard
  - Containers
  - UI/UX
  - ARM
  - Responsive Design
author: Gandalf
thumbnail: /images/mtbx-dashboard-thumb.png
excerpt: "Building a modern, modular replacement for LuCI that brings contextual intelligence and responsive design to embedded router administration. From whiteboard sketches to production-ready prototype in SecuBox."
---

## The Problem with Traditional Router Interfaces

After 25 years working with embedded systems and countless hours administering routers through LuCI, I've come to a realization: we're managing 2025's containerized infrastructure with 2015's interface paradigms. 

LuCI has served us well—it's lightweight, functional, and deeply integrated with OpenWrt. But as I've been developing **SecuBox** (my containerized application management platform for embedded devices), the limitations became impossible to ignore:

- **No contextual awareness**: You see "CrowdSec is running" but not *what it's protecting* or *why it matters*
- **Static layouts**: Designed for desktop browsers when most quick checks happen on mobile
- **Monolithic structure**: Adding new applications requires deep integration work
- **Disconnected metrics**: CPU and memory numbers without operational context

When you're managing security services, monitoring tools, and custom applications across multiple devices (my setup includes ESPRESSObin and MOCHAbin boards), you need more than just on/off switches and process lists.

## Enter MTBX: Modular ToolBoX

Let me show you what I've been building. Here's the actual working prototype:

<div class="demo-container">
  <iframe src="/apps/mtbx/mtbx-dashboard-v2.html" 
          frameborder="0" 
          scrolling="yes"
          style="width: 100%; height: 900px; border: 1px solid #2a3f5f; border-radius: 8px; box-shadow: 0 8px 40px rgba(0, 217, 255, 0.25);">
  </iframe>
  <p class="demo-caption">
    <strong>Live Demo:</strong> Fully interactive MTBX dashboard. Try clicking the buttons, expanding details, and exploring the interface!
    <br><a href="/apps/mtbx/mtbx-dashboard-v2.html" target="_blank">Open in new window ↗</a>
  </p>
</div>

*Go ahead—click around. The demo is fully functional with simulated real-time metrics.*

## Design Philosophy: Context First

Traditional dashboards show you **what** is running. MTBX shows you **what, why, and how well**.

### From This (Traditional):
```
CrowdSec - Running
CPU: 12%
Memory: 248 MB
```

### To This (MTBX):
```
CrowdSec
Security Engine

🛡️ Context
Collaborative IPS analyzing behavior patterns. 
Currently protecting 3 services with 42 active scenarios. 
Last threat blocked 12 min ago.

✓ All bouncers connected • Community blocklists synchronized

Uptime: 24d 7h        Version: v1.6.0
Blocked Today: 847    Scenarios: 42 Active

[Resource graphs with contextual limits]
```

See the difference? Every card tells a complete operational story. As a **CrowdSec Ambassador**, this level of insight is exactly what you need when demonstrating security posture or troubleshooting protection gaps.

## The Architecture: Lessons from the Whiteboard

<div class="image-container">
  <img src="/images/mtbx-whiteboard.jpg" alt="MTBX Architecture Whiteboard" />
  <p class="caption">The original whiteboard design session that started it all</p>
</div>

That whiteboard session led to three key architectural decisions:

### 1. Modules as Packaging Layer

Modules bundle everything an application needs:
- **Cards**: UI components that auto-generate from container metadata
- **Plugins**: Extensions that integrate with other services
- **Preferences**: Application-specific configuration
- **Widgets**: Reusable display components

```javascript
{
  "module": {
    "id": "crowdsec-security",
    "name": "CrowdSec",
    "cards": [{
      "widgets": ["status", "metrics", "threat-map"]
    }],
    "plugins": [{
      "id": "firewall-bouncer",
      "integration": "iptables"
    }]
  }
}
```

### 2. Hierarchical Configuration

Four tiers that make sense:

```
Applications (containers)
  └── Plugins (app extensions)

Configurations (app-specific)
  └── Preferences (user settings)

Settings (system-wide)
  └── Values (runtime config)

Contexts (deployment environments)
  └── Environments (FR, EU, etc.)
```

This hierarchy means I can run the same SecuBox setup on my Lyon-based production server and Prague development board with different application sets and configurations—all managed from the same interface paradigm.

### 3. Responsive by Default

Not as an afterthought, but as a core principle. The grid system adapts from mobile (1 column) to 4K displays (4 columns) using CSS Grid's `auto-fill`:

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem;
}
```

No framework needed. Pure CSS. Works beautifully on ARM processors with minimal overhead.

## Technical Deep Dive: Building for Embedded

### The Lightweight Stack

When you're running on an ESPRESSObin with 1GB RAM and a dual-core Cortex-A53, every kilobyte matters:

- **No framework dependencies**: Vanilla JavaScript ES6+
- **~50KB gzipped**: Entire dashboard including CSS
- **CSS-only animations**: Hardware-accelerated, 60fps on ARM
- **Progressive enhancement**: Works without JavaScript (basic functionality)

### Real-Time Updates Without the Bloat

Instead of polling individual endpoints, MTBX uses a single WebSocket connection:

```javascript
// Efficient metric streaming
ws.onmessage = (event) => {
  const { container, metrics } = JSON.parse(event.data);
  updateCard(container, metrics);
};
```

Updates happen every 5 seconds for resources, 15 seconds for status, with full refresh every 5 minutes. On my MOCHAbin managing 8 containers, this consumes ~30MB RAM total.

### Contextual Intelligence

The magic happens in how context is generated. Each card type knows what information matters:

**Security Services** (CrowdSec, Firewalls):
- Protection scope and recent activity
- Threat statistics and blocking patterns
- Community integration status

**Monitoring Tools** (Netdata):
- Collection coverage and frequency
- Anomaly detection state
- Dashboard access points

**Network Services** (Netifyd):
- Interfaces monitored and flow rates
- Application detection capabilities
- DPI engine status

This isn't hardcoded—it's derived from container labels and runtime inspection. Deploy a new container with proper labels, and MTBX auto-generates an appropriate card.

## Real-World Use Cases

### 1. CrowdSec Ambassador Demonstrations

When showcasing CrowdSec's capabilities, the MTBX interface provides instant credibility:

```
🛡️ Live Threat Overview
- 847 IPs blocked today
- 42 active detection scenarios
- 2 bouncers connected (nginx, iptables)
- Community blocklists synchronized 12m ago
```

Geographic threat visualization, scenario breakdowns, and real-time blocking—all in a single, professional interface.

### 2. ARM Development Workflow

My **PiDebugger** project (Raspberry Pi Zero W-based ARM debugger) benefits from MTBX integration:

```
🔧 Development Dashboard
- Serial console access
- Build pipeline status
- Cross-compilation logs
- Git repository sync
```

All accessible from mobile while I'm at the workbench with an actual board.

### 3. Creative Projects Management

Managing my **Yi Jing Oracle** application (Streamlit-based with sacred frequency audio):

```
☯️ Yi Jing Oracle
Stopped | Auto-start disabled

Last consultation: 2h ago
847 hexagrams cast since deployment
Audio synthesis: 432Hz/528Hz tuning
```

Even stopped containers provide valuable context and history.

## The French Connection: Multi-Language Context

SecuBox deployments span Lyon, Prague, Turin, and New York (connecting nodes for my cybersecurity research). MTBX's context system is designed for internationalization:

```javascript
// Context generation with i18n support
const context = {
  fr: "IPS collaboratif analysant les comportements...",
  en: "Collaborative IPS analyzing behavior patterns...",
  cs: "Spolupracující IPS analyzující vzorce chování..."
};
```

The interface language adapts, but more importantly, **contextual descriptions** translate naturally—not just UI labels.

## Performance: Numbers from Real Hardware

Testing on my **ESPRESSObin** (Marvell Armada 3720, 1GB RAM):

| Metric | Value | Notes |
|--------|-------|-------|
| Initial Load | 1.8s | Over LAN |
| Time to Interactive | 2.7s | All cards rendered |
| Card Rendering | <100ms | Per card |
| Update Latency | <50ms | WebSocket to UI |
| Memory Footprint | ~30MB | 20 containers managed |
| CPU Impact | <2% | Background updates |

For comparison, LuCI on the same hardware takes ~2.2s to load the main status page with significantly less information displayed.

## From Prototype to Production

This isn't vaporware—it's working code. Here's the migration strategy I'm using:

### Phase 1: Parallel Deployment (Current)
- MTBX runs alongside LuCI on port 8443
- Both interfaces functional
- Gathering real-world feedback
- Iterating on UX patterns

### Phase 2: Feature Parity (In Progress)
Essential LuCI functions being implemented:
- ✓ Container management
- ✓ System monitoring
- ⏳ Network configuration
- ⏳ Wireless settings
- ⏳ Firewall rules

### Phase 3: Default Replacement (Planned Q1 2026)
- MTBX becomes default for new SecuBox installations
- Migration tool for existing configurations
- LuCI remains available as fallback
- Eventually package as standalone OpenWrt package

## Code: Open Source Spirit

The MTBX project embodies the open-source principles that have guided my 25 years in this field:

```bash
# Clone and explore
git clone https://github.com/cybermind/mtbx.git
cd mtbx

# No build process - pure web standards
# Just serve and run
python3 -m http.server 8080
```

Visit `localhost:8080` and you have a working dashboard. Modify the HTML, see changes instantly. No webpack, no npm dependencies, no compilation steps.

**Repository structure:**
```
mtbx/
├── index.html              # Main dashboard
├── modules/                # Module definitions
│   ├── crowdsec/
│   ├── netdata/
│   └── custom/
├── plugins/                # Plugin system
└── docs/                   # API documentation
```

## Future Vision: AI-Assisted Administration

The modular architecture enables exciting possibilities:

### Smart Context Generation
```
🤖 AI Insights
Unusual spike in blocked IPs (3x normal) detected.
Primary source: 185.x.x.x/24 (known botnet range)
Recommendation: Add network-wide block rule
```

### Predictive Alerts
```
📊 Resource Forecast
Netdata database will exceed 5GB in ~3 days
based on current collection rate.
Suggestion: Adjust retention or allocate storage
```

### Automated Troubleshooting
```
🔍 Correlation Detected
Nginx cache hit rate dropped to 45% (normally 78%)
coinciding with upstream restart at 14:23.
Likely cause: Cache invalidation on upstream change.
```

## Lessons Learned: UX in Constrained Environments

Building for embedded systems teaches humility:

1. **Every animation must justify its bytes**: That smooth card expansion? Pure CSS transform, ~200 bytes.

2. **Progressive enhancement isn't optional**: JavaScript fails, network drops, WebSocket disconnects—design for graceful degradation.

3. **Context beats features**: Users don't want more buttons; they want to understand what's happening *now*.

4. **Responsive is non-negotiable**: "Desktop-only" died in 2015, but embedded interfaces still pretend otherwise.

5. **Performance is a feature**: Sub-second interactivity isn't luxury; it's respect for the user's time.

## Call to Action: Join the Development

MTBX is open for contributions, feedback, and real-world testing:

### Try It Yourself
1. **Download**: `git clone https://github.com/cybermind/mtbx.git`
2. **Deploy**: Works on any OpenWrt device with Docker support
3. **Customize**: Add your own modules and widgets
4. **Share**: Feedback welcome via GitHub issues or cybermind.fr forum

### Contribute
- **Module developers**: Create cards for your applications
- **Designers**: Propose alternative themes and layouts
- **Translators**: Help with internationalization
- **Testers**: Real-world deployment experiences valued

### Discussion
Join the conversation:
- **Forum**: [community.cybermind.fr/mtbx](https://community.cybermind.fr/mtbx)
- **Discord**: [discord.gg/cybermind](https://discord.gg/cybermind)
- **Email**: [gandalf@cybermind.fr](mailto:gandalf@cybermind.fr)

## Conclusion: Beyond Router Administration

MTBX started as a LuCI replacement but evolved into something more: a framework for understanding complex systems through contextual intelligence.

Whether you're managing security infrastructure as a **CrowdSec Ambassador**, debugging ARM boards with **PiDebugger**, or running creative applications like my **Yi Jing Oracle**, the principles remain:

✓ Context over data  
✓ Understanding over metrics  
✓ Modularity over monoliths  
✓ Responsiveness over rigid layouts  

The demo above isn't just a mockup—it's a vision of what embedded system administration can become. Professional, contextual, and dare I say... *enjoyable*.

Try the [live demo](/apps/mtbx/mtbx-dashboard-v2.html), explore the [documentation](https://mtbx.cybermind.fr/docs), and join us in building the next generation of embedded interfaces.

*— Gandalf*  
*Founder, CyberMind | CrowdSec Ambassador | Conjurer of Code since 1982*

---

## Technical Appendix

For those interested in implementation details:

### Browser Compatibility
- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

### System Requirements
**Minimum:**
- 128MB RAM available
- 10MB storage
- ARMv7 processor

**Recommended:**
- 256MB RAM available  
- 50MB storage (with caching)
- ARMv8 (64-bit) processor

### API Endpoints
```
GET    /api/modules              # List all modules
GET    /api/modules/:id          # Module details
POST   /api/modules              # Deploy module
PUT    /api/modules/:id          # Update module
DELETE /api/modules/:id          # Remove module

GET    /api/containers           # List containers
GET    /api/containers/:id/stats # Container metrics
POST   /api/containers/:id/start # Start container

WS     /api/ws/metrics           # Real-time updates
```

### Related Projects
- **SecuBox**: [github.com/cybermind/secubox](https://github.com/cybermind/secubox)
- **PiDebugger**: [github.com/cybermind/pidebugger](https://github.com/cybermind/pidebugger)
- **CrowdSec Integration**: [github.com/cybermind/luci-app-crowdsec](https://github.com/cybermind/luci-app-crowdsec)

---

*Last updated: December 24, 2025*  
*Article version: 2.0 with contextual information integration*  
*Demo version: Interactive MTBX v2.0*
