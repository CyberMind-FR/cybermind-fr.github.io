---
title: "Armbian Control Panel"
layout: portfolio
type: project
icon: 🐧
description: "Interface web d'administration pour Armbian, style LuCI/OpenWrt. Dashboard système, configuration réseau, gestion des services."
thumbnail: /images/portfolio/thumbnails/armbian-wui.svg
status: demo
featured: false
order: 3
tags_list:
  - armbian
  - linux
  - webui
  - administration
  - luci
project:
  type: "Interface Web"
  technologies:
    - HTML5
    - CSS3
    - JavaScript
    - Responsive
  duration: "Prototype"
  year: 2024
live_url: "/demos/armbian-wui.html"
---

## 🎯 Objectif

Créer une interface d'administration moderne pour Armbian, inspirée de LuCI (OpenWrt) mais avec un design plus contemporain et responsive.

## 📊 Dashboard

Le tableau de bord affiche en temps réel :

- **CPU** — Utilisation avec barre de progression
- **Mémoire** — RAM utilisée / totale
- **Température** — Monitoring thermique
- **Stockage** — Espace disque

## ⚙️ Fonctionnalités

### 🌐 Configuration Réseau
- Interfaces (eth0, wlan0)
- Adressage IP (DHCP/Statique)
- DNS et passerelle
- État des liens

### 📶 WiFi
- Configuration SSID
- Sécurité WPA2/WPA3
- Sélection de canal
- Mode AP/Client

### 🔧 Services
- SSH, Apache, Docker
- Démarrage/Arrêt/Redémarrage
- Activation au boot
- Statut en temps réel

### ⚡ Système
- Nom d'hôte
- Fuseau horaire
- Langue
- Redémarrage système

## 🎨 Design

- **Style LuCI** — Navigation familière pour les utilisateurs OpenWrt
- **Cards colorées** — Gradient moderne pour les stats
- **Responsive** — Adapté mobile/tablette/desktop
- **Sidebar** — Navigation par sections
