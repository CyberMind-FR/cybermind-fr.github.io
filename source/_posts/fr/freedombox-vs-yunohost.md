---
title: "🏠 FreedomBox vs YunoHost : Comparatif des Solutions d'Auto-Hébergement"
date: 2025-12-16 14:50:00
categories:
  - Self-Hosting
  - Cybersécurité
tags:
  - FreedomBox
  - YunoHost
  - Auto-hébergement
  - Debian
  - Privacy
  - Serveur Personnel
  - Open Source
thumbnail: /images/self-hosting-comparison.png
description: "Comparatif détaillé entre FreedomBox et YunoHost, deux solutions d'auto-hébergement basées sur Debian pour reprendre le contrôle de vos données."
---

## 🌐 Introduction

Dans un monde où nos données personnelles sont devenues une monnaie d'échange pour les géants du web, l'auto-hébergement représente une voie vers la **souveraineté numérique**. Deux projets se distinguent particulièrement pour rendre cette démarche accessible aux non-experts : **🦋 FreedomBox** et **🦎 YunoHost**.

Ces deux solutions partagent une base commune — Debian GNU/Linux — mais divergent significativement dans leur philosophie, leur catalogue d'applications et leur public cible. Examinons leurs forces et faiblesses respectives.

<!-- more -->

## 🎯 Philosophie et Gouvernance

### 🦋 FreedomBox : La Vision d'Eben Moglen

FreedomBox est né en 2010 d'un discours prophétique d'Eben Moglen, professeur de droit à Columbia, intitulé "Freedom in the Cloud". Sa vision était claire : créer des serveurs personnels dont le but est de faciliter la communication libre entre les personnes, en toute sécurité, au-delà de l'ambition de surveillance des pouvoirs les plus puissants.

> « We're building software for smart devices whose engineered purpose is to work together to facilitate free communication among people, safely and securely, beyond the ambition of the strongest power to penetrate. »
> — Eben Moglen, 2010

**✨ Points clés :**

- 🏛️ **Statut officiel** : FreedomBox est un *Debian Pure Blend*, intégré officiellement dans Debian
- 🏢 **Organisation** : Soutenu par la [FreedomBox Foundation](https://freedomboxfoundation.org/) (non-profit)
- 💻 **Code source** : [salsa.debian.org/freedombox-team](https://salsa.debian.org/freedombox-team/freedombox/)
- 🔒 **Focus** : Protection de la vie privée, décentralisation du web

### 🦎 YunoHost : L'Approche Techno-Critique

YunoHost, projet français lancé en 2012, adopte une approche plus pragmatique et communautaire. Le nom est un jeu de mots sur "Why you no host?" (Pourquoi tu n'héberges pas ?).

**🌱 Valeurs affichées :**

- ✊ **Techno-critique** : Projet non-lucratif questionnant notre rapport au numérique
- 🌍 **Décentralisation** : Internet décentralisé avec technologies ouvertes et interopérables
- ♻️ **Sobriété** : Redonner de la matérialité au numérique, encourager le réemploi
- 👥 **Communauté** : Développé et maintenu par des bénévoles

**🔗 Ressources :**

- 🌐 **Site officiel** : [yunohost.org](https://yunohost.org/)
- 📦 **Catalogue d'apps** : [apps.yunohost.org](https://apps.yunohost.org/)
- 💻 **Code source** : [github.com/YunoHost](https://github.com/YunoHost)
- 💬 **Forum** : [forum.yunohost.org](https://forum.yunohost.org/)

## 📦 Catalogue d'Applications

C'est probablement la différence la plus significative entre les deux solutions.

### 🦋 FreedomBox : Qualité sur Quantité

FreedomBox propose environ **30-40 applications** soigneusement sélectionnées et intégrées. Le projet privilégie des applications légères, respectueuses de la vie privée.

**📋 Applications principales :**

| Catégorie | Applications |
|-----------|--------------|
| 💬 **Communication** | Matrix (Synapse), Ejabberd (XMPP), Mumble, Roundcube |
| 📁 **Partage de fichiers** | Syncthing, Samba, MiniDLNA |
| 🛡️ **VPN & Sécurité** | OpenVPN, WireGuard, Tor, Privoxy, Shadowsocks |
| 🌐 **Web & Wiki** | MediaWiki, WordPress, Ikiwiki |
| 🔄 **Synchronisation** | Radicale (CalDAV/CardDAV) |
| 📰 **Agrégation RSS** | Tiny Tiny RSS |
| 🔍 **Métamoteur** | SearX |
| 🎮 **Jeux** | Minetest |

📚 **Documentation** : [wiki.debian.org/FreedomBox/Features](https://wiki.debian.org/FreedomBox/Features)

### 🦎 YunoHost : L'Abondance Communautaire

YunoHost propose un catalogue de **500+ applications** maintenues par la communauté, classées par catégories :

| Catégorie | Exemples d'Applications |
|-----------|------------------------|
| 🔄 **Synchronisation** | Nextcloud, Baïkal, Syncthing |
| 📝 **Publication** | WordPress, Ghost, Grav, MediaWiki, BookStack |
| 💬 **Communication** | Matrix (Synapse/Conduit), Element, Mattermost, Discourse, Jitsi Meet |
| 📊 **Bureau** | CryptPad, Collabora Online, HedgeDoc, Etherpad, Excalidraw |
| 📈 **Productivité** | Kanboard, Dolibarr, Invoice Ninja, Firefly III |
| 🎬 **Multimédia** | Jellyfin, Funkwhale, PeerTube, Immich, Audiobookshelf |
| 🐘 **Réseaux sociaux** | Mastodon, PeerTube, Lemmy, Mobilizon, GoToSocial |
| 📖 **Lecture** | FreshRSS, Miniflux, Calibre-web, Wallabag |
| ⚙️ **Outils système** | Borg Backup, Headscale, AdGuard Home, Grafana |
| 🛠️ **Développement** | Forgejo, GitLab, Jenkins, code-server |

📦 **Catalogue complet** : [apps.yunohost.org/catalog](https://apps.yunohost.org/catalog)

## 🖥️ Interface et Facilité d'Utilisation

### 🦋 FreedomBox : Plinth

L'interface web de FreedomBox, appelée **Plinth**, est minimaliste et fonctionnelle :

- ✅ Installation d'applications en quelques clics
- 🌐 Configuration réseau simplifiée (Pagekite, Let's Encrypt, firewall)
- 👤 Gestion des utilisateurs intégrée
- 🌍 Interface disponible en 16 langues

🎮 **Démo en ligne** : [freedombox.org/demo/](https://freedombox.org/demo/)

### 🦎 YunoHost : Webadmin Moderne

YunoHost propose une interface d'administration web plus riche :

- 🔐 **SSO (Single Sign-On)** : Connexion unique pour toutes les applications
- 🚪 **Portail utilisateur** : Interface personnalisée pour accéder aux apps
- ⚡ **Installation en un clic** : Déploiement automatisé avec formulaires de configuration
- ⚙️ **Panneau de configuration** : Réglages spécifiques par application
- 🩺 **Diagnostics intégrés** : Vérification automatique de la configuration
- 🌐 **Gestion DNS** : Configuration automatique des enregistrements

🎮 **Démo** : [doc.yunohost.org/try](https://doc.yunohost.org/try)

## 🔧 Matériel Supporté

Les deux solutions fonctionnent sur du matériel modeste.

### 🦋 FreedomBox

| Type | Exemples |
|------|----------|
| 🍇 **SBC officiellement supportés** | Olimex A20 OLinuXino Lime 2, BeagleBone Black, Raspberry Pi |
| 📦 **Pioneer Edition** | Kit complet pré-installé (~60-70€) vendu par [Olimex](https://www.olimex.com/) |
| 🖥️ **PC x86** | Tout ordinateur compatible Debian |
| ☁️ **VPS** | Installation possible sur serveur cloud |

⬇️ **Téléchargement** : [freedombox.org/download/](https://freedombox.org/download/)

### 🦎 YunoHost

| Type | Support |
|------|---------|
| 🍓 **Raspberry Pi** | 3, 4, 400, 5 (images pré-construites) |
| 🔌 **Cartes ARM** | Diverses (avec images Armbian) |
| 🦕 **"Ordinosaures"** | Vieux PC de bureau ou portables |
| ☁️ **VPS** | OVH, Scaleway, Digital Ocean, etc. |

📖 **Guide d'installation** : [doc.yunohost.org/install](https://doc.yunohost.org/install)

## 🔄 Stabilité et Maintenance

### 🦋 FreedomBox : La Stabilité Debian

- 📦 **Mises à jour** : Via les dépôts Debian stable
- 🐢 **Approche conservatrice** : Moins d'applications = moins de conflits potentiels
- 🤖 **Mises à jour automatiques** : Gérées par le système Debian
- 💾 **Sauvegardes** : Fonctionnalité intégrée

### 🦎 YunoHost : Dynamisme et Risques

- 🚀 **Mises à jour fréquentes** : Cycle de release plus rapide
- 📌 **Version actuelle** : YunoHost 12.1 (basé sur Debian Bookworm), version 13 (Trixie) en bêta
- ⚠️ **Risque de régression** : Plus élevé avec le grand nombre d'applications
- 💾 **Sauvegardes** : Système centralisé avec support Borg

> ⚠️ **Note importante** : Certains utilisateurs de YunoHost rapportent des difficultés lors de mises à jour complexes, notamment avec des applications ayant beaucoup de dépendances.

## ⚖️ Comparatif Synthétique

| Critère | 🦋 FreedomBox | 🦎 YunoHost |
|---------|------------|----------|
| **Base** | Debian Pure Blend | Distribution Debian |
| **Catalogue** | ~40 apps curées | 500+ apps communautaires |
| **Focus** | Vie privée, communication sécurisée | Polyvalence, auto-hébergement généraliste |
| **Stabilité** | ⭐⭐⭐⭐⭐ Très stable | ⭐⭐⭐ Variable selon les apps |
| **Interface** | Minimaliste | Riche et moderne |
| **SSO** | Partiel | Complet |
| **Communauté** | 🌍 Internationale, anglophone | 🇫🇷 Très active, francophone |
| **Documentation** | Wiki Debian | Documentation dédiée complète |
| **Difficulté** | 🔧 Légèrement plus technique | 👶 Plus accessible |
| **Idéal pour** | Serveur personnel stable, focus privacy | Association, PME, expérimentation |

## 🎯 Pour Qui ?

### ✅ Choisir FreedomBox si :

- 🔒 Vous voulez une solution **stable et minimaliste**
- 🛡️ Votre priorité est la **vie privée et les communications sécurisées**
- 🐧 Vous préférez l'intégration **pure Debian**
- 🍇 Vous avez du **matériel ARM limité** (les apps sont légères)
- 😴 Vous souhaitez **peu de maintenance** à long terme

### ✅ Choisir YunoHost si :

- 📦 Vous voulez un **large choix d'applications**
- 🏢 Vous hébergez des services pour une **association ou une petite structure**
- ✨ Vous appréciez une **interface moderne** et le SSO
- 🧪 Vous voulez **tester et comparer** plusieurs solutions
- 🔧 Vous êtes à l'aise avec une **maintenance plus active**

## 📚 Ressources Complémentaires

### 🦋 FreedomBox

| Ressource | Lien |
|-----------|------|
| 🌐 Site officiel | [freedombox.org](https://freedombox.org/) |
| 🏛️ Foundation | [freedomboxfoundation.org](https://freedomboxfoundation.org/) |
| 📖 Wiki Debian | [wiki.debian.org/FreedomBox](https://wiki.debian.org/FreedomBox) |
| 📚 Manuel | [wiki.debian.org/FreedomBox/Manual](https://wiki.debian.org/FreedomBox/Manual) |
| 💬 Forum | [discuss.freedombox.org](https://discuss.freedombox.org/) |
| 💬 Matrix | [#freedombox:matrix.org](https://matrix.to/#/#freedombox:matrix.org) |
| 📱 App Android | [F-Droid](https://f-droid.org/en/packages/org.freedombox.freedombox/) |

### 🦎 YunoHost

| Ressource | Lien |
|-----------|------|
| 🌐 Site officiel | [yunohost.org](https://yunohost.org/) |
| 📖 Documentation | [doc.yunohost.org](https://doc.yunohost.org/) |
| 📦 Catalogue d'apps | [apps.yunohost.org](https://apps.yunohost.org/) |
| 💬 Forum | [forum.yunohost.org](https://forum.yunohost.org/) |
| 💻 Code source | [github.com/YunoHost](https://github.com/YunoHost) |
| 🐘 Mastodon | [@yunohost@toot.aquilenet.fr](https://toot.aquilenet.fr/@yunohost) |
| 💝 Faire un don | [donate.yunohost.org](https://donate.yunohost.org/) |

## 🏁 Conclusion

FreedomBox et YunoHost représentent deux approches complémentaires de l'auto-hébergement. Le premier mise sur la **stabilité et la protection de la vie privée** avec un catalogue restreint mais solide. Le second offre une **flexibilité maximale** avec un écosystème d'applications impressionnant.

Pour un consultant en cybersécurité ou un passionné de Linux, les deux solutions méritent d'être testées :

- 🦋 **FreedomBox** pour un serveur personnel discret et stable
- 🦎 **YunoHost** pour des projets nécessitant une variété de services

L'essentiel est de **reprendre le contrôle de ses données** 🔐 — et ces deux projets le permettent admirablement.

---

*🧙‍♂️ Article rédigé pour [CyberMind.FR](https://cybermind.fr) — Décembre 2025*
