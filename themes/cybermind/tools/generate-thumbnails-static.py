#!/usr/bin/env python3
"""
Générateur de vignettes portfolio STATIQUES
Sans animations - Rendu professionnel type capture d'écran
À exécuter manuellement : python3 tools/generate-thumbnails-static.py
"""

from pathlib import Path

OUTPUT_DIR = "examples/images/portfolio/thumbnails"

PROJECTS = [
    {
        "id": "tresse-lemniscate",
        "title": "Tresse × Lemniscate",
        "subtitle": "Fusion A000940 • Géométrie Générative",
        "color": "#00F6FF",
        "bg": "#0A0E14",
        "url": "cybermind.fr/apps/tresse-lemniscate",
        "content": [
            ("app_header", "∞ Tresse × Lemniscate — Fusion A000940"),
            ("quote", "L'intelligence n'est pas un sommet, mais une trame."),
            ("divider", ""),
            ("lemniscate", "∞"),
            ("controls", [("n", "12"), ("Depth", "0.35"), ("Speed", "0.5")]),
            ("palette_preview", ["#B87333", "#C0C0C0", "#FFD700"]),
            ("buttons", ["Start", "Reset", "Export PNG"]),
            ("version", "v1.0 · PWA · © CyberMind Studio"),
        ]
    },
    {
        "id": "gk2-net",
        "title": "GK2.NET",
        "subtitle": "Premier ISP Personnel • 1996",
        "color": "#00ff88",
        "bg": "#0a1a10",
        "url": "gk2.com",
        "content": [
            ("header", "★ GK2.NET - Internet Service Provider ★"),
            ("menu", ["Home", "Services", "Email", "FTP", "Support"]),
            ("text", "Welcome to GK2.NET"),
            ("text", "Your Personal ISP since 1996"),
            ("divider", ""),
            ("info", "Server: Pentium Pro 200MHz"),
            ("info", "OS: RedHat Linux 5.2"),
            ("info", "Services: Web, Mail, FTP, Shell"),
            ("counter", "Visitors: 12,847"),
        ]
    },
    {
        "id": "ganimed",
        "title": "GANIMED",
        "subtitle": "Haute Magie & Géométrie Sacrée • 2015-2024",
        "color": "#9966ff",
        "bg": "#0d0015",
        "url": "ganimed.fr",
        "content": [
            ("logo", "✡ GANIMED"),
            ("tagline", "Haute Magie • Géométrie Sacrée"),
            ("divider", ""),
            ("sacred", "◯"),
            ("menu", ["Accueil", "Cymatics", "Hermétisme", "Alchimie", "666"]),
            ("text", "Exploration des mystères de la géométrie sacrée"),
            ("social", ["Facebook: Ganimance", "Pinterest: ANIELSAN"]),
        ]
    },
    {
        "id": "icieb",
        "title": "ICIEB",
        "subtitle": "Boutique Gravure Laser • 2018-2021",
        "color": "#ff6699",
        "bg": "#1a0a10",
        "url": "icieb.fr",
        "content": [
            ("shop_header", "ICIEB - Boutique"),
            ("breadcrumb", "Accueil > Gravure Laser > Géométrie"),
            ("products", [
                ("Fleur de Vie", "29,90€", "✿"),
                ("Crop Circle", "34,90€", "◎"),
                ("Métatron", "39,90€", "✡"),
            ]),
            ("info", "Gravure laser haute précision sur bois"),
            ("info", "Fait main • Pièces uniques"),
        ]
    },
    {
        "id": "kragzouy-blog",
        "title": "Kragzouy",
        "subtitle": "Univers Créatif • 1982-présent",
        "color": "#ffcc00",
        "bg": "#1a1505",
        "url": "kragzouy.blogspot.com",
        "content": [
            ("blog_header", "✦ Kragzouy ✦"),
            ("quote", "Dans l'ombre des mots, la lumière danse..."),
            ("divider", ""),
            ("post", "Dernière publication"),
            ("post_title", "Poésie & Musique Suno"),
            ("tags", ["Yi Jing", "Poésie", "Musique", "Philosophie"]),
            ("date", "Décembre 2025"),
        ]
    },
    {
        "id": "wengu-yijing",
        "title": "Wengu Yi Jing",
        "subtitle": "Ressources Classiques • 2000-2025",
        "color": "#e0e0e0",
        "bg": "#0a0a0a",
        "url": "wengu.tartarie.com",
        "content": [
            ("classic_header", "文古 Wengu"),
            ("yijing_symbol", "☯"),
            ("chinese", "易 經"),
            ("text", "Le Classique des Changements"),
            ("hexagrams", "䷀ ䷁ ䷂ ䷃ ䷄ ䷅ ䷆ ䷇"),
            ("info", "64 Hexagrammes • Textes classiques"),
            ("info", "Traductions & Commentaires"),
        ]
    },
    {
        "id": "michel-murty",
        "title": "Michel Murty",
        "subtitle": "Site Personnel • 2000-présent",
        "color": "#66ccff",
        "bg": "#051520",
        "url": "michelmurty.free.fr",
        "content": [
            ("free_header", "Michel Murty"),
            ("welcome", "Bienvenue sur ma page personnelle"),
            ("divider", ""),
            ("link", "→ Galerie photos"),
            ("link", "→ Mes projets"),
            ("link", "→ Contact"),
            ("hosted", "Hébergé par Free.fr"),
        ]
    },
    {
        "id": "armbian-wui",
        "title": "Armbian WUI",
        "subtitle": "Interface Web Admin • 2022",
        "color": "#ff6600",
        "bg": "#0f0a05",
        "url": "armbian.local",
        "content": [
            ("admin_header", "⬢ Armbian Config"),
            ("stats", [("CPU", "12%"), ("RAM", "45%"), ("Disk", "23%")]),
            ("menu", ["System", "Network", "Storage", "Users"]),
            ("terminal", "root@armbian:~# uptime"),
            ("output", "14 days, 3:22, load: 0.12"),
            ("version", "Armbian 24.2 • Kernel 6.1"),
        ]
    },
    {
        "id": "enigmasuite",
        "title": "EnigmaSuite",
        "subtitle": "Sécurité Réseau • 2023",
        "color": "#00ffcc",
        "bg": "#050f0f",
        "url": "enigma.local",
        "content": [
            ("security_header", "🛡️ EnigmaSuite"),
            ("status", "Protected"),
            ("counters", [("Blocked", "247"), ("Rules", "42"), ("Alerts", "3")]),
            ("log", "✓ CrowdSec sync OK"),
            ("log", "✓ Firewall active"),
            ("log", "✓ Last scan: 2m ago"),
            ("version", "v2.1.0 • OpenWrt"),
        ]
    }
]


def render_content_to_svg(content, color, x_start, y_start, width):
    """Convertit le contenu en éléments SVG"""
    elements = []
    y = y_start
    
    for item in content:
        item_type = item[0]
        data = item[1] if len(item) > 1 else ""
        
        if item_type == "header":
            elements.append(f'<text x="{x_start + width//2}" y="{y}" font-family="monospace" font-size="11" text-anchor="middle" fill="{color}" font-weight="bold">{data}</text>')
            y += 18
            
        elif item_type == "logo":
            elements.append(f'<text x="{x_start + width//2}" y="{y}" font-family="serif" font-size="14" text-anchor="middle" fill="{color}" font-weight="bold">{data}</text>')
            y += 20
            
        elif item_type == "tagline":
            elements.append(f'<text x="{x_start + width//2}" y="{y}" font-family="serif" font-size="8" text-anchor="middle" fill="#888">{data}</text>')
            y += 14
            
        elif item_type == "menu":
            menu_text = " | ".join(data)
            elements.append(f'<text x="{x_start + width//2}" y="{y}" font-family="sans-serif" font-size="7" text-anchor="middle" fill="#666">{menu_text}</text>')
            y += 14
            
        elif item_type == "text":
            elements.append(f'<text x="{x_start + 10}" y="{y}" font-family="sans-serif" font-size="9" fill="#ccc">{data}</text>')
            y += 14
            
        elif item_type == "info":
            elements.append(f'<text x="{x_start + 10}" y="{y}" font-family="monospace" font-size="7" fill="#888">{data}</text>')
            y += 12
            
        elif item_type == "divider":
            elements.append(f'<line x1="{x_start + 10}" y1="{y}" x2="{x_start + width - 10}" y2="{y}" stroke="{color}" stroke-width="0.5" opacity="0.3"/>')
            y += 10
            
        elif item_type == "counter":
            elements.append(f'<text x="{x_start + 10}" y="{y}" font-family="monospace" font-size="8" fill="{color}">{data}</text>')
            y += 14
            
        elif item_type == "sacred":
            elements.append(f'<text x="{x_start + width//2}" y="{y + 15}" font-size="40" text-anchor="middle" fill="{color}" opacity="0.3">{data}</text>')
            y += 50
            
        elif item_type == "yijing_symbol":
            elements.append(f'<text x="{x_start + width//2}" y="{y + 20}" font-size="45" text-anchor="middle" fill="#888">{data}</text>')
            y += 55
            
        elif item_type == "chinese":
            elements.append(f'<text x="{x_start + width//2}" y="{y}" font-family="serif" font-size="12" text-anchor="middle" fill="{color}">{data}</text>')
            y += 18
            
        elif item_type == "hexagrams":
            elements.append(f'<text x="{x_start + width//2}" y="{y}" font-size="14" text-anchor="middle" fill="#666">{data}</text>')
            y += 20
            
        elif item_type == "quote":
            elements.append(f'<text x="{x_start + 15}" y="{y}" font-family="serif" font-size="8" font-style="italic" fill="{color}">"{data}"</text>')
            y += 16
            
        elif item_type == "tags":
            tags_x = x_start + 10
            for tag in data:
                elements.append(f'<rect x="{tags_x}" y="{y - 8}" width="{len(tag) * 5 + 8}" height="12" rx="2" fill="{color}" opacity="0.15"/>')
                elements.append(f'<text x="{tags_x + 4}" y="{y}" font-family="monospace" font-size="6" fill="{color}">{tag}</text>')
                tags_x += len(tag) * 5 + 14
            y += 18
            
        elif item_type == "products":
            for name, price, icon in data:
                elements.append(f'<rect x="{x_start + 10}" y="{y - 10}" width="70" height="50" rx="3" fill="#1a1a1a" stroke="#333" stroke-width="0.5"/>')
                elements.append(f'<text x="{x_start + 45}" y="{y + 10}" font-size="18" text-anchor="middle" fill="{color}">{icon}</text>')
                elements.append(f'<text x="{x_start + 45}" y="{y + 28}" font-family="sans-serif" font-size="6" text-anchor="middle" fill="#ccc">{name}</text>')
                elements.append(f'<text x="{x_start + 45}" y="{y + 38}" font-family="monospace" font-size="7" text-anchor="middle" fill="{color}" font-weight="bold">{price}</text>')
                x_start_temp = x_start
                x_start += 80
            x_start = x_start_temp
            y += 55
            
        elif item_type == "stats":
            stats_x = x_start + 10
            for label, value in data:
                elements.append(f'<rect x="{stats_x}" y="{y - 8}" width="50" height="25" rx="3" fill="#1a1a1a" stroke="#333" stroke-width="0.5"/>')
                elements.append(f'<text x="{stats_x + 25}" y="{y + 2}" font-family="monospace" font-size="9" text-anchor="middle" fill="{color}">{value}</text>')
                elements.append(f'<text x="{stats_x + 25}" y="{y + 12}" font-family="sans-serif" font-size="5" text-anchor="middle" fill="#666">{label}</text>')
                stats_x += 55
            y += 30
            
        elif item_type == "counters":
            stats_x = x_start + 10
            for label, value in data:
                elements.append(f'<rect x="{stats_x}" y="{y - 8}" width="50" height="30" rx="3" fill="{color}" opacity="0.1" stroke="{color}" stroke-width="0.5" opacity="0.3"/>')
                elements.append(f'<text x="{stats_x + 25}" y="{y + 5}" font-family="monospace" font-size="11" text-anchor="middle" fill="{color}">{value}</text>')
                elements.append(f'<text x="{stats_x + 25}" y="{y + 16}" font-family="sans-serif" font-size="5" text-anchor="middle" fill="#666">{label}</text>')
                stats_x += 55
            y += 35
            
        elif item_type == "terminal":
            elements.append(f'<text x="{x_start + 10}" y="{y}" font-family="monospace" font-size="7" fill="#0f0">{data}</text>')
            y += 12
            
        elif item_type == "output":
            elements.append(f'<text x="{x_start + 10}" y="{y}" font-family="monospace" font-size="7" fill="#888">{data}</text>')
            y += 12
            
        elif item_type == "log":
            elements.append(f'<text x="{x_start + 10}" y="{y}" font-family="monospace" font-size="7" fill="#888">{data}</text>')
            y += 11
            
        elif item_type in ["version", "hosted", "date"]:
            elements.append(f'<text x="{x_start + 10}" y="{y}" font-family="monospace" font-size="6" fill="#555">{data}</text>')
            y += 12
            
        elif item_type == "link":
            elements.append(f'<text x="{x_start + 10}" y="{y}" font-family="sans-serif" font-size="8" fill="#66ccff" text-decoration="underline">{data}</text>')
            y += 14
            
        elif item_type == "app_header":
            elements.append(f'<rect x="{x_start}" y="{y - 12}" width="{width}" height="20" fill="{color}" opacity="0.1"/>')
            elements.append(f'<text x="{x_start + width//2}" y="{y + 2}" font-family="Orbitron,monospace" font-size="9" text-anchor="middle" fill="{color}" font-weight="bold">{data}</text>')
            y += 24
            
        elif item_type == "lemniscate":
            elements.append(f'<text x="{x_start + width//2}" y="{y + 30}" font-size="60" text-anchor="middle" fill="{color}" opacity="0.4">{data}</text>')
            y += 70
            
        elif item_type == "controls":
            ctrl_x = x_start + 10
            for label, value in data:
                elements.append(f'<rect x="{ctrl_x}" y="{y - 8}" width="55" height="22" rx="4" fill="#0D1420" stroke="#2A3240" stroke-width="0.5"/>')
                elements.append(f'<text x="{ctrl_x + 5}" y="{y}" font-family="monospace" font-size="6" fill="#9AA4AE">{label}</text>')
                elements.append(f'<text x="{ctrl_x + 5}" y="{y + 10}" font-family="monospace" font-size="8" fill="{color}">{value}</text>')
                ctrl_x += 60
            y += 28
            
        elif item_type == "palette_preview":
            pal_x = x_start + 10
            for i, col in enumerate(data):
                elements.append(f'<rect x="{pal_x}" y="{y - 5}" width="40" height="12" rx="2" fill="{col}"/>')
                pal_x += 45
            y += 18
            
        elif item_type == "buttons":
            btn_x = x_start + 10
            for btn in data:
                btn_w = len(btn) * 6 + 12
                is_primary = btn == "Start" or btn == "Export PNG"
                stroke = color if is_primary else "#2A3240"
                elements.append(f'<rect x="{btn_x}" y="{y - 8}" width="{btn_w}" height="18" rx="6" fill="#0D1420" stroke="{stroke}" stroke-width="1"/>')
                elements.append(f'<text x="{btn_x + btn_w//2}" y="{y + 2}" font-family="sans-serif" font-size="7" text-anchor="middle" fill="{"#fff" if is_primary else "#9AA4AE"}">{btn}</text>')
                btn_x += btn_w + 8
            y += 24
            
        elif item_type in ["shop_header", "admin_header", "security_header", "blog_header", "classic_header", "free_header"]:
            elements.append(f'<rect x="{x_start}" y="{y - 12}" width="{width}" height="18" fill="{color}" opacity="0.15"/>')
            elements.append(f'<text x="{x_start + 10}" y="{y}" font-family="sans-serif" font-size="10" fill="{color}" font-weight="bold">{data}</text>')
            y += 20
            
        elif item_type == "breadcrumb":
            elements.append(f'<text x="{x_start + 10}" y="{y}" font-family="sans-serif" font-size="6" fill="#666">{data}</text>')
            y += 12
            
        elif item_type == "welcome":
            elements.append(f'<text x="{x_start + 10}" y="{y}" font-family="sans-serif" font-size="9" fill="#ccc">{data}</text>')
            y += 16
            
        elif item_type == "social":
            for social in data:
                elements.append(f'<text x="{x_start + 10}" y="{y}" font-family="sans-serif" font-size="6" fill="#666">{social}</text>')
                y += 10
            
        elif item_type == "post":
            elements.append(f'<text x="{x_start + 10}" y="{y}" font-family="sans-serif" font-size="7" fill="#888">{data}</text>')
            y += 12
            
        elif item_type == "post_title":
            elements.append(f'<text x="{x_start + 10}" y="{y}" font-family="serif" font-size="10" fill="#ccc">{data}</text>')
            y += 16
            
        elif item_type == "status":
            elements.append(f'<circle cx="{x_start + 15}" cy="{y - 3}" r="4" fill="#0f0"/>')
            elements.append(f'<text x="{x_start + 25}" y="{y}" font-family="sans-serif" font-size="9" fill="#0f0">{data}</text>')
            y += 16
    
    return "\n    ".join(elements)


def generate_static_thumbnail(project):
    """Génère une vignette SVG statique (sans animations)"""
    p = project
    W, H = 800, 450
    
    # Zone de preview
    prev_x, prev_y = 380, 50
    prev_w, prev_h = 400, 300
    
    content_svg = render_content_to_svg(p["content"], p["color"], prev_x + 5, prev_y + 35, prev_w - 10)
    
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg-{p['id']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{p['bg']}"/>
      <stop offset="100%" stop-color="#000"/>
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="10" flood-color="#000" flood-opacity="0.5"/>
    </filter>
  </defs>
  
  <!-- Background -->
  <rect width="100%" height="100%" fill="url(#bg-{p['id']})"/>
  
  <!-- Subtle grid -->
  <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">
    <path d="M30 0L0 0 0 30" fill="none" stroke="{p['color']}" stroke-width="0.2" opacity="0.1"/>
  </pattern>
  <rect width="100%" height="100%" fill="url(#grid)"/>
  
  <!-- Top accent -->
  <rect x="0" y="0" width="100%" height="3" fill="{p['color']}" opacity="0.8"/>
  
  <!-- Left side info -->
  <circle cx="60" cy="120" r="40" fill="{p['bg']}" stroke="{p['color']}" stroke-width="2"/>
  <text x="60" y="130" font-size="28" text-anchor="middle" fill="{p['color']}">{"∞" if "tresse" in p['id'] else "🌐" if "gk2" in p['id'] else "🔮" if "ganimed" in p['id'] else "🌸" if "icieb" in p['id'] else "🧙" if "krag" in p['id'] else "☯️" if "wengu" in p['id'] else "👤" if "michel" in p['id'] else "🖥️" if "armbian" in p['id'] else "🔐"}</text>
  
  <text x="25" y="200" font-family="'JetBrains Mono',monospace" font-size="28" font-weight="bold" fill="{p['color']}">{p['title']}</text>
  <text x="25" y="230" font-family="system-ui,sans-serif" font-size="12" fill="#888">{p['subtitle']}</text>
  
  <!-- Browser window -->
  <g filter="url(#shadow)">
    <!-- Window frame -->
    <rect x="{prev_x}" y="{prev_y}" width="{prev_w}" height="{prev_h}" rx="8" fill="#1a1a1a" stroke="{p['color']}" stroke-width="1" opacity="0.9"/>
    
    <!-- Title bar -->
    <rect x="{prev_x}" y="{prev_y}" width="{prev_w}" height="25" rx="8" fill="#2a2a2a"/>
    <rect x="{prev_x}" y="{prev_y + 17}" width="{prev_w}" height="8" fill="#2a2a2a"/>
    
    <!-- Window buttons -->
    <circle cx="{prev_x + 15}" cy="{prev_y + 12}" r="5" fill="#ff5f56"/>
    <circle cx="{prev_x + 32}" cy="{prev_y + 12}" r="5" fill="#ffbd2e"/>
    <circle cx="{prev_x + 49}" cy="{prev_y + 12}" r="5" fill="#27c93f"/>
    
    <!-- URL bar -->
    <rect x="{prev_x + 65}" y="{prev_y + 5}" width="{prev_w - 80}" height="15" rx="3" fill="#1a1a1a"/>
    <text x="{prev_x + 75}" y="{prev_y + 15}" font-family="monospace" font-size="8" fill="#666">https://{p['url']}</text>
    
    <!-- Content area -->
    <rect x="{prev_x}" y="{prev_y + 25}" width="{prev_w}" height="{prev_h - 25}" fill="{p['bg']}"/>
    
    <!-- Content -->
    {content_svg}
  </g>
  
  <!-- Year badge -->
  <rect x="{W - 100}" y="15" width="85" height="24" rx="4" fill="{p['color']}" opacity="0.15"/>
  <rect x="{W - 100}" y="15" width="85" height="24" rx="4" fill="none" stroke="{p['color']}" stroke-width="1" opacity="0.4"/>
  <text x="{W - 57}" y="32" font-family="monospace" font-size="10" text-anchor="middle" fill="{p['color']}">ARCHIVED</text>
  
  <!-- Bottom bar -->
  <rect x="0" y="{H - 35}" width="100%" height="35" fill="#0a0a0a"/>
  <text x="15" y="{H - 12}" font-family="monospace" font-size="11" fill="{p['color']}" opacity="0.7">cybermind.fr/portfolio/{p['id']}</text>
  <text x="{W - 15}" y="{H - 12}" font-family="monospace" font-size="9" text-anchor="end" fill="#444">SNAPSHOT</text>
</svg>'''
    
    return svg


def main():
    output_path = Path(OUTPUT_DIR)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print("📸 Génération des vignettes STATIQUES...")
    print(f"📁 Dossier: {OUTPUT_DIR}")
    print()
    
    for project in PROJECTS:
        svg = generate_static_thumbnail(project)
        filename = f"{project['id']}.svg"
        filepath = output_path / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg)
        
        print(f"  ✅ {project['title']:20} → {filename}")
    
    print()
    print(f"✨ {len(PROJECTS)} vignettes statiques générées!")
    print()
    print("Usage: python3 tools/generate-thumbnails-static.py")


if __name__ == "__main__":
    main()
