#!/usr/bin/env python3
"""
Photo Cloud Generator - Version Complète (CLI)
Crée un nuage de photos autour d'une photo principale avec plusieurs modes de disposition.
Supporte tous les formats: JPEG, PNG, HEIC, RAW (CR2, NEF, ARW...), HDR, etc.

Installation:
    pip install pillow                    # Base
    pip install pillow-heif               # HEIC/HEIF/AVIF
    pip install rawpy                     # RAW (CR2, NEF, ARW...)
    pip install imageio numpy             # HDR (EXR, HDR, PFM)

Layouts disponibles:
- orbital: Photos sur plusieurs orbites concentriques
- spiral: Disposition en spirale
- cloud: Disposition aléatoire en nuage
- brick: Mur de briques avec décalage alterné

Usage:
    python photo_cloud_complete.py --main photo.jpg --photos dossier/ --layout orbital
    python photo_cloud_complete.py --main DSC_0001.NEF --photos raw_photos/ --layout brick
"""

import argparse
import math
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from PIL.ExifTags import TAGS

# =============================================================================
# CORRECTION D'ORIENTATION EXIF
# =============================================================================

def fix_orientation(img: Image.Image) -> Image.Image:
    """
    Corrige l'orientation de l'image selon les métadonnées EXIF.
    Retourne l'image redressée si nécessaire.
    """
    try:
        # Récupérer les données EXIF
        exif = img.getexif()
        if not exif:
            return img
        
        # Chercher le tag Orientation (0x0112 = 274)
        orientation = exif.get(274)  # 274 = Orientation tag
        
        if orientation is None:
            return img
        
        # Appliquer la transformation selon l'orientation EXIF
        # https://www.exif.org/Exif2-2.PDF (page 18)
        if orientation == 1:
            # Normal - pas de transformation
            pass
        elif orientation == 2:
            # Mirrored horizontal
            img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        elif orientation == 3:
            # Rotated 180°
            img = img.transpose(Image.Transpose.ROTATE_180)
        elif orientation == 4:
            # Mirrored vertical
            img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        elif orientation == 5:
            # Mirrored horizontal then rotated 90° CCW
            img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            img = img.transpose(Image.Transpose.ROTATE_90)
        elif orientation == 6:
            # Rotated 90° CW (270° CCW)
            img = img.transpose(Image.Transpose.ROTATE_270)
        elif orientation == 7:
            # Mirrored horizontal then rotated 90° CW
            img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            img = img.transpose(Image.Transpose.ROTATE_270)
        elif orientation == 8:
            # Rotated 90° CCW
            img = img.transpose(Image.Transpose.ROTATE_90)
        
        return img
    
    except Exception:
        # En cas d'erreur, retourner l'image originale
        return img

# =============================================================================
# SUPPORT DES FORMATS ÉTENDUS
# =============================================================================

HEIF_SUPPORT = False
RAW_SUPPORT = False
IMAGEIO_SUPPORT = False
NUMPY_SUPPORT = False

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
    HEIF_SUPPORT = True
except ImportError:
    pass

try:
    import rawpy
    RAW_SUPPORT = True
except ImportError:
    pass

try:
    import imageio.v3 as iio
    IMAGEIO_SUPPORT = True
except ImportError:
    try:
        import imageio as iio
        IMAGEIO_SUPPORT = True
    except ImportError:
        pass

try:
    import numpy as np
    NUMPY_SUPPORT = True
except ImportError:
    pass

# Extensions par catégorie
PILLOW_EXTENSIONS = {
    '.jpg', '.jpeg', '.jpe', '.jfif', '.png', '.gif', '.bmp', '.dib',
    '.tiff', '.tif', '.webp', '.ico', '.ppm', '.pgm', '.pbm', '.pnm',
    '.pcx', '.tga', '.icb', '.vda', '.vst', '.dds', '.sgi', '.rgb',
    '.rgba', '.bw', '.j2k', '.j2p', '.jpx', '.jp2', '.eps', '.ps',
    '.im', '.msp', '.xbm', '.palm', '.pdf', '.psd', '.qoi',
}

HEIF_EXTENSIONS = {'.heif', '.heifs', '.heic', '.heics', '.avci', '.avcs', '.avif', '.avifs'}

RAW_EXTENSIONS = {
    '.cr2', '.cr3', '.crw', '.nef', '.nrw', '.arw', '.srf', '.sr2',
    '.raf', '.orf', '.rw2', '.raw', '.pef', '.ptx', '.srw', '.x3f',
    '.rwl', '.dng', '.dcr', '.k25', '.kdc', '.mrw', '.erf', '.iiq',
    '.mef', '.3fr', '.fff', '.riff',
}

IMAGEIO_EXTENSIONS = {'.exr', '.hdr', '.rgbe', '.pfm', '.fits', '.fts'}


def get_all_supported_extensions():
    """Retourne toutes les extensions supportées."""
    extensions = set(PILLOW_EXTENSIONS)
    if HEIF_SUPPORT:
        extensions.update(HEIF_EXTENSIONS)
    if RAW_SUPPORT:
        extensions.update(RAW_EXTENSIONS)
    if IMAGEIO_SUPPORT:
        extensions.update(IMAGEIO_EXTENSIONS)
    return extensions


def print_format_support():
    """Affiche les formats supportés."""
    print("Formats supportés:")
    print("  ✓ Standards: JPEG, PNG, GIF, WebP, BMP, TIFF, TGA, PCX, PPM...")
    if HEIF_SUPPORT:
        print("  ✓ HEIF/HEIC/AVIF: Supporté (pillow-heif)")
    else:
        print("  ✗ HEIF/HEIC/AVIF: pip install pillow-heif")
    if RAW_SUPPORT:
        print("  ✓ RAW: CR2, CR3, NEF, ARW, RAF, DNG... (rawpy)")
    else:
        print("  ✗ RAW: pip install rawpy")
    if IMAGEIO_SUPPORT:
        print("  ✓ HDR: EXR, HDR, PFM (imageio)")
    else:
        print("  ✗ HDR: pip install imageio numpy")


# =============================================================================
# CHARGEMENT DES IMAGES
# =============================================================================

def load_image_pillow(path: str) -> Image.Image:
    """Charge une image avec Pillow et corrige l'orientation EXIF."""
    img = Image.open(path)
    img = fix_orientation(img)
    if img.mode not in ('RGB', 'RGBA'):
        img = img.convert('RGBA')
    return img


def load_image_raw(path: str) -> Image.Image:
    """Charge une image RAW avec rawpy."""
    if not RAW_SUPPORT:
        raise ImportError("rawpy non installé. Installez avec: pip install rawpy")
    
    with rawpy.imread(path) as raw:
        rgb = raw.postprocess(
            use_camera_wb=True,
            half_size=False,
            no_auto_bright=False,
            output_bps=8
        )
    img = Image.fromarray(rgb)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    return img


def load_image_imageio(path: str) -> Image.Image:
    """Charge une image avec imageio (HDR, EXR, etc.)."""
    if not IMAGEIO_SUPPORT:
        raise ImportError("imageio non installé. Installez avec: pip install imageio numpy")
    
    img_array = iio.imread(path)
    
    # Tone mapping pour HDR
    if NUMPY_SUPPORT and img_array.dtype in (np.float32, np.float64, np.float16):
        img_array = img_array / (1 + img_array)
        img_array = (img_array * 255).clip(0, 255).astype(np.uint8)
    elif NUMPY_SUPPORT and img_array.dtype == np.uint16:
        img_array = (img_array / 256).astype(np.uint8)
    
    img = Image.fromarray(img_array)
    if img.mode not in ('RGB', 'RGBA'):
        img = img.convert('RGBA')
    return img


def load_image(path: str) -> Image.Image:
    """Charge une image en détectant automatiquement le format."""
    path = str(path)
    ext = Path(path).suffix.lower()
    
    errors = []
    
    # HEIF/HEIC/AVIF
    if ext in HEIF_EXTENSIONS:
        if HEIF_SUPPORT:
            try:
                return load_image_pillow(path)
            except Exception as e:
                errors.append(f"HEIF: {e}")
        else:
            errors.append("HEIF: pillow-heif non installé")
    
    # RAW
    if ext in RAW_EXTENSIONS:
        if RAW_SUPPORT:
            try:
                return load_image_raw(path)
            except Exception as e:
                errors.append(f"RAW: {e}")
        else:
            errors.append("RAW: rawpy non installé")
    
    # HDR/EXR
    if ext in IMAGEIO_EXTENSIONS:
        if IMAGEIO_SUPPORT:
            try:
                return load_image_imageio(path)
            except Exception as e:
                errors.append(f"ImageIO: {e}")
        else:
            errors.append("HDR: imageio non installé")
    
    # Pillow (standard)
    try:
        return load_image_pillow(path)
    except Exception as e:
        errors.append(f"Pillow: {e}")
    
    # Fallback imageio
    if IMAGEIO_SUPPORT:
        try:
            return load_image_imageio(path)
        except Exception as e:
            errors.append(f"ImageIO fallback: {e}")
    
    raise ValueError(f"Impossible de charger {path}:\n" + "\n".join(errors))


# =============================================================================
# FONCTIONS DE TRAITEMENT D'IMAGE
# =============================================================================

def resize_to_fit(img: Image.Image, max_size: tuple) -> Image.Image:
    """Redimensionne l'image pour tenir dans max_size en conservant le ratio."""
    img = img.copy()
    img.thumbnail(max_size, Image.Resampling.LANCZOS)
    return img


def resize_cover(img: Image.Image, target_size: tuple) -> Image.Image:
    """Redimensionne l'image pour couvrir exactement target_size (crop au centre)."""
    target_w, target_h = target_size
    scale = max(target_w / img.width, target_h / img.height)
    new_w = int(img.width * scale)
    new_h = int(img.height * scale)
    img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    return img.crop((left, top, left + target_w, top + target_h))


def add_rounded_corners(img: Image.Image, radius: int) -> Image.Image:
    """Ajoute des coins arrondis à l'image."""
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), img.size], radius=radius, fill=255)
    result = img.copy()
    result.putalpha(mask)
    return result


def add_border(img: Image.Image, border_width: int = 3, 
               border_color: tuple = (255, 255, 255, 255)) -> Image.Image:
    """Ajoute une bordure à l'image."""
    if border_width <= 0:
        return img
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    bordered = Image.new('RGBA', 
                         (img.width + border_width * 2, img.height + border_width * 2),
                         border_color)
    bordered.paste(img, (border_width, border_width), img)
    return bordered


def add_shadow(img: Image.Image, offset: tuple = (8, 8), 
               blur_radius: int = 15, shadow_color: tuple = (0, 0, 0, 100)) -> Image.Image:
    """Ajoute une ombre portée à l'image."""
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    padding = blur_radius * 2 + max(abs(offset[0]), abs(offset[1]))
    shadow_size = (img.width + padding * 2, img.height + padding * 2)
    
    shadow = Image.new('RGBA', shadow_size, (0, 0, 0, 0))
    shadow_shape = Image.new('RGBA', img.size, shadow_color)
    shadow_shape.putalpha(img.split()[3])
    
    shadow.paste(shadow_shape, (padding + offset[0], padding + offset[1]))
    shadow = shadow.filter(ImageFilter.GaussianBlur(blur_radius))
    shadow.paste(img, (padding, padding), img)
    
    return shadow


# =============================================================================
# GÉNÉRATEURS DE POSITIONS
# =============================================================================

def generate_spiral_positions(center, num_photos, start_radius, max_radius, photo_size):
    """Génère des positions en spirale autour du centre."""
    positions = []
    angle = random.uniform(0, 2 * math.pi)
    radius = start_radius
    radius_range = max_radius - start_radius
    radius_increment = radius_range / max(num_photos, 1) * 0.8
    
    for i in range(num_photos):
        if radius > max_radius:
            radius = start_radius + random.uniform(0, radius_range * 0.3)
            angle += math.pi / 2
        
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        rotation = random.uniform(-15, 15)
        positions.append((x, y, rotation))
        
        angle += math.pi / 3 + random.uniform(-0.2, 0.2)
        radius += radius_increment + random.randint(-5, 10)
    
    return positions


def generate_orbital_positions(center, num_photos, min_radius, max_radius, photo_size):
    """Génère des positions orbitales sur plusieurs anneaux."""
    positions = []
    orbit_spacing = max(photo_size) * 1.2
    num_orbits = max(2, int((max_radius - min_radius) / orbit_spacing))
    
    photos_per_orbit = [num_photos // num_orbits] * num_orbits
    for i in range(num_photos % num_orbits):
        photos_per_orbit[i] += 1
    
    for orbit_idx, count in enumerate(photos_per_orbit):
        if count == 0:
            continue
        
        t = (orbit_idx + 0.5) / num_orbits
        radius = min_radius + t * (max_radius - min_radius)
        start_angle = random.uniform(0, 2 * math.pi)
        
        for i in range(count):
            angle = start_angle + (2 * math.pi * i / count)
            angle += random.uniform(-0.1, 0.1)
            radius_var = radius + random.uniform(-15, 15)
            
            x = center[0] + int(radius_var * math.cos(angle))
            y = center[1] + int(radius_var * math.sin(angle))
            rotation = random.uniform(-20, 20)
            positions.append((x, y, rotation))
    
    return positions


def generate_cloud_positions(center, num_photos, min_radius, max_radius, photo_size):
    """Génère des positions aléatoires en nuage avec exclusion du centre."""
    positions = []
    
    for _ in range(num_photos):
        r = min_radius + (max_radius - min_radius) * (random.random() ** 0.7)
        angle = random.uniform(0, 2 * math.pi)
        
        x = center[0] + int(r * math.cos(angle))
        y = center[1] + int(r * math.sin(angle))
        rotation = random.uniform(-25, 25)
        positions.append((x, y, rotation))
    
    return positions


def generate_brick_positions(center, num_photos, min_radius, max_radius,
                             photo_size, canvas_size, gap=4, brick_offset=0.5):
    """Génère des positions en mur de briques dans un anneau autour du centre."""
    positions = []
    brick_w, brick_h = photo_size
    
    cols = math.ceil(canvas_size[0] / (brick_w + gap)) + 2
    rows = math.ceil(canvas_size[1] / (brick_h + gap)) + 2
    start_x = (canvas_size[0] - cols * (brick_w + gap)) // 2
    start_y = (canvas_size[1] - rows * (brick_h + gap)) // 2
    
    all_positions = []
    
    for row in range(rows):
        row_offset = int((brick_w + gap) * brick_offset) if row % 2 == 1 else 0
        
        for col in range(cols):
            x = start_x + col * (brick_w + gap) + row_offset + brick_w // 2
            y = start_y + row * (brick_h + gap) + brick_h // 2
            
            dist = math.sqrt((x - center[0])**2 + (y - center[1])**2)
            
            if dist >= min_radius and dist <= max_radius:
                if 0 <= x < canvas_size[0] and 0 <= y < canvas_size[1]:
                    all_positions.append((x, y, 0, dist))
    
    all_positions.sort(key=lambda p: p[3])
    return [(x, y, r) for x, y, r, _ in all_positions[:num_photos]]


# =============================================================================
# FONCTION PRINCIPALE DE GÉNÉRATION
# =============================================================================

def create_photo_cloud(
    main_photo_path: str,
    surrounding_photos: list,
    output_path: str = None,
    canvas_size: tuple = (1920, 1080),
    main_photo_size: tuple = (400, 400),
    surrounding_size: tuple = (150, 150),
    layout: str = "orbital",
    background_color: tuple = (30, 30, 35, 255),
    add_shadows: bool = True,
    main_glow: bool = True,
    distance_fade: float = 0.5,
    fade_curve: float = 1.0,
    gap: int = 4,
    brick_ratio: float = 1.5,
    max_photos: int = None,
    corner_radius: int = 10,
) -> Image.Image:
    """Crée un nuage de photos avec une photo principale au centre."""
    
    # Créer le canvas
    canvas = Image.new('RGBA', canvas_size, background_color)
    center = (canvas_size[0] // 2, canvas_size[1] // 2)
    max_distance = math.sqrt(center[0]**2 + center[1]**2)
    
    # Charger et préparer la photo principale
    main_img = load_image(main_photo_path)
    
    if layout == "brick":
        main_img = resize_cover(main_img, main_photo_size)
    else:
        main_img = resize_to_fit(main_img, main_photo_size)
        if corner_radius > 0:
            main_img = add_rounded_corners(main_img, corner_radius + 5)
    
    main_img = add_border(main_img, 5, (255, 255, 255, 255))
    if corner_radius > 0 and layout != "brick":
        main_img = add_rounded_corners(main_img, corner_radius + 8)
    
    # Calculer les rayons
    main_radius = max(main_img.width, main_img.height) // 2
    min_radius = main_radius + max(surrounding_size) // 2 + 20
    max_radius = min(canvas_size[0], canvas_size[1]) // 2 - max(surrounding_size) // 2
    
    # Taille des photos environnantes
    if layout == "brick":
        brick_h = int(surrounding_size[0] / brick_ratio)
        actual_size = (surrounding_size[0], brick_h)
        min_radius = main_radius + 10
        max_radius = max(canvas_size) // 2 + max(actual_size)
    else:
        actual_size = surrounding_size
    
    # Charger les photos environnantes
    loaded_photos = []
    for path in surrounding_photos:
        try:
            img = load_image(path)
            loaded_photos.append(img)
        except Exception as e:
            print(f"⚠ Impossible de charger {path}: {e}")
    
    if not loaded_photos:
        print("Erreur: Aucune photo chargée!")
        return canvas
    
    # Limiter le nombre de photos
    if max_photos and len(loaded_photos) > max_photos:
        loaded_photos = loaded_photos[:max_photos]
    
    # Préparer les photos
    processed_photos = []
    for img in loaded_photos:
        if layout == "brick":
            img = resize_cover(img, actual_size)
        else:
            img = resize_to_fit(img, actual_size)
            if corner_radius > 0:
                img = add_rounded_corners(img, corner_radius)
            img = add_border(img, 3, (255, 255, 255, 230))
            if corner_radius > 0:
                img = add_rounded_corners(img, corner_radius + 3)
        processed_photos.append(img)
    
    # Générer les positions
    num_positions = len(processed_photos) if layout != "brick" else len(processed_photos) * 10
    
    if layout == "spiral":
        positions = generate_spiral_positions(center, num_positions, min_radius, max_radius, actual_size)
    elif layout == "orbital":
        positions = generate_orbital_positions(center, num_positions, min_radius, max_radius, actual_size)
    elif layout == "cloud":
        positions = generate_cloud_positions(center, num_positions, min_radius, max_radius, actual_size)
    elif layout == "brick":
        positions = generate_brick_positions(center, num_positions, min_radius, max_radius, 
                                             actual_size, canvas_size, gap)
    else:
        positions = generate_orbital_positions(center, num_positions, min_radius, max_radius, actual_size)
    
    # Trier par distance (les plus éloignés en dessous)
    if layout != "brick":
        random.shuffle(positions)
        positions.sort(key=lambda p: -math.sqrt((p[0]-center[0])**2 + (p[1]-center[1])**2))
    
    # Dessiner les photos environnantes
    for i, (x, y, rotation) in enumerate(positions):
        img = processed_photos[i % len(processed_photos)].copy()
        
        distance = math.sqrt((x - center[0])**2 + (y - center[1])**2)
        normalized_distance = (distance / max_distance) ** fade_curve
        
        if distance_fade > 0:
            brightness = 1.0 + (normalized_distance * distance_fade)
            brightness += random.uniform(-0.05, 0.05)
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(brightness)
            
            sat_factor = 1.0 - (normalized_distance * distance_fade * 0.3)
            sat_enhancer = ImageEnhance.Color(img)
            img = sat_enhancer.enhance(max(0.5, sat_factor))
        
        if layout != "brick" and abs(rotation) > 0.5:
            img = img.rotate(rotation, expand=True, resample=Image.Resampling.BICUBIC)
        
        if add_shadows and layout != "brick":
            img = add_shadow(img, offset=(5, 5), blur_radius=10)
        
        paste_x = x - img.width // 2
        paste_y = y - img.height // 2
        canvas.paste(img, (paste_x, paste_y), img)
    
    # Lueur autour de la photo principale
    if main_glow and layout != "brick":
        glow_size = (main_img.width + 60, main_img.height + 60)
        glow = Image.new('RGBA', glow_size, (0, 0, 0, 0))
        glow_center = (glow_size[0] // 2, glow_size[1] // 2)
        
        for i in range(30, 0, -1):
            alpha = int(8 * (30 - i) / 30)
            draw = ImageDraw.Draw(glow)
            draw.ellipse([
                glow_center[0] - main_img.width//2 - i,
                glow_center[1] - main_img.height//2 - i,
                glow_center[0] + main_img.width//2 + i,
                glow_center[1] + main_img.height//2 + i
            ], fill=(255, 255, 255, alpha))
        
        glow = glow.filter(ImageFilter.GaussianBlur(15))
        glow_paste_x = center[0] - glow.width // 2
        glow_paste_y = center[1] - glow.height // 2
        canvas.paste(glow, (glow_paste_x, glow_paste_y), glow)
    
    # Photo principale avec ombre
    if add_shadows:
        main_with_shadow = add_shadow(main_img, offset=(10, 10), blur_radius=20)
    else:
        main_with_shadow = main_img
    
    main_paste_x = center[0] - main_with_shadow.width // 2
    main_paste_y = center[1] - main_with_shadow.height // 2
    canvas.paste(main_with_shadow, (main_paste_x, main_paste_y), main_with_shadow)
    
    # Sauvegarder
    if output_path:
        canvas.save(output_path, 'PNG', quality=95)
        print(f"✓ Image sauvegardée: {output_path}")
    
    return canvas


def collect_photos_from_path(path):
    """Collecte les photos depuis un fichier ou un dossier."""
    path = Path(path)
    valid_extensions = get_all_supported_extensions()
    
    if path.is_file():
        if path.suffix.lower() in valid_extensions:
            return [str(path)]
        return []
    
    if path.is_dir():
        photos = []
        for ext in valid_extensions:
            photos.extend(str(p) for p in path.glob(f'*{ext}'))
            photos.extend(str(p) for p in path.glob(f'*{ext.upper()}'))
        return sorted(set(photos))
    
    return []


def main():
    parser = argparse.ArgumentParser(
        description='Crée un nuage de photos autour d\'une photo principale',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Formats supportés:
  Standards : JPEG, PNG, GIF, WebP, BMP, TIFF, TGA, PCX, PPM...
  Apple     : HEIC, HEIF, AVIF (nécessite pillow-heif)
  RAW       : CR2, CR3, NEF, ARW, RAF, DNG, ORF... (nécessite rawpy)
  HDR       : EXR, HDR, PFM (nécessite imageio)

Layouts disponibles:
  orbital - Photos sur plusieurs orbites concentriques
  spiral  - Disposition en spirale
  cloud   - Disposition aléatoire en nuage
  brick   - Mur de briques avec décalage alterné

Exemples:
  %(prog)s --main portrait.jpg --photos vacances/ --layout orbital
  %(prog)s --main photo.heic --photos iphone_photos/ --layout spiral
  %(prog)s --main DSC_0001.NEF --photos raw_photos/ --layout brick
  %(prog)s --formats  # Afficher les formats supportés
        """
    )
    
    parser.add_argument('--main', '-m', help='Photo principale (centre)')
    parser.add_argument('--photos', '-p', nargs='+', help='Photos environnantes (fichiers ou dossier)')
    parser.add_argument('--output', '-o', default='photo_cloud.png', help='Fichier de sortie')
    parser.add_argument('--size', '-s', default='1920x1080', help='Taille du canvas WxH')
    parser.add_argument('--layout', '-l', choices=['brick', 'spiral', 'orbital', 'cloud'], default='orbital')
    parser.add_argument('--main-size', default='400x400', help='Taille photo principale')
    parser.add_argument('--thumb-size', default='150x150', help='Taille miniatures')
    parser.add_argument('--bg-color', default='30,30,35', help='Couleur fond R,G,B')
    parser.add_argument('--transparent', '-t', action='store_true', help='Fond transparent')
    parser.add_argument('--no-shadows', action='store_true', help='Sans ombres')
    parser.add_argument('--no-glow', action='store_true', help='Sans lueur centrale')
    parser.add_argument('--fade', type=float, default=0.5, help='Éclaircissement (0-1)')
    parser.add_argument('--fade-curve', type=float, default=1.0, help='Courbe du fade')
    parser.add_argument('--gap', type=int, default=4, help='Espacement briques')
    parser.add_argument('--brick-ratio', type=float, default=1.5, help='Ratio L/H briques')
    parser.add_argument('--max-photos', type=int, help='Nombre max photos')
    parser.add_argument('--corner-radius', type=int, default=10, help='Coins arrondis')
    parser.add_argument('--formats', action='store_true', help='Afficher formats supportés')
    
    args = parser.parse_args()
    
    if args.formats:
        print_format_support()
        return 0
    
    if not args.main or not args.photos:
        parser.print_help()
        print("\nErreur: --main et --photos sont requis")
        return 1
    
    canvas_size = tuple(map(int, args.size.split('x')))
    main_size = tuple(map(int, args.main_size.split('x')))
    thumb_size = tuple(map(int, args.thumb_size.split('x')))
    
    if args.transparent:
        bg_color = (0, 0, 0, 0)
    else:
        bg_color = tuple(map(int, args.bg_color.split(','))) + (255,)
    
    surrounding_photos = []
    for p in args.photos:
        surrounding_photos.extend(collect_photos_from_path(p))
    
    main_path = str(Path(args.main).resolve())
    surrounding_photos = [p for p in surrounding_photos if str(Path(p).resolve()) != main_path]
    
    if not surrounding_photos:
        print("Erreur: Aucune photo environnante trouvée!")
        print_format_support()
        return 1
    
    print(f"Photo principale: {args.main}")
    print(f"Photos environnantes: {len(surrounding_photos)}")
    print(f"Layout: {args.layout}")
    print(f"Canvas: {canvas_size}")
    print(f"Fade: {args.fade} (courbe: {args.fade_curve})")
    
    create_photo_cloud(
        main_photo_path=args.main,
        surrounding_photos=surrounding_photos,
        output_path=args.output,
        canvas_size=canvas_size,
        main_photo_size=main_size,
        surrounding_size=thumb_size,
        layout=args.layout,
        background_color=bg_color,
        add_shadows=not args.no_shadows,
        main_glow=not args.no_glow,
        distance_fade=args.fade,
        fade_curve=args.fade_curve,
        gap=args.gap,
        brick_ratio=args.brick_ratio,
        max_photos=args.max_photos,
        corner_radius=args.corner_radius,
    )
    
    return 0


if __name__ == '__main__':
    exit(main())
