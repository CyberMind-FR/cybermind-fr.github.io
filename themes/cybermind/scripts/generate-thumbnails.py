#!/usr/bin/env python3
"""
Générateur de vignettes pour les projets portfolio CyberMind
Crée des images SVG stylisées pour chaque projet
"""

import os
import re
from pathlib import Path

# Configuration
OUTPUT_DIR = "source/images/portfolio/thumbnails"
THUMBNAIL_WIDTH = 800
THUMBNAIL_HEIGHT = 450

# Projets portfolio avec leurs métadonnées
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
        "style": "retro"
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
        "style": "mystique"
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
        "style": "artisan"
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
        "style": "creative"
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
        "style": "zen"
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
        "style": "personal"
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
        "style": "tech"
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
        "style": "security"
    }
]

def generate_pattern(style, color):
    """Génère un pattern SVG selon le style"""
    patterns = {
        "retro": f'''
            <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
                <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{color}" stroke-width="0.5" opacity="0.3"/>
            </pattern>
            <pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">
                <circle cx="10" cy="10" r="1" fill="{color}" opacity="0.2"/>
            </pattern>
        ''',
        "mystique": f'''
            <pattern id="sacred" width="60" height="60" patternUnits="userSpaceOnUse">
                <circle cx="30" cy="30" r="25" fill="none" stroke="{color}" stroke-width="0.5" opacity="0.2"/>
                <circle cx="30" cy="30" r="15" fill="none" stroke="{color}" stroke-width="0.5" opacity="0.15"/>
                <circle cx="30" cy="30" r="5" fill="{color}" opacity="0.1"/>
            </pattern>
        ''',
        "artisan": f'''
            <pattern id="wood" width="100" height="10" patternUnits="userSpaceOnUse">
                <line x1="0" y1="5" x2="100" y2="5" stroke="{color}" stroke-width="0.3" opacity="0.15"/>
                <line x1="0" y1="2" x2="60" y2="2" stroke="{color}" stroke-width="0.2" opacity="0.1"/>
                <line x1="40" y1="8" x2="100" y2="8" stroke="{color}" stroke-width="0.2" opacity="0.1"/>
            </pattern>
        ''',
        "creative": f'''
            <pattern id="stars" width="50" height="50" patternUnits="userSpaceOnUse">
                <polygon points="25,5 30,20 45,20 33,30 38,45 25,35 12,45 17,30 5,20 20,20" 
                         fill="{color}" opacity="0.1"/>
            </pattern>
        ''',
        "zen": f'''
            <pattern id="yinyang" width="80" height="80" patternUnits="userSpaceOnUse">
                <circle cx="40" cy="40" r="35" fill="none" stroke="{color}" stroke-width="0.5" opacity="0.15"/>
                <path d="M40,5 A35,35 0 0,1 40,75 A17.5,17.5 0 0,1 40,40 A17.5,17.5 0 0,0 40,5" 
                      fill="{color}" opacity="0.05"/>
            </pattern>
        ''',
        "personal": f'''
            <pattern id="lines" width="30" height="30" patternUnits="userSpaceOnUse">
                <line x1="0" y1="0" x2="30" y2="30" stroke="{color}" stroke-width="0.3" opacity="0.15"/>
            </pattern>
        ''',
        "tech": f'''
            <pattern id="circuit" width="40" height="40" patternUnits="userSpaceOnUse">
                <path d="M0,20 L15,20 L20,15 L20,0" fill="none" stroke="{color}" stroke-width="0.5" opacity="0.2"/>
                <path d="M40,20 L25,20 L20,25 L20,40" fill="none" stroke="{color}" stroke-width="0.5" opacity="0.2"/>
                <circle cx="20" cy="20" r="3" fill="{color}" opacity="0.15"/>
            </pattern>
        ''',
        "security": f'''
            <pattern id="shield" width="60" height="60" patternUnits="userSpaceOnUse">
                <path d="M30,5 L50,15 L50,35 L30,55 L10,35 L10,15 Z" 
                      fill="none" stroke="{color}" stroke-width="0.5" opacity="0.15"/>
            </pattern>
        '''
    }
    return patterns.get(style, patterns["tech"])

def generate_thumbnail_svg(project):
    """Génère le SVG pour un projet"""
    p = project
    pattern = generate_pattern(p["style"], p["color_primary"])
    pattern_id = {
        "retro": "grid", "mystique": "sacred", "artisan": "wood",
        "creative": "stars", "zen": "yinyang", "personal": "lines",
        "tech": "circuit", "security": "shield"
    }.get(p["style"], "grid")
    
    tags_html = " • ".join(p["tags"][:4])
    
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{THUMBNAIL_WIDTH}" height="{THUMBNAIL_HEIGHT}" viewBox="0 0 {THUMBNAIL_WIDTH} {THUMBNAIL_HEIGHT}" 
     xmlns="http://www.w3.org/2000/svg">
  <defs>
    {pattern}
    <linearGradient id="bg-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{p['color_secondary']};stop-opacity:1" />
      <stop offset="100%" style="stop-color:#000000;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="accent-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:{p['color_primary']};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{p['color_primary']};stop-opacity:0.5" />
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Background -->
  <rect width="100%" height="100%" fill="url(#bg-gradient)"/>
  <rect width="100%" height="100%" fill="url(#{pattern_id})" opacity="0.5"/>
  
  <!-- Accent line top -->
  <rect x="0" y="0" width="100%" height="4" fill="url(#accent-gradient)"/>
  
  <!-- Icon circle -->
  <circle cx="100" cy="{THUMBNAIL_HEIGHT//2}" r="60" fill="{p['color_secondary']}" stroke="{p['color_primary']}" stroke-width="2" opacity="0.8"/>
  <text x="100" y="{THUMBNAIL_HEIGHT//2 + 20}" font-size="50" text-anchor="middle" fill="{p['color_primary']}">{p['icon']}</text>
  
  <!-- Title -->
  <text x="200" y="{THUMBNAIL_HEIGHT//2 - 40}" font-family="monospace" font-size="48" font-weight="bold" fill="{p['color_primary']}" filter="url(#glow)">{p['title']}</text>
  
  <!-- Subtitle -->
  <text x="200" y="{THUMBNAIL_HEIGHT//2 + 10}" font-family="sans-serif" font-size="24" fill="#cccccc">{p['subtitle']}</text>
  
  <!-- Tags -->
  <text x="200" y="{THUMBNAIL_HEIGHT//2 + 50}" font-family="monospace" font-size="14" fill="#888888">{tags_html}</text>
  
  <!-- Year badge -->
  <rect x="{THUMBNAIL_WIDTH - 150}" y="20" width="130" height="36" rx="4" fill="{p['color_primary']}" opacity="0.2"/>
  <rect x="{THUMBNAIL_WIDTH - 150}" y="20" width="130" height="36" rx="4" fill="none" stroke="{p['color_primary']}" stroke-width="1"/>
  <text x="{THUMBNAIL_WIDTH - 85}" y="45" font-family="monospace" font-size="16" text-anchor="middle" fill="{p['color_primary']}">{p['year']}</text>
  
  <!-- Bottom bar -->
  <rect x="0" y="{THUMBNAIL_HEIGHT - 40}" width="100%" height="40" fill="{p['color_secondary']}" opacity="0.8"/>
  <text x="20" y="{THUMBNAIL_HEIGHT - 15}" font-family="monospace" font-size="14" fill="{p['color_primary']}">portfolio.cybermind.fr/{p['id']}</text>
  <text x="{THUMBNAIL_WIDTH - 20}" y="{THUMBNAIL_HEIGHT - 15}" font-family="monospace" font-size="12" text-anchor="end" fill="#666666">ARCHIVED</text>
  
  <!-- Corner accent -->
  <path d="M{THUMBNAIL_WIDTH},0 L{THUMBNAIL_WIDTH},{80} L{THUMBNAIL_WIDTH-80},0 Z" fill="{p['color_primary']}" opacity="0.1"/>
</svg>'''
    
    return svg

def main():
    """Génère toutes les vignettes"""
    output_path = Path(OUTPUT_DIR)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"🎨 Génération des vignettes portfolio...")
    print(f"📁 Dossier de sortie: {OUTPUT_DIR}")
    print()
    
    for project in PROJECTS:
        svg_content = generate_thumbnail_svg(project)
        filename = f"{project['id']}.svg"
        filepath = output_path / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        print(f"  ✅ {project['icon']} {project['title']:20} → {filename}")
    
    print()
    print(f"✨ {len(PROJECTS)} vignettes générées!")
    print()
    print("Pour utiliser dans le portfolio, référencez:")
    print(f"  thumbnail: /images/portfolio/thumbnails/[id].svg")

if __name__ == "__main__":
    main()
