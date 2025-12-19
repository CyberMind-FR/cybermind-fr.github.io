#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════
thumbnail-generator.py - Générateur de vignettes dynamiques pour Hexo
═══════════════════════════════════════════════════════════════════════════════

Génère des images de vignettes (1200x630) pour les apps/articles sans cover.

Usage:
    python3 thumbnail-generator.py --title "App Name" --icon "🧠" \
        --category "meditation" --tags "audio,visual,pwa" \
        --output "/path/to/output.jpg"

    python3 thumbnail-generator.py --config apps.json --output-dir /images/

═══════════════════════════════════════════════════════════════════════════════
"""

import argparse
import json
import math
import os
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Installer Pillow: pip install Pillow")
    sys.exit(1)

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

WIDTH = 1200
HEIGHT = 630

# Couleurs par catégorie
CATEGORY_THEMES = {
    'meditation': {
        'bg': (14, 22, 40),
        'accent': (6, 182, 212),
        'gradient': [(6, 182, 212), (59, 130, 246)],
        'pattern': 'circles'
    },
    'wellness': {
        'bg': (14, 31, 26),
        'accent': (16, 185, 129),
        'gradient': [(16, 185, 129), (6, 182, 212)],
        'pattern': 'waves'
    },
    'creative': {
        'bg': (31, 14, 31),
        'accent': (236, 72, 153),
        'gradient': [(236, 72, 153), (168, 85, 247)],
        'pattern': 'spirals'
    },
    'philosophy': {
        'bg': (26, 14, 40),
        'accent': (168, 85, 247),
        'gradient': [(168, 85, 247), (99, 102, 241)],
        'pattern': 'yinyang'
    },
    'security': {
        'bg': (31, 14, 14),
        'accent': (239, 68, 68),
        'gradient': [(239, 68, 68), (249, 115, 22)],
        'pattern': 'shield'
    },
    'cybersecurity': {
        'bg': (14, 31, 26),
        'accent': (0, 255, 136),
        'gradient': [(0, 255, 136), (6, 182, 212)],
        'pattern': 'matrix'
    },
    'dev': {
        'bg': (14, 22, 40),
        'accent': (59, 130, 246),
        'gradient': [(59, 130, 246), (6, 182, 212)],
        'pattern': 'code'
    },
    'tools': {
        'bg': (31, 26, 14),
        'accent': (249, 115, 22),
        'gradient': [(249, 115, 22), (234, 179, 8)],
        'pattern': 'gears'
    },
    'default': {
        'bg': (18, 18, 26),
        'accent': (99, 102, 241),
        'gradient': [(99, 102, 241), (168, 85, 247)],
        'pattern': 'dots'
    }
}

# Icônes par tag
TAG_ICONS = {
    'meditation': '🧘', 'audio': '🎵', 'visual': '👁️', 'pwa': '📱',
    'frequencies': '〰️', 'wellness': '💚', 'rife': '〰️', 'spooky2': '📡',
    'creative': '🎨', 'generative': '✨', 'art': '🖼️', 'geometry': '🔮',
    'neuroscience': '🧠', 'brainwave': '🌊', 'audiostrobe': '💡',
    'security': '🛡️', 'linux': '🐧', 'embedded': '⚙️', 'philosophy': '☯️',
    'open-source': '🔓', 'python': '🐍', 'javascript': '📜', 'react': '⚛️',
    'tutorial': '📖', 'guide': '📚', 'video': '🎬', 'music': '🎶'
}

# ═══════════════════════════════════════════════════════════════════════════════
# FONCTIONS UTILITAIRES
# ═══════════════════════════════════════════════════════════════════════════════

def lerp_color(c1, c2, t):
    """Interpolation linéaire entre deux couleurs"""
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

def get_font(size, bold=False):
    """Charge une police avec fallback"""
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "C:\\Windows\\Fonts\\arial.ttf"
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except:
                pass
    return ImageFont.load_default()

def get_emoji_font(size):
    """Charge une police avec support emoji"""
    emoji_paths = [
        "/usr/share/fonts/truetype/ancient-scripts/Symbola_hint.ttf",
        "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf",
        "/usr/share/fonts/truetype/symbola/Symbola.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Apple Color Emoji.ttc"
    ]
    for path in emoji_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except:
                pass
    return get_font(size)

# ═══════════════════════════════════════════════════════════════════════════════
# PATTERNS DE FOND
# ═══════════════════════════════════════════════════════════════════════════════

def draw_gradient_bg(draw, theme):
    """Dessine un fond dégradé"""
    bg = theme['bg']
    for y in range(HEIGHT):
        t = y / HEIGHT
        darker = tuple(max(0, c - 10) for c in bg)
        color = lerp_color(bg, darker, t)
        draw.line([(0, y), (WIDTH, y)], fill=color)

def draw_pattern_circles(draw, accent, opacity=0.1):
    """Cercles concentriques"""
    cx, cy = WIDTH // 2, HEIGHT // 2
    for i in range(8):
        r = 50 + i * 60
        color = tuple(int(c * opacity) for c in accent)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=2)

def draw_pattern_waves(draw, accent, opacity=0.15):
    """Ondes sinusoïdales"""
    for wave in range(4):
        points = []
        y_base = 150 + wave * 100
        for x in range(0, WIDTH, 4):
            y = y_base + 30 * math.sin(x * 0.02 + wave * 0.5)
            points.append((x, y))
        color = tuple(int(c * (opacity - wave * 0.02)) for c in accent)
        if len(points) > 1:
            draw.line(points, fill=color, width=2)

def draw_pattern_dots(draw, accent, opacity=0.1):
    """Grille de points"""
    color = tuple(int(c * opacity) for c in accent)
    for x in range(0, WIDTH, 40):
        for y in range(0, HEIGHT, 40):
            draw.ellipse([x-2, y-2, x+2, y+2], fill=color)

def draw_pattern_matrix(draw, accent, opacity=0.08):
    """Style matrix/code"""
    import random
    random.seed(42)
    chars = "01アイウエオカキクケコ"
    color = tuple(int(c * opacity) for c in accent)
    font = get_font(14)
    for x in range(0, WIDTH, 25):
        for y in range(0, HEIGHT, 25):
            if random.random() > 0.7:
                char = random.choice(chars)
                draw.text((x, y), char, font=font, fill=color)

def draw_pattern_gears(draw, accent, opacity=0.1):
    """Engrenages stylisés"""
    color = tuple(int(c * opacity) for c in accent)
    positions = [(200, 200, 80), (WIDTH - 200, 150, 60), (WIDTH // 2, HEIGHT - 150, 70)]
    for cx, cy, r in positions:
        # Cercle principal
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=2)
        # Dents
        for i in range(8):
            angle = i * math.pi / 4
            x1 = cx + r * math.cos(angle)
            y1 = cy + r * math.sin(angle)
            x2 = cx + (r + 15) * math.cos(angle)
            y2 = cy + (r + 15) * math.sin(angle)
            draw.line([(x1, y1), (x2, y2)], fill=color, width=3)

def draw_background_pattern(draw, theme):
    """Dessine le pattern de fond selon la catégorie"""
    accent = theme['accent']
    pattern = theme.get('pattern', 'dots')
    
    patterns = {
        'circles': draw_pattern_circles,
        'waves': draw_pattern_waves,
        'dots': draw_pattern_dots,
        'matrix': draw_pattern_matrix,
        'gears': draw_pattern_gears,
        'spirals': draw_pattern_circles,  # Fallback
        'yinyang': draw_pattern_circles,
        'shield': draw_pattern_dots,
        'code': draw_pattern_matrix
    }
    
    func = patterns.get(pattern, draw_pattern_dots)
    func(draw, accent)

# ═══════════════════════════════════════════════════════════════════════════════
# ÉLÉMENTS VISUELS
# ═══════════════════════════════════════════════════════════════════════════════

def draw_glow(draw, cx, cy, radius, color, intensity=0.3):
    """Effet de lueur"""
    for i in range(radius, 0, -5):
        alpha = intensity * (i / radius)
        glow_color = tuple(int(c * alpha) for c in color)
        draw.ellipse([cx - i, cy - i, cx + i, cy + i], fill=glow_color)

def draw_tags(draw, tags, x, y, accent):
    """Dessine les badges de tags"""
    font = get_font(18)
    emoji_font = get_emoji_font(16)
    current_x = x
    max_width = WIDTH - 100
    
    for tag in tags[:6]:  # Max 6 tags
        icon = TAG_ICONS.get(tag.lower(), '•')
        text = f"{tag}"
        
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0] + 40  # +40 pour icône
        
        if current_x + text_width > max_width:
            break
        
        # Fond du badge
        badge_bg = tuple(c // 6 for c in accent)
        draw.rounded_rectangle(
            [current_x, y, current_x + text_width, y + 30],
            radius=6, fill=badge_bg
        )
        
        # Icône emoji
        try:
            draw.text((current_x + 8, y + 5), icon, font=emoji_font, fill=(200, 200, 210))
        except:
            draw.text((current_x + 8, y + 5), "•", font=font, fill=accent)
        
        # Texte du tag
        draw.text((current_x + 28, y + 4), text, font=font, fill=(200, 200, 210))
        current_x += text_width + 10

def draw_category_badge(draw, category, x, y, accent):
    """Dessine le badge de catégorie"""
    font = get_font(16, bold=True)
    text = category.upper()
    
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0] + 24
    text_height = 28
    
    # Badge avec couleur accent
    draw.rounded_rectangle(
        [x, y, x + text_width, y + text_height],
        radius=4, fill=accent
    )
    
    # Texte noir sur fond coloré
    draw.text((x + 12, y + 4), text, font=font, fill=(0, 0, 0))

# ═══════════════════════════════════════════════════════════════════════════════
# GÉNÉRATION D'IMAGE
# ═══════════════════════════════════════════════════════════════════════════════

def generate_thumbnail(title, icon='🚀', category='default', tags=None, description='', output_path='thumbnail.jpg'):
    """
    Génère une image de vignette dynamique
    
    Args:
        title: Titre de l'app/article
        icon: Emoji principal
        category: Catégorie pour le thème de couleurs
        tags: Liste de tags
        description: Description courte (optionnel)
        output_path: Chemin de sortie
    """
    if tags is None:
        tags = []
    
    # Récupérer le thème
    theme = CATEGORY_THEMES.get(category.lower(), CATEGORY_THEMES['default'])
    accent = theme['accent']
    
    # Créer l'image
    img = Image.new('RGB', (WIDTH, HEIGHT), theme['bg'])
    draw = ImageDraw.Draw(img)
    
    # 1. Fond dégradé
    draw_gradient_bg(draw, theme)
    
    # 2. Pattern de fond
    draw_background_pattern(draw, theme)
    
    # 3. Lueur centrale
    draw_glow(draw, WIDTH // 2, HEIGHT // 2 - 50, 200, accent, 0.15)
    
    # 4. Badge catégorie (top right)
    draw_category_badge(draw, category, WIDTH - 180, 30, accent)
    
    # 5. Icône principale
    try:
        icon_font = get_emoji_font(100)
        draw.text((80, 120), icon, font=icon_font, fill=(255, 255, 255))
    except:
        # Fallback: dessiner un cercle avec l'initial
        draw.ellipse([80, 120, 180, 220], outline=accent, width=3)
        fallback_font = get_font(60, bold=True)
        draw.text((110, 140), icon[0] if icon else "?", font=fallback_font, fill=accent)
    
    # 6. Titre
    title_font = get_font(56, bold=True)
    # Ombre
    draw.text((82, 262), title, font=title_font, fill=(0, 0, 0))
    # Texte principal
    draw.text((80, 260), title, font=title_font, fill=accent)
    
    # 7. Description (si présente)
    if description:
        desc_font = get_font(24)
        # Tronquer si trop long
        if len(description) > 80:
            description = description[:77] + '...'
        draw.text((80, 340), description, font=desc_font, fill=(152, 152, 166))
    
    # 8. Tags
    if tags:
        tags_y = 400 if description else 350
        draw_tags(draw, tags, 80, tags_y, accent)
    
    # 9. Ligne décorative en bas
    gradient = theme['gradient']
    for x in range(WIDTH):
        t = x / WIDTH
        color = lerp_color(gradient[0], gradient[1], t)
        draw.line([(x, HEIGHT - 8), (x, HEIGHT)], fill=color)
    
    # 10. Watermark subtil
    wm_font = get_font(14)
    draw.text((WIDTH - 150, HEIGHT - 30), "CyberMind.fr", font=wm_font, fill=(80, 80, 90))
    
    # Sauvegarder
    img.save(output_path, 'JPEG', quality=90)
    print(f"✓ Vignette générée: {output_path}")
    return output_path

def generate_summary_thumbnail(title, icon='📄', description='', category='default', output_path='thumbnail.jpg'):
    """
    Génère une vignette style "résumé de contenu"
    Plus orientée texte avec mise en page article
    """
    theme = CATEGORY_THEMES.get(category.lower(), CATEGORY_THEMES['default'])
    accent = theme['accent']
    
    img = Image.new('RGB', (WIDTH, HEIGHT), theme['bg'])
    draw = ImageDraw.Draw(img)
    
    # Fond
    draw_gradient_bg(draw, theme)
    
    # Cadre principal
    margin = 60
    draw.rounded_rectangle(
        [margin, margin, WIDTH - margin, HEIGHT - margin],
        radius=20,
        outline=tuple(c // 3 for c in accent),
        width=2
    )
    
    # Icône
    icon_font = get_font(80)
    draw.text((margin + 40, margin + 40), icon, font=icon_font, fill=accent)
    
    # Titre
    title_font = get_font(42, bold=True)
    draw.text((margin + 40, margin + 150), title, font=title_font, fill=(232, 232, 237))
    
    # Description (multi-lignes)
    if description:
        desc_font = get_font(22)
        words = description.split()
        lines = []
        current_line = []
        max_width = WIDTH - 2 * margin - 80
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            bbox = draw.textbbox((0, 0), test_line, font=desc_font)
            if bbox[2] - bbox[0] < max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        if current_line:
            lines.append(' '.join(current_line))
        
        y = margin + 220
        for i, line in enumerate(lines[:4]):  # Max 4 lignes
            alpha = 1 - (i * 0.15)
            color = tuple(int(152 * alpha) for _ in range(2)) + (int(166 * alpha),)
            draw.text((margin + 40, y), line, font=desc_font, fill=color)
            y += 35
    
    # Badge catégorie
    draw_category_badge(draw, category, WIDTH - margin - 150, margin + 20, accent)
    
    # Ligne de lecture
    read_font = get_font(18)
    draw.text((margin + 40, HEIGHT - margin - 50), "Lire l'article →", font=read_font, fill=accent)
    
    img.save(output_path, 'JPEG', quality=90)
    print(f"✓ Vignette résumé générée: {output_path}")
    return output_path

# ═══════════════════════════════════════════════════════════════════════════════
# BATCH PROCESSING
# ═══════════════════════════════════════════════════════════════════════════════

def process_batch(config_path, output_dir):
    """
    Traite un fichier JSON de configuration pour générer plusieurs vignettes
    
    Format JSON attendu:
    [
        {
            "slug": "kasina-pro",
            "title": "Kasina θ Pro",
            "icon": "🧠",
            "category": "meditation",
            "tags": ["audio", "visual", "pwa"],
            "description": "Application de méditation..."
        },
        ...
    ]
    """
    with open(config_path, 'r', encoding='utf-8') as f:
        apps = json.load(f)
    
    os.makedirs(output_dir, exist_ok=True)
    
    for app in apps:
        slug = app.get('slug', 'app')
        output_path = os.path.join(output_dir, f"{slug}-thumb.jpg")
        
        generate_thumbnail(
            title=app.get('title', 'Application'),
            icon=app.get('icon', '🚀'),
            category=app.get('category', 'default'),
            tags=app.get('tags', []),
            description=app.get('description', ''),
            output_path=output_path
        )
    
    print(f"\n✓ {len(apps)} vignettes générées dans {output_dir}")

# ═══════════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description='Générateur de vignettes dynamiques')
    
    # Mode simple
    parser.add_argument('--title', help='Titre de l\'app')
    parser.add_argument('--icon', default='🚀', help='Emoji principal')
    parser.add_argument('--category', default='default', help='Catégorie')
    parser.add_argument('--tags', default='', help='Tags séparés par virgule')
    parser.add_argument('--description', default='', help='Description')
    parser.add_argument('--output', '-o', default='thumbnail.jpg', help='Fichier de sortie')
    parser.add_argument('--style', default='app', choices=['app', 'summary'], help='Style de vignette')
    
    # Mode batch
    parser.add_argument('--config', help='Fichier JSON de configuration')
    parser.add_argument('--output-dir', help='Dossier de sortie pour le batch')
    
    args = parser.parse_args()
    
    # Mode batch
    if args.config:
        if not args.output_dir:
            args.output_dir = './thumbnails'
        process_batch(args.config, args.output_dir)
        return
    
    # Mode simple
    if not args.title:
        parser.print_help()
        print("\nExemple:")
        print('  python3 thumbnail-generator.py --title "Mon App" --icon "🎵" --category "creative" --tags "audio,music" -o my-thumb.jpg')
        return
    
    tags = [t.strip() for t in args.tags.split(',') if t.strip()]
    
    if args.style == 'summary':
        generate_summary_thumbnail(
            title=args.title,
            icon=args.icon,
            description=args.description,
            category=args.category,
            output_path=args.output
        )
    else:
        generate_thumbnail(
            title=args.title,
            icon=args.icon,
            category=args.category,
            tags=tags,
            description=args.description,
            output_path=args.output
        )

if __name__ == '__main__':
    main()
