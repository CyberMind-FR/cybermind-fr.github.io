#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════
migrate-posts-to-blog.py - Migration des articles vers structure blog/{category}
═══════════════════════════════════════════════════════════════════════════════

Ce script:
1. Scanne les articles dans source/_posts/
2. Détecte leur catégorie (depuis le front matter)
3. Les déplace vers source/blog/{category}/
4. Met à jour le front matter si nécessaire

Usage:
  python3 migrate-posts-to-blog.py                    # Simulation (dry-run)
  python3 migrate-posts-to-blog.py --execute          # Exécution réelle
  python3 migrate-posts-to-blog.py --execute --backup # Avec backup

═══════════════════════════════════════════════════════════════════════════════
"""

import os
import re
import shutil
import argparse
from pathlib import Path
from datetime import datetime

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

# Mapping des catégories (aliases -> slug principal)
CATEGORY_MAP = {
    # Cybersecurity
    'cybersecurity': 'cybersecurity',
    'security': 'cybersecurity',
    'cyber': 'cybersecurity',
    'sécurité': 'cybersecurity',
    'securite': 'cybersecurity',
    'infosec': 'cybersecurity',
    
    # Embedded
    'embedded': 'embedded',
    'arm': 'embedded',
    'hardware': 'embedded',
    'raspberry': 'embedded',
    'raspberrypi': 'embedded',
    'raspberry-pi': 'embedded',
    'armbian': 'embedded',
    
    # Linux
    'linux': 'linux',
    'kernel': 'linux',
    'open-source': 'linux',
    'opensource': 'linux',
    
    # Creative
    'creative': 'creative',
    'créativité': 'creative',
    'creativite': 'creative',
    'art': 'creative',
    'generative': 'creative',
    'music': 'creative',
    'musique': 'creative',
    'poetry': 'creative',
    'poésie': 'creative',
    
    # Philosophy
    'philosophy': 'philosophy',
    'philosophie': 'philosophy',
    'yijing': 'philosophy',
    'yi-jing': 'philosophy',
    'yi jing': 'philosophy',
    
    # Tutorials
    'tutorials': 'tutorials',
    'tutorial': 'tutorials',
    'tuto': 'tutorials',
    'howto': 'tutorials',
    'how-to': 'tutorials',
    'guides': 'tutorials',
    'guide': 'tutorials',
}

# Catégorie par défaut si non détectée
DEFAULT_CATEGORY = 'uncategorized'

# ═══════════════════════════════════════════════════════════════════════════════
# FONCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def extract_front_matter(content):
    """Extrait le front matter YAML d'un fichier Markdown"""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        return match.group(1), match.end(), content[match.end():]
    return None, 0, content


def parse_front_matter(fm_text):
    """Parse le front matter en dictionnaire (simple, sans yaml lib)"""
    result = {}
    current_key = None
    current_list = None
    
    for line in fm_text.split('\n'):
        line = line.rstrip()
        
        # Liste YAML (  - item)
        if line.startswith('  - ') and current_key:
            if current_list is None:
                current_list = []
            current_list.append(line[4:].strip())
            result[current_key] = current_list
            continue
        
        # Fin de liste
        if current_list is not None and not line.startswith('  '):
            current_list = None
        
        # Clé: valeur
        if ':' in line:
            parts = line.split(':', 1)
            key = parts[0].strip()
            value = parts[1].strip() if len(parts) > 1 else ''
            
            # Valeur entre guillemets
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            
            # Liste inline [a, b, c]
            if value.startswith('[') and value.endswith(']'):
                items = value[1:-1].split(',')
                value = [i.strip().strip('"\'') for i in items if i.strip()]
            
            result[key] = value
            current_key = key
            
            # Si valeur vide, potentiellement une liste suit
            if value == '':
                current_list = []
    
    return result


def detect_category(fm_dict):
    """Détecte la catégorie depuis le front matter"""
    # 1. Champ 'category' (singulier)
    if 'category' in fm_dict and fm_dict['category']:
        cat = str(fm_dict['category']).lower().strip()
        return CATEGORY_MAP.get(cat, cat)
    
    # 2. Champ 'categories' (liste)
    if 'categories' in fm_dict:
        cats = fm_dict['categories']
        if isinstance(cats, list) and len(cats) > 0:
            cat = str(cats[0]).lower().strip()
            return CATEGORY_MAP.get(cat, cat)
        elif isinstance(cats, str) and cats:
            cat = cats.lower().strip()
            return CATEGORY_MAP.get(cat, cat)
    
    return None


def update_front_matter(fm_text, category):
    """Met à jour le front matter avec la catégorie"""
    lines = fm_text.split('\n')
    new_lines = []
    has_category = False
    
    for line in lines:
        # Remplacer category existant
        if line.startswith('category:'):
            new_lines.append(f'category: {category}')
            has_category = True
        # Supprimer categories: (on garde juste category)
        elif line.startswith('categories:'):
            if not has_category:
                new_lines.append(f'category: {category}')
                has_category = True
            # Skip cette ligne et les lignes de liste qui suivent
            continue
        elif line.startswith('  - ') and has_category:
            # Skip les items de la liste categories
            continue
        else:
            new_lines.append(line)
    
    # Ajouter category si absent
    if not has_category:
        # Insérer après title ou date
        for i, line in enumerate(new_lines):
            if line.startswith('date:') or line.startswith('title:'):
                new_lines.insert(i + 1, f'category: {category}')
                has_category = True
                break
        if not has_category:
            new_lines.append(f'category: {category}')
    
    return '\n'.join(new_lines)


def migrate_post(source_path, dest_dir, dry_run=True):
    """Migre un article vers le nouveau dossier"""
    try:
        content = source_path.read_text(encoding='utf-8')
    except Exception as e:
        return False, f"Erreur lecture: {e}"
    
    fm_text, fm_end, body = extract_front_matter(content)
    
    if not fm_text:
        return False, "Pas de front matter"
    
    fm_dict = parse_front_matter(fm_text)
    category = detect_category(fm_dict)
    
    if not category:
        return False, "Catégorie non détectée"
    
    # Normaliser la catégorie
    category = CATEGORY_MAP.get(category.lower(), category.lower())
    
    # Chemin destination
    dest_category_dir = dest_dir / category
    dest_path = dest_category_dir / source_path.name
    
    if dry_run:
        return True, f"→ blog/{category}/{source_path.name}"
    
    # Créer le dossier
    dest_category_dir.mkdir(parents=True, exist_ok=True)
    
    # Mettre à jour le front matter
    new_fm = update_front_matter(fm_text, category)
    new_content = f"---\n{new_fm}\n---\n{body}"
    
    # Écrire le fichier
    dest_path.write_text(new_content, encoding='utf-8')
    
    return True, f"→ blog/{category}/{source_path.name}"


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Migration des articles vers la structure blog/{category}",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('--execute', action='store_true', 
                        help='Exécuter la migration (sinon dry-run)')
    parser.add_argument('--backup', action='store_true',
                        help='Créer un backup avant migration')
    parser.add_argument('--source', default='source/_posts',
                        help='Dossier source (défaut: source/_posts)')
    parser.add_argument('--dest', default='source/blog',
                        help='Dossier destination (défaut: source/blog)')
    parser.add_argument('--delete-original', action='store_true',
                        help='Supprimer les fichiers originaux après migration')
    
    args = parser.parse_args()
    
    dry_run = not args.execute
    
    print("═" * 70)
    print("📦 MIGRATION DES ARTICLES VERS BLOG/{CATEGORY}")
    print("═" * 70)
    print(f"\n{'🔍 MODE SIMULATION' if dry_run else '🚀 MODE EXÉCUTION'}\n")
    
    source_dir = Path(args.source)
    dest_dir = Path(args.dest)
    
    if not source_dir.exists():
        print(f"❌ Dossier source introuvable: {source_dir}")
        print("   Assurez-vous d'être à la racine du projet Hexo")
        return 1
    
    # Lister les fichiers
    posts = list(source_dir.glob('*.md'))
    
    if not posts:
        print(f"⚠️  Aucun fichier .md trouvé dans {source_dir}")
        return 0
    
    print(f"📁 Source: {source_dir}")
    print(f"📁 Destination: {dest_dir}")
    print(f"📄 Articles trouvés: {len(posts)}\n")
    
    # Backup
    if args.backup and args.execute:
        backup_dir = Path(f"_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
        print(f"💾 Création du backup: {backup_dir}")
        shutil.copytree(source_dir, backup_dir)
        print(f"   ✅ Backup créé\n")
    
    # Migration
    results = {
        'success': [],
        'skipped': [],
        'error': []
    }
    
    by_category = {}
    
    for post_path in sorted(posts):
        success, message = migrate_post(post_path, dest_dir, dry_run)
        
        if success:
            results['success'].append((post_path.name, message))
            # Extraire la catégorie du message
            cat_match = re.search(r'blog/([^/]+)/', message)
            if cat_match:
                cat = cat_match.group(1)
                if cat not in by_category:
                    by_category[cat] = []
                by_category[cat].append(post_path.name)
        else:
            if "non détectée" in message:
                results['skipped'].append((post_path.name, message))
            else:
                results['error'].append((post_path.name, message))
    
    # Affichage par catégorie
    print("─" * 70)
    print("📊 RÉSULTATS PAR CATÉGORIE")
    print("─" * 70)
    
    for cat in sorted(by_category.keys()):
        print(f"\n📁 {cat.upper()} ({len(by_category[cat])} articles)")
        for name in by_category[cat]:
            print(f"   • {name}")
    
    # Articles sans catégorie
    if results['skipped']:
        print(f"\n⚠️  SANS CATÉGORIE ({len(results['skipped'])} articles)")
        print("   Ces articles ont besoin d'un champ 'category:' dans le front matter:")
        for name, msg in results['skipped']:
            print(f"   • {name}")
    
    # Erreurs
    if results['error']:
        print(f"\n❌ ERREURS ({len(results['error'])})")
        for name, msg in results['error']:
            print(f"   • {name}: {msg}")
    
    # Résumé
    print("\n" + "═" * 70)
    print("📈 RÉSUMÉ")
    print("═" * 70)
    print(f"   ✅ Migrés: {len(results['success'])}")
    print(f"   ⚠️  Sans catégorie: {len(results['skipped'])}")
    print(f"   ❌ Erreurs: {len(results['error'])}")
    
    if dry_run:
        print("\n💡 Pour exécuter la migration:")
        print("   python3 migrate-posts-to-blog.py --execute")
        print("   python3 migrate-posts-to-blog.py --execute --backup")
    else:
        print(f"\n✅ Migration terminée!")
        
        if args.delete_original and results['success']:
            print("\n🗑️  Suppression des originaux...")
            for name, _ in results['success']:
                orig = source_dir / name
                if orig.exists():
                    orig.unlink()
                    print(f"   Supprimé: {name}")
    
    # Instructions pour les articles sans catégorie
    if results['skipped']:
        print("\n" + "─" * 70)
        print("📝 POUR LES ARTICLES SANS CATÉGORIE")
        print("─" * 70)
        print("""
Ajoutez une ligne 'category: xxx' dans le front matter de chaque article.

Catégories disponibles:
  • cybersecurity  - Sécurité, pentests, CrowdSec
  • embedded       - ARM, Raspberry Pi, Armbian
  • linux          - Kernel, administration
  • creative       - Art génératif, musique, poésie
  • philosophy     - Yi Jing, réflexions
  • tutorials      - Guides, how-to

Exemple:
---
title: "Mon Article"
date: 2025-01-15
category: cybersecurity    # ← Ajouter cette ligne
tags: [crowdsec, security]
---
""")
    
    return 0


if __name__ == '__main__':
    exit(main())
