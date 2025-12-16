---
title: Photo Cloud Generator - Créez des nuages de photos artistiques
date: 2025-12-11 10:50:00
tags:
  - python
  - image-processing
  - pillow
  - streamlit
  - tool
  - photo
  - raw
  - heic
categories:
  - Outils
  - Python
thumbnail: /images/photo-cloud/thumbnail.png
description: Outil Python pour créer des compositions artistiques de photos avec plusieurs modes de disposition. Supporte tous les formats (JPEG, PNG, HEIC, RAW, HDR...) avec interface Streamlit, Web et CLI.
---

Créez des compositions artistiques de photos avec une photo principale entourée d'un nuage de photos secondaires. Supporte tous les formats d'image courants incluant RAW et HEIC.

<!-- more -->

## ✨ Fonctionnalités

- 🪐 **Mode Orbital** - Photos sur orbites concentriques
- 🌀 **Mode Spirale** - Disposition en spirale dynamique
- ☁️ **Mode Nuage** - Distribution aléatoire naturelle
- 🧱 **Mode Briques** - Mur de briques avec décalage
- 🎨 **Éclaircissement progressif** - Fade avec la distance
- 🔲 **Fond transparent** - Export PNG avec alpha
- 📷 **Tous formats** - JPEG, PNG, HEIC, RAW, HDR...
- 🔄 **Correction automatique** - Redressement EXIF des photos

---

## 📷 Formats Supportés

| Catégorie | Formats | Dépendance |
|-----------|---------|------------|
| **Standards** | JPEG, PNG, GIF, WebP, BMP, TIFF, TGA, PCX, PPM, ICO, PSD | Pillow |
| **Apple/Mobile** | HEIC, HEIF, AVIF | pillow-heif |
| **Canon RAW** | CR2, CR3, CRW | rawpy |
| **Nikon RAW** | NEF, NRW | rawpy |
| **Sony RAW** | ARW, SRF, SR2 | rawpy |
| **Fujifilm RAW** | RAF | rawpy |
| **Autres RAW** | ORF, RW2, PEF, DNG, MRW, ERF, RW2, X3F, IIQ, MEF, 3FR | rawpy |
| **HDR** | EXR, HDR, PFM, RGBE | imageio |
| **Scientifique** | FITS | imageio |
| **Autres** | RIFF, SGI, DDS, QOI, JPEG2000 | Pillow |

---

## 🎮 Démonstration Interactive

Testez l'outil directement dans votre navigateur :

{% raw %}
<style>
.photo-cloud-demo {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  border-radius: 15px;
  padding: 25px;
  margin: 30px 0;
  color: #e0e0e0;
}
.photo-cloud-demo h3 {
  color: #00d2ff;
  margin-top: 0;
  padding-bottom: 10px;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}
.demo-grid {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 20px;
  margin-top: 20px;
}
@media (max-width: 800px) {
  .demo-grid { grid-template-columns: 1fr; }
}
.demo-controls {
  background: rgba(0,0,0,0.3);
  border-radius: 10px;
  padding: 15px;
}
.demo-preview {
  background: rgba(0,0,0,0.3);
  border-radius: 10px;
  min-height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}
.demo-preview canvas {
  max-width: 100%;
  max-height: 400px;
  border-radius: 5px;
}
.layout-buttons {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 6px;
  margin-bottom: 15px;
}
.layout-btn {
  padding: 8px 4px;
  border: 2px solid rgba(255,255,255,0.2);
  border-radius: 8px;
  background: rgba(0,0,0,0.3);
  color: #fff;
  cursor: pointer;
  text-align: center;
  transition: all 0.2s;
  font-size: 0.75em;
}
.layout-btn:hover {
  border-color: rgba(0,210,255,0.5);
  background: rgba(0,210,255,0.1);
}
.layout-btn.active {
  border-color: #00d2ff;
  background: rgba(0,210,255,0.2);
}
.layout-btn .icon {
  font-size: 1.4em;
  display: block;
  margin-bottom: 2px;
}
.control-group {
  margin-bottom: 12px;
}
.control-group label {
  display: block;
  font-size: 0.8em;
  color: #aaa;
  margin-bottom: 4px;
}
.control-group input[type="range"] {
  width: 100%;
  margin: 3px 0;
}
.control-value {
  color: #00d2ff;
  font-weight: bold;
}
.checkbox-label {
  display: flex;
  align-items: center;
  cursor: pointer;
  font-size: 0.85em;
  margin-top: 10px;
}
.checkbox-label input {
  margin-right: 8px;
  width: 16px;
  height: 16px;
}
.demo-btn {
  width: 100%;
  padding: 10px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9em;
  font-weight: bold;
  margin-top: 8px;
  transition: all 0.3s;
}
.demo-btn.primary {
  background: linear-gradient(90deg, #00d2ff, #3a7bd5);
  color: white;
}
.demo-btn.secondary {
  background: rgba(255,255,255,0.1);
  color: #fff;
  border: 1px solid rgba(255,255,255,0.2);
}
.demo-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.3);
}
.checkerboard {
  background-image: 
    linear-gradient(45deg, #808080 25%, transparent 25%),
    linear-gradient(-45deg, #808080 25%, transparent 25%),
    linear-gradient(45deg, transparent 75%, #808080 75%),
    linear-gradient(-45deg, transparent 75%, #808080 75%);
  background-size: 20px 20px;
  background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
  background-color: #a0a0a0;
}
</style>

<div class="photo-cloud-demo">
  <h3>🖼️ Générateur de Nuage de Photos</h3>
  
  <div class="demo-grid">
    <div class="demo-controls">
      <div class="layout-buttons">
        <button class="layout-btn active" data-layout="orbital" onclick="demoSelectLayout('orbital')">
          <span class="icon">🪐</span>Orbital
        </button>
        <button class="layout-btn" data-layout="spiral" onclick="demoSelectLayout('spiral')">
          <span class="icon">🌀</span>Spirale
        </button>
        <button class="layout-btn" data-layout="cloud" onclick="demoSelectLayout('cloud')">
          <span class="icon">☁️</span>Nuage
        </button>
        <button class="layout-btn" data-layout="brick" onclick="demoSelectLayout('brick')">
          <span class="icon">🧱</span>Briques
        </button>
      </div>
      
      <div class="control-group">
        <label>Nombre de photos: <span class="control-value" id="demoCountValue">12</span></label>
        <input type="range" id="demoCount" min="6" max="30" value="12" oninput="demoUpdate()">
      </div>
      
      <div class="control-group">
        <label>Taille miniatures: <span class="control-value" id="demoThumbValue">40</span>px</label>
        <input type="range" id="demoThumb" min="25" max="60" value="40" oninput="demoUpdate()">
      </div>
      
      <div class="control-group">
        <label>Éclaircissement: <span class="control-value" id="demoFadeValue">0.50</span></label>
        <input type="range" id="demoFade" min="0" max="100" value="50" oninput="demoUpdate()">
      </div>
      
      <div class="control-group">
        <label>Courbe du fade: <span class="control-value" id="demoCurveValue">1.0</span></label>
        <input type="range" id="demoCurve" min="3" max="20" value="10" oninput="demoUpdate()">
      </div>
      
      <div class="control-group" id="demoGapGroup" style="display:none;">
        <label>Espacement: <span class="control-value" id="demoGapValue">3</span>px</label>
        <input type="range" id="demoGap" min="1" max="10" value="3" oninput="demoUpdate()">
      </div>
      
      <label class="checkbox-label">
        <input type="checkbox" id="demoTransparent" onchange="demoGenerate()">
        Fond transparent
      </label>
      
      <button class="demo-btn primary" onclick="demoGenerate()">🔄 Générer</button>
      <button class="demo-btn secondary" onclick="demoDownload()">💾 Télécharger PNG</button>
    </div>
    
    <div class="demo-preview" id="demoPreview">
      <canvas id="demoCanvas"></canvas>
    </div>
  </div>
</div>

<script>
(function() {
  var demoLayout = 'orbital';
  var demoColors = [
    ['#FF6B6B','#FF8E8E'],['#4ECDC4','#6EE7DF'],['#45B7D1','#67D1E8'],
    ['#96CEB4','#B8E6CC'],['#FFEAA7','#FFF3C4'],['#DDA0DD','#E8C0E8'],
    ['#98D8C8','#B8F0E0'],['#F7DC6F','#FAE8A0'],['#BB8FCE','#D4B8E0'],
    ['#85C1E9','#A8D4F0'],['#F8B500','#FAC832'],['#00CED1','#40E8E8'],
    ['#FF69B4','#FF8DC7'],['#32CD32','#64E164'],['#FF7F50','#FF9F7D'],
    ['#9370DB','#B090E8'],['#20B2AA','#50D2CA'],['#FFD700','#FFE44D'],
    ['#FF6347','#FF8673'],['#00FA9A','#50FCB8'],['#BA55D3','#D080E8'],
    ['#7B68EE','#9D90F0'],['#3CB371','#68D598'],['#FF4500','#FF6B33'],
    ['#1E90FF','#50A8FF'],['#FF1493','#FF50B0'],['#00BFFF','#40D0FF'],
    ['#ADFF2F','#C8FF6B'],['#DC143C','#E84868'],['#00FF7F','#50FFA0']
  ];

  window.demoSelectLayout = function(layout) {
    demoLayout = layout;
    document.querySelectorAll('.layout-btn').forEach(function(btn) {
      btn.classList.toggle('active', btn.getAttribute('data-layout') === layout);
    });
    document.getElementById('demoGapGroup').style.display = layout === 'brick' ? 'block' : 'none';
    demoGenerate();
  };

  window.demoUpdate = function() {
    document.getElementById('demoCountValue').textContent = document.getElementById('demoCount').value;
    document.getElementById('demoThumbValue').textContent = document.getElementById('demoThumb').value;
    document.getElementById('demoFadeValue').textContent = (document.getElementById('demoFade').value / 100).toFixed(2);
    document.getElementById('demoCurveValue').textContent = (document.getElementById('demoCurve').value / 10).toFixed(1);
    document.getElementById('demoGapValue').textContent = document.getElementById('demoGap').value;
    demoGenerate();
  };

  window.demoGenerate = function() {
    var canvas = document.getElementById('demoCanvas');
    var ctx = canvas.getContext('2d');
    var preview = document.getElementById('demoPreview');
    
    var width = 550, height = 380;
    canvas.width = width;
    canvas.height = height;
    
    var transparent = document.getElementById('demoTransparent').checked;
    var numPhotos = parseInt(document.getElementById('demoCount').value);
    var thumbSize = parseInt(document.getElementById('demoThumb').value);
    var fade = parseInt(document.getElementById('demoFade').value) / 100;
    var fadeCurve = parseInt(document.getElementById('demoCurve').value) / 10;
    var gap = parseInt(document.getElementById('demoGap').value);
    
    if (transparent) {
      preview.classList.add('checkerboard');
      ctx.clearRect(0, 0, width, height);
    } else {
      preview.classList.remove('checkerboard');
      ctx.fillStyle = '#1e1e23';
      ctx.fillRect(0, 0, width, height);
    }
    
    var cx = width / 2, cy = height / 2;
    var maxDist = Math.sqrt(cx * cx + cy * cy);
    var mainSize = 90, mainR = mainSize / 2;
    var minR = mainR + thumbSize / 2 + 12;
    var maxR = Math.min(width, height) / 2 - thumbSize / 2;
    
    var positions = [];
    if (demoLayout === 'orbital') positions = genOrbital(cx, cy, numPhotos, minR, maxR, thumbSize);
    else if (demoLayout === 'spiral') positions = genSpiral(cx, cy, numPhotos, minR, maxR);
    else if (demoLayout === 'cloud') positions = genCloud(cx, cy, numPhotos, minR, maxR);
    else if (demoLayout === 'brick') positions = genBrick(cx, cy, numPhotos, minR, maxR, thumbSize, width, height, gap);
    
    if (demoLayout !== 'brick') {
      positions.sort(function(a, b) {
        return Math.sqrt(Math.pow(b.x - cx, 2) + Math.pow(b.y - cy, 2)) - Math.sqrt(Math.pow(a.x - cx, 2) + Math.pow(a.y - cy, 2));
      });
    }
    
    positions.forEach(function(pos, i) {
      var col = demoColors[i % demoColors.length];
      var dist = Math.sqrt(Math.pow(pos.x - cx, 2) + Math.pow(pos.y - cy, 2));
      var norm = Math.pow(dist / maxDist, fadeCurve);
      var bright = 1 + norm * fade;
      
      ctx.save();
      ctx.translate(pos.x, pos.y);
      if (demoLayout !== 'brick' && pos.rot) ctx.rotate(pos.rot * Math.PI / 180);
      
      var w = thumbSize, h = demoLayout === 'brick' ? thumbSize / 1.5 : thumbSize;
      
      if (demoLayout !== 'brick') {
        ctx.shadowColor = 'rgba(0,0,0,0.4)';
        ctx.shadowBlur = 6;
        ctx.shadowOffsetX = 2;
        ctx.shadowOffsetY = 2;
      }
      
      ctx.fillStyle = 'rgba(255,255,255,' + (0.9 / bright) + ')';
      if (demoLayout !== 'brick') roundRect(ctx, -w/2-2, -h/2-2, w+4, h+4, 6);
      else ctx.fillRect(-w/2-2, -h/2-2, w+4, h+4);
      
      var grad = ctx.createLinearGradient(-w/2, -h/2, w/2, h/2);
      grad.addColorStop(0, adjBright(col[0], bright));
      grad.addColorStop(1, adjBright(col[1], bright));
      ctx.fillStyle = grad;
      ctx.shadowColor = 'transparent';
      
      if (demoLayout !== 'brick') roundRect(ctx, -w/2, -h/2, w, h, 4);
      else ctx.fillRect(-w/2, -h/2, w, h);
      ctx.restore();
    });
    
    if (demoLayout !== 'brick') {
      var grd = ctx.createRadialGradient(cx, cy, mainSize/2, cx, cy, mainSize/2 + 25);
      grd.addColorStop(0, 'rgba(255,255,255,0.12)');
      grd.addColorStop(1, 'rgba(255,255,255,0)');
      ctx.fillStyle = grd;
      ctx.beginPath();
      ctx.arc(cx, cy, mainSize/2 + 25, 0, Math.PI * 2);
      ctx.fill();
    }
    
    ctx.save();
    ctx.shadowColor = 'rgba(0,0,0,0.5)';
    ctx.shadowBlur = 12;
    ctx.shadowOffsetX = 4;
    ctx.shadowOffsetY = 4;
    ctx.fillStyle = '#fff';
    if (demoLayout !== 'brick') roundRect(ctx, cx - mainSize/2 - 4, cy - mainSize/2 - 4, mainSize + 8, mainSize + 8, 10);
    else ctx.fillRect(cx - mainSize/2 - 4, cy - mainSize/2 - 4, mainSize + 8, mainSize + 8);
    ctx.shadowColor = 'transparent';
    var mg = ctx.createLinearGradient(cx - mainSize/2, cy - mainSize/2, cx + mainSize/2, cy + mainSize/2);
    mg.addColorStop(0, '#2980b9');
    mg.addColorStop(1, '#3498db');
    ctx.fillStyle = mg;
    if (demoLayout !== 'brick') roundRect(ctx, cx - mainSize/2, cy - mainSize/2, mainSize, mainSize, 6);
    else ctx.fillRect(cx - mainSize/2, cy - mainSize/2, mainSize, mainSize);
    ctx.fillStyle = 'rgba(255,255,255,0.9)';
    ctx.font = 'bold 11px sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('PRINCIPALE', cx, cy);
    ctx.restore();
  };

  function genOrbital(cx, cy, num, minR, maxR) {
    var pos = [], orbits = Math.max(2, Math.ceil(num / 6)), perOrbit = Math.ceil(num / orbits), count = 0;
    for (var o = 0; o < orbits && count < num; o++) {
      var r = minR + (maxR - minR) * (o + 0.5) / orbits, n = Math.min(perOrbit, num - count), start = Math.random() * Math.PI * 2;
      for (var i = 0; i < n; i++) {
        var angle = start + (Math.PI * 2 * i / n) + (Math.random() - 0.5) * 0.2;
        pos.push({ x: cx + r * Math.cos(angle) + (Math.random() - 0.5) * 8, y: cy + r * Math.sin(angle) + (Math.random() - 0.5) * 8, rot: (Math.random() - 0.5) * 25 });
        count++;
      }
    }
    return pos;
  }

  function genSpiral(cx, cy, num, minR, maxR) {
    var pos = [], angle = Math.random() * Math.PI * 2, r = minR, inc = (maxR - minR) / num * 0.9;
    for (var i = 0; i < num; i++) {
      if (r > maxR) { r = minR + Math.random() * (maxR - minR) * 0.3; angle += Math.PI / 2; }
      pos.push({ x: cx + r * Math.cos(angle), y: cy + r * Math.sin(angle), rot: (Math.random() - 0.5) * 20 });
      angle += Math.PI / 3 + (Math.random() - 0.5) * 0.3;
      r += inc + (Math.random() - 0.5) * 6;
    }
    return pos;
  }

  function genCloud(cx, cy, num, minR, maxR) {
    var pos = [];
    for (var i = 0; i < num; i++) {
      var r = minR + (maxR - minR) * Math.pow(Math.random(), 0.7), angle = Math.random() * Math.PI * 2;
      pos.push({ x: cx + r * Math.cos(angle), y: cy + r * Math.sin(angle), rot: (Math.random() - 0.5) * 35 });
    }
    return pos;
  }

  function genBrick(cx, cy, num, minR, maxR, size, w, h, gap) {
    var pos = [], bw = size, bh = size / 1.5;
    var cols = Math.ceil(w / (bw + gap)) + 2, rows = Math.ceil(h / (bh + gap)) + 2;
    var sx = (w - cols * (bw + gap)) / 2, sy = (h - rows * (bh + gap)) / 2;
    var all = [];
    for (var row = 0; row < rows; row++) {
      var off = row % 2 ? (bw + gap) * 0.5 : 0;
      for (var col = 0; col < cols; col++) {
        var x = sx + col * (bw + gap) + off + bw / 2, y = sy + row * (bh + gap) + bh / 2;
        var d = Math.sqrt(Math.pow(x - cx, 2) + Math.pow(y - cy, 2));
        if (d >= minR && d <= maxR && x > 0 && x < w && y > 0 && y < h) all.push({ x: x, y: y, rot: 0, d: d });
      }
    }
    all.sort(function(a, b) { return a.d - b.d; });
    return all.slice(0, num);
  }

  function adjBright(hex, f) {
    var r = Math.min(255, parseInt(hex.slice(1,3), 16) * f);
    var g = Math.min(255, parseInt(hex.slice(3,5), 16) * f);
    var b = Math.min(255, parseInt(hex.slice(5,7), 16) * f);
    return 'rgb(' + Math.round(r) + ',' + Math.round(g) + ',' + Math.round(b) + ')';
  }

  function roundRect(ctx, x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.arcTo(x + w, y, x + w, y + h, r);
    ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r);
    ctx.arcTo(x, y, x + w, y, r);
    ctx.closePath();
    ctx.fill();
  }

  window.demoDownload = function() {
    var canvas = document.getElementById('demoCanvas');
    var link = document.createElement('a');
    link.download = 'photo-cloud-' + demoLayout + '.png';
    link.href = canvas.toDataURL('image/png');
    link.click();
  };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function() { demoGenerate(); });
  else setTimeout(demoGenerate, 100);
})();
</script>
{% endraw %}

---

## 🔄 Correction Automatique de l'Orientation

Les photos sont automatiquement redressées selon leurs métadonnées EXIF. Plus besoin de corriger manuellement les photos prises en portrait !

| Orientation EXIF | Transformation appliquée |
|------------------|--------------------------|
| 1 | Normale (aucune) |
| 2 | Miroir horizontal |
| 3 | Rotation 180° |
| 4 | Miroir vertical |
| 5 | Miroir H + rotation 90° |
| 6 | Rotation 90° CW (iPhone portrait) |
| 7 | Miroir H + rotation 270° |
| 8 | Rotation 90° CCW |

**Cas typiques corrigés automatiquement :**
- 📱 Photos iPhone/Android prises en portrait
- 📷 Photos reflex avec appareil tenu verticalement
- 🔄 Photos pivotées dans l'appareil photo

---

## 📦 Installation

### Dépendances de base

```bash
pip install pillow
```

### Support formats étendus (optionnel)

```bash
# HEIC/HEIF/AVIF (photos iPhone, etc.)
pip install pillow-heif

# RAW (appareils photo reflex/hybrides)
pip install rawpy

# HDR (EXR, HDR, PFM)
pip install imageio numpy

# Interface Streamlit
pip install streamlit

# Interface Web Flask
pip install flask
```

### Installation complète

```bash
pip install pillow pillow-heif rawpy imageio numpy streamlit flask
```

---

## 🚀 3 Interfaces Disponibles

### 1. Application Streamlit (Recommandée)

Interface graphique moderne et interactive.

```bash
streamlit run photo_cloud_streamlit.py
```

Ouvre automatiquement `http://localhost:8501`

**Fonctionnalités:**
- Glisser-déposer multi-fichiers
- Tous formats supportés (HEIC, RAW, HDR...)
- Prévisualisation temps réel
- Export PNG/JPEG
- Interface responsive

### 2. Interface Web Flask

Interface web légère.

```bash
python photo_cloud_web.py
```

Ouvrir `http://localhost:5000`

### 3. Ligne de Commande

Pour l'automatisation et les scripts.

```bash
python photo_cloud_complete.py --main photo.jpg --photos dossier/ --layout orbital
```

---

## 🖥️ Utilisation CLI

### Syntaxe

```bash
python photo_cloud_complete.py --main PHOTO --photos DOSSIER [OPTIONS]
```

### Exemples par layout

**Orbital**
```bash
python photo_cloud_complete.py \
  --main portrait.jpg \
  --photos vacances/ \
  --layout orbital \
  --fade 0.5 \
  --output resultat.png
```

**Spirale**
```bash
python photo_cloud_complete.py \
  --main portrait.jpg \
  --photos photos/ \
  --layout spiral \
  --fade 0.7 \
  --fade-curve 0.8
```

**Nuage**
```bash
python photo_cloud_complete.py \
  --main portrait.jpg \
  --photos photos/ \
  --layout cloud \
  --transparent
```

**Briques avec fond transparent**
```bash
python photo_cloud_complete.py \
  --main portrait.jpg \
  --photos photos/ \
  --layout brick \
  --transparent \
  --gap 5 \
  --brick-ratio 1.5
```

**Haute résolution 4K**
```bash
python photo_cloud_complete.py \
  --main portrait.jpg \
  --photos photos/ \
  --size 3840x2160 \
  --main-size 800x800 \
  --thumb-size 250x250
```

**Avec photos RAW**
```bash
python photo_cloud_complete.py \
  --main DSC_0001.NEF \
  --photos raw_photos/ \
  --layout orbital
```

---

## ⚙️ Paramètres

| Paramètre | Description | Défaut |
|-----------|-------------|--------|
| `--main, -m` | Photo principale | (requis) |
| `--photos, -p` | Photos ou dossier | (requis) |
| `--output, -o` | Fichier de sortie | photo_cloud.png |
| `--layout, -l` | orbital, spiral, cloud, brick | orbital |
| `--size, -s` | Taille canvas (LxH) | 1920x1080 |
| `--main-size` | Taille photo principale | 400x400 |
| `--thumb-size` | Taille miniatures | 150x150 |
| `--fade` | Éclaircissement (0-1) | 0.5 |
| `--fade-curve` | Courbe (<1 rapide, >1 lent) | 1.0 |
| `--transparent, -t` | Fond transparent | false |
| `--bg-color` | Couleur fond R,G,B | 30,30,35 |
| `--gap` | Espacement briques | 4 |
| `--brick-ratio` | Ratio L/H briques | 1.5 |
| `--max-photos` | Limite nombre photos | ∞ |
| `--corner-radius` | Coins arrondis | 10 |
| `--no-shadows` | Sans ombres | false |
| `--no-glow` | Sans lueur centrale | false |

---

## 🐍 Utilisation comme Module

```python
from photo_cloud_complete import create_photo_cloud, load_image, collect_photos_from_path

# Charger les photos
main = load_image("portrait.jpg")
photos = [load_image(p) for p in collect_photos_from_path("mes_photos/")]

# Générer
result = create_photo_cloud(
    main_photo_path="portrait.jpg",
    surrounding_photos=["photo1.jpg", "photo2.jpg", ...],
    output_path="resultat.png",
    canvas_size=(1920, 1080),
    main_photo_size=(500, 500),
    surrounding_size=(150, 150),
    layout="orbital",
    background_color=(0, 0, 0, 0),  # Transparent
    distance_fade=0.5,
    fade_curve=1.0,
)

result.show()
```

---

## 💡 Conseils

### Choix du layout

| Layout | Usage idéal |
|--------|-------------|
| **Orbital** | Équilibré, portraits de groupe |
| **Spiral** | Dynamique, timeline |
| **Cloud** | Naturel, décontracté |
| **Brick** | Mosaïque, mur de souvenirs |

### Paramètres d'éclaircissement

| Fade | Effet |
|------|-------|
| 0.0 - 0.3 | Subtil |
| 0.4 - 0.6 | Modéré |
| 0.7 - 1.0 | Spotlight prononcé |

| Courbe | Comportement |
|--------|--------------|
| < 1.0 | Rapide près du centre |
| 1.0 | Linéaire |
| > 1.0 | Progressif vers les bords |

### Nombre de photos recommandé

- **8-15** : Compositions aérées
- **15-30** : Compositions denses
- **30+** : Mode brick recommandé

---

## 📁 Fichiers

| Fichier | Description |
|---------|-------------|
| `photo_cloud_streamlit.py` | Interface Streamlit |
| `photo_cloud_web.py` | Interface Web Flask |
| `photo_cloud_complete.py` | CLI + Module Python |

---

## 📄 Licence

MIT License - Libre d'utilisation et modification.

---

## 🔗 Téléchargements

{% btn /downloads/photo_cloud_streamlit.py, Streamlit App, download fa-fw %}
{% btn /downloads/photo_cloud_web.py, Web Flask, download fa-fw %}
{% btn /downloads/photo_cloud_complete.py, CLI, download fa-fw %}
