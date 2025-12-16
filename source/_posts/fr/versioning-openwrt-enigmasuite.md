---
title: Gestion des versions – OpenWRT & Enigma Suite
date: 2025-12-03 08:55:00
tags:
  - openwrt
  - versioning
  - devops
categories:
  - contrib
---

# Gestion des versions : Upstream, Frozen, Tags

L’architecture Enigma Suite s’appuie sur OpenWRT et nécessite une stratégie claire de gestion des sources.
<!-- more -->
## Branches principales

### **1. Upstream**
Code directement issu du projet OpenWRT.
- Synchronisation régulière  
- Import des nouveautés  
- Suivi des correctifs de sécurité  

### **2. Frozen**
Version figée utilisée pour :
- stabiliser les features  
- garantir la reproductibilité  
- assurer des builds cohérents pour les devices  

### **3. Tags**
Points fixes pour :
- releases  
- debug  
- reproductibilité exacte des binaires  

---

## Services liés au versioning

- **Live custom servers**
- **CJDNS (configs externes ?)**
- **TOR (intégration optionnelle)**

Ces services peuvent être activés ou désactivés selon les branches, et intégrés dans les images finales.

