---
title: Yi Jing Oracle v2.2 - Guide Complet
date: 2025-12-15 08:59:00
updated: 2025-12-15  09:00:00
categories:
  - Tutoriels
  - Spiritualité
  - Python
  - Méditation
tags:
  - yi-jing
  - oracle
  - divination
  - python
  - pdf
  - audio
  - frequencies
  - 432hz
  - kasina
  - mindplace
  - avs
  - binaural
  - meditation
  - animation
toc: true
cover: /images/yijing-oracle-cover.png
excerpt: Guide complet pour utiliser l'Oracle du Yi Jing avec grilles animées, textes complets, rapport PDF détaillé (5 pages), fichiers audio aux fréquences sacrées et méditation Kasina AVS.
---

# 易經 Yi Jing Oracle v2.2

## Introduction

Le **Yi Jing** (易經), également connu sous le nom de **I Ching** ou **Livre des Mutations**, est l'un des plus anciens textes de sagesse chinoise, datant d'environ 3000 ans. Ce système divinatoire utilise 64 hexagrammes composés de 6 traits (Yin ou Yang) pour guider la réflexion et la prise de décision.

Cette application combine la sagesse millénaire du Yi Jing avec :
- Les **grilles visuelles animées** de "La Livrée d'Hermès" (Anibal Edelbert Amiot)
- Les **fréquences sacrées** du Solfège ancien (432 Hz)
- La génération automatique de **rapports PDF détaillés** (3-5 pages)
- Les **textes complets** des 6 traits et de l'interprétation
- La **méditation AVS Kasina** avec battements binauraux

<!-- more -->

---

## Nouveautés v2.2

### 🎮 Animation entre les grilles

L'application propose désormais une **transition animée** entre la grille de l'hexagramme principal et celle de la mutation :

- **Boutons de navigation** : Basculer entre les deux grilles
- **Animation automatique** : Mode auto-switch toutes les 2 secondes
- **Transitions CSS** fluides avec effets de fondu

{% asset_img grille-animation.gif "Animation entre les grilles" %}

### 📜 Textes complets

Tous les textes traditionnels sont maintenant affichés :

- **Description** de l'hexagramme
- **Le Jugement** (encadré orange)
- **L'Image** (encadré bleu)
- **Les 6 traits** : Chaque trait avec son texte complet dans un onglet dédié
- **Traits mutants** : Mis en évidence avec animation pulsante

### 📄 Rapport PDF Détaillé (3-5 pages)

Le rapport PDF a été considérablement enrichi :

| Page | Contenu |
|------|---------|
| **Page 1** | Hexagramme principal, trigrammes, traits tirés, grille |
| **Page 2** | Le Jugement, L'Image, interprétation générale |
| **Page 3** | Les 6 traits avec textes complets |
| **Page 4** | Traits mutants détaillés (si présents) |
| **Page 5** | Hexagramme de mutation avec grille et jugement |

### 🧘 Méditation Kasina / Mindplace

L'application génère des sessions de méditation au format **KBS** (Kasina Basic Session) compatibles avec les appareils **Mindplace Kasina** et **Limina**.

- **Fichier .kbs** : Format natif Mindplace
- **Audio WAV binaural** : Battements binauraux stéréo
- **Durée** : 5 minutes par session
- **États cérébraux** : Alpha (relaxation) → Theta (méditation profonde)

{% note success %}
**Version 2.2** : Animation des grilles, textes complets, PDF enrichi !
{% endnote %}

---

## Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation des dépendances

```bash
pip install pillow reportlab numpy scipy
```

### Installation Streamlit (optionnel)

Pour l'interface web :

```bash
pip install streamlit
```

### Téléchargement du projet

```bash
# Cloner ou télécharger le projet
git clone https://github.com/cybermind-fr/yijing-oracle.git
cd yijing-oracle
```

### Structure des fichiers

```
yijing-oracle/
├── yijing_oracle.py          # Programme principal CLI
├── app.py                    # Application Streamlit (1500+ lignes)
├── yijing_complet.json       # Base de données des 64 hexagrammes
├── images/                   # Grilles La Livrée d'Hermès (24 PNG)
│   ├── lldh-YY-YANG-1.png
│   ├── lldh-YY-YANG-2.png
│   └── ...
├── output/                   # Fichiers générés
├── .streamlit/config.toml    # Configuration Streamlit
├── requirements.txt
└── README.md
```

---

## 🎮 Animation des Grilles

### Principe

Lorsqu'un tirage comporte des traits mutants (6 ou 9), l'hexagramme évolue vers un **hexagramme de mutation**. L'application v2.2 permet de visualiser cette transformation avec une animation entre les deux grilles.

### Fonctionnalités

- **Boutons de navigation** : Cliquez pour basculer entre la grille principale et la grille de mutation
- **Animation CSS** : Transition fluide avec effet de fondu (fade)
- **Mode automatique** : Activez l'animation auto pour voir les grilles alterner toutes les 2 secondes
- **Indicateurs visuels** : Les boutons changent de couleur selon la grille active

### CSS Animation (extrait)

```css
.grille-slide {
    transition: all 0.8s ease-in-out;
}

.crossfade-img {
    transition: opacity 1.5s ease-in-out;
}

.mutation-card {
    animation: glow-mutation 3s ease-in-out infinite;
}

@keyframes glow-mutation {
    0%, 100% { box-shadow: 0 0 5px rgba(233, 30, 99, 0.3); }
    50% { box-shadow: 0 0 20px rgba(233, 30, 99, 0.5); }
}
```

---

## 📜 Affichage des Textes Complets

### Structure de l'affichage

L'application affiche tous les textes traditionnels du Yi Jing dans un ordre logique :

1. **Description de l'hexagramme** - Contexte général et symbolisme
2. **Le Jugement** - Sentence divinatoire principale
3. **L'Image** - Conseil pratique basé sur les trigrammes
4. **Les 6 Traits** - Chaque trait avec son texte dans un onglet dédié
5. **Traits Mutants** - Section spéciale pour les traits en transformation
6. **Hexagramme de Mutation** - Textes de l'hexagramme résultant

### Mise en forme

| Élément | Style | Couleur |
|---------|-------|---------|
| Le Jugement | Encadré orange | `#FFF3E0` / `#FF9800` |
| L'Image | Encadré bleu | `#E3F2FD` / `#2196F3` |
| Traits normaux | Encadré violet | `#F3E5F5` / `#9C27B0` |
| Traits mutants | Encadré rouge pulsant | `#FFEBEE` / `#E91E63` |

### Animation des traits mutants

Les traits mutants sont mis en évidence avec une animation CSS pulsante :

```css
.trait-mutant-box {
    animation: pulse-border 2s infinite;
}

@keyframes pulse-border {
    0%, 100% { border-left-color: #E91E63; }
    50% { border-left-color: #F48FB1; }
}
```

---

## Utilisation

### Tirage aléatoire

La méthode la plus simple : le programme simule le lancer de 3 pièces pour chaque trait.

```bash
python yijing_oracle.py
```

### Tirage avec question

Formulez votre question pour une consultation plus ciblée :

```bash
python yijing_oracle.py -q "Quelle direction prendre pour mon projet ?"
```

### Définir les traits manuellement

Si vous avez effectué un tirage physique avec des pièces ou des baguettes d'achillée :

```bash
python yijing_oracle.py -t 7 6 7 6 6 7
```

**Valeurs des traits :**

| Valeur | Type | Symbole | Description |
|--------|------|---------|-------------|
| 6 | Vieux Yin | ━━ ✕ ━━ | Yin mutant (se transforme en Yang) |
| 7 | Jeune Yang | ━━━━━━━ | Yang stable |
| 8 | Jeune Yin | ━━   ━━ | Yin stable |
| 9 | Vieux Yang | ━━━◯━━━ | Yang mutant (se transforme en Yin) |

### Générer tous les fichiers

```bash
python yijing_oracle.py -q "Ma question" --all
```

Cette commande génère :
- **Grille PNG** : Superposition visuelle des 6 traits
- **Rapport PDF** : Document complet avec interprétation
- **Fichier audio** : Séquence sonore aux fréquences sacrées

### Générer une méditation Kasina

```bash
python yijing_oracle.py -q "Ma question" --kasina
```

Cette commande génère :
- **Fichier .kbs** : Session Kasina au format Mindplace
- **Fichier .txt** : Séquence LED
- **Fichier .wav** : Audio binaural stéréo (casque requis)

### Interface Web Streamlit

```bash
streamlit run app.py
```

Puis ouvrir `http://localhost:8501` dans votre navigateur.

---

## Les Grilles "La Livrée d'Hermès"

### Principe

Les 24 grilles créées par **Anibal Edelbert Amiot** représentent les différentes configurations des traits :

| Type | Fichiers | Description |
|------|----------|-------------|
| Yang stable | YANG-1 à YANG-6 | Traits pleins (positions 1-6) |
| Yin stable | YING-1 à YING-6 | Traits brisés (positions 1-6) |
| Yang mutant | YANG-MUT-1 à YANG-MUT-6 | Yang en transformation |
| Yin mutant | YING-MUT-1 à YING-MUT-6 | Yin en transformation |

### Superposition

La grille finale est créée par **superposition multiplicative** des 6 couches correspondant au tirage. Cette technique préserve les couleurs (violet et orange) tout en créant un motif unique pour chaque consultation.

```
Trait 6 (haut)  ────┐
Trait 5         ────┼───► Superposition = Grille unique
Trait 4         ────┤
Trait 3         ────┤
Trait 2         ────┤
Trait 1 (bas)   ────┘
```

{% asset_img grille-exemple.png "Exemple de grille générée" %}

---

## Les Fréquences Sacrées

### Accord 432 Hz

L'application utilise l'accord **432 Hz** (La naturel), considéré comme plus harmonieux que le standard moderne de 440 Hz. Cette fréquence est mathématiquement liée aux proportions naturelles et cosmiques.

### Fréquences des Trigrammes

Chaque trigramme est associé à une fréquence du **Solfège ancien** :

| Trigramme | Symbole | Élément | Fréquence | Bienfait |
|-----------|---------|---------|-----------|----------|
| ☰ Qián (K'ien) | ≡ | Ciel | **852 Hz** | Éveil spirituel |
| ☷ Kūn (K'ouen) | ⚏ | Terre | **396 Hz** | Libération des peurs |
| ☳ Zhèn (Tchen) | ⚌ | Tonnerre | **417 Hz** | Transformation |
| ☵ Kǎn (K'an) | ⚍ | Eau | **528 Hz** | Réparation ADN |
| ☶ Gèn (Ken) | ⚎ | Montagne | **639 Hz** | Connexion, relations |
| ☴ Xùn (Souen) | ⚋ | Vent | **741 Hz** | Expression, intuition |
| ☲ Lí (Li) | ⚊ | Feu | **963 Hz** | Transcendance |
| ☱ Duì (Touei) | ⚏ | Lac | **432 Hz** | Harmonie universelle |

### Fréquences des Traits

| Trait | Fréquence | Note | Description |
|-------|-----------|------|-------------|
| Yang stable (7) | 256 Hz | DO | Ancrage, fondation |
| Yin stable (8) | 192 Hz | SOL-1 | Réceptivité, repos |
| Yang mutant (9) | 288 Hz | RÉ | Expansion créatrice |
| Yin mutant (6) | 216 Hz | LA-1 | Transformation douce |

---

## 🧘 Méditation Kasina / AVS Technology

### Qu'est-ce que l'AVS ?

L'**AVS (Audio-Visual Stimulation)** ou **stimulation audio-visuelle** est une technique utilisant des lumières pulsées et des sons pour induire des états de conscience modifiés par le principe de **FFR (Frequency Following Response)**.

{% note info %}
**FFR** : Le cerveau tend à synchroniser ses ondes cérébrales avec une stimulation externe rythmique. C'est le principe des battements de tambour chamaniques ou des lumières stroboscopiques méditatives.
{% endnote %}

### Format KBS (Kasina Basic Session)

Le format **KBS v2** est le format propriétaire de **Mindplace** pour leurs appareils Kasina et Limina. Un fichier KBS est compact (~3-4 Ko) et contient :

- **Paramètres globaux** : Mode couleur, ColorSet
- **Segments** : Phases de la session avec tous les paramètres

### Paramètres KBS utilisés

| Paramètre | Description | Valeurs Yi Jing |
|-----------|-------------|-----------------|
| `Time` | Durée du segment (secondes) | 5-90s |
| `Beat` | Fréquence de stimulation (Hz) | 5-10 Hz |
| `LPtch` | Pitch oreille gauche (Hz) | 432-852 Hz |
| `RPtch` | Pitch oreille droite (Hz) | LPtch + Beat |
| `LAMDpth` | Profondeur modulation lumière | 50-85% |
| `SAMDpth` | Profondeur modulation son | 0 (binaural pur) |
| `Bright` | Luminosité LED | 0-60% |
| `Vol` | Volume audio | 0-60% |
| `SndWF` | Forme d'onde son | Sine |
| `LgtModWF` | Forme d'onde lumière | Sine |
| `Red/Green/Blue` | Couleur RGB (0-100%) | Selon trigramme |

### États cérébraux ciblés

| État | Fréquence | Caractéristiques |
|------|-----------|------------------|
| **Beta** | 15-30 Hz | Concentration, vigilance |
| **SMR** | 12-15 Hz | Focus calme, attention |
| **Alpha** | 8-13 Hz | Relaxation, visualisation, créativité |
| **Theta** | 4-7 Hz | Méditation profonde, mémoire, insight |
| **Delta** | 0.5-4 Hz | Sommeil profond, guérison |

### Structure de la méditation Yi Jing (5 minutes)

La session est structurée pour guider progressivement vers un état méditatif profond :

| Phase | Durée | Beat | Fréquence | État | Description |
|-------|-------|------|-----------|------|-------------|
| **Fade In** | 5s | 10 Hz | 432 Hz | Alpha | Préparation |
| **Ancrage** | 55s | 10 Hz | 432 Hz | Alpha | Relaxation initiale |
| **Transition** | 15s | 8 Hz | Variable | Alpha→Theta | Descente |
| **Trigramme Bas** | 75s | 7 Hz | Freq. trig. | Theta | Méditation |
| **Transition** | 15s | 6 Hz | Variable | Theta | Approfondissement |
| **Trigramme Haut** | 75s | 5 Hz | Freq. trig. | Theta profond | Insight |
| **Transition** | 15s | 7 Hz | 528 Hz | Theta→Alpha | Remontée |
| **Intégration** | 35s | 8 Hz | 528 Hz | Alpha | Assimilation |
| **Fade Out** | 10s | 10 Hz | 528 Hz | Alpha | Retour |

### Correspondance Trigrammes → Couleurs AVS

Les couleurs sont choisies selon les principes AVS documentés :

| Trigramme | Élément | RGB (%) | Couleur | Principe AVS |
|-----------|---------|---------|---------|--------------|
| ☰ K'ien | Ciel | 100,100,100 | Blanc | Spirituel, transcendance |
| ☷ K'ouen | Terre | 60,40,20 | Ambre | Ancrage, SMR |
| ☳ Tchen | Tonnerre | 100,80,0 | Or | Énergie, éveil |
| ☵ K'an | Eau | 0,40,100 | Bleu | Alpha, relaxation profonde |
| ☶ Ken | Montagne | 50,50,60 | Gris-bleu | Calme, stabilité |
| ☴ Souen | Vent | 30,100,50 | Vert | SMR, relaxation légère |
| ☲ Li | Feu | 100,30,0 | Rouge-orange | Beta, éveil |
| ☱ Touei | Lac | 0,70,100 | Cyan | Alpha, harmonie |

{% note warning %}
**Bleu** : Meilleur pour la relaxation et l'Alpha, mais bloque la mélatonine (éviter avant le sommeil).
**Rouge** : Favorise le Beta et la vigilance, peut supprimer l'Alpha.
**Vert** : Excellent pour le SMR et la relaxation équilibrée.
{% endnote %}

### Utilisation des fichiers Kasina

#### Avec un appareil Mindplace Kasina/Limina

1. **Copier** le fichier `.kbs` sur la carte SD de l'appareil
2. **Insérer** la carte SD dans le Kasina
3. **Naviguer** vers "User Sessions"
4. **Sélectionner** la session Yi Jing
5. **S'installer** confortablement, yeux fermés
6. **Utiliser** les lunettes LED et le casque fournis

#### Sans appareil Kasina (audio uniquement)

1. **Télécharger** le fichier `.wav` généré
2. **Utiliser** un casque stéréo (OBLIGATOIRE pour les battements binauraux)
3. **S'installer** dans un endroit calme, yeux fermés
4. **Écouter** la session complète sans interruption

{% note danger %}
**⚠️ Contre-indications AVS :**
- Épilepsie ou antécédents de crises
- Photosensibilité
- Prise de médicaments psychotropes
- Traumatismes crâniens récents
Consultez un médecin en cas de doute.
{% endnote %}

### Exemple de fichier KBS

```ini
; Yi Jing Meditation - Hexagramme 1: Le Créateur
; Trigramme Bas: K'ien (852 Hz) - Ciel
; Trigramme Haut: K'ien (852 Hz) - Ciel
; Format: KBS v2 - Mindplace Kasina/Limina

[Global]
ColorControlMode=3
GlobalColorSet=1

[Segment0]
; Fade In - Preparation
Time=5.00
Beat=10.00
LPtch=432.00
RPtch=442.00
LPhse=50
SPhse=50
LAMDpth=50
SAMDpth=0
Bright=30
Vol=30
SndWF=Sine
SndModWF=Sine
LgtModWF=Sine
Red=40
Green=0
Blue=80

[Segment1]
; Ancrage Alpha - 432 Hz
Time=55.00
Beat=10.00
...
```

---

## Le Rapport PDF Complet

Le rapport généré en v2.2 contient **3 à 5 pages** selon le tirage :

### Page 1 : Hexagramme Principal

- **En-tête** : Date, heure et question posée
- **Carte hexagramme** : Numéro, caractère chinois, nom pinyin et français
- **Trigrammes** : Supérieur et inférieur avec fréquences et descriptions
- **Traits tirés** : Liste des 6 traits avec fréquences et indication des mutants
- **Grille** La Livrée d'Hermès en couleur (50mm × 65mm)
- **Description** de l'hexagramme

### Page 2 : Textes Traditionnels

- **Le Jugement** : Encadré orange avec texte complet
- **L'Image** : Encadré bleu avec texte complet
- **Interprétation générale** : 
  - Résumé de la combinaison des trigrammes
  - Indication du nombre de traits mutants
  - Direction de l'évolution (si mutation)

### Page 3 : Les Six Traits

Chaque trait est présenté dans un encadré coloré :
- **Yang stable** : Fond vert clair
- **Yin stable** : Fond bleu clair
- **Yang mutant** : Fond orange avec mention "MUTANT 🔄"
- **Yin mutant** : Fond rose avec mention "MUTANT 🔄"

Contenu de chaque encadré :
- Symbole du trait (━━━━━ ou ━━   ━━)
- Type et fréquence (ex: "Yang mutant - 288 Hz (RÉ)")
- Titre traditionnel (ex: "Neuf au commencement")
- Texte complet de l'interprétation

### Page 4 : Traits Mutants (si présents)

Page dédiée uniquement aux traits qui changent :
- **Encadrés agrandis** rouge/rose
- **Direction de la mutation** : "Yin → Yang" ou "Yang → Yin"
- **Texte complet** avec mise en forme spéciale
- **Conseil** : "Portez une attention particulière à ces aspects de votre situation"

### Page 5 : Hexagramme de Mutation (si applicable)

- **Carte mutation** : Numéro, caractère, nom de l'hexagramme résultant
- **Grille après mutation** en couleur
- **Description** de l'hexagramme de mutation
- **Jugement** de l'hexagramme de mutation

### Exemple de génération

```python
from yijing_oracle import generate_pdf_report_complete

# Générer le rapport complet
pdf_data = generate_pdf_report_complete(
    traits=[7, 6, 7, 8, 9, 7],
    question="Quelle direction prendre ?",
    hex_data=hex_data,
    hex_mute_data=hex_mute_data,
    grille_img=grille,
    grille_mut_img=grille_mutation
)

# Sauvegarder
with open("rapport.pdf", "wb") as f:
    f.write(pdf_data)
```

---

## Base de Données JSON

Les données des 64 hexagrammes sont stockées dans `yijing_complet.json` :

```json
{
  "hexagrammes": [
    {
      "numero": 1,
      "nom_pinyin": "K'ien",
      "nom_fr": "Le Créateur",
      "caractere": "乾",
      "trigramme_haut": "K'ien",
      "trigramme_haut_desc": "Le Créateur, le Ciel",
      "trigramme_bas": "K'ien",
      "trigramme_bas_desc": "Le Créateur, le Ciel",
      "description": "L'hexagramme est entièrement composé...",
      "jugement_texte": "LE CRÉATEUR opère...",
      "image_texte": "Le mouvement du ciel...",
      "traits": [
        {
          "position": 1,
          "type_trait": "Neuf",
          "titre": "Neuf au commencement",
          "texte": "Dragon caché. N'agis pas."
        }
      ]
    }
  ]
}
```

---

## Exemples de Code

### Utilisation en tant que bibliothèque Python

```python
from yijing_oracle import YiJingOracle, save_kasina_files

# Créer l'oracle
oracle = YiJingOracle(
    images_dir="./images",
    output_dir="./output",
    json_path="./yijing_complet.json"
)

# Tirage aléatoire
oracle.effectuer_tirage("Quelle est la meilleure approche ?")

# Ou traits manuels
oracle.definir_traits([7, 6, 7, 6, 6, 7], "Ma question")

# Afficher le résultat
oracle.afficher_resultat()

# Accéder aux données
print(f"Hexagramme: {oracle.hexagramme['numero']}")
print(f"Traits: {oracle.traits}")
print(f"Nom: {oracle.hex_data.get('nom_fr')}")

# Générer les fichiers
grille = oracle.sauvegarder_grille()
pdf = oracle.generer_rapport_pdf()
audio = oracle.generer_audio_sequence()

# Générer la méditation Kasina
wav, txt, xml = save_kasina_files(oracle)
print(f"Session Kasina: {wav}")
```

### Personnalisation des chemins

```python
oracle = YiJingOracle(
    images_dir="/chemin/vers/images",
    output_dir="/chemin/vers/sortie",
    json_path="/chemin/vers/yijing_complet.json"
)
```

### Génération Kasina personnalisée

```python
from yijing_oracle import generate_kasina_meditation, TRIGRAMMES

# Générer une méditation avec des paramètres personnalisés
traits = [7, 6, 7, 8, 9, 7]
hex_data = {
    'numero': 37,
    'nom_fr': 'La Famille',
    'trigramme_bas': 'Li',
    'trigramme_haut': 'Souen'
}

# Générer audio et séquence
audio, sequence = generate_kasina_meditation(traits, hex_data, duration_min=5)

# Accéder aux phases
for phase in sequence:
    print(f"{phase['name']}: {phase['freq']} Hz, binaural {phase['beat']} Hz")
```

---

## FAQ

### Les caractères chinois ne s'affichent pas dans le PDF ?

Le programme tente d'utiliser la police CJK `STSong-Light`. Si elle n'est pas disponible, installez les polices Noto CJK :

```bash
# Ubuntu/Debian
sudo apt install fonts-noto-cjk

# Fedora
sudo dnf install google-noto-sans-cjk-fonts
```

### Comment interpréter les traits mutants ?

Les traits mutants (6 et 9) indiquent une situation en transformation. Lisez :
1. D'abord l'hexagramme principal (situation actuelle)
2. Puis les textes des traits mutants (conseil spécifique)
3. Enfin l'hexagramme de mutation (évolution probable)

### Puis-je utiliser mes propres grilles ?

Oui ! Les grilles doivent être :
- Format PNG avec transparence (RGBA)
- Dimensions identiques (595 × 842 pixels recommandé)
- Nommées selon le schéma : `lldh-YY-[YANG|YING][-MUT]-[1-6].png`

### Le fichier KBS ne fonctionne pas sur mon Kasina ?

Vérifiez que :
1. Le fichier est bien copié à la racine de la carte SD
2. L'extension est `.kbs` (pas `.kbs.txt`)
3. Le firmware du Kasina est à jour
4. Le fichier n'est pas corrompu (essayez de le regénérer)

### Puis-je utiliser l'audio binaural sans Kasina ?

Oui ! Le fichier WAV contient les battements binauraux. Utilisez simplement un **casque stéréo** (les écouteurs ou haut-parleurs ne fonctionneront pas pour l'effet binaural).

### Comment créer une session plus longue ?

Modifiez le paramètre `duration_minutes` dans le code :

```python
kbs_content, segments = generate_kbs_session(hex_data, duration_minutes=10)
```

---

## Références AVS

### Documentation Mindplace

- [Mindplace Support](https://mindplacesupport.com)
- Documentation KBS v2 (Kbs-v2-description-1.pdf)

### Études et articles

- "AVS Technology" - Ayrmetes Advanced Cognitive Technologies (2004, 2009)
- "The Clinical Guide to Sound and Light" - Thomas Budzynski, Ph.D.
- "Mind States 2" - Michael Landgraf

### Fréquences cérébrales

- **Résonance de Schumann** : 7.83 Hz (±0.5 Hz) - Fréquence électromagnétique terrestre
- **Alpha** : Relaxation, visualisation (proche de Schumann)
- **Theta** : Accès à l'inconscient, traitement émotionnel

---

## Crédits

- **Grilles "La Livrée d'Hermès"** : Anibal Edelbert Amiot
- **Développement** : [CyberMind.FR](https://cybermind.fr)
- **Textes Yi Jing** : Traduction Wilhelm/Perrot
- **Source des textes** : [wengu.tartarie.com](http://wengu.tartarie.com/wg/wengu.php?l=Yijing&lang=fr)
- **Format KBS** : Mindplace Inc.
- **Principes AVS** : Robert Austin (Mindplace), Dr. Harold Russell, Thomas Budzynski

---

## Ressources

- [Yi Jing sur Wikipedia](https://fr.wikipedia.org/wiki/Yi_Jing)
- [Les 64 Hexagrammes](https://fr.wikipedia.org/wiki/Hexagramme_du_Yi_Jing)
- [Solfège sacré](https://fr.wikipedia.org/wiki/Solfège_sacré)
- [Accord 432 Hz](https://fr.wikipedia.org/wiki/La_432_Hz)
- [Mindplace](https://mindplace.com)
- [AVS Journal](https://avsjournal.com)

---

> *易經 - Le changement est la seule constante de l'univers*

{% note info %}
**Téléchargement** : Le package complet est disponible sur [GitHub](https://github.com/cybermind-fr/yijing-oracle) ou en téléchargement direct.
{% endnote %}

{% note success %}
**Version 2.1** : Avec génération de sessions Kasina KBS pour méditation AVS !
{% endnote %}

--> https://yijing-oracle.streamlit.app/
