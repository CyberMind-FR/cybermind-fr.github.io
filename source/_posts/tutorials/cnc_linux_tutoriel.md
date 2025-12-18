---
title: Tutoriel - Utiliser des logiciels open source pour CNC sous Linux
lang: fr
date: 2025-11-06 17:00:00
tags: 
- FabLab
- Cyber
- Mood
- contribute
categories:
- Cyber
- Mood
author: 🧙 -- Gandalf (from "The Conjurers")
publish: true
hidden: false
---
## 🛠️ Tutoriel : Utiliser des logiciels open source pour CNC sous Linux 🐧

Voici un guide pour t’aider à démarrer avec des logiciels open source compatibles **GRBL** sur **Linux**.
<!-- more -->
### 1️⃣ Universal Gcode Sender (UGS)

Universal Gcode Sender est une interface populaire pour envoyer des commandes **G-code** à ta CNC GRBL.

🔗 **Site officiel** : [winder.github.io/ugs_website](https://winder.github.io/ugs_website/)  
💻 **Installation** :
- ☕ Requiert **Java 8+**
- 📦 Télécharge la version **UGS Platform**
- 🖥️ Exécute le fichier `.sh` (ex : `ugsplatform-linux.sh`)

✨ **Fonctionnalités** :
- 🎮 Contrôle manuel des axes (jogging)
- 🧭 Visualisation du G-code
- 🔁 Contrôle de flux GRBL

---

### 2️⃣ Candle

Candle est une autre interface simple et efficace pour piloter une machine GRBL.

🔗 **GitHub** : [github.com/Denvi/Candle](https://github.com/Denvi/Candle)  
💻 **Installation** :
- 📥 Télécharge le binaire `.AppImage` ou `.tar.gz`
- 🔓 Rends-le exécutable : `chmod +x fichier`
- 🚀 Lance-le

✨ **Fonctionnalités** :
- 🖱️ Interface intuitive
- 🧱 Visualisation 3D du G-code
- ⚙️ Réglages faciles de GRBL

---

### 3️⃣ LinuxCNC (option avancée)

🔧 **LinuxCNC** est une solution puissante, mais non compatible GRBL. Idéale pour les machines plus complexes.

🔗 **Site officiel** : [linuxcnc.org](http://linuxcnc.org/)  
📌 **Note** : fonctionne souvent avec des ports parallèles ou cartes spécifiques.

---

### 4️⃣ Connexion & configuration GRBL

🧩 Étapes de connexion :
- 🔍 Vérifie le port avec : `ls /dev/ttyUSB*`
- ⚡ Configure le **baud rate** à `115200`
- 🧪 Teste la communication avec la commande `$$` dans le terminal G-code

---

### 5️⃣ Ressources utiles 📚

- 📖 [Documentation GRBL](https://github.com/gnea/grbl/wiki)
- 💬 [Forum CNCZone (FR)](https://www.cnczone.com/forums/french-discussion/)

---

🧰 Avec ces outils, tu seras prêt à piloter ta fraiseuse CNC GRBL sous Linux comme un pro. Bonne fabrication ! 🪚💡
