---
title: "Yi Jing 易經 - Oracle avec Grilles La Livrée d'Hermès"
date: 2025-12-14 05:55:00
updated: 2025-12-14 05:55:00
categories:
  - Ésotérisme
  - Outils Interactifs
tags:
  - Yi Jing
  - I Ching
  - Oracle
  - Divination
  - La Livrée d'Hermès
  - Hexagrammes
  - Taoïsme
  - Application Web
keywords:
  - yi jing oracle
  - i ching tirage
  - hexagrammes chinois
  - livre des mutations
  - divination taoïste
  - la livrée d'hermès
description: "Application interactive de consultation du Yi Jing (I Ching) avec visualisation sur les grilles de jeu La Livrée d'Hermès. Tirage des 64 hexagrammes, interprétation des traits mutants et animation des transformations."
thumbnail: /images/yijing-oracle-thumb.png
toc: true
comments: true
---

## Introduction au Yi Jing 易經

Le **Yi Jing** (易經), également connu sous le nom de **I Ching** ou **Livre des Mutations**, est l'un des plus anciens textes classiques chinois. Datant de plus de 3000 ans, il constitue à la fois un système de divination et un traité philosophique fondamental du taoïsme et du confucianisme.

<!-- more -->

Le Yi Jing repose sur un système binaire de **64 hexagrammes**, chacun composé de six traits qui peuvent être soit **Yang** (trait plein ━━━) soit **Yin** (trait brisé ━ ━). Ces hexagrammes représentent les différentes configurations possibles du changement universel.

### Les Traits et leur Signification

| Valeur | Type | Symbole | Signification |
|--------|------|---------|---------------|
| 6 | Yin mutant | ━ ✕ ━ | Yin en transformation vers Yang |
| 7 | Yang stable | ━━━━━ | Force, action, lumière |
| 8 | Yin stable | ━ _ ━ | Réceptivité, repos, obscurité |
| 9 | Yang mutant | ━━◯━━ | Yang en transformation vers Yin |

Les traits **mutants** (6 et 9) indiquent une situation en évolution. Ils génèrent un **hexagramme de mutation** qui révèle vers quoi la situation évolue.

---

## La Livrée d'Hermès

**La Livrée d'Hermès** est un système de jeu ésotérique créé par **Anibal Edelbert Amiot**, utilisant des grilles géométriques aux motifs symboliques. Chaque grille représente une configuration énergétique particulière, combinant les principes de la géométrie sacrée avec la symbolique hermétique.

Dans cette application, les 24 grilles de La Livrée d'Hermès sont associées aux différents types de traits du Yi Jing :

- **6 grilles YANG** (positions 1 à 6) - traits Yang stables
- **6 grilles YING** (positions 1 à 6) - traits Yin stables  
- **6 grilles YANG-MUT** (positions 1 à 6) - traits Yang mutants
- **6 grilles YING-MUT** (positions 1 à 6) - traits Yin mutants

La **superposition des 6 grilles** correspondant à un tirage crée un motif unique, une sorte de "mandala divinatoire" propre à chaque consultation.

---

## Comment Consulter l'Oracle

### Méthode Traditionnelle des Trois Pièces

La méthode utilisée ici simule le tirage traditionnel des **trois pièces de monnaie** :

1. On lance trois pièces simultanément
2. Chaque **Face** vaut 3, chaque **Pile** vaut 2
3. Le total donne la valeur du trait :
   - **6** (2+2+2) = Yin mutant
   - **7** (2+2+3) = Yang stable
   - **8** (2+3+3) = Yin stable
   - **9** (3+3+3) = Yang mutant

L'opération est répétée **six fois** pour construire l'hexagramme de bas en haut.

### Les Huit Trigrammes (Bagua 八卦)

Chaque hexagramme est composé de deux **trigrammes** (groupes de 3 traits) :

| Trigramme | Symbole | Élément | Qualité |
|-----------|---------|---------|---------|
| ☰ Qián (Ciel) | ≡ | Métal | Force créatrice |
| ☷ Kūn (Terre) | ⚏ | Terre | Réceptivité |
| ☳ Zhèn (Tonnerre) | ⚌ | Bois | Éveil, mouvement |
| ☵ Kǎn (Eau) | ⚍ | Eau | Danger, profondeur |
| ☶ Gèn (Montagne) | ⚎ | Terre | Immobilité, arrêt |
| ☴ Xùn (Vent) | ⚋ | Bois | Pénétration douce |
| ☲ Lí (Feu) | ⚊ | Feu | Clarté, lumière |
| ☱ Duì (Lac) | ⚏ | Métal | Joie, sérénité |

---

## Application Interactive

{% raw %}
<div id="yijing-app-container" style="width: 100%; margin: 20px 0;">
  <iframe 
    src="/apps/yijing_oracle_grilles.html" 
    style="width: 100%; height: 800px; border: none; border-radius: 15px; box-shadow: 0 5px 30px rgba(0,0,0,0.2);"
    loading="lazy"
    title="Oracle Yi Jing avec Grilles La Livrée d'Hermès">
  </iframe>
</div>
{% endraw %}

{% note info %}
**Téléchargement** : Vous pouvez également [télécharger l'application autonome](/downloads/yijing_oracle_grilles.html) pour une utilisation hors-ligne.
{% endnote %}

---

## Fonctionnalités de l'Application

### 🎲 Tirage Automatique Animé

L'animation montre le lancer des trois pièces pour chaque trait, avec construction progressive de l'hexagramme et des grilles superposées.

### 🎮 Visualisation sur Grilles

Les **6 grilles correspondant au tirage** sont fusionnées en temps réel pour créer une image composite unique représentant l'énergie de votre consultation.

### 🔀 Animation des Mutations

Lorsque des traits mutants sont présents, une animation fluide montre la transition entre l'hexagramme principal et l'hexagramme de mutation.

### 📥 Export PNG

Téléchargez les grilles fusionnées en haute résolution pour les conserver ou les méditer.

### ✍️ Mode Manuel

Possibilité de saisir directement les valeurs des traits (6, 7, 8, 9) pour reproduire un tirage effectué avec de vraies pièces.

---

## Les 64 Hexagrammes

Le Yi Jing comprend 64 hexagrammes, numérotés selon l'ordre du Roi Wen :

<details>
<summary><strong>Voir la liste complète des 64 hexagrammes</strong></summary>

| № | Caractère | Pinyin | Français |
|---|-----------|--------|----------|
| 1 | 乾 | Qián | Le Créateur |
| 2 | 坤 | Kūn | Le Réceptif |
| 3 | 屯 | Zhūn | La Difficulté Initiale |
| 4 | 蒙 | Méng | La Folie Juvénile |
| 5 | 需 | Xū | L'Attente |
| 6 | 訟 | Sòng | Le Conflit |
| 7 | 師 | Shī | L'Armée |
| 8 | 比 | Bǐ | La Solidarité |
| 9 | 小畜 | Xiǎo Xù | Le Petit Apprivoisement |
| 10 | 履 | Lǚ | La Marche |
| 11 | 泰 | Tài | La Paix |
| 12 | 否 | Pǐ | La Stagnation |
| 13 | 同人 | Tóng Rén | La Communauté |
| 14 | 大有 | Dà Yǒu | Le Grand Avoir |
| 15 | 謙 | Qiān | L'Humilité |
| 16 | 豫 | Yù | L'Enthousiasme |
| 17 | 隨 | Suí | La Suite |
| 18 | 蠱 | Gǔ | Le Travail sur le Corrompu |
| 19 | 臨 | Lín | L'Approche |
| 20 | 觀 | Guān | La Contemplation |
| 21 | 噬嗑 | Shì Kè | Mordre au Travers |
| 22 | 賁 | Bì | La Grâce |
| 23 | 剝 | Bō | L'Éclatement |
| 24 | 復 | Fù | Le Retour |
| 25 | 無妄 | Wú Wàng | L'Innocence |
| 26 | 大畜 | Dà Xù | Le Grand Apprivoisement |
| 27 | 頤 | Yí | Les Commissures des Lèvres |
| 28 | 大過 | Dà Guò | La Prépondérance du Grand |
| 29 | 坎 | Kǎn | L'Insondable (Eau) |
| 30 | 離 | Lí | Ce qui s'Attache (Feu) |
| 31 | 咸 | Xián | L'Influence |
| 32 | 恆 | Héng | La Durée |
| 33 | 遯 | Dùn | La Retraite |
| 34 | 大壯 | Dà Zhuàng | La Puissance du Grand |
| 35 | 晉 | Jìn | Le Progrès |
| 36 | 明夷 | Míng Yí | L'Obscurcissement de la Lumière |
| 37 | 家人 | Jiā Rén | La Famille |
| 38 | 睽 | Kuí | L'Opposition |
| 39 | 蹇 | Jiǎn | L'Obstacle |
| 40 | 解 | Xiè | La Libération |
| 41 | 損 | Sǔn | La Diminution |
| 42 | 益 | Yì | L'Augmentation |
| 43 | 夬 | Guài | La Percée |
| 44 | 姤 | Gòu | Venir à la Rencontre |
| 45 | 萃 | Cuì | Le Rassemblement |
| 46 | 升 | Shēng | La Poussée vers le Haut |
| 47 | 困 | Kùn | L'Accablement |
| 48 | 井 | Jǐng | Le Puits |
| 49 | 革 | Gé | La Révolution |
| 50 | 鼎 | Dǐng | Le Chaudron |
| 51 | 震 | Zhèn | L'Éveilleur (Tonnerre) |
| 52 | 艮 | Gèn | L'Immobilisation (Montagne) |
| 53 | 漸 | Jiàn | Le Développement |
| 54 | 歸妹 | Guī Mèi | L'Épousée |
| 55 | 豐 | Fēng | L'Abondance |
| 56 | 旅 | Lǚ | Le Voyageur |
| 57 | 巽 | Xùn | Le Doux (Vent) |
| 58 | 兌 | Duì | Le Joyeux (Lac) |
| 59 | 渙 | Huàn | La Dispersion |
| 60 | 節 | Jié | La Limitation |
| 61 | 中孚 | Zhōng Fú | La Vérité Intérieure |
| 62 | 小過 | Xiǎo Guò | La Prépondérance du Petit |
| 63 | 既濟 | Jì Jì | Après l'Accomplissement |
| 64 | 未濟 | Wèi Jì | Avant l'Accomplissement |

</details>

---

## Conseils pour la Consultation

{% note warning %}
### Avant de consulter l'Oracle

1. **Formulez clairement votre question** - Évitez les questions fermées (oui/non). Préférez "Quelle est la nature de..." ou "Comment aborder..."

2. **Créez un espace propice** - Un moment de calme et de concentration améliore la qualité de la lecture.

3. **Une question à la fois** - Ne posez pas plusieurs questions en même temps.

4. **Restez ouvert** - L'oracle révèle souvent des aspects auxquels nous n'avions pas pensé.
{% endnote %}

### Interpréter le Résultat

- **L'hexagramme principal** décrit la situation présente
- **Les traits mutants** (s'il y en a) indiquent les points d'évolution
- **L'hexagramme de mutation** montre vers quoi la situation évolue
- **Les trigrammes** donnent des indications sur les forces en présence

---

## Crédits et Références

- **Grilles La Livrée d'Hermès** : Anibal Edelbert Amiot
- **Textes du Yi Jing** : Traduction de Richard Wilhelm
- **Application** : Développée pour CyberMind.FR

### Bibliographie Recommandée

- *Yi King - Le Livre des Transformations*, Richard Wilhelm (traduction)
- *Le Yi Jing*, Cyrille Javary
- *I Ching : The Book of Changes*, James Legge

---

{% note success %}
**Téléchargement Hors-Ligne**

Cette application fonctionne entièrement hors-ligne. Téléchargez le fichier HTML autonome pour l'utiliser sans connexion internet :

[📥 Télécharger l'Oracle Yi Jing (HTML autonome)](/downloads/yijing_oracle_grilles.html)
{% endnote %}

---

*易經 - Le changement est la seule constante de l'univers.*
