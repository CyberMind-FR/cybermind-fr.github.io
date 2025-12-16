#!/usr/bin/env python3
"""
Photo Cloud Generator - Interface Web Flask
Supporte tous les formats: JPEG, PNG, HEIC, RAW (CR2, NEF, ARW...), HDR, etc.

Installation:
    pip install flask pillow pillow-heif rawpy imageio numpy

Lancer: python photo_cloud_web.py
Ouvrir: http://localhost:5000
"""

import os, io, math, random, uuid, base64, tempfile
from pathlib import Path
from flask import Flask, render_template_string, request, jsonify
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

# =============================================================================
# CORRECTION D'ORIENTATION EXIF
# =============================================================================

def fix_orientation(img):
    """Corrige l'orientation selon les métadonnées EXIF."""
    try:
        exif = img.getexif()
        if not exif:
            return img
        orientation = exif.get(274)
        if orientation is None:
            return img
        if orientation == 2:
            img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        elif orientation == 3:
            img = img.transpose(Image.Transpose.ROTATE_180)
        elif orientation == 4:
            img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        elif orientation == 5:
            img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            img = img.transpose(Image.Transpose.ROTATE_90)
        elif orientation == 6:
            img = img.transpose(Image.Transpose.ROTATE_270)
        elif orientation == 7:
            img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            img = img.transpose(Image.Transpose.ROTATE_270)
        elif orientation == 8:
            img = img.transpose(Image.Transpose.ROTATE_90)
        return img
    except:
        return img

# Support formats étendus
HEIF_SUPPORT = RAW_SUPPORT = IMAGEIO_SUPPORT = NUMPY_SUPPORT = False

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
    HEIF_SUPPORT = True
except ImportError: pass

try:
    import rawpy
    RAW_SUPPORT = True
except ImportError: pass

try:
    import imageio.v3 as iio
    IMAGEIO_SUPPORT = True
except ImportError:
    try:
        import imageio as iio
        IMAGEIO_SUPPORT = True
    except ImportError: pass

try:
    import numpy as np
    NUMPY_SUPPORT = True
except ImportError: pass

HEIF_EXT = {'.heif','.heifs','.heic','.heics','.avci','.avcs','.avif','.avifs'}
RAW_EXT = {'.cr2','.cr3','.crw','.nef','.nrw','.arw','.srf','.sr2','.raf','.orf','.rw2','.raw','.pef','.ptx','.srw','.x3f','.rwl','.dng','.dcr','.k25','.kdc','.mrw','.erf','.iiq','.mef','.3fr','.fff','.riff'}
HDR_EXT = {'.exr','.hdr','.rgbe','.pfm','.fits','.fts'}

def load_image_from_upload(file_storage):
    filename = file_storage.filename
    ext = Path(filename).suffix.lower()
    data = file_storage.read()
    file_storage.seek(0)
    
    if ext in HEIF_EXT and HEIF_SUPPORT:
        try:
            img = Image.open(io.BytesIO(data))
            img = fix_orientation(img)
            return img.convert('RGBA')
        except: pass
    
    if ext in RAW_EXT and RAW_SUPPORT:
        try:
            with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as tmp:
                tmp.write(data)
                tmp_path = tmp.name
            try:
                with rawpy.imread(tmp_path) as raw:
                    rgb = raw.postprocess(use_camera_wb=True, half_size=False, output_bps=8)
                return Image.fromarray(rgb).convert('RGBA')
            finally:
                os.unlink(tmp_path)
        except: pass
    
    if ext in HDR_EXT and IMAGEIO_SUPPORT and NUMPY_SUPPORT:
        try:
            arr = iio.imread(io.BytesIO(data))
            if arr.dtype in (np.float32, np.float64, np.float16):
                arr = ((arr / (1 + arr)) * 255).clip(0, 255).astype(np.uint8)
            elif arr.dtype == np.uint16:
                arr = (arr / 256).astype(np.uint8)
            return Image.fromarray(arr).convert('RGBA')
        except: pass
    
    img = Image.open(io.BytesIO(data))
    img = fix_orientation(img)
    return img.convert('RGBA')

# Traitement d'images
def resize_to_fit(img, max_size):
    img = img.copy()
    img.thumbnail(max_size, Image.Resampling.LANCZOS)
    return img

def resize_cover(img, target_size):
    tw, th = target_size
    scale = max(tw / img.width, th / img.height)
    img = img.resize((int(img.width * scale), int(img.height * scale)), Image.Resampling.LANCZOS)
    left, top = (img.width - tw) // 2, (img.height - th) // 2
    return img.crop((left, top, left + tw, top + th))

def add_rounded_corners(img, radius):
    mask = Image.new('L', img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([(0, 0), img.size], radius=radius, fill=255)
    result = img.copy()
    result.putalpha(mask)
    return result

def add_border(img, width, color=(255, 255, 255, 255)):
    if width <= 0: return img
    bordered = Image.new('RGBA', (img.width + width*2, img.height + width*2), color)
    bordered.paste(img, (width, width), img if img.mode == 'RGBA' else None)
    return bordered

def add_shadow(img, offset=(8, 8), blur=15):
    padding = blur * 2 + max(abs(offset[0]), abs(offset[1]))
    shadow = Image.new('RGBA', (img.width + padding*2, img.height + padding*2), (0,0,0,0))
    shadow_shape = Image.new('RGBA', img.size, (0, 0, 0, 100))
    shadow_shape.putalpha(img.split()[3])
    shadow.paste(shadow_shape, (padding + offset[0], padding + offset[1]))
    shadow = shadow.filter(ImageFilter.GaussianBlur(blur))
    shadow.paste(img, (padding, padding), img)
    return shadow

# Générateurs de positions
def gen_orbital(center, num, min_r, max_r, photo_size):
    positions = []
    orbits = max(2, int((max_r - min_r) / (max(photo_size) * 1.2)))
    per = [num // orbits] * orbits
    for i in range(num % orbits): per[i] += 1
    for oi, cnt in enumerate(per):
        if cnt == 0: continue
        r = min_r + ((oi + 0.5) / orbits) * (max_r - min_r)
        start = random.uniform(0, 2 * math.pi)
        for i in range(cnt):
            angle = start + (2 * math.pi * i / cnt) + random.uniform(-0.1, 0.1)
            rv = r + random.uniform(-15, 15)
            positions.append((center[0] + int(rv * math.cos(angle)), center[1] + int(rv * math.sin(angle)), random.uniform(-20, 20)))
    return positions

def gen_spiral(center, num, min_r, max_r, photo_size):
    positions = []
    angle, r = random.uniform(0, 2 * math.pi), min_r
    inc = (max_r - min_r) / max(num, 1) * 0.8
    for _ in range(num):
        if r > max_r: r, angle = min_r + random.uniform(0, (max_r-min_r)*0.3), angle + math.pi/2
        positions.append((center[0] + int(r * math.cos(angle)), center[1] + int(r * math.sin(angle)), random.uniform(-15, 15)))
        angle += math.pi/3 + random.uniform(-0.2, 0.2)
        r += inc + random.randint(-5, 10)
    return positions

def gen_cloud(center, num, min_r, max_r, photo_size):
    positions = []
    for _ in range(num):
        r = min_r + (max_r - min_r) * (random.random() ** 0.7)
        angle = random.uniform(0, 2 * math.pi)
        positions.append((center[0] + int(r * math.cos(angle)), center[1] + int(r * math.sin(angle)), random.uniform(-25, 25)))
    return positions

def gen_brick(center, num, min_r, max_r, photo_size, canvas_size, gap):
    bw, bh = photo_size
    cols, rows = math.ceil(canvas_size[0]/(bw+gap))+2, math.ceil(canvas_size[1]/(bh+gap))+2
    sx, sy = (canvas_size[0] - cols*(bw+gap))//2, (canvas_size[1] - rows*(bh+gap))//2
    all_pos = []
    for row in range(rows):
        off = int((bw+gap)*0.5) if row%2 else 0
        for col in range(cols):
            x, y = sx + col*(bw+gap) + off + bw//2, sy + row*(bh+gap) + bh//2
            d = math.sqrt((x-center[0])**2 + (y-center[1])**2)
            if min_r <= d <= max_r and 0 <= x < canvas_size[0] and 0 <= y < canvas_size[1]:
                all_pos.append((x, y, 0, d))
    all_pos.sort(key=lambda p: p[3])
    return [(x, y, r) for x, y, r, _ in all_pos[:num]]

def create_photo_cloud(main_img, photos, canvas_size, main_size, thumb_size, layout, fade, fade_curve, gap, brick_ratio, transparent):
    bg = (0,0,0,0) if transparent else (30,30,35,255)
    canvas = Image.new('RGBA', canvas_size, bg)
    center = (canvas_size[0]//2, canvas_size[1]//2)
    max_dist = math.sqrt(center[0]**2 + center[1]**2)
    cr = 10 if layout != 'brick' else 0
    
    main_p = resize_cover(main_img.copy(), main_size) if layout == 'brick' else resize_to_fit(main_img.copy(), main_size)
    if cr > 0: main_p = add_rounded_corners(main_p, cr + 5)
    main_p = add_border(main_p, 5)
    if cr > 0 and layout != 'brick': main_p = add_rounded_corners(main_p, cr + 8)
    
    main_r = max(main_p.width, main_p.height) // 2
    min_r, max_r = main_r + thumb_size//2 + 20, min(canvas_size)//2 - thumb_size//2
    
    if layout == 'brick':
        photo_size = (thumb_size, int(thumb_size / brick_ratio))
        min_r, max_r = main_r + 10, max(canvas_size)//2 + max(photo_size)
    else:
        photo_size = (thumb_size, thumb_size)
    
    processed = []
    for img in photos:
        p = resize_cover(img.copy(), photo_size) if layout == 'brick' else resize_to_fit(img.copy(), photo_size)
        if layout != 'brick':
            if cr > 0: p = add_rounded_corners(p, cr)
            p = add_border(p, 3, (255,255,255,230))
            if cr > 0: p = add_rounded_corners(p, cr + 3)
        processed.append(p)
    
    if not processed: return canvas
    
    num = len(processed) if layout != 'brick' else len(processed) * 10
    if layout == 'spiral': positions = gen_spiral(center, num, min_r, max_r, photo_size)
    elif layout == 'orbital': positions = gen_orbital(center, num, min_r, max_r, photo_size)
    elif layout == 'cloud': positions = gen_cloud(center, num, min_r, max_r, photo_size)
    else: positions = gen_brick(center, num, min_r, max_r, photo_size, canvas_size, gap)
    
    if layout != 'brick':
        random.shuffle(positions)
        positions.sort(key=lambda p: -math.sqrt((p[0]-center[0])**2 + (p[1]-center[1])**2))
    
    for i, (x, y, rot) in enumerate(positions):
        img = processed[i % len(processed)].copy()
        d = math.sqrt((x-center[0])**2 + (y-center[1])**2)
        nd = (d / max_dist) ** fade_curve
        if fade > 0:
            img = ImageEnhance.Brightness(img).enhance(1.0 + nd * fade + random.uniform(-0.05, 0.05))
            img = ImageEnhance.Color(img).enhance(max(0.5, 1.0 - nd * fade * 0.3))
        if layout != 'brick' and abs(rot) > 0.5:
            img = img.rotate(rot, expand=True, resample=Image.Resampling.BICUBIC)
        if layout != 'brick':
            img = add_shadow(img, (5,5), 10)
        canvas.paste(img, (x - img.width//2, y - img.height//2), img)
    
    if layout != 'brick':
        glow = Image.new('RGBA', (main_p.width+60, main_p.height+60), (0,0,0,0))
        gc = (glow.width//2, glow.height//2)
        for i in range(30, 0, -1):
            ImageDraw.Draw(glow).ellipse([gc[0]-main_p.width//2-i, gc[1]-main_p.height//2-i, gc[0]+main_p.width//2+i, gc[1]+main_p.height//2+i], fill=(255,255,255,int(8*(30-i)/30)))
        glow = glow.filter(ImageFilter.GaussianBlur(15))
        canvas.paste(glow, (center[0]-glow.width//2, center[1]-glow.height//2), glow)
    
    main_s = add_shadow(main_p, (10,10), 20)
    canvas.paste(main_s, (center[0]-main_s.width//2, center[1]-main_s.height//2), main_s)
    return canvas

# Flask app
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024
UPLOAD_FOLDER = tempfile.mkdtemp()
uploaded_images = {}

@app.route('/')
def index():
    formats = "JPEG, PNG, GIF, WebP, TIFF"
    if HEIF_SUPPORT: formats += ", HEIC/HEIF/AVIF"
    if RAW_SUPPORT: formats += ", RAW (CR2/NEF/ARW...)"
    if IMAGEIO_SUPPORT: formats += ", HDR (EXR/HDR)"
    return render_template_string(HTML_TEMPLATE, formats=formats)

@app.route('/upload', methods=['POST'])
def upload():
    if 'files' not in request.files:
        return jsonify({'error': 'No files'}), 400
    
    results = []
    for f in request.files.getlist('files'):
        if f.filename:
            try:
                img = load_image_from_upload(f)
                img_id = str(uuid.uuid4())
                uploaded_images[img_id] = img
                
                thumb = img.copy()
                thumb.thumbnail((150, 150), Image.Resampling.LANCZOS)
                if thumb.mode == 'RGBA':
                    bg = Image.new('RGB', thumb.size, (40, 40, 45))
                    bg.paste(thumb, mask=thumb.split()[3])
                    thumb = bg
                
                buf = io.BytesIO()
                thumb.save(buf, format='JPEG', quality=85)
                b64 = base64.b64encode(buf.getvalue()).decode()
                
                ext = Path(f.filename).suffix.upper().lstrip('.')
                results.append({'id': img_id, 'name': f.filename, 'thumb': f'data:image/jpeg;base64,{b64}', 'format': ext})
            except Exception as e:
                results.append({'error': str(e), 'name': f.filename})
    
    return jsonify({'photos': results})

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    main_id = data.get('main_id')
    photo_ids = data.get('photo_ids', [])
    
    if main_id not in uploaded_images:
        return jsonify({'error': 'Main photo not found'}), 400
    
    main_img = uploaded_images[main_id]
    photos = [uploaded_images[pid] for pid in photo_ids if pid in uploaded_images]
    
    if not photos:
        return jsonify({'error': 'No photos'}), 400
    
    canvas_size = (data.get('canvas_width', 1920), data.get('canvas_height', 1080))
    main_size = (data.get('main_width', 400), data.get('main_height', 400))
    
    result = create_photo_cloud(
        main_img=main_img, photos=photos, canvas_size=canvas_size, main_size=main_size,
        thumb_size=data.get('thumb_size', 150), layout=data.get('layout', 'orbital'),
        fade=data.get('fade', 0.5), fade_curve=data.get('fade_curve', 1.0),
        gap=data.get('gap', 4), brick_ratio=data.get('brick_ratio', 1.5),
        transparent=data.get('transparent', False)
    )
    
    buf = io.BytesIO()
    result.save(buf, format='PNG')
    b64 = base64.b64encode(buf.getvalue()).decode()
    
    return jsonify({'image': f'data:image/png;base64,{b64}'})

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Photo Cloud Generator</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:linear-gradient(135deg,#1a1a2e,#16213e);min-height:100vh;color:#e0e0e0}
.container{max-width:1400px;margin:0 auto;padding:20px}
h1{text-align:center;background:linear-gradient(90deg,#00d2ff,#3a7bd5);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-size:2.5em;margin-bottom:10px}
.subtitle{text-align:center;color:#888;margin-bottom:20px;font-size:0.85em}
.main-grid{display:grid;grid-template-columns:350px 1fr;gap:20px}
@media(max-width:900px){.main-grid{grid-template-columns:1fr}}
.panel{background:rgba(255,255,255,0.05);backdrop-filter:blur(10px);border-radius:15px;padding:20px;border:1px solid rgba(255,255,255,0.1)}
.panel h2{font-size:1.2em;margin-bottom:15px;color:#00d2ff}
.upload-zone{border:2px dashed rgba(255,255,255,0.3);border-radius:10px;padding:30px;text-align:center;cursor:pointer;transition:all 0.3s;margin-bottom:15px}
.upload-zone:hover,.upload-zone.dragover{border-color:#00d2ff;background:rgba(0,210,255,0.1)}
.upload-icon{font-size:3em;margin-bottom:10px}
.photos-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;max-height:250px;overflow-y:auto;padding:5px}
.photo-item{aspect-ratio:1;border-radius:8px;overflow:hidden;cursor:pointer;position:relative;border:3px solid transparent;transition:all 0.2s}
.photo-item:hover{transform:scale(1.05)}
.photo-item.selected{border-color:#4CAF50;box-shadow:0 0 10px rgba(76,175,80,0.5)}
.photo-item img{width:100%;height:100%;object-fit:cover}
.photo-item .badge{position:absolute;top:5px;right:5px;background:#4CAF50;color:white;font-size:0.7em;padding:2px 5px;border-radius:3px}
.photo-item .format-badge{position:absolute;bottom:3px;left:3px;background:rgba(0,0,0,0.7);color:#00d2ff;font-size:0.6em;padding:1px 4px;border-radius:3px}
.layout-buttons{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:15px 0}
.layout-btn{padding:10px 5px;border:2px solid rgba(255,255,255,0.2);border-radius:10px;background:rgba(0,0,0,0.3);color:#fff;cursor:pointer;text-align:center;transition:all 0.2s}
.layout-btn:hover{border-color:rgba(0,210,255,0.5)}
.layout-btn.active{border-color:#00d2ff;background:rgba(0,210,255,0.2)}
.layout-btn .icon{font-size:1.5em;display:block}
.layout-btn .label{font-size:0.75em}
.param-group{margin-bottom:12px}
.param-group label{display:block;font-size:0.85em;color:#aaa;margin-bottom:3px}
.param-group input[type="range"]{width:100%}
.param-value{color:#00d2ff;font-weight:bold}
.checkbox-group{margin:10px 0}
.checkbox-label{display:flex;align-items:center;cursor:pointer;font-size:0.9em}
.checkbox-label input{margin-right:8px}
.btn{width:100%;padding:12px;border:none;border-radius:8px;cursor:pointer;font-weight:bold;margin-top:10px;transition:all 0.3s}
.btn-primary{background:linear-gradient(90deg,#00d2ff,#3a7bd5);color:white}
.btn-secondary{background:rgba(255,255,255,0.1);color:#fff;border:1px solid rgba(255,255,255,0.2)}
.btn:hover{transform:translateY(-2px);box-shadow:0 5px 15px rgba(0,0,0,0.3)}
.preview{min-height:400px;display:flex;align-items:center;justify-content:center;position:relative}
.preview img{max-width:100%;max-height:600px;border-radius:10px;box-shadow:0 10px 30px rgba(0,0,0,0.3)}
.preview .placeholder{text-align:center;color:#666}
.preview .placeholder .icon{font-size:4em;margin-bottom:10px}
.brick-options{display:none}
.brick-options.show{display:block}
.loading{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center}
.spinner{width:50px;height:50px;border:4px solid rgba(0,210,255,0.3);border-top-color:#00d2ff;border-radius:50%;animation:spin 1s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
</style>
</head>
<body>
<div class="container">
<h1>📸 Photo Cloud Generator</h1>
<p class="subtitle">Formats: {{ formats }}</p>
<div class="main-grid">
<div class="panel">
<h2>📁 Photos</h2>
<div class="upload-zone" id="uploadZone" onclick="document.getElementById('fileInput').click()">
<div class="upload-icon">📷</div>
<p>Glissez vos photos ici<br><small>ou cliquez pour sélectionner</small></p>
</div>
<input type="file" id="fileInput" multiple accept="image/*,.heic,.heif,.cr2,.cr3,.nef,.arw,.raf,.dng,.orf,.rw2,.raw,.exr,.hdr" style="display:none">
<div class="photos-grid" id="photosGrid"></div>

<h2 style="margin-top:20px">🎨 Layout</h2>
<div class="layout-buttons">
<button class="layout-btn active" data-layout="orbital" onclick="setLayout('orbital')"><span class="icon">🪐</span><span class="label">Orbital</span></button>
<button class="layout-btn" data-layout="spiral" onclick="setLayout('spiral')"><span class="icon">🌀</span><span class="label">Spirale</span></button>
<button class="layout-btn" data-layout="cloud" onclick="setLayout('cloud')"><span class="icon">☁️</span><span class="label">Nuage</span></button>
<button class="layout-btn" data-layout="brick" onclick="setLayout('brick')"><span class="icon">🧱</span><span class="label">Briques</span></button>
</div>

<div class="param-group"><label>Canvas: <span class="param-value" id="sizeValue">1920×1080</span></label>
<input type="range" id="canvasWidth" min="800" max="3840" value="1920" oninput="updateSize()">
<input type="range" id="canvasHeight" min="600" max="2160" value="1080" oninput="updateSize()"></div>
<div class="param-group"><label>Photo principale: <span class="param-value" id="mainValue">400</span>px</label>
<input type="range" id="mainSize" min="200" max="800" value="400" oninput="updateVal('main')"></div>
<div class="param-group"><label>Miniatures: <span class="param-value" id="thumbValue">150</span>px</label>
<input type="range" id="thumbSize" min="80" max="300" value="150" oninput="updateVal('thumb')"></div>
<div class="param-group"><label>Éclaircissement: <span class="param-value" id="fadeValue">0.50</span></label>
<input type="range" id="fade" min="0" max="100" value="50" oninput="updateVal('fade')"></div>
<div class="param-group"><label>Courbe: <span class="param-value" id="curveValue">1.0</span></label>
<input type="range" id="fadeCurve" min="3" max="20" value="10" oninput="updateVal('curve')"></div>
<div class="brick-options" id="brickOptions">
<div class="param-group"><label>Espacement: <span class="param-value" id="gapValue">4</span>px</label>
<input type="range" id="gap" min="0" max="15" value="4" oninput="updateVal('gap')"></div>
<div class="param-group"><label>Ratio: <span class="param-value" id="ratioValue">1.5</span></label>
<input type="range" id="brickRatio" min="10" max="25" value="15" oninput="updateVal('ratio')"></div>
</div>
<div class="checkbox-group"><label class="checkbox-label"><input type="checkbox" id="transparent">Fond transparent</label></div>
<button class="btn btn-primary" onclick="generate()">🎨 Générer</button>
<button class="btn btn-secondary" onclick="download()">💾 Télécharger PNG</button>
</div>
<div class="panel">
<h2>👁️ Prévisualisation</h2>
<div class="preview" id="preview">
<div class="placeholder"><div class="icon">🖼️</div><p>Uploadez des photos et cliquez sur Générer</p></div>
</div>
</div>
</div>
</div>
<script>
let photos=[], mainIndex=null, currentLayout='orbital', resultImage=null;
const uploadZone=document.getElementById('uploadZone'), fileInput=document.getElementById('fileInput'), photosGrid=document.getElementById('photosGrid'), preview=document.getElementById('preview');

['dragenter','dragover','dragleave','drop'].forEach(e=>uploadZone.addEventListener(e,ev=>{ev.preventDefault();ev.stopPropagation()}));
['dragenter','dragover'].forEach(e=>uploadZone.addEventListener(e,()=>uploadZone.classList.add('dragover')));
['dragleave','drop'].forEach(e=>uploadZone.addEventListener(e,()=>uploadZone.classList.remove('dragover')));
uploadZone.addEventListener('drop',e=>handleFiles(e.dataTransfer.files));
fileInput.addEventListener('change',e=>handleFiles(e.target.files));

function handleFiles(files){
const fd=new FormData();
[...files].forEach(f=>fd.append('files',f));
preview.innerHTML='<div class="loading"><div class="spinner"></div><p>Chargement...</p></div>';
fetch('/upload',{method:'POST',body:fd}).then(r=>r.json()).then(data=>{
if(data.photos){
data.photos.forEach(p=>{if(!p.error)photos.push(p)});
if(mainIndex===null&&photos.length>0)mainIndex=0;
renderPhotos();
}
preview.innerHTML='<div class="placeholder"><div class="icon">🖼️</div><p>Cliquez sur Générer</p></div>';
});
}

function renderPhotos(){
photosGrid.innerHTML=photos.map((p,i)=>`<div class="photo-item ${i===mainIndex?'selected':''}" onclick="selectMain(${i})"><img src="${p.thumb}"><span class="format-badge">${p.format}</span>${i===mainIndex?'<span class="badge">★</span>':''}</div>`).join('');
}

function selectMain(i){mainIndex=i;renderPhotos()}
function setLayout(l){currentLayout=l;document.querySelectorAll('.layout-btn').forEach(b=>b.classList.toggle('active',b.dataset.layout===l));document.getElementById('brickOptions').classList.toggle('show',l==='brick')}
function updateSize(){document.getElementById('sizeValue').textContent=document.getElementById('canvasWidth').value+'×'+document.getElementById('canvasHeight').value}
function updateVal(t){
const m={main:['mainSize','mainValue',v=>v],thumb:['thumbSize','thumbValue',v=>v],fade:['fade','fadeValue',v=>(v/100).toFixed(2)],curve:['fadeCurve','curveValue',v=>(v/10).toFixed(1)],gap:['gap','gapValue',v=>v],ratio:['brickRatio','ratioValue',v=>(v/10).toFixed(1)]};
const[id,vid,fmt]=m[t];document.getElementById(vid).textContent=fmt(document.getElementById(id).value);
}

function generate(){
if(mainIndex===null||photos.length<2){alert('Sélectionnez au moins 2 photos');return}
preview.innerHTML='<div class="loading"><div class="spinner"></div><p>Génération...</p></div>';
fetch('/generate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({
main_id:photos[mainIndex].id,photo_ids:photos.filter((_,i)=>i!==mainIndex).map(p=>p.id),
canvas_width:+document.getElementById('canvasWidth').value,canvas_height:+document.getElementById('canvasHeight').value,
main_width:+document.getElementById('mainSize').value,main_height:+document.getElementById('mainSize').value,
thumb_size:+document.getElementById('thumbSize').value,layout:currentLayout,
fade:document.getElementById('fade').value/100,fade_curve:document.getElementById('fadeCurve').value/10,
gap:+document.getElementById('gap').value,brick_ratio:document.getElementById('brickRatio').value/10,
transparent:document.getElementById('transparent').checked
})}).then(r=>r.json()).then(data=>{
if(data.image){resultImage=data.image;preview.innerHTML=`<img src="${data.image}">`}
else{preview.innerHTML='<div class="placeholder"><p>Erreur</p></div>'}
});
}

function download(){
if(!resultImage)return;
const a=document.createElement('a');a.href=resultImage;a.download='photo_cloud_'+currentLayout+'.png';a.click();
}
</script>
</body>
</html>'''

if __name__ == '__main__':
    print(f"Photo Cloud Generator - Web Interface")
    print(f"Formats: JPEG, PNG" + (", HEIC" if HEIF_SUPPORT else "") + (", RAW" if RAW_SUPPORT else "") + (", HDR" if IMAGEIO_SUPPORT else ""))
    print(f"Open: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
