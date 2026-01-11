#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════
add-categories.py - Ajouter des catégories aux articles qui n'en ont pas
═══════════════════════════════════════════════════════════════════════════════

Ce script:
1. Scanne les articles dans source/_posts/
2. Affiche ceux qui n'ont pas de catégorie
3. Propose d'ajouter une catégorie par défaut ou interactive

Usage:
  python3 add-categories.py                  # Mode interactif
  python3 add-categories.py --default linux  # Ajouter "linux" à tous
  python3 add-categories.py --dry-run        # Simulation

═══════════════════════════════════════════════════════════════════════════════
"""

import os
import re
import sys
import argparse

CATEGORIES = ['cybersecurity', 'embedded', 'linux', 'creative', 'philosophy', 'tutorials']

def extract_front_matter(content):
    """Extrait le front matter"""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        return match.group(1), match.end(), content[match.end():]
    return None, 0, content

def has_category(fm_text):
    """Vérifie si le front matter a une catégorie"""
    if re.search(r'^category:\s*\S', fm_text, re.MULTILINE):
        return True
    if re.search(r'^categories:\s*$', fm_text, re.MULTILINE):
        # Vérifier s'il y a des items de liste après
        if re.search(r'^categories:\s*\n\s+-', fm_text, re.MULTILINE):
            return True
    if re.search(r'^categories:\s*\[.+\]', fm_text, re.MULTILINE):
        return True
    return False

def get_title(fm_text):
    """Extrait le titre"""
    match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm_text, re.MULTILINE)
    return match.group(1) if match else 'Sans titre'

def add_category_to_fm(fm_text, category):
    """Ajoute une catégorie au front matter"""
    lines = fm_text.split('\n')
    new_lines = []
    added = False
    
    for i, line in enumerate(lines):
        new_lines.append(line)
        # Ajouter après date: ou title:
        if not added and (line.startswith('date:') or line.startswith('title:')):
            # Vérifier que la ligne suivante n'est pas déjà category:
            if i + 1 < len(lines) and not lines[i + 1].startswith('category'):
                new_lines.append(f'category: {category}')
                added = True
    
    if not added:
        # Ajouter à la fin
        new_lines.append(f'category: {category}')
    
    return '\n'.join(new_lines)

def process_file(filepath, category, dry_run=False):
    """Traite un fichier"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, f"Erreur lecture: {e}"
    
    fm_text, fm_end, body = extract_front_matter(content)
    
    if not fm_text:
        return False, "Pas de front matter"
    
    if has_category(fm_text):
        return False, "Déjà une catégorie"
    
    if dry_run:
        return True, f"Ajouterait category: {category}"
    
    new_fm = add_category_to_fm(fm_text, category)
    new_content = f"---\n{new_fm}\n---\n{body}"
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, f"Ajouté category: {category}"
    except Exception as e:
        return False, f"Erreur écriture: {e}"

def main():
    parser = argparse.ArgumentParser(description="Ajouter des catégories aux articles")
    parser.add_argument('--default', choices=CATEGORIES, help='Catégorie par défaut')
    parser.add_argument('--dry-run', action='store_true', help='Simulation')
    parser.add_argument('--path', default='source/_posts', help='Dossier des articles')
    args = parser.parse_args()
    
    if not os.path.isdir(args.path):
        print(f"❌ Dossier non trouvé: {args.path}")
        return 1
    
    print("═" * 70)
    print("📂 AJOUT DE CATÉGORIES AUX ARTICLES")
    print("═" * 70)
    print(f"\n{'🔍 MODE SIMULATION' if args.dry_run else '🚀 MODE EXÉCUTION'}\n")
    
    # Lister les fichiers sans catégorie
    files_without_category = []
    
    for filename in sorted(os.listdir(args.path)):
        if not filename.endswith('.md'):
            continue
        
        filepath = os.path.join(args.path, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            continue
        
        fm_text, _, _ = extract_front_matter(content)
        if fm_text and not has_category(fm_text):
            title = get_title(fm_text)
            files_without_category.append((filepath, filename, title))
    
    if not files_without_category:
        print("✅ Tous les articles ont déjà une catégorie!")
        return 0
    
    print(f"📄 {len(files_without_category)} articles sans catégorie:\n")
    
    for i, (filepath, filename, title) in enumerate(files_without_category, 1):
        print(f"  {i}. {filename}")
        print(f"     Titre: {title}")
    
    print(f"\n📋 Catégories disponibles: {', '.join(CATEGORIES)}\n")
    
    # Mode par défaut
    if args.default:
        category = args.default
        print(f"🏷️  Catégorie par défaut: {category}\n")
        
        for filepath, filename, title in files_without_category:
            success, msg = process_file(filepath, category, args.dry_run)
            status = "✅" if success else "⏭️"
            print(f"  {status} {filename}: {msg}")
        
        print(f"\n{'Simulation terminée.' if args.dry_run else 'Terminé!'}")
        return 0
    
    # Mode interactif
    print("─" * 70)
    print("Mode interactif - Entrez une catégorie pour chaque article")
    print("(Appuyez sur Entrée pour passer, 'q' pour quitter)")
    print("─" * 70)
    
    for filepath, filename, title in files_without_category:
        print(f"\n📄 {filename}")
        print(f"   Titre: {title}")
        
        while True:
            choice = input(f"   Catégorie [{'/'.join(CATEGORIES)}]: ").strip().lower()
            
            if choice == 'q':
                print("\nArrêt.")
                return 0
            
            if choice == '':
                print("   ⏭️  Passé")
                break
            
            if choice in CATEGORIES:
                success, msg = process_file(filepath, choice, args.dry_run)
                print(f"   {'✅' if success else '❌'} {msg}")
                break
            
            print(f"   ⚠️  Catégorie invalide. Choisir parmi: {', '.join(CATEGORIES)}")
    
    print("\n✅ Terminé!")
    return 0

if __name__ == '__main__':
    sys.exit(main())
