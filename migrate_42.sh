#!/bin/bash
# migrate-posts.sh - Migrer les anciens articles vers la nouvelle structure

SOURCE_DIR="source/_posts/fr"
DEST_DIR="source/blog"

# Créer les dossiers de catégories
mkdir -p "$DEST_DIR"/{cybersecurity,embedded,linux,creative,philosophy,tutorials}

# Pour chaque article, détecter la catégorie et déplacer
for file in "$SOURCE_DIR"/*.md; do
  # Extraire la catégorie du front matter
  category=$(grep -m1 "^category:" "$file" | cut -d: -f2 | tr -d ' ')
  
  if [ -n "$category" ] && [ -d "$DEST_DIR/$category" ]; then
    cp "$file" "$DEST_DIR/$category/"
    echo "Migré: $(basename $file) → $category/"
  else
    echo "⚠️ Catégorie inconnue pour: $(basename $file)"
  fi
done