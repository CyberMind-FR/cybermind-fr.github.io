---
title: Poésie - La Minute Papillon — Mix orchestral complet…
lang: fr
date: 2025-11-07 09:17:00
tags:
- Poésie
- Limours
- ICIEB
categories:
- Mind
- Poésies
##publish: true
private: false
hidden: false
---
  
  # 🎧 La Minute Papillon — Mix orchestral complet (🎙️ chant + 🎻 accompagnement ambiant moderne)

Ce guide explique comment générer **automatiquement** un **mix final** de *La Minute Papillon* :  
> **voix chantée (MP3)** + **orchestration ambiante moderne** (🎹 piano, 🎻 cordes, 🌫️ pad, 🪈 flûte, 🎸 basse, 🥁 percussions).

---<!-- more -->

## ⚙️ Prérequis

Installe Python 3.9+ et les bibliothèques nécessaires :

```bash
python -m pip install midiutil pyfluidsynth librosa soundfile numpy scipy
```
💡 Installe aussi un **SoundFont GM (.sf2)** (ex. `FluidR3_GM.sf2`, `Arachno SoundFont.sf2`, `MuseScore_General.sf2`).

---

## 📁 Préparation du projet

1. Place ton **fichier vocal** dans le même dossier : `la minute papillon.mp3` 🎙️  
2. Télécharge un **.sf2** et indique son chemin dans `SOUNDFONT_PATH` ci‑dessous 🪗.

---

## 🧠 Structure & orchestration

- **Tempo :** 76 BPM ⏱️  
- **Tonalité :** Ré mineur (Dm) 🎼  
- **Durée cible :** ~4:00 ⏳  
- **Style :** *chanson poétique intime* en version **ambiant moderne** 🌫️

**Progressions d’accords par section :**  
- Intro : Dm – Bb – F – C  
- Couplet : Dm – Bb – F – C  
- Refrain : Bb – F – Gm – A7  
- Pont : Gm – Dm – Bb – A7  
- Final : Dm – Bb – F – Dm

---

## 🧩 Script Python (copie‑colle dans `mix_orchestral_papillon.py`)

```python
# -*- coding: utf-8 -*-
"""
La Minute Papillon - Mix final (chant + orchestre ambiant moderne)
- Génère un accompagnement orchestral (MIDI) en Dm, 76 bpm, ~4:00
- Rendre le MIDI en WAV via FluidSynth (SoundFont GM)
- Charger la voix (MP3), caler, traitement pro léger, mixer et exporter en WAV
"""

import os
import math
import tempfile
import numpy as np
import soundfile as sf
import librosa
import librosa.effects
from midiutil import MIDIFile
from scipy.signal import butter, lfilter

# =========
# CONFIG
# =========
INPUT_MP3_PATH   = "la minute papillon.mp3"   # <-- Ton MP3 voix finale
SOUNDFONT_PATH   = "/chemin/vers/ton/GM.sf2"  # <-- Ton .sf2 (ex: FluidR3_GM.sf2)
OUTPUT_WAV_PATH  = "La_Minute_Papillon_Mix_Final.wav"

TEMPO_BPM        = 76
KEY_ROOT_MIDI    = 62  # D4
TARGET_DURATION  = 240.0  # ~4 minutes (secondes)
INTENSITY_DB     = -20.0  # niveau d'accompagnement (plus bas = plus doux)
ORCH_OFFSET_SEC  = 0.0    # décalage si besoin (+/- secondes)

# ======================
# HARMONIE & FORMES
# ======================
Dm = [62, 65, 69]; Bb = [58, 62, 65]; F  = [53, 57, 60]; C  = [55, 59, 62]
Gm = [55, 58, 62]; A7 = [57, 61, 64]

INTRO   = [Dm, Bb, F, C]
COUPLET = [Dm, Bb, F, C]
REFRAIN = [Bb, F, Gm, A7]
PONT    = [Gm, Dm, Bb, A7]
FINAL   = [Dm, Bb, F, Dm]

SECTIONS = [
    ("Intro",   INTRO),
    ("Couplet", COUPLET),
    ("Refrain", REFRAIN),
    ("Couplet", COUPLET),
    ("Refrain", REFRAIN),
    ("Pont",    PONT),
    ("Refrain", REFRAIN),
    ("Final",   FINAL),
]

# ===============
# OUTILS AUDIO
# ===============
def db_to_lin(db): return 10.0 ** (db / 20.0)

def normalize_peak(y, peak=0.98):
    m = np.max(np.abs(y)) + 1e-12
    return y * (peak / m)

def butter_highpass(y, sr, cutoff=80.0, order=2):
    b, a = butter(order, cutoff / (0.5 * sr), btype='high')
    return lfilter(b, a, y)

def simple_comp(y, thresh_db=-14, ratio=2.5, makeup_db=0.0):
    rms = np.sqrt(np.mean(y**2) + 1e-12)
    lvl_db = 20*np.log10(rms + 1e-12)
    if lvl_db > thresh_db:
        diff = lvl_db - thresh_db
        gain_red_db = diff - diff/ratio
        y = y * db_to_lin(-(gain_red_db))
    if makeup_db != 0.0:
        y *= db_to_lin(makeup_db)
    return y

# =============================
# MIDI → ORCHESTRATION (GM)
# =============================
def build_orchestral_midi(midi_path, tempo=TEMPO_BPM):
    """
    Pistes:
    0 Piano, 1 Flute (lignes discrètes), 2 Strings, 3 Pad, 4 Bass, 5 Percs
    Orchestration "ambiant moderne": nappes, arpèges doux, percs vaporeuses.
    """
    mf = MIDIFile(6)
    for trk in range(6):
        mf.addTempo(trk, 0, tempo)

    CH_PIANO, CH_FLUTE, CH_STR, CH_PAD, CH_BASS, CH_DR = 0,1,2,3,4,9
    PRG_PIANO, PRG_FLUTE, PRG_STR, PRG_PAD, PRG_BASS = 0,73,48,89,32
    mf.addProgramChange(0, CH_PIANO, 0, PRG_PIANO)
    mf.addProgramChange(1, CH_FLUTE, 0, PRG_FLUTE)
    mf.addProgramChange(2, CH_STR,   0, PRG_STR)
    mf.addProgramChange(3, CH_PAD,   0, PRG_PAD)
    mf.addProgramChange(4, CH_BASS,  0, PRG_BASS)
    # Percussions sur CH 9 (GM) : pas de ProgramChange

    flute_motif = [62, 64, 65, 67, 69, 70, 72, 74]

    t = 0.0
    for name, sect in SECTIONS:
        for chord in sect:
            dur = 4.0
            root = min(chord); third = sorted(chord)[1]; fifth = max(chord)

            # Piano: arpèges feutrés (8 croches)
            arp = [root, fifth, third, fifth, root, fifth, third, fifth]
            for i, n in enumerate(arp):
                mf.addNote(0, CH_PIANO, n, t + i*0.5, 0.48, 60)

            # Strings: nappes aérées (+12) tenues
            for n in chord:
                mf.addNote(2, CH_STR, n+12, t, dur, 50)

            # Pad: fondamentale/quinte en bas, très doux
            mf.addNote(3, CH_PAD, root-12,  t, dur, 38)
            mf.addNote(3, CH_PAD, fifth-12, t, dur, 34)

            # Basse: fondamentale tenue avec souffle
            mf.addNote(4, CH_BASS, root-24, t,   2.8, 48)
            mf.addNote(4, CH_BASS, root-24, t+2.0, 1.6, 44)

            # Flûte: petite respiration mélodique
            mf.addNote(1, CH_FLUTE, flute_motif[(int(t)) % len(flute_motif)], t+2.5, 1.2, 54)

            # Percussions vaporeuses (GM: 42 HH, 37 SideStick, 44 Pedal HH)
            mf.addNote(5, 9, 42, t+0.0, 0.08, 22)
            mf.addNote(5, 9, 37, t+1.5, 0.08, 20)
            mf.addNote(5, 9, 42, t+2.0, 0.08, 22)
            mf.addNote(5, 9, 44, t+3.0, 0.08, 18)

            t += dur

    with open(midi_path, "wb") as f:
        mf.writeFile(f)

def render_midi_to_wav(midi_path, sf2_path, out_wav_path, sr=48000):
    """Rendu via pyfluidsynth / FluidSynth."""
    import fluidsynth
    fs = fluidsynth.Synth(samplerate=sr)
    sfid = fs.sfload(sf2_path)
    fs.program_select(0, sfid, 0, 0)
    fs.start(driver="file", filename=out_wav_path)
    fs.midi_load(midi_path)
    fs.midi_play()
    fs.delete()

# ============
# PIPELINE
# ============
def main():
    assert os.path.exists(INPUT_MP3_PATH), f"Introuvable: {INPUT_MP3_PATH}"
    assert os.path.exists(SOUNDFONT_PATH), f"Introuvable: {SOUNDFONT_PATH}"

    # 1) Charger la voix
    voice, sr_v = librosa.load(INPUT_MP3_PATH, sr=48000, mono=True)
    voice = normalize_peak(voice, 0.98)

    # 2) Générer et rendre l'orchestre
    with tempfile.TemporaryDirectory() as td:
        midi_path = os.path.join(td, "orch.mid")
        wav_orch  = os.path.join(td, "orch.wav")
        build_orchestral_midi(midi_path, tempo=TEMPO_BPM)
        render_midi_to_wav(midi_path, SOUNDFONT_PATH, wav_orch, sr=48000)
        orch, sr_o = sf.read(wav_orch, dtype="float32")
        if orch.ndim == 2:
            orch = orch.mean(axis=1)  # downmix mono doux

    # 3) Rééchantillonner si besoin
    if sr_o != sr_v:
        orch = librosa.resample(orch, orig_sr=sr_o, target_sr=sr_v)
        sr_mix = sr_v
    else:
        sr_mix = sr_o

    # 4) Traitement pro léger VOIX
    v = voice.copy()
    v = butter_highpass(v, sr_mix, cutoff=80.0, order=2)  # coupe-bas
    v = simple_comp(v, thresh_db=-14, ratio=2.5, makeup_db=0.0)

    # 5) Mise à niveau ORCHESTRE (plus doux que la voix)
    orch = orch * db_to_lin(INTENSITY_DB)

    # 6) Harmonisation des longueurs
    n = max(len(v), len(orch))
    if len(v)   < n: v    = np.pad(v,    (0, n-len(v)))
    if len(orch)< n: orch = np.pad(orch, (0, n-len(orch)))

    # 7) Mix & normalisation de crête
    mix = v + orch
    mix = normalize_peak(mix, 0.98)

    # 8) Export WAV 48k / 24-bit
    sf.write(OUTPUT_WAV_PATH, mix, sr_mix, subtype="PCM_24")
    print(f"✅ Mix final exporté : {OUTPUT_WAV_PATH}")

if __name__ == "__main__":
    main()
```

---

## ▶️ Utilisation

```bash
python mix_orchestral_papillon.py
```
🎉 Sortie : **`La_Minute_Papillon_Mix_Final.wav`** — **chant + orchestre ambiant moderne**, mix doux et poétique.

---

## 🔧 Réglages rapides

- **Décalage synchro** : `ORCH_OFFSET_SEC = 0.0` → augmente à `0.2` si l’orchestre démarre trop tôt.  
- **Niveau orchestre** : `INTENSITY_DB = -22.0` (plus doux) ou `-16.0` (plus présent).  
- **Tempo** : `TEMPO_BPM = 76` (garde l’intimité).

---

## 🪶 Crédit

Création orchestrale & script : **KERMA** — *La Minute Papillon* 🌙  
Poésie et souffle : **voix + lumière** ✨
