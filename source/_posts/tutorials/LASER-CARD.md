---
title: Fiches - RÉGLAGES – GRAVURE PEINTURE SUR ALU (LightBurn)
lang: fr
date: 2025-11-05 13:08:00
author: 🧙 -- Gandalf (from "The Conjurers")
tags: 
- LASER
- Creativity
- Mood
- FabLab
- contribute
category: fablab
##publish: true
private: false
hidden: false

---
# FICHE RÉGLAGES – GRAVURE PEINTURE SUR ALU (LightBurn)

**Machine :** Ortur 20W (LU3-20A)  
**Fichier :** PNG 1-bit Floyd–Steinberg **inversé** (noir = zone gravée)  
**Format :** 85×54 mm (carte de visite)

---<!-- more -->

## 1) Quel fichier utiliser
Privilégier l’image **tramée et inversée** (fond blanc, traits noirs) :
- 600 DPI (recommandé) : `card_85x54_bw_floyd_inverted_600dpi.png`  
- 300 DPI (plus léger) : `card_85x54_bw_floyd_inverted_300dpi.png`

> Pour découpe / gabarit : `card_outline_85x54mm_r3mm.svg`

---

## 2) Import dans LightBurn (image déjà tramée)
- **Image Mode :** `Pass-Through` (évite le double tramage)  
- **Taille :** `Largeur 85 mm`, `Hauteur 54 mm` (pas de redimensionnement auto)  
- **Line Interval :** `0.10 mm` (≈ 254 DPI) • possible : `0.08–0.12 mm`  
- **Bidirectional Scan :** ON • **Overscan :** 3–5 % • **Angle :** 0°

---

## 3) Paramètres de départ (Ortur 20W · peinture sur alu)
- **Vitesse :** `9000 mm/min`  
- **Puissance :** `70 %`  
- **Passes :** `1` (2 si peinture tenace)  
- **Air Assist :** léger à moyen  
- **Focus :** précis, surface plane (gabarit conseillé)

---

## 4) Ajustements rapides
- **La peinture ne part pas assez :** `7000–8000 mm/min` ou `80–90 %` ; 2 passes si besoin.  
- **Trait trop large / bave :** `11 000–13 000 mm/min`, `60–65 %`, ou `interval 0.12 mm`.  
- **Contraste faible :** garder `0.10 mm`, viser `8000 mm/min` & `80–90 %`.

> Plage utile (20 W sur peinture) : **6000–13000 mm/min**, **60–90 %**, **1–2 passes**.

---

## 5) Alternatives de fichier
- **Grayscale (8-bit) inversé @ 600 DPI** : uniquement si votre workflow gère bien la modulation.  
  Sur peinture, le **1-bit** est souvent **plus net**.  
- **Versions 300 DPI** : fichiers plus légers.

---

## 6) Sécurité & nettoyage
- Ventilation / masque (fumées de peinture).  
- Nettoyage : **alcool isopropylique (IPA)** pour les résidus.  
- Masquage (tape de transfert) si la peinture s’écaille.

---

## 7) Fichiers conseillés (liens)
- 600 DPI : [card_85x54_bw_floyd_inverted_600dpi.png](sandbox:/mnt/data/card_85x54_bw_floyd_inverted_600dpi.png)  
- 300 DPI : [card_85x54_bw_floyd_inverted_300dpi.png](sandbox:/mnt/data/card_85x54_bw_floyd_inverted_300dpi.png)  
- Outline SVG (r=3 mm) : [card_outline_85x54mm_r3mm.svg](sandbox:/mnt/data/card_outline_85x54mm_r3mm.svg)

---

*Astuce :* créez un gabarit (SVG) pour positionner la carte toujours à l’identique.
