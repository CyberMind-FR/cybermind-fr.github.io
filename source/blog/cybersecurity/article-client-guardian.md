---
title: "Client Guardian : NAC & Portail Captif Nouvelle Génération pour OpenWrt"
date: 2024-12-20
categories: [OpenWrt, LuCI, Security, Networking]
tags: [openwrt, luci, nac, captive-portal, parental-control, security, network]
author: Gandalf
image: /images/client-guardian-hero.png
description: "Un système complet de contrôle d'accès réseau avec quarantaine automatique, portail captif, contrôle parental et alertes SMS/Email pour OpenWrt."
---

# Client Guardian : Reprenez le Contrôle de Votre Réseau

Dans un monde où chaque appareil veut se connecter à votre réseau, comment distinguer les légitimes des intrus ? **Client Guardian** apporte la réponse avec un système de contrôle d'accès réseau (NAC) moderne et un portail captif nouvelle génération.

## 🎯 Le Problème

Votre réseau domestique ou d'entreprise fait face à plusieurs défis :

- **Appareils inconnus** qui se connectent sans votre accord
- **Objets IoT** qui devraient être isolés mais ne le sont pas
- **Enfants** qui accèdent à du contenu inapproprié
- **Invités** qui ont accès à tout votre réseau local
- **Aucune visibilité** sur qui est connecté et fait quoi

## 💡 La Solution : Quarantaine par Défaut

Client Guardian inverse le paradigme traditionnel :

> **Par défaut, tout nouveau client est ISOLÉ jusqu'à approbation explicite.**

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Nouvel Appareil│────►│   QUARANTAINE   │────►│    DÉCISION     │
│  Se Connecte    │     │   (Isolation)   │     │  Admin requise  │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
                              ┌──────────────────────────┼──────────────────────────┐
                              │                          │                          │
                              ▼                          ▼                          ▼
                    ┌─────────────────┐        ┌─────────────────┐        ┌─────────────────┐
                    │   ✅ APPROUVER   │        │   ⏳ ATTENDRE    │        │   🚫 BANNIR     │
                    │   Assigner Zone  │        │   Rester Isolé  │        │   Bloquer MAC   │
                    └─────────────────┘        └─────────────────┘        └─────────────────┘
```

## 🏠 Six Zones de Sécurité

### 1. LAN Privé 🏠
Votre réseau de confiance avec accès complet.
- ✅ Internet illimité
- ✅ Accès au réseau local
- ✅ Communication inter-clients

### 2. IoT 🔧
Pour vos objets connectés, isolés par défaut.
- ✅ Internet (contrôlé)
- ❌ Pas d'accès au LAN
- ❌ Isolés entre eux

### 3. Enfants 👶
Accès filtré avec contrôle parental.
- ✅ Internet filtré
- ✅ Accès local limité
- ⏰ Plages horaires
- 🔒 SafeSearch forcé

### 4. Invités 👥
Pour les visiteurs temporaires.
- ✅ Internet limité
- ❌ Pas d'accès au LAN
- 🚪 Portail captif requis
- ⏱️ Session limitée

### 5. Quarantaine ⏳
Zone d'attente pour les inconnus.
- ❌ Pas d'Internet
- ❌ Pas d'accès local
- 🚪 Portail uniquement
- ⏳ En attente d'approbation

### 6. Bloqué 🚫
Pour les intrus et indésirables.
- ❌ Aucun accès
- ❌ Tout trafic bloqué
- 📝 Historique conservé

## 🚪 Portail Captif Nouvelle Génération

Le portail captif n'est plus une simple page d'authentification. C'est une vraie expérience utilisateur :

### Fonctionnalités

| Feature | Description |
|---------|-------------|
| **Design Moderne** | Interface sombre élégante, personnalisable |
| **Multi-Auth** | Mot de passe, inscription, social login |
| **Terms & Conditions** | Acceptation obligatoire des CGU |
| **Branding** | Logo, couleurs, textes personnalisables |
| **Session Timer** | Durée de session configurable |
| **Bandwidth Info** | Affichage du quota restant |

### Personnalisation

```javascript
// Configuration du portail
config portal 'portal'
    option title 'Bienvenue sur le Réseau'
    option subtitle 'Veuillez vous identifier'
    option accent_color '#ef4444'
    option require_terms '1'
    option auth_method 'password'
    option guest_password 'guest2024'
    option session_duration '7200'
```

## 👨‍👩‍👧‍👦 Contrôle Parental Avancé

### Plages Horaires

Définissez quand vos enfants peuvent accéder à Internet :

| Planning | Horaires | Jours | Action |
|----------|----------|-------|--------|
| 🌙 Nuit | 22:00 - 07:00 | Tous | Bloquer |
| 🎓 École | 08:00 - 16:00 | Lun-Ven | Bloquer |
| 🎮 Weekend | Toute la journée | Sam-Dim | Quota 3h |

### Filtrage de Contenu

```
┌─────────────────────────────────────────────────────────────┐
│                    CATÉGORIES BLOQUÉES                       │
├─────────────────────────────────────────────────────────────┤
│  🔞 Adulte    │  🔫 Violence  │  🎰 Jeux d'argent           │
│  💊 Drogues   │  🔪 Armes     │  ☠️ Contenu illégal         │
└─────────────────────────────────────────────────────────────┘
```

### SafeSearch Forcé

- **Google** : Safe Search activé
- **Bing** : Mode strict
- **YouTube** : Mode restreint
- **DuckDuckGo** : Safe mode

### Listes Personnalisées

```bash
# Liste Blanche (toujours autorisé)
google.com
wikipedia.org
education.gouv.fr
scratch.mit.edu
khanacademy.org

# Liste Noire (toujours bloqué)
tiktok.com
snapchat.com
discord.com
```

## 🔔 Alertes en Temps Réel

### Types d'Alertes

| Alerte | Déclencheur | Priorité |
|--------|-------------|----------|
| 🆕 Nouveau Client | Appareil inconnu détecté | Haute |
| 🚫 Client Banni | Tentative de reconnexion | Critique |
| 📊 Quota Dépassé | Limite temps/données atteinte | Moyenne |
| ⚠️ Activité Suspecte | Scan de ports, intrusion | Critique |

### Canaux de Notification

#### 📧 Email (SMTP)
```bash
config email 'email'
    option enabled '1'
    option smtp_server 'smtp.gmail.com'
    option smtp_port '587'
    option smtp_user 'alerts@gmail.com'
    list recipients 'admin@example.com'
```

#### 📱 SMS (Twilio/Nexmo/OVH)
```bash
config sms 'sms'
    option enabled '1'
    option provider 'twilio'
    option api_key 'ACxxxxx'
    list recipients '+33612345678'
```

### Templates Personnalisables

```
🆕 Nouveau client détecté sur votre réseau
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MAC: {mac}
IP: {ip}
Hostname: {hostname}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Action: Mis en quarantaine
Connectez-vous pour approuver ou bannir.
```

## 📊 Surveillance en Temps Réel

### Dashboard Overview

Le dashboard affiche en un coup d'œil :

- **12** Clients en ligne
- **18** Approuvés
- **3** En quarantaine
- **2** Bannis
- **6** Zones actives
- **5** Alertes aujourd'hui

### Informations par Client

| Champ | Description |
|-------|-------------|
| 📱 Icône | Détection automatique du type d'appareil |
| 🏷️ Nom | Hostname DHCP ou nom personnalisé |
| 🔢 MAC | Adresse MAC unique |
| 📍 IP | Adresse IP (DHCP ou statique) |
| 🏠 Zone | Zone de sécurité assignée |
| 📊 Trafic | RX/TX en temps réel |
| ⏱️ Dernière activité | Timestamp de dernière connexion |

## 🔧 Installation

```bash
# Prérequis
opkg update
opkg install luci-base rpcd dnsmasq-full iptables

# Installation
git clone https://github.com/gkerma/luci-app-client-guardian.git
cd luci-app-client-guardian
make install

# Redémarrer
/etc/init.d/rpcd restart
```

## 🎨 Interface Utilisateur

### Thème Sécurité

- **Couleur principale** : Rouge alarme (#ef4444)
- **Fond** : Dark mode professionnel
- **Animations** : Pulse pour les alertes
- **Responsive** : Mobile-friendly

### Navigation

```
Services → Client Guardian
    ├── Overview (tableau de bord)
    ├── Clients (liste complète)
    ├── Zones (configuration)
    ├── Portal (portail captif)
    ├── Parental (contrôle parental)
    ├── Alerts (notifications)
    └── Logs (journal)
```

## 🔐 Cas d'Usage

### 1. Réseau Domestique
- Surveiller tous les appareils familiaux
- Contrôler le temps d'écran des enfants
- Isoler les objets IoT
- Recevoir des alertes d'intrusion

### 2. Petite Entreprise
- Séparer WiFi employés et invités
- Portail captif pour les visiteurs
- Logs de connexion pour audit
- Isolation des imprimantes/IoT

### 3. Location Airbnb
- Portail captif avec mot de passe rotatif
- Isolation complète des invités
- Quota de bande passante
- Pas d'accès aux caméras/IoT

## 🛣️ Roadmap

- [x] Surveillance temps réel
- [x] Gestion des zones
- [x] Portail captif
- [x] Contrôle parental
- [x] Alertes SMS/Email
- [ ] Intégration Pi-hole
- [ ] Graphiques historiques
- [ ] Application mobile
- [ ] API REST externe

## 🔗 Ressources

- **GitHub** : [github.com/gkerma/luci-app-client-guardian](https://github.com/gkerma/luci-app-client-guardian)
- **Démo** : [cybermind.fr/demos/client-guardian](https://cybermind.fr/demos/client-guardian)
- **Documentation OpenWrt** : [openwrt.org](https://openwrt.org/docs/start)

## 🎬 Conclusion

**Client Guardian** transforme votre routeur OpenWrt en véritable gardien de votre réseau. Plus d'appareils inconnus, plus de zones grises, plus de surprises. Chaque connexion est surveillée, chaque client est identifié, chaque accès est contrôlé.

> *"La sécurité n'est pas un produit, mais un processus."* — Bruce Schneier

Avec Client Guardian, ce processus devient simple, visuel et efficace.

---

*Dashboard créé par [Gandalf @ CyberMind.fr](https://cybermind.fr) - Licence Apache-2.0*
