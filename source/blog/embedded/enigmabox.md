---
title: "Enigmabox : tentative de box de confidentialité (archive & bilan)"
date: 2025-12-01 17:00:00
tags:
  - privacy
  - hardware
  - vpn
  - enigmabox
categories:
  - sécurité
  - Internet
author: "Gérald Kerma"
cover: ""
thumbnail: ""
permalink: /enigmabox-bilan/
description: "Revue et bilan d'Enigmabox (archive 2019) : promesses, fonctionnement technique, critiques et recommandations."
---

> Résumé : Enigmabox se présentait comme une « privacy box » plug-and-play (mesh + VPN + chiffrement). L'idée était intéressante, mais en pratique le projet a rencontré des problèmes (support, fiabilité, dépendance aux exit-servers). Voici un condensé des éléments techniques, des critiques et des conseils alternatifs.
<!-- more -->
## 1. Qu'est-ce que revendiquait Enigmabox ?

Selon l'archive du site (2019), Enigmabox promettait une appliance qui :
- chiffre et protège la connexion Internet (« Everything is encrypted »),
- met en place un réseau pair-à-pair (mesh) basé sur des technologies comme **cjdns** pour créer des connexions IPv6 chiffrées entre participants,
- fournit des fonctionnalités : navigation chiffrée, appels chiffrés, e-mails chiffrés, partage de fichiers, hébergement web personnel,
- s'insérait entre ta box/modem et ton réseau local pour sécuriser tout le trafic (approche « plug & play »).

Source principale : archive web (Wayback Machine) — version 2019 :  
https://web.archive.org/web/20190301012804/https://en.enigmabox.net/

## 2. Fonctionnement technique résumé

- Architecture : réseau mesh p2p + serveurs « exit » (sortie vers Internet public).
- Chiffrement : communications chiffrées dans le mesh (mais le trafic qui sort via les exit-servers dépend de la confiance qu’on place en eux).
- Usage ciblé : personnes cherchant à contourner la censure ou réduire la traçabilité en ligne.

## 3. Principaux problèmes et critiques

- **Support et maintenance pauvres** : documentation insuffisante et support client jugé défaillant par plusieurs retours d'utilisateurs.
- **Fiabilité** : mises à jour ou changements de configuration ont rendu certains dispositifs inutilisables selon des retours.
- **Sécurité / anonymat partiel** : dépendance aux serveurs de sortie. Si un exit-server est compromis, la confidentialité est affaiblie.
- **Coût vs valeur** : prix élevé pour un produit qui, dans la pratique, demandait souvent des compétences techniques et des interventions manuelles.
- **Promesses marketing ≠ expérience utilisateur** : le qualificatif « plug & play » était discuté par des testeurs.

## 4. Évaluation générale (bref)

L'idée d'une appliance dédiée à la confidentialité reste séduisante. En pratique, Enigmabox souffrait d'un mauvais rapport qualité/prix, d'un manque de transparence et de support. Pour la plupart des utilisateurs aujourd'hui (2025), il est préférable de s'orienter vers des solutions bien maintenues et éprouvées : VPN réputés, chiffrement de bout en bout pour communications, ou solutions auto-hébergées maîtrisées par l'utilisateur.

## 5. Alternatives & recommandations rapides

- Si tu veux **protéger ta vie privée sans gadget** : choisis un VPN réputé (politique no-logs claire, audits indépendants) + HTTPS Everywhere + bloqueurs de traceurs.
- Si tu veux **auto-héberger** : configure ton propre serveur VPN/OpenVPN/ WireGuard sur un VPS que tu contrôles.
- Si tu veux **décentralisation avancée** : regarde des projets open source bien maintenus (p.ex. solutions mesh open source, Tor pour l'anonymat, ou Réseaux privés auto-hébergés), mais attends-toi à nécessiter des compétences techniques.

---

## Références & lectures

- Archive Wayback (page produit Enigmabox, 2019) — https://web.archive.org/web/20190301012804/https://en.enigmabox.net/  
- Retours et tests publics (articles & forums) — synthèse de critiques autour du support, des serveurs de sortie et du rapport qualité/prix.

---

Si tu veux, je peux :
- transformer cet article en **plusieurs billets** (par ex. : 1) présentation technique, 2) guide d'alternatives, 3) guide d'auto-hébergement WireGuard) ;  
- ou générer une **version plus courte** (extrait pour la page d'accueil Hexo) ;  
- ou préparer un post avec **images / captures d'archive** prêtes à l'emploi pour Hexo.  

Dis-moi ce que tu veux que je génère ensuite — je m'en occupe tout de suite.