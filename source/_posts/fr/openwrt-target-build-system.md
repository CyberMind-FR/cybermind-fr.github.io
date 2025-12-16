---
title: Système de build OpenWRT pour EnigmaBox
date: 2025-12-03 09:55:02
tags:
  - openwrt
  - build
  - firmware
categories:
  - contrib
---

# Système de Build OpenWRT

Le build OpenWRT constitue le cœur de la distribution EnigmaBox Suite.  
<!-- more -->
Il combine configuration, paquets standard et programmes personnalisés.

## Architecture générale
```
       Master
  +---------------+
  | packages 24.10|
  +---------------+
        |
     config
        |
+----------------+
| custom PRGs |
+----------------+
```

### **Master**
Base OpenWRT (snapshot ou stable).

### **Paquets 24.10**
Sélection précise de packages supportés.

### **Configuration**
- règles réseau  
- services  
- sécurisation  
- intégrations spécifiques Enigma  

### **Custom PRGs**
Développement interne :
- services additionnels  
- outils réseau  
- modules système  

---

## Objectifs du build

- Reproductibilité  
- Sécurité renforcée  
- Modularité (services activables)  
- Maintenabilité (intégration CI/CD)  


