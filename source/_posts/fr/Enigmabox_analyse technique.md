---
title: "Enigmabox - analyse technique du réseau privé chiffré"
date: 2025-12-01 17:12:00
tags:
  - mesh
  - vpn
  - cjdns
  - enigmabox
categories:
  - technique
  - réseau
---

Ce deuxième billet détaille le fonctionnement interne d'Enigmabox, ses objectifs réseaux et les technologies utilisées.
<!-- more -->
## Réseau mesh chiffré

Le cœur du système reposait sur un réseau **pair-à-pair chiffré**, basé sur des technologies comparables à **cjdns** :

- attribution d’adresses IPv6 cryptographiquement dérivées des clés publiques,  
- routage automatique entre pairs,  
- cryptage intégré dans les communications internes.

## Les « exit servers »

Pour accéder à Internet public, Enigmabox utilisait des serveurs relais appelés « exit servers » :

- ils sortaient le trafic vers le Web classique ;
- ils masquaient l’adresse IP réelle de l’utilisateur ;
- mais ils introduisaient une **zone de confiance obligatoire**.

## Fonctionnalités techniques dérivées

- tunnel VPN transparent pour protéger la navigation,  
- résolution DNS interne au mesh,  
- service d’hébergement web local accessible dans le réseau privé,  
- possibilité de services pair-à-pair entre propriétaires d’Enigmabox.

## Limites structurelles

- dépendance à des serveurs opérés par un tiers ;  
- stabilité variable ;  
- nécessité d'une maintenance continue pour rester fiable ;  
- configuration parfois complexe malgré la promesse de simplicité.

Ce système hybride (VPN + mesh + appliances) était ambitieux, mais difficile à maintenir dans le temps.

```
           ╔════════════╗
           ║ Internet   ║
           ╚════╤═══════╝
                │
         ┌──────┴──────┐
         │ Exit Server │   (relay -> Internet public)
         └──────┬──────┘
                │ encrypted tunnel / NAT
       ┌────────┴────────┐
       │   Mesh Backbone │  (cjdns / p2p overlay)
       └────────┬────────┘
  Peer A  Peer B│   Peer C
   ╲   ╱   ╲  ╱  │   ╱  ╲
    ╲╱     ╲╱   ╰─╴╱    ╲
     ╔════════════════════════╗
     ║       Enigmabox        ║  (local node in mesh)
     ╚════════════════════════╝
       ┌───┬───────────────┬───┐
       │WG │ DNS resolver  │SSH│
       │tunnel (WireGuard)│/Web│
       └───┴───────────────┴───┘
           │
     [Home Router / LAN]
      ┌────┴────┐
      │Clients  │
      └─────────┘
```
