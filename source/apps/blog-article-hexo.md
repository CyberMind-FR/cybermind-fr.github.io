---
title: "Kasina θ Pro : L'Art de l'Entrainement Neuronal"
date: 2025-12-19
categories:
  - Projets
  - Bien-être
tags:
  - meditation
  - neuroscience
  - pwa
  - audiostrobe
  - brainwave
  - open-source
cover: /images/kasina-theta-pro-cover.jpg
excerpt: "Présentation de Kasina θ Pro, une application web progressive open-source pour générer des sessions audio-visuelles de méditation et d'entraînement cérébral avec encodage AudioStrobe® et SpectraStrobe™."
---

# Kasina θ Pro : L'Art de l'Entrainement Neuronal

> *"La conscience est une musique que l'on peut accorder"*

Après plusieurs mois de développement, je suis heureux de présenter **Kasina θ Pro**, une Progressive Web App (PWA) open-source dédiée à la génération de sessions audio-visuelles pour la méditation et l'entraînement cérébral.

<!-- more -->

## 🧠 Le Concept : Entrainement Neuronal

Notre cerveau produit naturellement des ondes électromagnétiques à différentes fréquences, chacune correspondant à un état de conscience particulier :

| Onde | Fréquence | État de Conscience |
|------|-----------|-------------------|
| **δ Delta** | 0.5-4 Hz | Sommeil profond, régénération cellulaire |
| **θ Theta** | 4-8 Hz | Méditation profonde, créativité, accès inconscient |
| **α Alpha** | 8-13 Hz | Relaxation éveillée, apprentissage optimal |
| **β Beta** | 13-30 Hz | Concentration active, analyse, productivité |
| **γ Gamma** | 30-100 Hz | États de conscience élevés, insight |

Le phénomène d'**entrainement neuronal** (brainwave entrainment) exploite la tendance naturelle du cerveau à synchroniser son activité sur des stimuli rythmiques externes. En combinant :

- **Battements binauraux** (différence de fréquence entre oreilles)
- **Stimulation lumineuse photic** (via lunettes GanzFrames)
- **Géométries sacrées** pour la contemplation visuelle

...on peut influencer de manière non-invasive les rythmes cérébraux et faciliter l'accès à des états méditatifs, créatifs ou de concentration profonde.

## ✨ Les Fonctionnalités

### Audio Engine Avancé

L'application génère des **battements binauraux** précis avec :

- Fréquences L/R indépendantes (50-655 Hz)
- Multiple formes d'onde (sine, square, triangle, sawtooth)
- Pink noise calibré pour masquer les distractions
- **Whispers subliminaux** en 9 langues + Sanskrit
- **Anti-habituation** : micro-variations aléatoires pour maintenir l'attention du cerveau

Le tout orchestré par un **clock maître unique** basé sur `AudioContext.currentTime` garantissant une synchronisation sample-accurate entre audio et visuels.

### Géométries Sacrées Évolutives

Le moteur visuel propose plusieurs patterns de **géométrie sacrée** :

- 🌸 **Fleur de Vie** : Harmonie universelle
- 🔺 **Sri Yantra** : Méditation tantrique
- ⬡ **Cube de Métatron** : Structure de l'univers
- 🍩 **Torus** : Flux énergétique
- 🐚 **Spirale Fibonacci** : Nombre d'or
- 👁️ **Vesica Piscis** : Union des opposés

Ces mandalas **pulsent en synchronisation** avec la respiration et les battements lumineux, créant un effet hypnotique propice à la méditation.

### Encodage AudioStrobe® et SpectraStrobe™

Pour les utilisateurs d'appareils AVS (Audio-Visual Stimulation) comme le **MindPlace Kasina** ou **Limina**, l'application encode les signaux de contrôle lumineux directement dans les fichiers audio :

**AudioStrobe®** (2 canaux) :
```
Signal = Audio + (Carrier_19kHz × Modulation_Lumière × Niveau)
```

**SpectraStrobe™** (6 canaux RGB) :
```
Porteuses : L-R@17.5k  L-G@18.0k  L-B@18.5k
            R-R@19.0k  R-G@19.5k  R-B@20.0k
```

Exportez en WAV ou MP3, copiez sur la carte SD du Kasina, et vos lunettes GanzFrames s'illumineront en synchronisation parfaite avec l'audio !

### Capteurs Mobile

Sur smartphone, l'application exploite les **capteurs IMU** pour :

- 🚶 **Marche méditative** : détection du rythme de pas
- 🧠 **Détection de fatigue** : analyse de la variabilité du pas
- 🌬️ **Synchronisation souffle** : via le microphone

La session s'adapte ainsi à votre physiologie réelle.

### Mode Rituel

Inspiré des traditions contemplatives, le **mode rituel** permet de :

1. **Poser une intention** avant la session
2. Pratiquer en pleine conscience
3. **Clôturer** avec statistiques et notes personnelles
4. **Exporter** un journal de pratique

## 📱 PWA Offline

Kasina θ Pro est une **Progressive Web App** :

- ✅ Installation sur écran d'accueil (mobile & desktop)
- ✅ Fonctionnement **100% hors-ligne**
- ✅ Mode **plein écran verrouillé** pour immersion totale
- ✅ Aucune dépendance serveur après installation

## 🛠️ Architecture Technique

Le projet est structuré en **modules ES6** :

```
kasina-pro/
├── js/
│   ├── profiles.js      # 20 sous-profils + whispers multilingues
│   ├── audio-engine.js  # Génération audio + encodage AS/SS
│   ├── visual-engine.js # Mandalas + particules
│   ├── sensors.js       # IMU + microphone
│   └── app.js           # Orchestration
├── sw.js                # Service Worker offline
└── manifest.json        # PWA manifest
```

### Clock Maître Unique

Toute la synchronisation repose sur `AudioContext.currentTime` :

```javascript
getMasterTime() {
    return this.audioContext.currentTime;
}

// La lumière est dérivée de l'audio (sample-accurate)
calculateLightMod(t, params) {
    const wavePhase = t * params.beat * Math.PI * 2;
    return Math.sin(wavePhase) * 0.5 + 0.5;
}
```

### Anti-Habituation

Pour éviter que le cerveau ne "s'habitue" aux stimuli, des **micro-variations aléatoires** sont appliquées :

```javascript
getMicroVariation(t, baseFreq, amount) {
    const v1 = Math.sin(t * 0.1) * 0.3;
    const v2 = Math.sin(t * 0.23) * 0.2;
    const v3 = Math.sin(t * 0.07) * 0.5;
    return baseFreq + (v1 + v2 + v3) * amount * baseFreq * 0.02;
}
```

## 🚀 Essayer l'Application

### Demo Live

👉 **[Kasina θ Pro - Demo](https://cybermind.fr/apps/kasina-pro/)**

### Code Source

Le projet est **open-source** sous licence MIT :

👉 **[GitHub Repository](https://github.com/gandalf-music/kasina-pro)**

### Installation PWA

1. Ouvrez le lien sur votre smartphone/tablette
2. Menu navigateur → "Ajouter à l'écran d'accueil"
3. L'app fonctionne désormais offline !

## ⚠️ Avertissements

### ÉPILEPSIE
**Les stimulations lumineuses peuvent déclencher des crises chez les personnes photosensibles.**

### Recommandations
- Commencez par des sessions courtes (5-10 min)
- Volume audio modéré
- Ne pas utiliser en conduisant
- Consultez un professionnel si troubles psychiatriques

## 🎯 Prochaines Étapes

La roadmap prévoit :

- [ ] Intégration **HRV** (variabilité cardiaque)
- [ ] Mode **biofeedback EEG** (via Muse, OpenBCI...)
- [ ] Sessions **guidées vocales**
- [ ] Synchronisation **multi-utilisateurs**
- [ ] Export **MIDI** pour synthétiseurs modulaires

## 🙏 Conclusion

Kasina θ Pro représente une convergence entre :

- Les **neurosciences** modernes
- Les **traditions contemplatives** millénaires
- La **technologie web** actuelle

L'objectif n'est pas de remplacer une pratique méditative authentique, mais d'offrir un **outil d'exploration** pour ceux qui souhaitent expérimenter avec les états de conscience.

Comme le disait Aldous Huxley : *"Les portes de la perception se nettoient, et tout apparaît tel qu'il est : infini."*

Bonne exploration intérieure ! 🧿

---

**Tags** : #meditation #neuroscience #pwa #audiostrobe #brainwave #opensource #kasina #mindplace

**Ressources** :
- [MindPlace - Fabricant du Kasina](https://mindplace.com/)
- [Brainwave Entrainment - Wikipedia](https://en.wikipedia.org/wiki/Brainwave_entrainment)
- [AudioStrobe Specification](http://audiostrobe.com/)
