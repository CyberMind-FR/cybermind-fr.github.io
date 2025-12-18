#!/usr/bin/env python3
"""
Générateur de vignettes portfolio avec snapshots réels et animations
CyberMind Theme v4.1
"""

import os
import base64
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime

# Configuration
OUTPUT_DIR = "source/images/portfolio/thumbnails"
THUMBNAIL_WIDTH = 800
THUMBNAIL_HEIGHT = 450
SNAPSHOT_WIDTH = 320
SNAPSHOT_HEIGHT = 200

# Projets avec URLs de snapshots
PROJECTS = [
    {
        "id": "gk2-net",
        "title": "GK2.NET",
        "subtitle": "Premier ISP Personnel",
        "icon": "🌐",
        "year": "1996",
        "tags": ["Linux", "RedHat", "Apache", "Pionnier"],
        "color_primary": "#00ff88",
        "color_secondary": "#003322",
        "color_tertiary": "#001a11",
        "style": "retro",
        "archive_url": "https://web.archive.org/web/20010401091245/http://www.gk2.com/",
        "wayback_timestamp": "20010401091245",
        "original_url": "http://www.gk2.com/"
    },
    {
        "id": "ganimed",
        "title": "GANIMED",
        "subtitle": "Haute Magie & Géométrie Sacrée",
        "icon": "🔮",
        "year": "2015-2024",
        "tags": ["Magie", "Cymatics", "Hermétisme", "Alchimie"],
        "color_primary": "#9966ff",
        "color_secondary": "#1a0033",
        "color_tertiary": "#0d001a",
        "style": "mystique",
        "archive_url": "https://web.archive.org/web/20240914150157/https://ganimed.fr/",
        "wayback_timestamp": "20240914150157",
        "original_url": "https://ganimed.fr/"
    },
    {
        "id": "icieb",
        "title": "ICIEB",
        "subtitle": "Gravure Laser & Géométrie Sacrée",
        "icon": "🌸",
        "year": "2018-2021",
        "tags": ["Gravure", "Bois", "Fleur de Vie", "Artisanat"],
        "color_primary": "#ff6699",
        "color_secondary": "#330011",
        "color_tertiary": "#1a0009",
        "style": "artisan",
        "archive_url": "https://web.archive.org/web/20210318200344/https://icieb.fr/",
        "wayback_timestamp": "20210318200344",
        "original_url": "https://icieb.fr/"
    },
    {
        "id": "kragzouy-blog",
        "title": "Kragzouy",
        "subtitle": "Univers Créatif depuis 1982",
        "icon": "🧙",
        "year": "1982-présent",
        "tags": ["Poésie", "Musique", "Créatif", "Philosophie"],
        "color_primary": "#ffcc00",
        "color_secondary": "#332200",
        "color_tertiary": "#1a1100",
        "style": "creative",
        "archive_url": "https://kragzouy.blogspot.com/",
        "wayback_timestamp": None,
        "original_url": "https://kragzouy.blogspot.com/"
    },
    {
        "id": "wengu-yijing",
        "title": "Wengu Yi Jing",
        "subtitle": "Ressources Classiques",
        "icon": "☯️",
        "year": "2000-2025",
        "tags": ["Yi Jing", "Philosophie", "Taoïsme", "Hexagrammes"],
        "color_primary": "#ffffff",
        "color_secondary": "#111111",
        "color_tertiary": "#080808",
        "style": "zen",
        "archive_url": "https://web.archive.org/web/20250219091819/http://wengu.tartarie.com/wg/wengu.php?l=intro",
        "wayback_timestamp": "20250219091819",
        "original_url": "http://wengu.tartarie.com/"
    },
    {
        "id": "michel-murty",
        "title": "Michel Murty",
        "subtitle": "Site Personnel",
        "icon": "👤",
        "year": "2000-présent",
        "tags": ["Personnel", "Archive", "Free.fr"],
        "color_primary": "#66ccff",
        "color_secondary": "#002233",
        "color_tertiary": "#00111a",
        "style": "personal",
        "archive_url": "http://michelmurty.free.fr/",
        "wayback_timestamp": None,
        "original_url": "http://michelmurty.free.fr/"
    },
    {
        "id": "armbian-wui",
        "title": "Armbian WUI",
        "subtitle": "Interface Web Armbian",
        "icon": "🖥️",
        "year": "2022",
        "tags": ["Armbian", "Linux", "Web UI", "ARM"],
        "color_primary": "#ff6600",
        "color_secondary": "#331100",
        "color_tertiary": "#1a0900",
        "style": "tech",
        "archive_url": None,
        "wayback_timestamp": None,
        "original_url": None
    },
    {
        "id": "enigmasuite",
        "title": "EnigmaSuite",
        "subtitle": "Outils Sécurité Réseau",
        "icon": "🔐",
        "year": "2023",
        "tags": ["Sécurité", "OpenWrt", "CrowdSec", "Firewall"],
        "color_primary": "#00ffcc",
        "color_secondary": "#003333",
        "color_tertiary": "#001a1a",
        "style": "security",
        "archive_url": None,
        "wayback_timestamp": None,
        "original_url": None
    }
]

def get_wayback_thumbnail_url(timestamp, url):
    """Génère l'URL du thumbnail Wayback Machine"""
    if timestamp and url:
        # Format: https://web.archive.org/web/[timestamp]im_/[url]
        return f"https://web.archive.org/web/{timestamp}im_/{url}"
    return None

def generate_scan_lines():
    """Génère les lignes de scan CRT animées"""
    return '''
    <pattern id="scanlines" patternUnits="userSpaceOnUse" width="4" height="4">
      <line x1="0" y1="0" x2="4" y2="0" stroke="rgba(255,255,255,0.03)" stroke-width="1"/>
    </pattern>
    '''

def generate_glitch_animation(color):
    """Génère l'animation de glitch"""
    return f'''
    <style>
      @keyframes glitch {{
        0%, 100% {{ opacity: 1; transform: translate(0, 0); }}
        20% {{ opacity: 0.8; transform: translate(-2px, 0); }}
        40% {{ opacity: 0.9; transform: translate(2px, 0); }}
        60% {{ opacity: 0.7; transform: translate(-1px, 1px); }}
        80% {{ opacity: 0.95; transform: translate(1px, -1px); }}
      }}
      @keyframes scan {{
        0% {{ transform: translateY(-100%); }}
        100% {{ transform: translateY(450px); }}
      }}
      @keyframes pulse {{
        0%, 100% {{ opacity: 0.8; }}
        50% {{ opacity: 1; }}
      }}
      @keyframes flicker {{
        0%, 100% {{ opacity: 1; }}
        92% {{ opacity: 1; }}
        93% {{ opacity: 0.8; }}
        94% {{ opacity: 1; }}
        95% {{ opacity: 0.9; }}
        96% {{ opacity: 1; }}
      }}
      .snapshot-frame {{ animation: pulse 3s ease-in-out infinite; }}
      .scan-line {{ animation: scan 4s linear infinite; }}
      .title-text {{ animation: flicker 5s linear infinite; }}
      .glitch-overlay {{ animation: glitch 0.3s ease-in-out infinite; opacity: 0; }}
      .card:hover .glitch-overlay {{ opacity: 0.5; }}
    </style>
    '''

def generate_animated_thumbnail_svg(project, snapshot_placeholder=True):
    """Génère le SVG animé avec emplacement pour snapshot"""
    p = project
    tags_html = " • ".join(p["tags"][:4])
    
    # Position du snapshot
    snap_x = 480
    snap_y = 80
    snap_w = SNAPSHOT_WIDTH
    snap_h = SNAPSHOT_HEIGHT
    
    # URL du snapshot (placeholder ou réel)
    snapshot_url = ""
    if p.get("wayback_timestamp") and p.get("original_url"):
        snapshot_url = get_wayback_thumbnail_url(p["wayback_timestamp"], p["original_url"])
    
    # Pattern selon le style
    patterns = {
        "retro": f'''<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{p['color_primary']}" stroke-width="0.5" opacity="0.2"/>
          </pattern>''',
        "mystique": f'''<pattern id="sacred" width="60" height="60" patternUnits="userSpaceOnUse">
            <circle cx="30" cy="30" r="28" fill="none" stroke="{p['color_primary']}" stroke-width="0.3" opacity="0.15"/>
            <circle cx="30" cy="30" r="14" fill="none" stroke="{p['color_primary']}" stroke-width="0.3" opacity="0.1"/>
          </pattern>''',
        "artisan": f'''<pattern id="wood" width="100" height="8" patternUnits="userSpaceOnUse">
            <line x1="0" y1="4" x2="100" y2="4" stroke="{p['color_primary']}" stroke-width="0.3" opacity="0.1"/>
          </pattern>''',
        "creative": f'''<pattern id="stars" width="50" height="50" patternUnits="userSpaceOnUse">
            <circle cx="25" cy="25" r="1" fill="{p['color_primary']}" opacity="0.2"/>
          </pattern>''',
        "zen": f'''<pattern id="yinyang" width="80" height="80" patternUnits="userSpaceOnUse">
            <circle cx="40" cy="40" r="35" fill="none" stroke="{p['color_primary']}" stroke-width="0.3" opacity="0.1"/>
          </pattern>''',
        "personal": f'''<pattern id="lines" width="30" height="30" patternUnits="userSpaceOnUse">
            <line x1="0" y1="0" x2="30" y2="30" stroke="{p['color_primary']}" stroke-width="0.2" opacity="0.1"/>
          </pattern>''',
        "tech": f'''<pattern id="circuit" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M0,20 L15,20 L20,15 L20,0" fill="none" stroke="{p['color_primary']}" stroke-width="0.4" opacity="0.15"/>
            <circle cx="20" cy="20" r="2" fill="{p['color_primary']}" opacity="0.1"/>
          </pattern>''',
        "security": f'''<pattern id="shield" width="60" height="60" patternUnits="userSpaceOnUse">
            <path d="M30,5 L50,15 L50,35 L30,50 L10,35 L10,15 Z" fill="none" stroke="{p['color_primary']}" stroke-width="0.3" opacity="0.1"/>
          </pattern>'''
    }
    
    pattern = patterns.get(p["style"], patterns["tech"])
    pattern_id = p["style"] if p["style"] in ["retro", "mystique", "artisan", "creative", "zen", "personal", "tech", "security"] else "tech"
    pattern_id_map = {"retro": "grid", "mystique": "sacred", "artisan": "wood", "creative": "stars", 
                      "zen": "yinyang", "personal": "lines", "tech": "circuit", "security": "shield"}
    pattern_ref = pattern_id_map.get(p["style"], "grid")
    
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{THUMBNAIL_WIDTH}" height="{THUMBNAIL_HEIGHT}" viewBox="0 0 {THUMBNAIL_WIDTH} {THUMBNAIL_HEIGHT}" 
     xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="portfolio-thumbnail">
  <defs>
    {pattern}
    {generate_scan_lines()}
    
    <linearGradient id="bg-grad-{p['id']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{p['color_secondary']}"/>
      <stop offset="50%" stop-color="{p['color_tertiary']}"/>
      <stop offset="100%" stop-color="#000000"/>
    </linearGradient>
    
    <linearGradient id="accent-grad-{p['id']}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{p['color_primary']}"/>
      <stop offset="100%" stop-color="{p['color_primary']}" stop-opacity="0.3"/>
    </linearGradient>
    
    <linearGradient id="snapshot-overlay-{p['id']}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="transparent"/>
      <stop offset="70%" stop-color="transparent"/>
      <stop offset="100%" stop-color="{p['color_tertiary']}"/>
    </linearGradient>
    
    <filter id="glow-{p['id']}">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    
    <filter id="noise">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="1" result="noise"/>
      <feColorMatrix type="saturate" values="0"/>
      <feBlend in="SourceGraphic" in2="noise" mode="multiply" result="blend"/>
      <feComposite in="blend" in2="SourceGraphic" operator="in"/>
    </filter>
    
    <clipPath id="snapshot-clip-{p['id']}">
      <rect x="{snap_x}" y="{snap_y}" width="{snap_w}" height="{snap_h}" rx="8"/>
    </clipPath>
    
    <mask id="vignette-{p['id']}">
      <rect x="{snap_x}" y="{snap_y}" width="{snap_w}" height="{snap_h}" fill="white"/>
      <rect x="{snap_x}" y="{snap_y}" width="{snap_w}" height="{snap_h}" fill="url(#snapshot-overlay-{p['id']})"/>
    </mask>
  </defs>
  
  {generate_glitch_animation(p['color_primary'])}
  
  <!-- Background -->
  <rect width="100%" height="100%" fill="url(#bg-grad-{p['id']})"/>
  <rect width="100%" height="100%" fill="url(#{pattern_ref})" opacity="0.6"/>
  
  <!-- Scanlines overlay -->
  <rect width="100%" height="100%" fill="url(#scanlines)" opacity="0.5"/>
  
  <!-- Animated scan line -->
  <rect class="scan-line" x="0" y="0" width="100%" height="2" fill="{p['color_primary']}" opacity="0.1"/>
  
  <!-- Top accent bar -->
  <rect x="0" y="0" width="100%" height="3" fill="url(#accent-grad-{p['id']})"/>
  
  <!-- Left content area -->
  <g class="content-left">
    <!-- Icon with glow -->
    <circle cx="80" cy="180" r="50" fill="{p['color_tertiary']}" stroke="{p['color_primary']}" stroke-width="2" opacity="0.9" class="snapshot-frame"/>
    <text x="80" y="195" font-size="40" text-anchor="middle" fill="{p['color_primary']}">{p['icon']}</text>
    
    <!-- Title -->
    <text x="30" y="280" font-family="'JetBrains Mono', monospace" font-size="36" font-weight="bold" 
          fill="{p['color_primary']}" filter="url(#glow-{p['id']})" class="title-text">{p['title']}</text>
    
    <!-- Subtitle -->
    <text x="30" y="315" font-family="system-ui, sans-serif" font-size="16" fill="#aaaaaa">{p['subtitle']}</text>
    
    <!-- Tags -->
    <text x="30" y="350" font-family="'JetBrains Mono', monospace" font-size="11" fill="#666666">{tags_html}</text>
  </g>
  
  <!-- Snapshot area -->
  <g class="snapshot-area">
    <!-- Frame background -->
    <rect x="{snap_x-4}" y="{snap_y-4}" width="{snap_w+8}" height="{snap_h+8}" rx="10" 
          fill="{p['color_tertiary']}" stroke="{p['color_primary']}" stroke-width="1" opacity="0.8"/>
    
    <!-- Snapshot placeholder or image -->
    <g clip-path="url(#snapshot-clip-{p['id']})">
      <!-- Placeholder gradient background -->
      <rect x="{snap_x}" y="{snap_y}" width="{snap_w}" height="{snap_h}" fill="{p['color_secondary']}"/>
      
      <!-- Grid pattern for placeholder -->
      <rect x="{snap_x}" y="{snap_y}" width="{snap_w}" height="{snap_h}" fill="url(#{pattern_ref})" opacity="0.3"/>
      
      <!-- Placeholder text -->
      <text x="{snap_x + snap_w//2}" y="{snap_y + snap_h//2 - 10}" font-family="monospace" font-size="12" 
            text-anchor="middle" fill="{p['color_primary']}" opacity="0.5">SNAPSHOT</text>
      <text x="{snap_x + snap_w//2}" y="{snap_y + snap_h//2 + 10}" font-family="monospace" font-size="10" 
            text-anchor="middle" fill="#666666">{(p.get('original_url') or 'No URL')[:30]}...</text>
      
      <!-- Image element (to be replaced with actual snapshot) -->
      <!-- <image xlink:href="[SNAPSHOT_URL]" x="{snap_x}" y="{snap_y}" width="{snap_w}" height="{snap_h}" preserveAspectRatio="xMidYMid slice"/> -->
      
      <!-- Vignette overlay -->
      <rect x="{snap_x}" y="{snap_y}" width="{snap_w}" height="{snap_h}" fill="url(#snapshot-overlay-{p['id']})"/>
    </g>
    
    <!-- Corner decorations -->
    <path d="M{snap_x},{snap_y+15} L{snap_x},{snap_y} L{snap_x+15},{snap_y}" fill="none" stroke="{p['color_primary']}" stroke-width="2"/>
    <path d="M{snap_x+snap_w-15},{snap_y} L{snap_x+snap_w},{snap_y} L{snap_x+snap_w},{snap_y+15}" fill="none" stroke="{p['color_primary']}" stroke-width="2"/>
    <path d="M{snap_x},{snap_y+snap_h-15} L{snap_x},{snap_y+snap_h} L{snap_x+15},{snap_y+snap_h}" fill="none" stroke="{p['color_primary']}" stroke-width="2"/>
    <path d="M{snap_x+snap_w-15},{snap_y+snap_h} L{snap_x+snap_w},{snap_y+snap_h} L{snap_x+snap_w},{snap_y+snap_h-15}" fill="none" stroke="{p['color_primary']}" stroke-width="2"/>
    
    <!-- Archive label -->
    <rect x="{snap_x + snap_w - 80}" y="{snap_y + snap_h - 24}" width="76" height="20" rx="3" fill="{p['color_primary']}" opacity="0.2"/>
    <text x="{snap_x + snap_w - 42}" y="{snap_y + snap_h - 10}" font-family="monospace" font-size="9" 
          text-anchor="middle" fill="{p['color_primary']}">ARCHIVED</text>
  </g>
  
  <!-- Year badge -->
  <g class="year-badge">
    <rect x="{THUMBNAIL_WIDTH - 120}" y="15" width="105" height="30" rx="4" fill="{p['color_primary']}" opacity="0.15"/>
    <rect x="{THUMBNAIL_WIDTH - 120}" y="15" width="105" height="30" rx="4" fill="none" stroke="{p['color_primary']}" stroke-width="1" opacity="0.5"/>
    <text x="{THUMBNAIL_WIDTH - 67}" y="36" font-family="monospace" font-size="14" text-anchor="middle" fill="{p['color_primary']}">{p['year']}</text>
  </g>
  
  <!-- Bottom bar -->
  <rect x="0" y="{THUMBNAIL_HEIGHT - 35}" width="100%" height="35" fill="{p['color_tertiary']}" opacity="0.95"/>
  <line x1="0" y1="{THUMBNAIL_HEIGHT - 35}" x2="100%" y2="{THUMBNAIL_HEIGHT - 35}" stroke="{p['color_primary']}" stroke-width="1" opacity="0.3"/>
  <text x="15" y="{THUMBNAIL_HEIGHT - 12}" font-family="monospace" font-size="12" fill="{p['color_primary']}" opacity="0.8">cybermind.fr/portfolio/{p['id']}</text>
  
  <!-- Status indicator -->
  <circle cx="{THUMBNAIL_WIDTH - 25}" cy="{THUMBNAIL_HEIGHT - 17}" r="4" fill="{p['color_primary']}" opacity="0.8">
    <animate attributeName="opacity" values="0.8;0.4;0.8" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="{THUMBNAIL_WIDTH - 40}" y="{THUMBNAIL_HEIGHT - 12}" font-family="monospace" font-size="10" text-anchor="end" fill="#666666">LIVE</text>
  
  <!-- Glitch overlay (activé au hover via CSS externe) -->
  <rect class="glitch-overlay" x="0" y="0" width="100%" height="100%" fill="{p['color_primary']}" opacity="0"/>
  
  <!-- Corner accent -->
  <path d="M{THUMBNAIL_WIDTH},0 L{THUMBNAIL_WIDTH},60 L{THUMBNAIL_WIDTH-60},0 Z" fill="{p['color_primary']}" opacity="0.08"/>
</svg>'''
    
    return svg


def main():
    """Génère toutes les vignettes animées"""
    output_path = Path(OUTPUT_DIR)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print("🎬 Génération des vignettes portfolio animées...")
    print(f"📁 Dossier de sortie: {OUTPUT_DIR}")
    print()
    
    for project in PROJECTS:
        svg_content = generate_animated_thumbnail_svg(project)
        filename = f"{project['id']}.svg"
        filepath = output_path / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        status = "📸" if project.get("archive_url") else "📄"
        print(f"  {status} {project['icon']} {project['title']:20} → {filename}")
    
    print()
    print(f"✨ {len(PROJECTS)} vignettes animées générées!")
    print()
    print("Fonctionnalités:")
    print("  • Animations CSS intégrées (scan, pulse, flicker)")
    print("  • Emplacement snapshot avec cadre stylisé")
    print("  • Indicateur LIVE animé")
    print("  • Effet glitch au hover (via CSS externe)")


if __name__ == "__main__":
    main()
