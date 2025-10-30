---
title: 'Magie - Les invisibles (IDÉE COOL - #002)'
lang: fr
date: 2022-06-18 11:28:00
author: 🧙 -- Gandalf (from "The Conjurers")
tags:
- Idée Cool
- M@DZ GE3X
- Écologie
- Invisibles
- Technologie
- Solutions
- The Conjurers
- Nature
- Sons
- Savoie
- contribute
categories:
- Cyber
- KragZouïlles
publish: true
hidden: false
---

# Découvrir et rendre visible les invisibles

C'est un de *mes* sujets…
C'est une de *mes* magies !

Comme la vulgarisation, le partage, ce sont des parties de *ma* philosophie…

	Il est des moments magiques…
	Des pages de livres qui jamais ne se referment !
	Et c'est bien, c'est heureux, c'est la vie et ses surprises…

<!-- more -->

ÉDIT:
	Mon enregistreur ZOOM H2n enregistre bien les Ultra-Sons !!! 💪🧙‍♂️👍

# CAPTURE

Enregistrement de ce matin… section du fichier original (amplifié) un son avec une ZOOM H2n….

J'ai vu passer une chauve-souris juste après avoir allumé et déposé l'enregistreur…
	Chauve-souris sur l'enregistreur à tester (retrouver si le son la bien capturée…)
	en début de rendez-vous avec la lune !! 🍀(ça sera un autre sujet/billet… 😜)

<img src="/uploads/images/CHIRO/002/signal-2022-06-11-195640_001.png" heigth="300px">

C'est mon enregistreur acheté tout récemment !!!!
Il est au catalogue de la boutique LPO (Ligue de Protection des Oiseaux) dans la section "Détecteurs Enregistreurs Ultrasons" > "Enregistreur Numérique H2N".

DONC, il doit me permettre de tester (tel que) des enregistrements pour les ultrasons !!!
Et, si c'est le cas je vais halluciner, car je l'ai pris, après de longues hésitations, mais pas du tout pour ça.
À l'origine, pour les chouettes ou pour m'enregistrer, en tant que micro USB ou en portatif !
J'ai pu le tester à un concert, à une conférence, mais aussi à des rendez-vous ou discrètement lors de réunions.

## Enregistrement

<img src="/uploads/images/CHIRO/002/H2n_frontBack_softshadow.png" heigth="300px">

Perso je suis en RAW (wave) à 96KHz sur 32 Bits pour ce test…
Avec les 4 canaux (micro) dans un mode stéréo …

96KHz pour le H2N, <100KHz (MAX) pour les ultrasons donc, oui, ça doit marcher… ! 👍

<img src="/uploads/images/CHIRO/002/SurroundSoundPattern_2.jpg" heigth="300px">

# EXPORTS

Section originale de l'enregistrement…

{% dplayer "url=/uploads/images/CHIRO/002/220617-045832-DETECT-002-REDO-EXPORT.m4a" "pic="  "api=https://api.prprpr.me/dplayer/" "loop=no" "theme=#FADFA3" "autoplay=false" %}

<img src="/uploads/images/CHIRO/002/signal-2022-06-17-133855_001.png" heigth="300px">
<img src="/uploads/images/CHIRO/002/signal-2022-06-17-133855_002.jpeg" heigth="300px">

# NETTOYAGES

Quelques traitements plus tard, anti-bruit de fond et amplifications…

{% dplayer "url=/uploads/images/CHIRO/002/220617-045832-DETECT-002-REDO-EXPORT-AMPLIFY-UNNOISE-UNNOISE.m4a" "pic="  "api=https://api.prprpr.me/dplayer/" "loop=no" "theme=#FADFA3" "autoplay=false" %}

# ANALYSES

Là, 2 choix…
 Vu que les écoutes causent pas des masses !

À part le fait que dans les bande de fréquences on a des ultrasons.

Les fréquences des ondes ultrasonores sont comprises entre 15 000 et 150 000 Hz (hertz) alors que celles de la voix humaine sont comprises entre 125 et 210 Hz.
L’oreille humaine perçoit en principe les sons entre 20 Hz et 20 000 Hz mais avec l’âge croissant l’audition des fréquences supérieures à 12 000 Hz diminue. 

## Hétérodyne

Hétérodyne (traitement de transposition des 
fréquences sans changer la vitesse) 

Voci le même fichier mais après un traitement hétérodyne avec la formule Audacity NyQuist :

```
---8<---
;version 4
(lowpass8 (mult *track* (hzosc 30000)) 10000)
---8<---
```
{% dplayer "url=/uploads/images/CHIRO/002/220617-045832-DETECT-002-REDO-EXPORT-AMPLIFY-HETERODYNE-AMPLIFY-UNNOISE-UNNOISE.m4a" "pic="  "api=https://api.prprpr.me/dplayer/" "loop=no" "theme=#FADFA3" "autoplay=false" %}

<img src="/uploads/images/CHIRO/002/signal-2022-06-17-134222_001.png" heigth="300px">
<img src="/uploads/images/CHIRO/002/signal-2022-06-17-134222_002.jpeg" heigth="300px">

Autre avantage on voit très facilement les "restes", après filtrage, donc les ultrasons.

## Modification de vitesse

Décalage (étalage, expansion) de temps. (modification de vitesse x10)

Voici, à peu prêt la même partie, en mode débruité, amplifiée et par contre modifié en vitesse  divisée par 10.

On a toujours les oiseaux MAIS on a un sons ÉTRANGES qui correspond au précédents en hétérodyne mais ici en vitesse rallongée (x10)…

{% dplayer "url=/uploads/images/CHIRO/002/220617-045832-DETECT-002-REDO-EXPORT-AMPLIFY-UNNOISE-UNNOISE-TIMEEXPAND-CUTPART.m4a" "pic="  "api=https://api.prprpr.me/dplayer/" "loop=no" "theme=#FADFA3" "autoplay=false" %}

# REFS
- Audacity: [Audacity @ WikiPédia](https://fr.wikipedia.org/wiki/Audacity) & [Audacity @ Site Officiel](https://www.audacityteam.org/)
- OCENAUDIO: [OcenAudio @ Site Officiel](https://www.ocenaudio.com/)
- Ultrason: [Ultrason @ WikiPédia](https://fr.wikipedia.org/wiki/Ultrason)
- Hétérodyne: [Hétérodyne @ WikiPédia](https://fr.wikipedia.org/wiki/H%C3%A9t%C3%A9rodyne)
- Chiroptera: [Chiroptera @ WikiPédia](https://fr.wikipedia.org/wiki/Chiroptera)
- LPO: [LPO (Ligue de Protection des Oiseaux) @ Boutique](https://boutique.lpo.fr/catalogue/materiel-optique/detecteurs-enregistreurs-ultrasons/enregistreur-numerique-h2n)
- ZOOM: [H2n @ ZOOM](https://zoomcorp.com/fr/fr/enregistreurs-portatifs/handheld-recorders/h2n-handy-recorder/) & [Accessoires H2n @ ZOOM](https://zoomcorp.com/fr/fr/accessoires/bonnette-et-packs-daccessoires/sph-2n/)

# BREF

Plein d'idées suites à ces manipulations et aux outils (qu'il faut que je retrouve) sur les analyses et traitements de SON !! 
J'adore, voir et entendre l'invisible et comprendre ou imaginer autrement…
Les Baleines, les Dauphins et les Chauves souris communiquent ou utilisent ces types de "SONs" pour leur répérage par ECHO… et les Rats les produisent sous forme de ricanements quand il sont caressés… 
À suivre !

# À suivre sur @CyberMindFR… #

- D'autres billets suivront à propos de la "magie des invisibles" ([les “KragZouÿs” 🤖 + 🎲 = 💡 -> 💧 (ÉPISODES 002 - IDÉE COOL)](https://cybermind.fr/tags/Idee-Cool/))
- …

⚠️ Attention, cette page risque d'être mise à jour régulièrement ! 👀

🧙 -- [Gandalf (from "The Conjurers")](mailto:Gandalf@Gk2.NET?subject=The%20Conjurers%20%3F) ©️ 1982-2022
