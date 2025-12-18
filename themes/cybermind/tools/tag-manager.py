#!/usr/bin/env python3
"""
🏷️ Tag Manager - Gestionnaire de tags pour Hexo
================================================

Fonctionnalités :
- Analyse tous les tags utilisés dans les articles
- Détecte les tags orphelins (utilisés 1 seule fois)
- Propose des fusions de tags similaires
- Corrige les tags en masse
- Supprime les tags inutilisés
- Génère un rapport détaillé

Usage :
  python3 tools/tag-manager.py                    # Analyse et rapport
  python3 tools/tag-manager.py --fix              # Applique les corrections
  python3 tools/tag-manager.py --dry-run          # Simule les corrections
  python3 tools/tag-manager.py --report tags.md   # Export rapport Markdown

Auteur: CyberMind
"""

import os
import re
import yaml
import argparse
from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher

# ═══════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

# Dossiers à scanner (relatifs à la racine du projet Hexo)
SOURCE_DIRS = [
    "source/_posts",
    "source/blog",
    "source/apps",
    "source/portfolio",
    "source/services",
    "source/pages",
    # Pour les tests avec examples/
    "examples/blog",
    "examples/apps",
    "examples/portfolio",
    "examples/services",
    "examples/pages",
]

# Tags à renommer automatiquement (ancien -> nouveau)
TAG_RENAMES = {
    # Normalisation casse
    "CrowdSec": "crowdsec",
    "OpenWrt": "openwrt",
    "Armbian": "armbian",
    "RaspberryPi": "raspberry-pi",
    "Raspberry Pi": "raspberry-pi",
    "raspberry pi": "raspberry-pi",
    "Yi Jing": "yi-jing",
    "yi jing": "yi-jing",
    "yijing": "yi-jing",
    "Yi-Jing": "yi-jing",
    
    # Corrections orthographiques
    "securite": "sécurité",
    "securité": "sécurité",
    "geometrie": "géométrie",
    "creatif": "créatif",
    "creative": "créatif",
    
    # Fusions de tags similaires
    "linux-kernel": "kernel",
    "kernel-linux": "kernel",
    "arm-soc": "arm",
    "arm-cpu": "arm",
    "javascript": "js",
    "JavaScript": "js",
    "python3": "python",
    "Python": "python",
    "cyber-securite": "cybersécurité",
    "cyber-security": "cybersécurité",
    "infosec": "cybersécurité",
}

# Tags à supprimer (trop génériques ou inutiles)
TAGS_TO_REMOVE = [
    "misc",
    "divers",
    "other",
    "test",
    "draft",
    "todo",
    "wip",
    "temp",
    "uncategorized",
]

# Seuil pour considérer un tag comme "orphelin" (utilisé X fois ou moins)
ORPHAN_THRESHOLD = 1

# Seuil de similarité pour suggérer une fusion (0.0 à 1.0)
SIMILARITY_THRESHOLD = 0.8


# ═══════════════════════════════════════════════════════════════════════════
# FONCTIONS UTILITAIRES
# ═══════════════════════════════════════════════════════════════════════════

def extract_front_matter(content):
    """Extrait le front matter YAML d'un fichier Markdown"""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1)), match.end()
        except yaml.YAMLError:
            return None, 0
    return None, 0


def update_front_matter(content, new_fm):
    """Met à jour le front matter d'un fichier"""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        new_yaml = yaml.dump(new_fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
        return f"---\n{new_yaml}---\n{content[match.end():]}"
    return content


def similarity(a, b):
    """Calcule la similarité entre deux chaînes (0.0 à 1.0)"""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def normalize_tag(tag):
    """Normalise un tag (minuscules, tirets)"""
    if not tag:
        return ""
    # Garder les accents mais normaliser
    tag = tag.strip().lower()
    tag = re.sub(r'\s+', '-', tag)
    tag = re.sub(r'-+', '-', tag)
    return tag


# ═══════════════════════════════════════════════════════════════════════════
# CLASSE PRINCIPALE
# ═══════════════════════════════════════════════════════════════════════════

class TagManager:
    def __init__(self, base_path="."):
        self.base_path = Path(base_path)
        self.files = []           # Liste des fichiers analysés
        self.tags = defaultdict(list)  # tag -> [fichiers]
        self.tag_counts = defaultdict(int)  # tag -> count
        self.issues = []          # Problèmes détectés
        self.changes = []         # Changements à appliquer
        
    def scan_files(self):
        """Scanne tous les fichiers Markdown"""
        print("📁 Scan des fichiers...")
        
        for source_dir in SOURCE_DIRS:
            dir_path = self.base_path / source_dir
            if not dir_path.exists():
                continue
                
            for md_file in dir_path.rglob("*.md"):
                self.files.append(md_file)
                
        print(f"   → {len(self.files)} fichiers trouvés")
        
    def analyze_tags(self):
        """Analyse les tags de tous les fichiers"""
        print("\n🏷️  Analyse des tags...")
        
        for file_path in self.files:
            try:
                content = file_path.read_text(encoding='utf-8')
                fm, _ = extract_front_matter(content)
                
                if not fm:
                    continue
                    
                # Récupérer les tags (plusieurs formats possibles)
                file_tags = []
                
                # Format: tags: [tag1, tag2]
                if 'tags' in fm:
                    if isinstance(fm['tags'], list):
                        file_tags.extend(fm['tags'])
                    elif isinstance(fm['tags'], str):
                        file_tags.append(fm['tags'])
                        
                # Format: tags_list: [tag1, tag2]
                if 'tags_list' in fm:
                    if isinstance(fm['tags_list'], list):
                        file_tags.extend(fm['tags_list'])
                        
                # Enregistrer les tags
                for tag in file_tags:
                    if tag:
                        tag_str = str(tag).strip()
                        self.tags[tag_str].append(file_path)
                        self.tag_counts[tag_str] += 1
                        
            except Exception as e:
                print(f"   ⚠️ Erreur lecture {file_path}: {e}")
                
        print(f"   → {len(self.tags)} tags uniques trouvés")
        
    def detect_issues(self):
        """Détecte les problèmes de tags"""
        print("\n🔍 Détection des problèmes...")
        
        all_tags = list(self.tags.keys())
        
        for tag in all_tags:
            # 1. Tags à renommer
            if tag in TAG_RENAMES:
                self.issues.append({
                    'type': 'rename',
                    'tag': tag,
                    'new_tag': TAG_RENAMES[tag],
                    'files': self.tags[tag],
                    'reason': 'Configuration TAG_RENAMES'
                })
                
            # 2. Tags à supprimer
            elif tag.lower() in [t.lower() for t in TAGS_TO_REMOVE]:
                self.issues.append({
                    'type': 'remove',
                    'tag': tag,
                    'files': self.tags[tag],
                    'reason': 'Tag dans liste de suppression'
                })
                
            # 3. Tags orphelins
            elif self.tag_counts[tag] <= ORPHAN_THRESHOLD:
                self.issues.append({
                    'type': 'orphan',
                    'tag': tag,
                    'files': self.tags[tag],
                    'count': self.tag_counts[tag],
                    'reason': f'Utilisé {self.tag_counts[tag]} fois seulement'
                })
                
        # 4. Tags similaires (potentielles fusions)
        checked = set()
        for tag1 in all_tags:
            for tag2 in all_tags:
                if tag1 != tag2 and (tag2, tag1) not in checked:
                    sim = similarity(tag1, tag2)
                    if sim >= SIMILARITY_THRESHOLD:
                        self.issues.append({
                            'type': 'similar',
                            'tag': tag1,
                            'similar_to': tag2,
                            'similarity': f"{sim:.0%}",
                            'reason': f'Similaire à "{tag2}" ({sim:.0%})'
                        })
                    checked.add((tag1, tag2))
                    
        print(f"   → {len(self.issues)} problèmes détectés")
        
    def generate_report(self):
        """Génère un rapport détaillé"""
        report = []
        report.append("# 🏷️ Rapport d'analyse des tags\n")
        report.append(f"**Fichiers analysés:** {len(self.files)}\n")
        report.append(f"**Tags uniques:** {len(self.tags)}\n")
        report.append(f"**Problèmes détectés:** {len(self.issues)}\n")
        
        # Stats globales
        report.append("\n## 📊 Statistiques\n")
        report.append("| Tag | Occurrences |")
        report.append("|-----|-------------|")
        for tag, count in sorted(self.tag_counts.items(), key=lambda x: -x[1])[:20]:
            report.append(f"| `{tag}` | {count} |")
            
        # Tags orphelins
        orphans = [i for i in self.issues if i['type'] == 'orphan']
        if orphans:
            report.append(f"\n## 👻 Tags orphelins ({len(orphans)})\n")
            report.append("Tags utilisés une seule fois :\n")
            for issue in orphans:
                report.append(f"- `{issue['tag']}` → {issue['files'][0].name}")
                
        # Tags à renommer
        renames = [i for i in self.issues if i['type'] == 'rename']
        if renames:
            report.append(f"\n## ✏️ Tags à renommer ({len(renames)})\n")
            report.append("| Ancien | Nouveau | Fichiers |")
            report.append("|--------|---------|----------|")
            for issue in renames:
                report.append(f"| `{issue['tag']}` | `{issue['new_tag']}` | {len(issue['files'])} |")
                
        # Tags similaires
        similars = [i for i in self.issues if i['type'] == 'similar']
        if similars:
            report.append(f"\n## 🔀 Tags similaires ({len(similars)})\n")
            report.append("Potentielles fusions :\n")
            for issue in similars:
                report.append(f"- `{issue['tag']}` ↔ `{issue['similar_to']}` ({issue['similarity']})")
                
        # Tags à supprimer
        removes = [i for i in self.issues if i['type'] == 'remove']
        if removes:
            report.append(f"\n## 🗑️ Tags à supprimer ({len(removes)})\n")
            for issue in removes:
                report.append(f"- `{issue['tag']}` ({len(issue['files'])} fichiers)")
                
        # Liste complète des tags
        report.append("\n## 📋 Liste complète des tags\n")
        report.append("```")
        for tag in sorted(self.tags.keys(), key=str.lower):
            report.append(f"{tag}: {self.tag_counts[tag]}")
        report.append("```")
        
        return "\n".join(report)
        
    def apply_fixes(self, dry_run=False):
        """Applique les corrections"""
        prefix = "🔄 [DRY-RUN]" if dry_run else "✅"
        print(f"\n{prefix} Application des corrections...")
        
        files_modified = set()
        
        for issue in self.issues:
            if issue['type'] == 'rename':
                for file_path in issue['files']:
                    if not dry_run:
                        self._fix_tag_in_file(file_path, issue['tag'], issue['new_tag'])
                    files_modified.add(file_path)
                    print(f"   {prefix} {file_path.name}: '{issue['tag']}' → '{issue['new_tag']}'")
                    
            elif issue['type'] == 'remove':
                for file_path in issue['files']:
                    if not dry_run:
                        self._remove_tag_from_file(file_path, issue['tag'])
                    files_modified.add(file_path)
                    print(f"   {prefix} {file_path.name}: supprimé '{issue['tag']}'")
                    
        print(f"\n   → {len(files_modified)} fichiers {'à modifier' if dry_run else 'modifiés'}")
        
    def _fix_tag_in_file(self, file_path, old_tag, new_tag):
        """Remplace un tag dans un fichier"""
        try:
            content = file_path.read_text(encoding='utf-8')
            fm, fm_end = extract_front_matter(content)
            
            if not fm:
                return
                
            modified = False
            
            # Modifier tags
            if 'tags' in fm:
                if isinstance(fm['tags'], list):
                    fm['tags'] = [new_tag if t == old_tag else t for t in fm['tags']]
                    modified = True
                elif fm['tags'] == old_tag:
                    fm['tags'] = new_tag
                    modified = True
                    
            # Modifier tags_list
            if 'tags_list' in fm:
                if isinstance(fm['tags_list'], list):
                    fm['tags_list'] = [new_tag if t == old_tag else t for t in fm['tags_list']]
                    modified = True
                    
            if modified:
                new_content = update_front_matter(content, fm)
                file_path.write_text(new_content, encoding='utf-8')
                
        except Exception as e:
            print(f"   ⚠️ Erreur modification {file_path}: {e}")
            
    def _remove_tag_from_file(self, file_path, tag_to_remove):
        """Supprime un tag d'un fichier"""
        try:
            content = file_path.read_text(encoding='utf-8')
            fm, fm_end = extract_front_matter(content)
            
            if not fm:
                return
                
            modified = False
            
            # Supprimer de tags
            if 'tags' in fm:
                if isinstance(fm['tags'], list):
                    fm['tags'] = [t for t in fm['tags'] if t != tag_to_remove]
                    modified = True
                elif fm['tags'] == tag_to_remove:
                    del fm['tags']
                    modified = True
                    
            # Supprimer de tags_list
            if 'tags_list' in fm:
                if isinstance(fm['tags_list'], list):
                    fm['tags_list'] = [t for t in fm['tags_list'] if t != tag_to_remove]
                    modified = True
                    
            if modified:
                new_content = update_front_matter(content, fm)
                file_path.write_text(new_content, encoding='utf-8')
                
        except Exception as e:
            print(f"   ⚠️ Erreur modification {file_path}: {e}")


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="🏷️ Tag Manager - Gestionnaire de tags pour Hexo",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  python3 tools/tag-manager.py                    # Analyse seule
  python3 tools/tag-manager.py --fix              # Applique les corrections
  python3 tools/tag-manager.py --dry-run          # Simule les corrections
  python3 tools/tag-manager.py --report tags.md   # Export rapport
        """
    )
    parser.add_argument('--fix', action='store_true', help='Applique les corrections automatiques')
    parser.add_argument('--dry-run', action='store_true', help='Simule les corrections sans modifier')
    parser.add_argument('--report', metavar='FILE', help='Exporte le rapport dans un fichier')
    parser.add_argument('--path', default='.', help='Chemin du projet Hexo (défaut: .)')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🏷️  TAG MANAGER - Gestionnaire de tags Hexo")
    print("=" * 60)
    
    manager = TagManager(args.path)
    manager.scan_files()
    manager.analyze_tags()
    manager.detect_issues()
    
    # Afficher le rapport
    report = manager.generate_report()
    print("\n" + report)
    
    # Exporter le rapport
    if args.report:
        Path(args.report).write_text(report, encoding='utf-8')
        print(f"\n📄 Rapport exporté: {args.report}")
        
    # Appliquer les corrections
    if args.fix or args.dry_run:
        manager.apply_fixes(dry_run=args.dry_run)
        
    print("\n" + "=" * 60)
    print("✅ Terminé!")
    print("=" * 60)


if __name__ == "__main__":
    main()
