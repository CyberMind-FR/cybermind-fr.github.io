#!/bin/bash

# Script de diagnostic pour trouver les tags Hexo mal fermés

echo "🔍 Recherche des tags mal fermés dans vos articles..."
echo ""

POSTS_DIR="source/_posts"

# Fonction pour vérifier un fichier
check_file() {
    local file="$1"
    local has_error=0
    
    # Liste des tags qui nécessitent une fermeture
    tags=("youtuber" "youtube" "pdf" "dplayer" "video" "quote" "note" "collapse" "codegroup")
    
    for tag in "${tags[@]}"; do
        # Compter les ouvertures et fermetures
        opens=$(grep -c "{% ${tag}" "$file" 2>/dev/null || echo 0)
        closes=$(grep -c "{% end${tag}" "$file" 2>/dev/null || echo 0)
        
        if [ $opens -ne $closes ]; then
            if [ $has_error -eq 0 ]; then
                echo "❌ Erreur dans: $file"
                has_error=1
            fi
            echo "   Tag {%${tag}%}: $opens ouvertures, $closes fermetures"
        fi
    done
    
    return $has_error
}

# Vérifier tous les fichiers markdown
find "$POSTS_DIR" -name "*.md" -type f | while read -r file; do
    check_file "$file"
done

echo ""
echo "🔎 Recherche de patterns suspects..."
echo ""

# Chercher les tags orphelins
echo "Tags d'ouverture trouvés:"
grep -rn "{% \(youtuber\|youtube\|pdf\|dplayer\|video\|quote\|note\|collapse\)" "$POSTS_DIR" | head -20

echo ""
echo "Tags de fermeture trouvés:"
grep -rn "{% end\(youtuber\|youtube\|pdf\|dplayer\|video\|quote\|note\|collapse\)" "$POSTS_DIR" | head -20

echo ""
echo "✅ Diagnostic terminé"
