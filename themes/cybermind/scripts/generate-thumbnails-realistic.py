#!/usr/bin/env python3
"""
Générateur de vignettes portfolio avec previews réalistes des sites
Crée des SVG avec des maquettes fidèles au design original des sites
"""

import os
from pathlib import Path

OUTPUT_DIR = "examples/images/portfolio/thumbnails"

# Données des projets avec leur design réel
PROJECTS = [
    {
        "id": "gk2-net",
        "title": "GK2.NET",
        "subtitle": "Premier ISP Personnel",
        "icon": "🌐",
        "year": "1996-2001",
        "color_primary": "#00ff88",
        "color_bg": "#003322",
        "archive_url": "web.archive.org/web/2001/gk2.com",
        # Design du site réel: style années 90, frames, fond sombre
        "preview_html": """
            <div style="background:#1a1a2e;width:100%;height:100%;font-family:Courier,monospace;padding:8px;box-sizing:border-box">
                <div style="background:#000033;border:2px solid #00ff88;padding:4px;margin-bottom:4px">
                    <span style="color:#00ff88;font-size:16px;font-weight:bold">★ GK2.NET ★</span>
                </div>
                <div style="display:flex;gap:4px;height:calc(100% - 40px)">
                    <div style="background:#000020;border:1px solid #004400;width:60px;padding:4px">
                        <div style="color:#00ff88;font-size:6px;margin:2px 0">• Home</div>
                        <div style="color:#00ff88;font-size:6px;margin:2px 0">• Services</div>
                        <div style="color:#00ff88;font-size:6px;margin:2px 0">• Email</div>
                        <div style="color:#00ff88;font-size:6px;margin:2px 0">• FTP</div>
                        <div style="color:#00ff88;font-size:6px;margin:2px 0">• Web</div>
                    </div>
                    <div style="flex:1;background:#000015;border:1px solid #003300;padding:6px">
                        <div style="color:#ffff00;font-size:8px;text-align:center">Welcome to GK2.NET</div>
                        <div style="color:#888;font-size:5px;margin-top:4px">Your Personal ISP since 1996</div>
                        <div style="color:#00ff88;font-size:5px;margin-top:6px">━━━━━━━━━━━━━━━━━</div>
                        <div style="color:#aaa;font-size:5px;margin-top:4px">RedHat Linux Server</div>
                        <div style="color:#aaa;font-size:5px">Pentium Pro 200MHz</div>
                    </div>
                </div>
            </div>
        """
    },
    {
        "id": "ganimed",
        "title": "GANIMED",
        "subtitle": "Haute Magie & Géométrie Sacrée",
        "icon": "🔮",
        "year": "2015-2024",
        "color_primary": "#9966ff",
        "color_bg": "#1a0033",
        "archive_url": "web.archive.org/web/2024/ganimed.fr",
        # Design réel: WordPress sombre, géométrie sacrée
        "preview_html": """
            <div style="background:linear-gradient(180deg,#1a0a2e 0%,#0d0015 100%);width:100%;height:100%;font-family:Georgia,serif;overflow:hidden">
                <div style="background:rgba(153,102,255,0.1);padding:6px 8px;border-bottom:1px solid #9966ff33">
                    <span style="color:#9966ff;font-size:11px;font-weight:bold;letter-spacing:2px">GANIMED</span>
                    <span style="color:#666;font-size:6px;margin-left:8px">Haute Magie</span>
                </div>
                <div style="padding:8px;text-align:center">
                    <div style="width:50px;height:50px;margin:0 auto;border:1px solid #9966ff44;border-radius:50%;display:flex;align-items:center;justify-content:center">
                        <div style="width:30px;height:30px;border:1px solid #9966ff66;border-radius:50%;display:flex;align-items:center;justify-content:center">
                            <div style="color:#9966ff;font-size:10px">✡</div>
                        </div>
                    </div>
                    <div style="color:#9966ff;font-size:7px;margin-top:6px;letter-spacing:1px">GÉOMÉTRIE SACRÉE</div>
                    <div style="color:#666;font-size:5px;margin-top:2px">Cymatics • Hermétisme • Alchimie</div>
                </div>
                <div style="position:absolute;bottom:6px;left:8px;right:8px;display:flex;justify-content:space-around">
                    <span style="color:#9966ff44;font-size:5px">▲</span>
                    <span style="color:#9966ff44;font-size:5px">◆</span>
                    <span style="color:#9966ff44;font-size:5px">●</span>
                    <span style="color:#9966ff44;font-size:5px">◆</span>
                    <span style="color:#9966ff44;font-size:5px">▲</span>
                </div>
            </div>
        """
    },
    {
        "id": "icieb",
        "title": "ICIEB",
        "subtitle": "Gravure Laser & Géométrie Sacrée",
        "icon": "🌸",
        "year": "2018-2021",
        "color_primary": "#ff6699",
        "color_bg": "#330011",
        "archive_url": "web.archive.org/web/2021/icieb.fr",
        # Design réel: PrestaShop boutique, produits bois
        "preview_html": """
            <div style="background:#ffffff;width:100%;height:100%;font-family:Arial,sans-serif;overflow:hidden">
                <div style="background:#2a2a2a;padding:4px 8px;display:flex;justify-content:space-between;align-items:center">
                    <span style="color:#ff6699;font-size:10px;font-weight:bold">ICIEB</span>
                    <span style="color:#888;font-size:5px">🛒 Panier</span>
                </div>
                <div style="background:#f5f5f5;padding:4px 8px;border-bottom:1px solid #ddd">
                    <span style="color:#333;font-size:5px">Accueil</span>
                    <span style="color:#999;font-size:5px;margin:0 4px">›</span>
                    <span style="color:#ff6699;font-size:5px">Boutique</span>
                </div>
                <div style="padding:6px;display:flex;gap:4px">
                    <div style="background:#f9f9f9;border:1px solid #eee;width:45%;padding:4px;text-align:center">
                        <div style="background:#d4a574;height:35px;border-radius:2px;display:flex;align-items:center;justify-content:center">
                            <span style="color:#fff;font-size:14px">✿</span>
                        </div>
                        <div style="color:#333;font-size:5px;margin-top:3px">Fleur de Vie</div>
                        <div style="color:#ff6699;font-size:6px;font-weight:bold">29,90€</div>
                    </div>
                    <div style="background:#f9f9f9;border:1px solid #eee;width:45%;padding:4px;text-align:center">
                        <div style="background:#8b7355;height:35px;border-radius:2px;display:flex;align-items:center;justify-content:center">
                            <span style="color:#fff;font-size:12px">◎</span>
                        </div>
                        <div style="color:#333;font-size:5px;margin-top:3px">Crop Circle</div>
                        <div style="color:#ff6699;font-size:6px;font-weight:bold">34,90€</div>
                    </div>
                </div>
            </div>
        """
    },
    {
        "id": "kragzouy-blog",
        "title": "Kragzouy",
        "subtitle": "Univers Créatif depuis 1982",
        "icon": "🧙",
        "year": "1982-présent",
        "color_primary": "#ffcc00",
        "color_bg": "#332200",
        "archive_url": "kragzouy.blogspot.com",
        # Design réel: Blogspot, créatif, poésie
        "preview_html": """
            <div style="background:#1a1a1a;width:100%;height:100%;font-family:Georgia,serif;overflow:hidden">
                <div style="background:linear-gradient(90deg,#ffcc00,#ff9900);padding:6px 8px">
                    <span style="color:#000;font-size:12px;font-weight:bold;text-shadow:1px 1px 0 #fff3">Kragzouy</span>
                </div>
                <div style="padding:8px">
                    <div style="color:#ffcc00;font-size:7px;font-style:italic;border-left:2px solid #ffcc00;padding-left:6px">
                        "Dans l'ombre des mots,<br/>la lumière danse..."
                    </div>
                    <div style="margin-top:8px;padding-top:6px;border-top:1px solid #333">
                        <div style="color:#888;font-size:5px">📅 Dernier article</div>
                        <div style="color:#ccc;font-size:6px;margin-top:2px">Poésie & Musique</div>
                    </div>
                    <div style="margin-top:6px;display:flex;gap:4px">
                        <span style="background:#ffcc0022;color:#ffcc00;font-size:4px;padding:1px 3px;border-radius:2px">Yi Jing</span>
                        <span style="background:#ffcc0022;color:#ffcc00;font-size:4px;padding:1px 3px;border-radius:2px">Poésie</span>
                        <span style="background:#ffcc0022;color:#ffcc00;font-size:4px;padding:1px 3px;border-radius:2px">Musique</span>
                    </div>
                </div>
            </div>
        """
    },
    {
        "id": "wengu-yijing",
        "title": "Wengu Yi Jing",
        "subtitle": "Ressources Classiques",
        "icon": "☯️",
        "year": "2000-2025",
        "color_primary": "#ffffff",
        "color_bg": "#111111",
        "archive_url": "wengu.tartarie.com",
        # Design réel: site classique Yi Jing, minimaliste
        "preview_html": """
            <div style="background:#f5f5f0;width:100%;height:100%;font-family:'Times New Roman',serif;overflow:hidden">
                <div style="background:#222;padding:4px 8px;text-align:center">
                    <span style="color:#fff;font-size:9px">文 古 · Wengu</span>
                </div>
                <div style="padding:6px;text-align:center">
                    <div style="font-size:28px;color:#333;line-height:1">☯</div>
                    <div style="color:#666;font-size:8px;margin-top:4px;font-style:italic">易 經</div>
                    <div style="color:#333;font-size:6px;margin-top:2px">Le Classique des Changements</div>
                </div>
                <div style="padding:0 8px;display:flex;justify-content:center;gap:3px;flex-wrap:wrap">
                    <span style="color:#000;font-size:7px">䷀</span>
                    <span style="color:#000;font-size:7px">䷁</span>
                    <span style="color:#000;font-size:7px">䷂</span>
                    <span style="color:#000;font-size:7px">䷃</span>
                    <span style="color:#000;font-size:7px">䷄</span>
                    <span style="color:#000;font-size:7px">䷅</span>
                    <span style="color:#000;font-size:7px">䷆</span>
                    <span style="color:#000;font-size:7px">䷇</span>
                </div>
                <div style="margin-top:6px;padding:4px;background:#eee;text-align:center">
                    <span style="color:#666;font-size:5px">64 Hexagrammes • Textes classiques</span>
                </div>
            </div>
        """
    },
    {
        "id": "michel-murty",
        "title": "Michel Murty",
        "subtitle": "Site Personnel",
        "icon": "👤",
        "year": "2000-présent",
        "color_primary": "#66ccff",
        "color_bg": "#002233",
        "archive_url": "michelmurty.free.fr",
        # Design réel: site Free.fr classique
        "preview_html": """
            <div style="background:#e8e8e8;width:100%;height:100%;font-family:Verdana,sans-serif;overflow:hidden">
                <div style="background:linear-gradient(180deg,#4080c0,#2060a0);padding:6px 8px">
                    <span style="color:#fff;font-size:10px;font-weight:bold">Michel Murty</span>
                </div>
                <div style="background:#fff;margin:6px;padding:6px;border:1px solid #ccc">
                    <div style="color:#333;font-size:7px;font-weight:bold">Bienvenue</div>
                    <div style="color:#666;font-size:5px;margin-top:4px;line-height:1.4">
                        Page personnelle hébergée sur Free.fr
                    </div>
                    <div style="margin-top:6px;padding-top:4px;border-top:1px dashed #ccc">
                        <div style="color:#0066cc;font-size:5px;text-decoration:underline">→ Galerie photos</div>
                        <div style="color:#0066cc;font-size:5px;text-decoration:underline;margin-top:2px">→ Contact</div>
                    </div>
                </div>
                <div style="text-align:center;margin-top:4px">
                    <span style="color:#999;font-size:4px">Hébergé par Free</span>
                </div>
            </div>
        """
    },
    {
        "id": "armbian-wui",
        "title": "Armbian WUI",
        "subtitle": "Interface Web Armbian",
        "icon": "🖥️",
        "year": "2022",
        "color_primary": "#ff6600",
        "color_bg": "#331100",
        "archive_url": None,
        # Design: Interface d'administration Linux
        "preview_html": """
            <div style="background:#1e1e1e;width:100%;height:100%;font-family:'Courier New',monospace;overflow:hidden">
                <div style="background:#2d2d2d;padding:4px 8px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #ff660044">
                    <span style="color:#ff6600;font-size:8px;font-weight:bold">⬢ Armbian</span>
                    <span style="color:#888;font-size:5px">admin@armbian</span>
                </div>
                <div style="display:flex;height:calc(100% - 24px)">
                    <div style="background:#252525;width:50px;padding:4px;border-right:1px solid #333">
                        <div style="color:#ff6600;font-size:5px;padding:2px 0">📊 System</div>
                        <div style="color:#888;font-size:5px;padding:2px 0">🌐 Network</div>
                        <div style="color:#888;font-size:5px;padding:2px 0">💾 Storage</div>
                        <div style="color:#888;font-size:5px;padding:2px 0">⚙️ Config</div>
                    </div>
                    <div style="flex:1;padding:6px">
                        <div style="color:#0f0;font-size:5px">● CPU: 12% | RAM: 45%</div>
                        <div style="background:#333;height:4px;margin:4px 0;border-radius:2px">
                            <div style="background:#ff6600;height:100%;width:45%;border-radius:2px"></div>
                        </div>
                        <div style="color:#888;font-size:5px;margin-top:4px">Uptime: 14d 3h 22m</div>
                        <div style="color:#ff6600;font-size:5px;margin-top:2px">armbian 24.2 • kernel 6.1</div>
                    </div>
                </div>
            </div>
        """
    },
    {
        "id": "enigmasuite",
        "title": "EnigmaSuite",
        "subtitle": "Outils Sécurité Réseau",
        "icon": "🔐",
        "year": "2023",
        "color_primary": "#00ffcc",
        "color_bg": "#003333",
        "archive_url": None,
        # Design: Dashboard sécurité
        "preview_html": """
            <div style="background:#0a1a1a;width:100%;height:100%;font-family:'Segoe UI',sans-serif;overflow:hidden">
                <div style="background:linear-gradient(90deg,#00ffcc22,transparent);padding:4px 8px;border-bottom:1px solid #00ffcc33">
                    <span style="color:#00ffcc;font-size:9px;font-weight:bold">🛡️ EnigmaSuite</span>
                </div>
                <div style="padding:6px">
                    <div style="display:flex;gap:4px;margin-bottom:6px">
                        <div style="background:#00ffcc11;border:1px solid #00ffcc33;flex:1;padding:4px;text-align:center;border-radius:3px">
                            <div style="color:#00ffcc;font-size:10px">247</div>
                            <div style="color:#666;font-size:4px">Blocked</div>
                        </div>
                        <div style="background:#00ffcc11;border:1px solid #00ffcc33;flex:1;padding:4px;text-align:center;border-radius:3px">
                            <div style="color:#0f0;font-size:10px">●</div>
                            <div style="color:#666;font-size:4px">Protected</div>
                        </div>
                    </div>
                    <div style="background:#0f1f1f;padding:4px;border-radius:3px;border:1px solid #00ffcc22">
                        <div style="color:#00ffcc;font-size:5px;opacity:0.7">Recent Activity</div>
                        <div style="color:#888;font-size:4px;margin-top:2px">✓ CrowdSec sync OK</div>
                        <div style="color:#888;font-size:4px">✓ Firewall rules: 42</div>
                        <div style="color:#888;font-size:4px">✓ Last scan: 2m ago</div>
                    </div>
                </div>
            </div>
        """
    }
]


def html_to_svg_foreignobject(html, x, y, width, height):
    """Convertit le HTML en foreignObject SVG"""
    # Nettoyer le HTML pour l'intégration SVG
    clean_html = html.strip().replace('\n', '').replace('  ', '')
    return f'''
    <foreignObject x="{x}" y="{y}" width="{width}" height="{height}">
        <div xmlns="http://www.w3.org/1999/xhtml" style="width:100%;height:100%;overflow:hidden;border-radius:6px;">
            {clean_html}
        </div>
    </foreignObject>
    '''


def generate_realistic_thumbnail(project):
    """Génère une vignette avec preview HTML réaliste"""
    p = project
    
    # Dimensions
    W, H = 800, 450
    preview_x, preview_y = 420, 60
    preview_w, preview_h = 360, 280
    
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" 
     xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <linearGradient id="bg-{p['id']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{p['color_bg']}"/>
      <stop offset="100%" stop-color="#000"/>
    </linearGradient>
    <linearGradient id="accent-{p['id']}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{p['color_primary']}"/>
      <stop offset="100%" stop-color="{p['color_primary']}" stop-opacity="0.2"/>
    </linearGradient>
    <filter id="shadow-{p['id']}">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000" flood-opacity="0.5"/>
    </filter>
    <filter id="glow-{p['id']}">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="preview-clip-{p['id']}">
      <rect x="{preview_x}" y="{preview_y}" width="{preview_w}" height="{preview_h}" rx="8"/>
    </clipPath>
    <style>
      @keyframes pulse {{ 0%,100% {{ opacity:0.8 }} 50% {{ opacity:1 }} }}
      @keyframes scan {{ 0% {{ transform:translateY(0) }} 100% {{ transform:translateY({H}px) }} }}
    </style>
  </defs>
  
  <!-- Background -->
  <rect width="100%" height="100%" fill="url(#bg-{p['id']})"/>
  
  <!-- Grid pattern -->
  <pattern id="grid-{p['id']}" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0L0 0 0 40" fill="none" stroke="{p['color_primary']}" stroke-width="0.3" opacity="0.15"/>
  </pattern>
  <rect width="100%" height="100%" fill="url(#grid-{p['id']})"/>
  
  <!-- Top accent bar -->
  <rect x="0" y="0" width="100%" height="4" fill="url(#accent-{p['id']})"/>
  
  <!-- Scan line animation -->
  <rect x="0" y="0" width="100%" height="2" fill="{p['color_primary']}" opacity="0.08">
    <animate attributeName="y" values="0;{H};0" dur="4s" repeatCount="indefinite"/>
  </rect>
  
  <!-- Left side: Info -->
  <g>
    <!-- Icon -->
    <circle cx="70" cy="140" r="45" fill="{p['color_bg']}" stroke="{p['color_primary']}" stroke-width="2" opacity="0.9" style="animation:pulse 3s infinite"/>
    <text x="70" y="155" font-size="36" text-anchor="middle" fill="{p['color_primary']}">{p['icon']}</text>
    
    <!-- Title -->
    <text x="30" y="240" font-family="'JetBrains Mono',monospace" font-size="32" font-weight="bold" 
          fill="{p['color_primary']}" filter="url(#glow-{p['id']})">{p['title']}</text>
    
    <!-- Subtitle -->
    <text x="30" y="275" font-family="system-ui,sans-serif" font-size="14" fill="#999">{p['subtitle']}</text>
    
    <!-- Archive URL -->
    <text x="30" y="310" font-family="monospace" font-size="10" fill="#555">{p.get('archive_url', 'Local project')}</text>
  </g>
  
  <!-- Right side: Live Preview -->
  <g filter="url(#shadow-{p['id']})">
    <!-- Browser chrome -->
    <rect x="{preview_x-2}" y="{preview_y-24}" width="{preview_w+4}" height="{preview_h+28}" rx="10" 
          fill="#1a1a1a" stroke="{p['color_primary']}" stroke-width="1" opacity="0.9"/>
    
    <!-- Browser header -->
    <circle cx="{preview_x+12}" cy="{preview_y-12}" r="4" fill="#ff5f56"/>
    <circle cx="{preview_x+26}" cy="{preview_y-12}" r="4" fill="#ffbd2e"/>
    <circle cx="{preview_x+40}" cy="{preview_y-12}" r="4" fill="#27ca3f"/>
    
    <!-- URL bar -->
    <rect x="{preview_x+55}" y="{preview_y-18}" width="{preview_w-70}" height="14" rx="3" fill="#2a2a2a"/>
    <text x="{preview_x+62}" y="{preview_y-8}" font-family="monospace" font-size="7" fill="#666">
      {(p.get('archive_url') or p['id']+'.local')[:40]}
    </text>
    
    <!-- Preview content (foreignObject with HTML) -->
    <g clip-path="url(#preview-clip-{p['id']})">
      {html_to_svg_foreignobject(p['preview_html'], preview_x, preview_y, preview_w, preview_h)}
    </g>
    
    <!-- Corner decorations -->
    <path d="M{preview_x},{preview_y+12} L{preview_x},{preview_y} L{preview_x+12},{preview_y}" fill="none" stroke="{p['color_primary']}" stroke-width="2" opacity="0.5"/>
    <path d="M{preview_x+preview_w-12},{preview_y} L{preview_x+preview_w},{preview_y} L{preview_x+preview_w},{preview_y+12}" fill="none" stroke="{p['color_primary']}" stroke-width="2" opacity="0.5"/>
    <path d="M{preview_x},{preview_y+preview_h-12} L{preview_x},{preview_y+preview_h} L{preview_x+12},{preview_y+preview_h}" fill="none" stroke="{p['color_primary']}" stroke-width="2" opacity="0.5"/>
    <path d="M{preview_x+preview_w-12},{preview_y+preview_h} L{preview_x+preview_w},{preview_y+preview_h} L{preview_x+preview_w},{preview_y+preview_h-12}" fill="none" stroke="{p['color_primary']}" stroke-width="2" opacity="0.5"/>
  </g>
  
  <!-- Year badge -->
  <rect x="{W-130}" y="15" width="115" height="28" rx="4" fill="{p['color_primary']}" opacity="0.15"/>
  <rect x="{W-130}" y="15" width="115" height="28" rx="4" fill="none" stroke="{p['color_primary']}" stroke-width="1" opacity="0.5"/>
  <text x="{W-72}" y="35" font-family="monospace" font-size="12" text-anchor="middle" fill="{p['color_primary']}">{p['year']}</text>
  
  <!-- Bottom bar -->
  <rect x="0" y="{H-38}" width="100%" height="38" fill="#0a0a0a" opacity="0.95"/>
  <line x1="0" y1="{H-38}" x2="100%" y2="{H-38}" stroke="{p['color_primary']}" stroke-width="1" opacity="0.3"/>
  <text x="15" y="{H-14}" font-family="monospace" font-size="11" fill="{p['color_primary']}" opacity="0.8">cybermind.fr/portfolio/{p['id']}</text>
  
  <!-- Live indicator -->
  <circle cx="{W-30}" cy="{H-19}" r="5" fill="{p['color_primary']}" opacity="0.9">
    <animate attributeName="opacity" values="0.9;0.4;0.9" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="{W-50}" y="{H-14}" font-family="monospace" font-size="9" text-anchor="end" fill="#666">PREVIEW</text>
  
  <!-- Corner accent -->
  <path d="M{W},0 L{W},50 L{W-50},0 Z" fill="{p['color_primary']}" opacity="0.06"/>
</svg>'''
    
    return svg


def main():
    output_path = Path(OUTPUT_DIR)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print("🎬 Génération des vignettes avec previews réalistes...")
    print(f"📁 Dossier: {OUTPUT_DIR}")
    print()
    
    for project in PROJECTS:
        svg = generate_realistic_thumbnail(project)
        filename = f"{project['id']}.svg"
        filepath = output_path / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg)
        
        print(f"  ✅ {project['icon']} {project['title']:20} → {filename}")
    
    print()
    print(f"✨ {len(PROJECTS)} vignettes avec previews réalistes générées!")


if __name__ == "__main__":
    main()
