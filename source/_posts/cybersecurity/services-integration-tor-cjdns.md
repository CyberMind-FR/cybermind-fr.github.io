---
title: Intégration des services réseau (TOR, CJDNS, Serveurs custom)
date: 2025-12-03 09:55:04
tags:
  - tor
  - cjdns
  - networking
  - privacy
categories:
  - contrib
---

# Intégration des Services Réseau

La distribution Enigma Suite intègre plusieurs services avancés orientés confidentialité et résilience.
<!-- more -->
## Services majeurs

### **1. Live Custom Servers**
Serveurs gérés côté infrastructure :
- accès externes  
- VPN / overlay  
- synchronisation réseau  

### **2. CJDNS**
Possibilité d’intégration avec configurations externes.

Points ouverts :
- gestion centralisée ?  
- injection automatique des configs ?

### **3. TOR**
Support optionnel pour :
- anonymisation du trafic  
- services cachés  
- passerelles TOR relay  

---

## Notes d’intégration

- Chaque service doit pouvoir être activé/désactivé selon les versions (Frozen / Tag / Upstream).  
- Le design vise un haut niveau de sécurité sans sacrifier la simplicité.  

