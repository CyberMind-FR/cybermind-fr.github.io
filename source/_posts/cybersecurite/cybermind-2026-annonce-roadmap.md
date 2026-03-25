---
title: "CyberMind 2026 — Bilan, Rework UI & Roadmap"
date: 2026-03-25 10:00:00
categories:
  - Projets
  - Cybersecurite
tags:
  - CyberMind
  - SecuBox
  - 2026
  - Roadmap
  - HamHash
  - KRE360
  - OpenSource
  - Debian
  - ZKP
excerpt: "Annonce 2026 : nouveau colorset CRT/SecuBox, migration SecuBox-Deb (base Debian), architecture GK·HAM-HASH ZKP 3 niveaux, KRE-360 et roadmap du lab CyberMind."
---

<style>
/* Article styles inline SecuBox Deck */
.cm-article-hero {
  background: linear-gradient(135deg, #050810 0%, #0d1425 100%);
  border: 1px solid rgba(0,229,255,0.15);
  border-left: 4px solid #c23b22;
  padding: 28px 32px;
  margin: 0 0 32px;
  font-family: 'IBM Plex Mono', monospace;
}
.cm-article-hero h2 {
  font-family: 'Cinzel', serif !important;
  color: #c8a84b !important;
  font-size: 1.4rem !important;
  margin: 0 0 8px !important;
  letter-spacing: 0.06em !important;
}
.cm-article-hero p {
  color: #7a9ab8 !important;
  font-size: 13px !important;
  line-height: 1.7 !important;
  margin: 0 !important;
}
.cm-status-row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin: 20px 0;
}
.cm-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 12px;
  border: 1px solid rgba(0,229,255,0.2);
  background: rgba(0,229,255,0.05);
  font-size: 11px;
  font-family: 'IBM Plex Mono', monospace;
  letter-spacing: 0.08em;
  color: #7a9ab8;
}
.cm-badge.live  { border-color: rgba(0,255,65,0.3); color: #00c832; background: rgba(0,255,65,0.05); }
.cm-badge.build { border-color: rgba(200,168,75,0.3); color: #c8a84b; background: rgba(200,168,75,0.05); }
.cm-badge.wip   { border-color: rgba(194,59,34,0.3); color: #c23b22; background: rgba(194,59,34,0.05); }
.cm-section-label {
  font-size: 10px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #c23b22;
  margin-bottom: 8px;
  font-family: 'IBM Plex Mono', monospace;
}
.cm-section-label::before { content: '// '; color: #4a6080; }
.cm-divider {
  border: none;
  border-top: 1px solid rgba(0,229,255,0.12);
  margin: 32px 0;
}
.cm-terminal-block {
  background: #080d18;
  border: 1px solid rgba(0,229,255,0.13);
  border-left: 3px solid #00e5ff;
  padding: 16px 20px;
  font-family: 'Share Tech Mono', 'Courier New', monospace;
  font-size: 12px;
  color: #00c832;
  margin: 16px 0;
  line-height: 2;
}
.cm-terminal-block .t-prompt { color: #00e5ff; }
.cm-terminal-block .t-cmd    { color: #e8c96a; }
.cm-terminal-block .t-out    { color: #7a9ab8; }
.cm-arch-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 12px;
  margin: 20px 0;
}
.cm-arch-card {
  background: #080d18;
  border: 1px solid rgba(0,229,255,0.13);
  border-top: 2px solid #00e5ff;
  padding: 16px 18px;
}
.cm-arch-card.gold { border-top-color: #c8a84b; }
.cm-arch-card.red  { border-top-color: #c23b22; }
.cm-arch-card h4 {
  font-family: 'Cinzel', serif;
  font-size: 13px;
  color: #c8a84b;
  margin: 0 0 8px;
  letter-spacing: 0.06em;
}
.cm-arch-card p {
  font-size: 11px;
  color: #7a9ab8;
  line-height: 1.6;
  margin: 0;
}
</style>

<div class="cm-article-hero">
  <h2>CyberMind Security Lab · Q1 2026</h2>
  <p>Annonce de rework UI, migration infrastructure, nouvelles architectures cryptographiques et projets actifs en cours. Document de reference pour le lab CyberMind · Savoie · France.</p>
</div>

<div class="cm-section-label">ETAT DES PROJETS</div>

<div class="cm-status-row">
  <span class="cm-badge live">SecuBox-Deb LIVE</span>
  <span class="cm-badge live">Tailscale ACTIVE</span>
  <span class="cm-badge build">HamCoin ZKP BUILD</span>
  <span class="cm-badge build">KRE-360 WIP</span>
  <span class="cm-badge live">ALERTE·DEPOT LIVE</span>
  <span class="cm-badge wip">UI Rework 2026</span>
</div>

<hr class="cm-divider">

## Rework UI — Nouveau Colorset CRT/SecuBox

CyberMind.fr adopte un nouveau langage visuel coherent avec l'interface SecuBox, l'esthetique des dashboards LuCI, et l'identite **CyberMind** developpee depuis plusieurs annees.

<div class="cm-section-label">PALETTE</div>

Le colorset **SecuBox Deck** s'articule autour de quatre registres :

- **Cosmos-black** (`#050810` → `#0d1425`) — fonds en couches, profondeur CRT
- **Phosphor-gold** (`#c8a84b` / `#e8c96a`) — titres Cinzel, elements primaires
- **Cinnabar** (`#c23b22`) — accents alerte, bordures actives, CTA
- **Cyan phosphore** (`#00e5ff`) — liens, etats live, accents tech

Les scanlines CRT et la vignette phosphore sont appliquees en CSS pur via `body::before` / `body::after`, sans JavaScript.

**Typographie :**
- `Cinzel` — titres, logo, metriques principales (serif lapidaire)
- `IBM Plex Mono` — corps de texte, navigation, descriptions
- `Share Tech Mono` — blocs terminaux, outputs systeme

<hr class="cm-divider">

## Migration SecuBox vers Base Debian

<div class="cm-section-label">INFRASTRUCTURE</div>

SecuBox-OpenWrt est **abandonne**. La nouvelle base est **SecuBox-Deb** sur Debian stable.

<div class="cm-terminal-block">
<span class="t-prompt">gandalf@secubox-deb</span> ~ <span class="t-cmd">$ systemctl status secubox tailscale</span><br>
<span class="t-out">secubox.service — CyberMind Security Platform · ACTIVE (running)</span><br>
<span class="t-out">tailscaled.service — Tailscale VPN · ACTIVE (running)</span><br>
<span class="t-prompt">gandalf@secubox-deb</span> ~ <span class="t-cmd">$ uname -r</span><br>
<span class="t-out">6.1.0-28-arm64 · Marvell Armada A8040 · MOCHAbin</span>
</div>

**Motivations de la migration :**

La base OpenWrt, bien qu'excellente pour le routage embarque, imposait des contraintes importantes sur le stack applicatif (packaging, Python, conteneurs, LLM locaux). Debian offre une surface de deploiement standard, la compatibilite systemd native, et l'integration directe avec Tailscale, Docker et le reste de l'outillage SecuBox.

L'ensemble du stack — CrowdSec, HAProxy, nftables, Tailscale, WireGuard, netifyd/nDPId, mitmproxy — est desormais operationnel sur base Debian, avec une meilleure isolation des services.

<hr class="cm-divider">

## GK·HAM-HASH — Architecture ZKP 3 Niveaux

<div class="cm-section-label">CRYPTOGRAPHIE</div>

Le framework **GK·HAM-HASH** (papier academique GK-HAM-2025) implemente une architecture d'authentification et de routage a 3 couches, basee sur la NP-completude des cycles hamiltoniens.

<div class="cm-arch-grid">
  <div class="cm-arch-card">
    <h4>L1 · Auth Twins</h4>
    <p>Prover / Verifier asymetriques. NIZKProof hamiltonien, rotation G 24h, Perfect Forward Secrecy.</p>
  </div>
  <div class="cm-arch-card gold">
    <h4>L2 · Routing Twins</h4>
    <p>Double-buffer active/shadow. Atomic swap conditionne ZKP, rollback 4R, conformite CSPN.</p>
  </div>
  <div class="cm-arch-card red">
    <h4>L3 · Endpoint Twins</h4>
    <p>Service/Witness MirrorNet P2P. did:plc, WireGuard, Chain of Hamiltonians vers HamCoin, notarisation aveugle ALERTE·DEPOT.</p>
  </div>
</div>

Chaque paire de twins implemente des roles asymetriques complementaires avec separation de privileges formelle par couche. La propriete principale est qu'un attaquant compromettant L1 ne peut pas remonter aux secrets L2/L3 sans resoudre un probleme NP-complet different a chaque niveau.

<hr class="cm-divider">

## Projets Actifs Q1/Q2 2026

<div class="cm-section-label">ROADMAP</div>

**KRE-360 / RESPIRE·CUBES·25** — Systeme de tuiles hexagrammes Yi Jing en cube, en collaboration avec Anibal Edelberto Amiot. Matrice hexagonale 360, axes AKR, correspondances Yi Jing / Kabbale. Dossier GANIMED en cours.

**MAGIC·CHESS·360** — Application canvas animee avec tuiles hexagrammes Yi Jing, reactivite audio, moteur de couleurs TAO PRISM. Architecture double-buffer, sync audio FFT.

**HERMES·360** — Oracle Yi Jing complet (64 hexagrammes, traductions Wilhelm FR), modes de tirage multiples. Deploye sur `cybermind.fr/apps`.

**ALERTE·DEPOT** — Plateforme whistleblower avec pipeline OSINT CC-OSINT (Common Crawl). Notarisation aveugle via chaine hamiltonienne HamCoin.

**Ham-Hash / HamCoin** — Publication academique GK-HAM-2025, implementation de reference du framework ZKP hamiltonien. Soumission en cours.

**Association Cordeliers de La Chambre** — Travaux de preservation du patrimoine pour le Couvent des Cordeliers (Maurienne, Savoie). Dossiers Mission Patrimoine, catalogage archivistique.

<hr class="cm-divider">

## Infrastructure Lab

<div class="cm-section-label">HARDWARE</div>

| Plateforme | CPU | Role | OS |
|---|---|---|---|
| Globalscale **MOCHAbin** | Marvell Armada A8040 | SecuBox-Deb principal | Debian arm64 |
| Globalscale **ESPRESSObin** | Marvell Armada A3720 | Edge / test | Debian arm64 |
| **GK2.NET ISP** | Pentium Pro vers ARM | FAI personnel historique | Linux |

Contributeur Linux kernel — drivers SD/MMC pour plateformes Marvell ARM (`mmc: sdhci-xenon`).

<hr class="cm-divider">

<div class="cm-section-label">CONTACT</div>

> **Gerald Kerma (aka Gandalf)** · CyberMind · Notre-Dame-du-Cruet, Savoie
> GitHub : [CyberMind-FR](https://github.com/CyberMind-FR)
> Patreon : [patreon.com/cybermind](https://patreon.com/cybermind)
> PayPal : [paypal.me/Kerma](https://paypal.me/Kerma)

---

*Article genere le 25 mars 2026 · CyberMind Security Lab · Tous droits reserves*
