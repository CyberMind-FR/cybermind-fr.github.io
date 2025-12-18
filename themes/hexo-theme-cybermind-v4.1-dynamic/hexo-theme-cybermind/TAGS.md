# Tags Personnalisés - Hexo Theme CyberMind

Le thème CyberMind inclut **18 tags personnalisés** pour enrichir vos articles.

## 🎬 Vidéos

### YouTube

**Syntaxe simple :**
```markdown
{% youtuber VIDEO_ID %}
```

**Syntaxe avec fermeture (alternative) :**
```markdown
{% youtuber VIDEO_ID %}
{% endyoutuber %}
```

**Exemple :**
```markdown
{% youtuber dQw4w9WgXcQ %}

<!-- OU -->

{% youtuber dQw4w9WgXcQ %}
{% endyoutuber %}
```

**Ou avec tag `youtube` et titre personnalisé :**
```markdown
{% youtube dQw4w9WgXcQ "Mon tutoriel vidéo" %}

<!-- OU -->

{% youtube dQw4w9WgXcQ "Mon tutoriel vidéo" %}
{% endyoutube %}
```

### Vimeo

```markdown
{% vimeo VIDEO_ID %}
```

**Exemple :**
```markdown
{% vimeo 123456789 %}
```

### DPlayer (Lecteur vidéo HTML5)

**Syntaxe simple :**
```markdown
{% dplayer url="video.mp4" %}
```

**Avec poster/thumbnail :**
```markdown
{% dplayer url="video.mp4" pic="poster.jpg" %}
```

**Avec options :**
```markdown
{% dplayer url="video.mp4" pic="poster.jpg" loop="true" %}
```

**Syntaxe avec fermeture :**
```markdown
{% dplayer url="video.mp4" %}
{% enddplayer %}
```

**Exemples :**
```markdown
<!-- Vidéo locale -->
{% dplayer url="/videos/demo.mp4" %}

<!-- Vidéo avec poster -->
{% dplayer url="/videos/tutorial.mp4" pic="/images/poster.jpg" %}

<!-- Vidéo en boucle -->
{% dplayer url="https://example.com/video.mp4" loop="true" %}

<!-- Vidéo avec autoplay -->
{% dplayer url="/videos/intro.mp4" autoplay="true" %}
```

### Video (Alternative simple)

**Syntaxe :**
```markdown
{% video /path/to/video.mp4 %}
{% video /path/to/video.mp4 /path/to/poster.jpg %}
```

**Exemples :**
```markdown
<!-- Vidéo simple -->
{% video /videos/demo.mp4 %}

<!-- Vidéo avec poster -->
{% video /videos/tutorial.mp4 /images/thumbnail.jpg %}

<!-- URL externe -->
{% video https://example.com/video.mp4 %}
```

### PDF

**Syntaxe simple :**
```markdown
{% pdf /path/to/document.pdf %}
```

**Avec hauteur personnalisée :**
```markdown
{% pdf /path/to/document.pdf 800 %}
```

**Syntaxe avec fermeture (alternative) :**
```markdown
{% pdf /path/to/document.pdf %}
{% endpdf %}
```

**Lien de téléchargement uniquement :**
```markdown
{% pdflink /path/to/document.pdf "Télécharger le document" %}
```

**Exemples :**
```markdown
<!-- PDF intégré avec hauteur par défaut (600px) -->
{% pdf /files/guide-cybersecurity.pdf %}

<!-- PDF intégré avec hauteur personnalisée -->
{% pdf /files/rapport-annuel.pdf 800 %}

<!-- URL externe -->
{% pdf https://example.com/whitepaper.pdf %}

<!-- Juste un lien de téléchargement -->
{% pdflink /files/cheatsheet.pdf "Télécharger la cheatsheet" %}
```

---

## 🎵 Audio

### APlayer (Lecteur audio HTML5)

**Syntaxe complète :**
```markdown
{% aplayer "Titre" "Artiste" "/music/song.mp3" %}
```

**Avec image de couverture :**
```markdown
{% aplayer "Titre" "Artiste" "/music/song.mp3" "/images/cover.jpg" %}
```

**Syntaxe avec fermeture :**
```markdown
{% aplayer "Titre" "Artiste" "/music/song.mp3" %}
{% endaplayer %}
```

**Exemples :**
```markdown
<!-- Fichier audio local -->
{% aplayer "Ma Chanson" "Mon Groupe" "/music/track.mp3" %}

<!-- Avec couverture -->
{% aplayer "Song Title" "Artist Name" "/music/song.mp3" "/images/album-cover.jpg" %}

<!-- URL externe -->
{% aplayer "Podcast Episode" "Host Name" "https://example.com/audio.mp3" %}
```

### Audio (Alternative simple)

**Syntaxe :**
```markdown
{% audio /path/to/audio.mp3 %}
```

**Exemples :**
```markdown
<!-- Audio simple -->
{% audio /music/track.mp3 %}

<!-- URL externe -->
{% audio https://example.com/podcast.mp3 %}
```

---

## 🖼️ Images

### Image avec légende

```markdown
{% img /path/to/image.jpg "Texte alternatif" "Légende de l'image" %}
```

**Exemple :**
```markdown
{% img /images/screenshot.png "Capture d'écran" "Interface de l'application v2.0" %}
```

---

## 💬 Citations

### Citation avec auteur

```markdown
{% quote Auteur %}
Texte de la citation ici.
{% endquote %}
```

**Exemple :**
```markdown
{% quote Linus Torvalds %}
Talk is cheap. Show me the code.
{% endquote %}
```

---

## 📝 Boîtes de notes

### Types disponibles

```markdown
{% note info %}
Message informatif
{% endnote %}

{% note warning %}
Message d'avertissement
{% endnote %}

{% note success %}
Message de succès
{% endnote %}

{% note error %}
Message d'erreur
{% endnote %}
```

**Rendu :**
- 🔵 **info** - Fond bleu clair
- 🟠 **warning** - Fond orange clair
- 🟢 **success** - Fond vert clair
- 🔴 **error** - Fond rouge clair

**Exemple :**
```markdown
{% note warning %}
⚠️ **Attention** : Cette commande supprimera tous vos fichiers.
Assurez-vous d'avoir une sauvegarde avant de continuer.
{% endnote %}
```

---

## 📦 Section repliable (Collapse)

```markdown
{% collapse Titre de la section %}
Contenu caché par défaut.

- Liste
- D'éléments

Plus de texte...
{% endcollapse %}
```

**Exemple :**
```markdown
{% collapse Solution de l'exercice %}
La réponse est 42.

Explication détaillée ici...
{% endcollapse %}
```

---

## 🔘 Boutons

**Syntaxe complète :**
```markdown
{% button URL "Texte du bouton" %}
```

**Syntaxe courte (alias) :**
```markdown
{% btn URL "Texte du bouton" %}
```

**Exemples :**
```markdown
{% button https://cybermind.fr "Visiter le blog" %}
{% btn https://github.com/user/repo "Voir sur GitHub" %}
```

Les deux tags produisent exactement le même résultat.

---

## 💻 Code externes

### GitHub Gist

```markdown
{% gist username/gist_id %}
```

**Exemple :**
```markdown
{% gist torvalds/1f1e47f234567890abcdef %}
```

### CodePen

```markdown
{% codepen username/pen_id %}
{% codepen username/pen_id 600 %}  <!-- avec hauteur personnalisée -->
```

**Exemple :**
```markdown
{% codepen cybermind/aBcDeF %}
{% codepen cybermind/xYzAbC 800 %}
```

---

## 📚 Exemples d'utilisation

### Article avec vidéo et notes

```markdown
---
title: "Tutoriel Linux"
date: 2025-12-16
categories:
  - tutorials
tags:
  - linux
  - command-line
---

# Introduction

Bienvenue dans ce tutoriel sur les commandes Linux essentielles.

{% note info %}
Ce tutoriel suppose que vous utilisez une distribution Linux basée sur Debian (Ubuntu, Mint, etc.).
{% endnote %}

## Vidéo de démonstration

{% youtuber dQw4w9WgXcQ %}

## Commandes importantes

{% note warning %}
Les commandes suivantes nécessitent les privilèges root.
{% endnote %}

\`\`\`bash
sudo apt update
sudo apt upgrade
\`\`\`

{% collapse Explications détaillées %}
La commande `apt update` met à jour la liste des paquets disponibles.
La commande `apt upgrade` installe les mises à jour.
{% endcollapse %}
```

### Article avec images et citations

```markdown
---
title: "Architecture ARM"
date: 2025-12-16
categories:
  - embedded
---

# Les processeurs ARM

{% img /images/arm-architecture.png "Architecture ARM" "Schéma de l'architecture ARM Cortex" %}

{% quote Alan Kay %}
The best way to predict the future is to invent it.
{% endquote %}

## En savoir plus

{% button https://arm.com "Documentation officielle ARM" %}
```

---

## 🎨 Styles personnalisables

Tous les styles de ces tags sont dans `themes/cybermind/source/css/style.css` et peuvent être personnalisés :

```css
/* Note boxes */
.note-info { background: rgba(59, 130, 246, 0.1); }
.note-warning { background: rgba(245, 158, 11, 0.1); }
.note-success { background: rgba(16, 185, 129, 0.1); }
.note-error { background: rgba(239, 68, 68, 0.1); }

/* YouTube/Vimeo embeds */
.youtube-embed, .vimeo-embed {
    border-radius: 12px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.3);
}
```

---

## 🔧 Créer vos propres tags

Ajoutez de nouveaux tags dans `themes/cybermind/scripts/` :

```javascript
// themes/cybermind/scripts/custom-tags.js
hexo.extend.tag.register('mon_tag', function(args, content) {
    return `<div class="mon-tag">${content}</div>`;
}, {ends: true});
```

Puis ajoutez les styles correspondants dans `style.css`.

---

## ❓ Troubleshooting

### Tag non reconnu

Si vous obtenez une erreur `unknown block tag`, vérifiez que :
1. Les fichiers dans `themes/cybermind/scripts/` existent
2. Hexo a été redémarré : `hexo clean && hexo generate`
3. La syntaxe du tag est correcte

### Rendu incorrect

Si un tag ne s'affiche pas correctement :
1. Inspectez le HTML généré
2. Vérifiez les styles CSS
3. Assurez-vous qu'il n'y a pas de conflit avec d'autres plugins

---

## 📖 Ressources

- Documentation Hexo Tags : https://hexo.io/api/tag
- Documentation Hexo Helpers : https://hexo.io/api/helper

---

**Note** : Ces tags sont spécifiques au thème CyberMind. Si vous changez de thème, vous devrez adapter vos articles ou recréer ces tags.
