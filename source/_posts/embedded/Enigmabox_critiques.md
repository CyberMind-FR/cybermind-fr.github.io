---
title: "Enigmabox - critiques, limites et meilleures alternatives actuelles"
date: 2025-12-01 17:14:00
tags:
  - vpn
  - alternatives
  - sécurité
  - enigmabox
categories:
  - sécurité
  - analyse
---

Ce troisième billet examine les critiques formulées contre Enigmabox, puis propose des alternatives actuelles.
<!-- more -->
## Principaux problèmes rencontrés

- Support client considéré comme insuffisant.  
- Documentation peu claire ou incomplète.  
- Instabilité lors de mises à jour firmware.  
- Dépendance à des exit-servers non transparents.  
- Rapport qualité/prix faible par rapport à des VPN professionnels.  
- Complexité réelle plus élevée que la promesse « plug and play ».

## Le projet aujourd’hui

Le dispositif n'est plus activement soutenu et la communauté s'est largement dispersée. Les retours d'usagers évoquent un abandon progressif.

## Alternatives fiables en 2025

### 1. Solutions simples et éprouvées
- VPN de confiance **audités** (WireGuard/OpenVPN).  
- Chiffrement de bout en bout pour e-mails et messagerie.

### 2. Solutions techniques « maison »
- Un Raspberry Pi transformé en **routeur WireGuard**.  
- Un serveur VPN personnel sur un VPS (OpenBSD, Debian + WireGuard).

### 3. Solutions décentralisées
- Tor pour l’anonymat  
- Solutions mesh open-source maintenues (Tinc, Yggdrasil, cjdns forks)

## Conclusion

Enigmabox avait une vision ambitieuse : rendre la confidentialité facile et matérielle.  
Mais les limitations techniques, le manque de support et la fragilité opérationnelle ont limité son adoption.

Aujourd'hui, les alternatives modernes — plus transparentes, auditées et maintenues — offrent une protection fiable sans devoir dépendre d’un appareil propriétaire.

```
                 +---------------------+
                 |   Internet Public   |
                 +----------+----------+
                            |
               (1) Exit Server / Relay
                            |
                ┌───────────▼───────────┐
                │   Enigmabox Network   │  <-- Mesh overlay (cjdns / peers)
                │  (encrypted p2p links)│
                └───────┬───────┬───────┘
                        │       │
        ┌───────────────┘       └──────────────┐
        │                                      │
  [Local Services]                        [Mesh Peers]
  ┌──────────────┐                        ┌─────────┐
  │ Web / SSH    │                        │Peer X   │
  │ Mail (IMAP)  │                        │Peer Y   │
  │ DNS resolver │                        │Peer Z   │
  └─────┬────────┘                        └─────────┘
        │
   [Home LAN Router]
   ┌────┼───────────────┐
   │ PC │ Phone / Tablet│
   └────┴───────────────┘

Legend / Risks:
 - Traffic inside mesh: encrypted between peers (good).
 - Traffic via Exit Server: leaves trusted mesh -> requires trust in the exit operator.
 - Firmware / updates: if broken, could sever mesh or leak config.
```
