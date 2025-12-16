---
date: 2025-11-21 14:12:00
layout: post
title: Mode d'emploi -- Jeu Divinatoire des 24 Cartes
---

# Mode d'emploi -- Jeu Divinatoire des 24 Cartes

Système divinatoire interactif & concept de jeu

Ce document présente :\
1. Le **concept du jeu**\
2. Le **mode d'emploi complet**\
3. Le **tableau des cartes** avec leurs symboles\
4. Un **système d'interprétation**\
5. Une **intégration Streamlit** pour un tirage interactif
<!-- more -->
------------------------------------------------------------------------

# 1. Concept général du jeu

Le Jeu des 24 Cartes est un système symbolique inspiré des cycles, des
archétypes et des rythmes du monde.\
Chaque carte représente une **énergie**, un **moment**, un **archétype
humain**, une **saison**, ou une **idée primordiale**.

Le jeu peut être utilisé pour :\
- L'introspection\
- L'écriture créative\
- La génération de scénarios narratifs\
- La divination ludique\
- L'aide à la prise de décision

Les cartes sont autonomes mais peuvent aussi se **répondre entre
elles**, formant un réseau symbolique.

------------------------------------------------------------------------

# 2. Mode d'emploi

## 2.1 Préparation

Mélanger les cartes ou déclencher un tirage aléatoire via l'application
Streamlit.

Formuler une question :\
- « Quel est mon état actuel ? »\
- « Quelle est la prochaine étape ? »\
- « Quelle énergie dois-je comprendre ? »

## 2.2 Types de tirages

### Tirage simple (1 carte)

Message direct, réponse brute.

### Tirage en 3 cartes

-   **1** : Situation actuelle\
-   **2** : Obstacle / dynamique cachée\
-   **3** : Issue / énergie de résolution

### Tirage en 4 saisons

-   **Printemps** : Départ, initiative\
-   **Été** : Énergie, expansion\
-   **Automne** : Récolte, bilan\
-   **Hiver** : Silence, transformation

### Tirage en 7 étapes

Parcours initiatique complet, incluant Source, Cycles, Surprise,
Réalisation, Battement, Souffle, Labyrinthe.

------------------------------------------------------------------------

# 3. Tableau des cartes et symboles

| Numéro | Nom         | Symboles clés         | Thèmes                         |
|-------|-------------|------------------------|--------------------------------|
| 1     | Source      | Origines, sagesse, eau | Commencement, racines          |
| 2     | Cycles      | Lune, saisons, cercle  | Répétition, apprentissage      |
| 3     | Surprise    | Jaillissement, porte   | Révélation, intuition          |
| 4     | Réalisation | Origami, création      | Ingéniosité, découverte        |
| 5     | Battement   | Cœur, rythme           | Émotion, perception subtile    |
| 6     | Souffle     | Papillon, air          | Souhait, échange, respiration  |
| 7     | Passé       | Ruines, mémoire        | Ancêtres, histoire             |
| 8     | Maintenant  | Joker, soleil          | Présence, action immédiate     |
| 9     | Séduction   | Fleur, couleurs        | Enfance, joie, attraction      |
| 10    | Espoirs     | Spirale, vibration     | Futur, confiance, risque       |
| 11    | Oubli       | Nuage, eau             | Lâcher prise, trauma           |
| 12    | Secret      | Moine, intériorité     | Discrétion, mystère            |
| 13    | Enfant      | Visage jeune           | Renouveau, spontanéité         |
| 14    | Mère        | Oiseau, remède         | Protection, soin               |
| 15    | Père        | Force, ancrage         | Modèle, labeur                 |
| 16    | Avatar      | Masque, rôle           | Identité, façade               |
| 17    | Dieu        | Symbole triple         | Foi, création, absolu          |
| 18    | Labyrinthe  | Spirale, pointe        | Quête, choix difficiles        |
| 19    | Ève         | Féminin, sève          | Origine, douceur               |
| 20    | Adam        | Masculin, voyage       | Exploration, décision          |
| 21    | Automne     | Arbre, fruits          | Transition, bilan              |
| 22    | Hiver       | Neige, froid           | Pause, purification            |
| 23    | Printemps   | Spirale verte          | Début, floraison               |
| 24    | Été         | Foudre, chaleur        | Puissance, mouvement           |

------------------------------------------------------------------------

---
| N° | Nom         | Symboles visuels (depuis l’image)                                      | Texte inscrit sur la carte                                             |
|----|-------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| 1  | Source      | Montagnes + spirales + étoile colorée                                  | - Le retour aux origines<br>- Les sagesses ancestrales<br>- Les connaissances anciennes |
| 2  | Cycles      | Cercle bleu + noyau noir (formes lunaires)                            | - Les phases de la lune<br>- Le cycle des saisons<br>- Les boucles sans fin |
| 3  | Surprise    | Forme jaillissante orange/jaune comme un ressort                      | - Les directions de la vie<br>- Les images des rêves<br>- Le souvenir des merveilles |
| 4  | Réalisation | Oiseau / origami multicolore                                          | - Le hasard des mélanges<br>- Les découvertes humaines<br>- Les inventions technologiques |
| 5  | Battement   | Cœur rose stylisé                                                     | - Les rythmes invisibles<br>- Les sourires cachés<br>- Le reflet caché |
| 6  | Souffle     | Papillon bleu avec antennes jaunes                                    | - Les mouvements de la vie<br>- Les échanges invisibles<br>- Le sourire annoncé |
| 7  | Passé       | Carrés bleus superposés (strates de mémoire)                          | - Les civilisations perdues<br>- Les 7 merveilles du Monde<br>- Le temps perdu |
| 8  | Maintenant  | Étoile à 8 branches + couleurs vives                                  | - Le joker<br>- Les matins ensoleillés<br>- Les instants présents |
| 9  | Séduction   | Fleur multicolore                                                     | - Le plaisir de l’enfance<br>- Les jeux de société<br>- Les musiques de la nature |
| 10 | Espoirs     | Bulbe violet/bleu entouré d’un halo                                   | - Les projets d’avenir<br>- Les clés de la réussite<br>- Le plaisir de l’inconnu |
| 11 | Oubli       | Nuage bleu avec taches claires                                        | - Les douleurs du passé<br>- Les événements tragiques<br>- Le désir de l’enfance |
| 12 | Secret      | Silhouette assise / personnage méditatif                              | - Les autres<br>- Les échanges discrets<br>- Le monde personnel |
| 13 | Enfant      | Visage rond jaune + yeux larges                                        | - Les projets d’avenir<br>- Les sourires de demain<br>- Le bonheur de la jeunesse |
| 14 | Mère        | Figure insectoïde / oiseau sacré                                      | - Les origines du Monde<br>- Les remèdes ancestraux<br>- Le souvenir de la douceur |
| 15 | Père        | Figure rouge + disque doré                                             | - Les sources d’inspiration<br>- Les recettes anciennes<br>- Le pouvoir de la famille |
| 16 | Avatar      | Silhouette robotique + masques et outils                               | - Les costumes de la vie<br>- Les ombres et lumières<br>- Le parcours discret |
| 17 | Dieu        | Composition tripartite : goutte rose, ailes vertes                    | - Les croyances personnelles<br>- Les sociétés secrètes<br>- Le souvenir d’un faiseur |
| 18 | Labyrinthe  | Spirale verte + pointe triangulaire orange                            | - Le parcours initiatique<br>- Les chemins de traverse<br>- Les portes dérobées |
| 19 | Ève         | Personnage féminin rose + cœurs bleus                                 | - Les mères des mères<br>- Les femmes du monde<br>- Le premier pas |
| 20 | Adam        | Silhouette masculine simple + boucle jaune                            | - Les pères des anciens<br>- Les premiers hommes<br>- Le premier voyageur |
| 21 | Automne     | Arbre circulaire rempli de fruits colorés                             | - Le temps d’après<br>- Les fins de cycles<br>- Les souvenirs de demain |
| 22 | Hiver       | Arbre stylisé bleu + flocons                                          | - Les fins des temps<br>- Les réserves de froid<br>- Le blanc immaculé |
| 23 | Printemps   | Spirale rose/verte + bourgeons                                        | - Le début de la route<br>- Les premiers amusements<br>- Les parfums floraux |
| 24 | Été         | Foudre jaune + silhouette mauve dans la chaleur                       | - Les fruits et saveurs<br>- Les réserves de chaleur<br>- Le temps des jeux |

---

# 4. Interprétation des symboles

## Symboles récurrents

-   **Cercle / spirale** : mouvement, cycle, ascension ou répétition\
-   **Origine / Source** : fondement, vérité première\
-   **Figures humaines** : rôles, archétypes, phases de vie\
-   **Éléments naturels** (eau, feu, air, terre) : forces fondamentales\
-   **Arbres / saisons** : transformation, temporalité\
-   **Papillon / souffle** : mouvement léger, message subtil\
-   **Foudre / choc** : révélation, décision rapide

## Interprétation générale

Le tirage se lit en identifiant les **énergies dominantes** et les
**transitions** entre les cartes.\
Une carte peut : - confirmer un état\
- annoncer une évolution\
- révéler une tension\
- ouvrir une possibilité

------------------------------------------------------------------------

# 5. Code Streamlit pour tirage interactif

Copiez ce script dans `app.py` :

``` python
import streamlit as st
import random

# Définition des cartes
cards = {
    1: ("Source", "Retour aux origines, sagesse ancienne, fondement."),
    2: ("Cycles", "Répétition, apprentissage, mouvements lunaires."),
    3: ("Surprise", "Révélation, intuition, émergence soudaine."),
    4: ("Réalisation", "Ingéniosité, création, découverte humaine."),
    5: ("Battement", "Rythmes invisibles, émotions fines, écoute intérieure."),
    6: ("Souffle", "Souhait, échange, légèreté."),
    7: ("Passé", "Ancêtres, mémoire, civilisations perdues."),
    8: ("Maintenant", "Présence, décision immédiate, instant vécu."),
    9: ("Séduction", "Joie, enfance, attraction naturelle."),
    10: ("Espoirs", "Futur, confiance, plaisir de l’inconnu."),
    11: ("Oubli", "Lâcher prise, trauma, dissolution."),
    12: ("Secret", "Intériorité, monde personnel, discrétion."),
    13: ("Enfant", "Renouveau, spontanéité, projets futurs."),
    14: ("Mère", "Protection, soin, remèdes ancestraux."),
    15: ("Père", "Ancrage, modèle, force constructive."),
    16: ("Avatar", "Identité, rôle, masques de la vie."),
    17: ("Dieu", "Foi, absolu, création personnelle."),
    18: ("Labyrinthe", "Quête, choix, chemins complexes."),
    19: ("Ève", "Origine féminine, douceur, intuition."),
    20: ("Adam", "Origine masculine, voyage, décision."),
    21: ("Automne", "Transition, bilan, fin de cycle."),
    22: ("Hiver", "Pause, purification, silence."),
    23: ("Printemps", "Début, floraison, départ."),
    24: ("Été", "Puissance, chaleur, mouvement.")
}

st.title("Tirage Divinatoire – Jeu des 24 Cartes")

tirage = st.button("Tirer une carte")

if tirage:
    n = random.randint(1, 24)
    name, meaning = cards[n]
    st.subheader(f"Carte {n} : {name}")
    st.write(meaning)
```

------------------------------------------------------------------------

# Téléchargement

Ce fichier est prêt à être utilisé dans HexoJS ou tout autre moteur
Markdown.
