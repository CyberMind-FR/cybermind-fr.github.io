---
title: "CDN Cache Dashboard : Optimisez votre Bande Passante avec un Proxy Cache Local"
date: 2025-01-15
author: Gandalf
tags: [secubox, openwrt, cdn, cache, proxy, bandwidth, nginx]
categories: [SecuBox, OpenWrt, Networking]
image: /images/cdn-cache-hero.png
description: "Découvrez comment réduire votre consommation de bande passante de 40-60% avec un proxy cache local intégré à OpenWrt. Le 8ème module de la suite SecuBox."
---

# CDN Cache Dashboard : Optimisez votre Bande Passante

Après les 7 premiers modules de la suite SecuBox, je suis heureux de vous présenter le **8ème module** : **CDN Cache Dashboard**, un proxy cache local qui peut réduire votre consommation de bande passante de **40 à 60%**.

## 🎯 Le Problème : Téléchargements Redondants

Combien de fois avez-vous téléchargé les mêmes fichiers sur votre réseau ?

- **Windows Update** : Chaque PC télécharge les mêmes correctifs
- **Mises à jour Linux** : `apt update && apt upgrade` sur plusieurs machines
- **Applications mobiles** : Les mêmes APKs sur chaque téléphone
- **Ressources web** : jQuery, Bootstrap, polices Google téléchargés à chaque visite

Sur un réseau familial ou d'entreprise, ces téléchargements redondants peuvent représenter **des gigaoctets par mois** de bande passante gaspillée.

## 💡 La Solution : Cache Local Intelligent

CDN Cache Dashboard transforme votre routeur OpenWrt en **proxy cache intelligent** qui :

1. **Intercepte** les requêtes HTTP sortantes
2. **Stocke** les fichiers téléchargés localement
3. **Sert** les fichiers depuis le cache pour les requêtes suivantes
4. **Économise** bande passante et temps de téléchargement

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │────▶│  SecuBox    │────▶│  Internet   │
│  (1er DL)   │     │  CDN Cache  │     │   (100MB)   │
└─────────────┘     └──────┬──────┘     └─────────────┘
                          │
                    ┌─────▼─────┐
                    │   Cache   │
                    │  (100MB)  │
                    └───────────┘

┌─────────────┐     ┌─────────────┐
│   Client    │────▶│  SecuBox    │  ✗ Pas d'accès Internet
│  (2ème DL)  │◀────│  CDN Cache  │    Servi depuis le cache
└─────────────┘     └──────┬──────┘
                          │
                    ┌─────▼─────┐
                    │   Cache   │
                    │  (HIT!)   │
                    └───────────┘
```

## 📊 Résultats Réels

Sur mon réseau de test (5 PC, 8 mobiles, 2 tablettes) :

| Métrique | Avant | Après | Économie |
|----------|-------|-------|----------|
| Bande passante mensuelle | 120 GB | 52 GB | **-57%** |
| Temps Windows Update | 45 min | 8 min | **-82%** |
| Hit Ratio moyen | N/A | 73% | — |

## 🖥️ Dashboard Intuitif

### Vue Overview

Le dashboard principal affiche en temps réel :

- **Hit Ratio** : Pourcentage de requêtes servies depuis le cache
- **Économies** : Bande passante économisée en MB/GB
- **Cache utilisé** : Espace disque consommé vs disponible
- **Top domaines** : Quels sites bénéficient le plus du cache

### Vue Cache

Visualisez le contenu du cache :

- Liste des fichiers avec taille, âge, domaine
- Purge sélective par domaine
- Icônes par type de fichier (exe, deb, js, images...)

### Vue Policies

Configurez des règles de cache intelligentes :

```
┌─────────────────────────────────────────────────────┐
│ Policy: Windows Update                              │
├─────────────────────────────────────────────────────┤
│ Domaines: windowsupdate.com, download.microsoft.com│
│ Extensions: .exe .msu .cab .msi                     │
│ Durée cache: 7 jours                                │
│ Taille max: 2 GB                                    │
│ Priorité: 10 (haute)                                │
└─────────────────────────────────────────────────────┘
```

### Vue Statistics

Graphiques temporels pour analyser les tendances :

- Évolution du hit ratio (24h, 7j, 30j)
- Économies de bande passante cumulées
- Pics d'utilisation

### Vue Maintenance

Outils d'administration :

- **Purge complète** : Vider tout le cache
- **Purge expirés** : Nettoyer les fichiers périmés
- **Préchargement** : Télécharger une URL à l'avance
- **Logs** : Consulter l'activité du proxy

## 🔧 Policies Préconfigurées

Le module inclut des policies optimisées pour les cas d'usage courants :

### 1. Windows Update (Priorité haute)

```uci
config cache_policy 'windows_update'
    option enabled '1'
    option name 'Windows Update'
    option domains 'windowsupdate.com download.microsoft.com'
    option extensions 'exe msu cab msi'
    option cache_time '10080'  # 7 jours
    option max_size '2048'     # 2 GB max par fichier
```

### 2. Dépôts Linux

```uci
config cache_policy 'linux_repos'
    option enabled '1'
    option name 'Linux Repositories'
    option domains 'archive.ubuntu.com deb.debian.org mirrors.kernel.org'
    option extensions 'deb rpm pkg.tar.zst'
    option cache_time '4320'   # 3 jours
```

### 3. Applications Android

```uci
config cache_policy 'android_apps'
    option enabled '1'
    option name 'Android Apps'
    option domains 'play.googleapis.com'
    option extensions 'apk obb'
    option cache_time '10080'  # 7 jours
```

### 4. Contenu Web Statique

```uci
config cache_policy 'static_content'
    option enabled '1'
    option name 'Static Web Content'
    option domains '*'
    option extensions 'js css woff woff2 ttf png jpg jpeg gif svg ico webp'
    option cache_time '1440'   # 1 jour
```

## 🚫 Exclusions Intelligentes

Certains contenus ne doivent **jamais** être cachés :

```uci
config exclusion 'bypass_https'
    option enabled '1'
    option name 'HTTPS Banking'
    option domains 'bank paypal stripe'
    option reason 'Security sensitive'

config exclusion 'bypass_streaming'
    option enabled '1'
    option name 'Video Streaming'
    option domains 'netflix.com youtube.com twitch.tv'
    option reason 'Real-time content'
```

## 📦 Installation

### Prérequis

- OpenWrt 23.05+ avec LuCI
- Nginx (inclus comme dépendance)
- Espace disque disponible (recommandé : 1-4 GB)

### Installation

```bash
# Depuis les packages SecuBox
opkg update
opkg install luci-app-cdn-cache

# Redémarrer RPCD
/etc/init.d/rpcd reload
```

### Configuration minimale

```bash
# Activer et configurer
uci set cdn-cache.main.enabled=1
uci set cdn-cache.main.cache_size=2048  # 2 GB
uci set cdn-cache.main.listen_port=3128
uci commit cdn-cache

# Démarrer
/etc/init.d/cdn-cache start
/etc/init.d/cdn-cache enable
```

### Configuration des clients

**Option 1 : Proxy manuel**

Configurez chaque appareil pour utiliser le proxy :
- Adresse : `192.168.1.1` (IP du routeur)
- Port : `3128`

**Option 2 : Proxy transparent** (avancé)

Redirigez automatiquement le trafic HTTP :

```bash
# Redirection iptables
iptables -t nat -A PREROUTING -i br-lan -p tcp --dport 80 \
    -j REDIRECT --to-port 3128
```

## 🔬 Architecture Technique

Le module utilise **Nginx** comme moteur de cache :

```nginx
proxy_cache_path /var/cache/cdn levels=1:2 
    keys_zone=cdn_cache:64m 
    max_size=2048m 
    inactive=7d 
    use_temp_path=off;

location / {
    proxy_pass http://$host$request_uri;
    proxy_cache cdn_cache;
    proxy_cache_valid 200 1440m;
    proxy_cache_key $scheme$host$request_uri;
    add_header X-Cache-Status $upstream_cache_status;
}
```

### Avantages de Nginx

- **Performance** : Optimisé pour le caching
- **Mémoire** : Empreinte légère (~10-20 MB RAM)
- **Fiabilité** : Utilisé par les plus grands CDN
- **Flexibilité** : Configuration fine des règles

## 📈 Cas d'Usage

### 1. Famille avec plusieurs appareils

- 3 PC Windows, 2 Mac, smartphones
- Windows Update : téléchargé 1 fois, servi 3 fois
- Économie : ~500 MB par mois de correctifs

### 2. Bureau / PME

- 20 postes Windows
- Mises à jour Office 365, navigateurs, antivirus
- Économie : ~5-10 GB par mois

### 3. Établissement scolaire

- 50+ ordinateurs identiques
- Images système, logiciels éducatifs
- Économie : ~20-50 GB par mois

### 4. Café / Espace public WiFi

- Nombreux appareils de passage
- Ressources web statiques (JS, CSS, polices)
- Amélioration vitesse de navigation

## 🔗 Intégration SecuBox

CDN Cache s'intègre parfaitement avec les autres modules :

| Module | Intégration |
|--------|-------------|
| **System Hub** | Statistiques cache dans le dashboard central |
| **Netdata** | Métriques Nginx (connexions, hit rate) |
| **Netifyd** | Identification du trafic cacheable |
| **Client Guardian** | Cache différencié par groupe d'utilisateurs |

## 📊 Métriques Clés à Surveiller

1. **Hit Ratio** : Objectif > 60%
   - < 40% : Revoir les policies
   - 40-60% : Normal
   - > 60% : Excellent

2. **Utilisation Cache** : Éviter > 90%
   - Le cache plein force des évictions prématurées

3. **Top Domaines** : Identifier les opportunités
   - Domaines fréquents non cachés = ajouter policy

## 🎯 Conclusion

CDN Cache Dashboard est le **8ème module** de la suite SecuBox, complétant l'offre avec :

- ✅ Économies de bande passante significatives (40-60%)
- ✅ Accélération des téléchargements répétitifs
- ✅ Dashboard intuitif avec statistiques temps réel
- ✅ Policies préconfigurées pour les cas courants
- ✅ Architecture légère basée sur Nginx

## 📥 Téléchargement

- **GitHub** : [github.com/gkerma/luci-app-cdn-cache](https://github.com/gkerma/luci-app-cdn-cache)
- **Documentation** : [cybermind.fr/apps/cdn-cache](/apps/cdn-cache)
- **Démo interactive** : [cybermind.fr/apps/cdn-cache/demo](/apps/cdn-cache/demo)

---

*Prochain article : Intégration des 8 modules SecuBox dans un firmware OpenWrt unifié pour les appliances GlobalScale.*

**Tags** : #SecuBox #OpenWrt #CDN #Cache #Proxy #Nginx #BandwidthOptimization
