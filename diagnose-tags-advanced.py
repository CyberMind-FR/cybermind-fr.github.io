#!/usr/bin/env python3
"""
Script de diagnostic pour trouver les tags Hexo mal fermés
Usage: python3 diagnose-tags-advanced.py
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Tags qui nécessitent une fermeture
BLOCK_TAGS = [
    'youtuber', 'youtube', 'pdf', 'dplayer', 'video',
    'quote', 'note', 'collapse', 'codegroup'
]

def find_tags_in_file(filepath):
    """Trouve tous les tags ouvrants et fermants dans un fichier"""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    tags = defaultdict(lambda: {'open': [], 'close': []})
    
    for tag in BLOCK_TAGS:
        # Trouver les tags ouvrants
        open_pattern = r'\{%\s*' + tag + r'\s+'
        for match in re.finditer(open_pattern, content):
            line_num = content[:match.start()].count('\n') + 1
            tags[tag]['open'].append(line_num)
        
        # Trouver les tags fermants
        close_pattern = r'\{%\s*end' + tag + r'\s*%\}'
        for match in re.finditer(close_pattern, content):
            line_num = content[:match.start()].count('\n') + 1
            tags[tag]['close'].append(line_num)
    
    return tags

def check_file(filepath):
    """Vérifie si un fichier a des tags mal fermés"""
    tags = find_tags_in_file(filepath)
    errors = []
    
    for tag, positions in tags.items():
        open_count = len(positions['open'])
        close_count = len(positions['close'])
        
        if open_count != close_count:
            errors.append({
                'tag': tag,
                'open': open_count,
                'close': close_count,
                'open_lines': positions['open'],
                'close_lines': positions['close']
            })
    
    return errors

def main():
    print("🔍 Diagnostic des tags Hexo\n")
    print("=" * 60)
    
    posts_dir = Path('source/_posts/fr')
    
    if not posts_dir.exists():
        print("❌ Erreur: Le dossier source/_posts n'existe pas")
        print("   Lancez ce script depuis la racine de votre blog Hexo")
        return
    
    # Trouver tous les fichiers markdown
    md_files = list(posts_dir.rglob('*.md'))
    print(f"📁 {len(md_files)} fichiers markdown trouvés\n")
    
    problems_found = False
    
    for md_file in md_files:
        errors = check_file(md_file)
        
        if errors:
            problems_found = True
            print(f"\n❌ ERREUR dans: {md_file}")
            print("-" * 60)
            
            for error in errors:
                print(f"\n  Tag: {{% {error['tag']} %}}")
                print(f"  Ouvertures: {error['open']} (lignes: {error['open_lines']})")
                print(f"  Fermetures: {error['close']} (lignes: {error['close_lines']})")
                
                if error['open'] > error['close']:
                    print(f"  ⚠️  Il manque {error['open'] - error['close']} balise(s) de fermeture")
                    print(f"      Ajoutez {{% end{error['tag']} %}} aux lignes appropriées")
                else:
                    print(f"  ⚠️  Il y a {error['close'] - error['open']} balise(s) de fermeture en trop")
                    print(f"      Supprimez les {{% end{error['tag']} %}} superflues")
    
    print("\n" + "=" * 60)
    
    if not problems_found:
        print("✅ Aucun problème de tags détecté !")
        print("\nSi vous avez toujours l'erreur 'unexpected end of file',")
        print("vérifiez manuellement les tags complexes ou imbriqués.")
    else:
        print("\n💡 Conseils de correction:")
        print("  1. Ouvrez le(s) fichier(s) problématique(s)")
        print("  2. Allez aux lignes indiquées")
        print("  3. Ajoutez/supprimez les balises de fermeture")
        print("  4. Testez avec: hexo clean && hexo generate")
        print("\n  Alternative: Utilisez la syntaxe courte (sans fermeture)")
        print("  Exemple: {% youtuber VIDEO_ID %} (sans {% endyoutuber %})")
    
    print("\n")

if __name__ == '__main__':
    main()
