#!/bin/bash

# Script pour trouver quel article cause l'erreur "unexpected end of file"
# Usage: ./find-problematic-article.sh

set -e

echo "🔍 Recherche de l'article problématique..."
echo ""

POSTS_DIR="source/_posts"
BACKUP_DIR="source/_posts_backup_$(date +%s)"

# Vérifier qu'on est dans un blog Hexo
if [ ! -d "$POSTS_DIR" ]; then
    echo "❌ Erreur: Dossier $POSTS_DIR introuvable"
    echo "   Lancez ce script depuis la racine de votre blog Hexo"
    exit 1
fi

# Sauvegarder tous les articles
echo "📦 Sauvegarde des articles dans $BACKUP_DIR..."
cp -r "$POSTS_DIR" "$BACKUP_DIR"

# Vider le dossier _posts
echo "🗑️  Vidage temporaire de $POSTS_DIR..."
find "$POSTS_DIR" -name "*.md" -type f -delete

# Tester que ça marche sans articles
echo "✅ Test sans articles..."
if ! hexo generate >/dev/null 2>&1; then
    echo "❌ Erreur même sans articles! Problème avec le thème?"
    echo "   Restauration..."
    rm -rf "$POSTS_DIR"
    mv "$BACKUP_DIR" "$POSTS_DIR"
    exit 1
fi

echo "✅ Hexo fonctionne sans articles"
echo ""
echo "🔎 Test des articles un par un..."
echo ""

# Tester chaque article
problematic_files=()

for file in "$BACKUP_DIR"/**/*.md; do
    # Obtenir le chemin relatif
    rel_path="${file#$BACKUP_DIR/}"
    target="$POSTS_DIR/$rel_path"
    
    # Créer le dossier si nécessaire
    mkdir -p "$(dirname "$target")"
    
    # Copier l'article
    cp "$file" "$target"
    
    # Tester la génération
    echo -n "Test: $rel_path ... "
    
    if hexo generate >/dev/null 2>&1; then
        echo "✅ OK"
    else
        echo "❌ ERREUR TROUVÉE!"
        problematic_files+=("$rel_path")
        
        # Supprimer l'article problématique
        rm "$target"
    fi
done

echo ""
echo "=" * 60
echo ""

if [ ${#problematic_files[@]} -eq 0 ]; then
    echo "✅ Aucun article problématique trouvé!"
    echo "   L'erreur vient peut-être d'une interaction entre plusieurs articles."
else
    echo "❌ Article(s) problématique(s) trouvé(s):"
    echo ""
    for file in "${problematic_files[@]}"; do
        echo "  - $file"
    done
    
    echo ""
    echo "💡 Prochaines étapes:"
    echo "  1. Ouvrez le(s) fichier(s) ci-dessus"
    echo "  2. Vérifiez les tags avec: grep -n '{% ' \"$BACKUP_DIR/$file\""
    echo "  3. Corrigez les balises de fermeture manquantes"
    echo "  4. Utilisez diagnose-tags-advanced.py pour plus de détails"
fi

echo ""
echo "📦 Restauration des articles..."
rm -rf "$POSTS_DIR"
mv "$BACKUP_DIR" "$POSTS_DIR"

echo ""
echo "✅ Articles restaurés. Vous pouvez maintenant corriger les fichiers problématiques."
