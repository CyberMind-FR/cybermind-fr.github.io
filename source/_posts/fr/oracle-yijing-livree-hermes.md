---
title: "Oracle Yi Jing : La Livrée d'Hermès en Application Web"
date: 2025-12-16 17:45:00
updated: 2025-12-16 17:45:00
categories:
  - Projets
  - Spiritualité
tags:
  - Yi Jing
  - I Ching
  - Oracle
  - PWA
  - JavaScript
  - La Livrée d'Hermès
  - Divination
  - Taoïsme
thumbnail: /images/yijing-oracle-thumb.png
excerpt: "Découvrez l'Oracle Yi Jing en version web progressive, enrichi des grilles décoratives de La Livrée d'Hermès. Une application complète pour consulter le Livre des Transformations, disponible hors-ligne sur tous vos appareils."
---

## Le Yi Jing : Sagesse Millénaire

Le **Yi Jing** (易經), ou *Livre des Mutations*, est l'un des textes fondateurs de la pensée chinoise. Vieux de plus de trois mille ans, ce classique confucéen n'est pas qu'un simple oracle divinatoire : c'est un véritable traité philosophique sur le changement, l'équilibre des forces et la nature cyclique de l'existence.

Chaque consultation du Yi Jing génère un **hexagramme** — une figure composée de six traits, pleins (Yang ☰) ou brisés (Yin ☷). Ces 64 combinaisons possibles forment une cartographie complète des situations humaines et cosmiques.

## La Livrée d'Hermès : L'Art au Service de l'Oracle

Pour cette application, j'ai intégré les magnifiques **grilles décoratives** issues de *La Livrée d'Hermès*, un jeu de société ésotérique aux motifs géométriques violet et or. Chaque trait de l'hexagramme est représenté par une grille unique, créant une superposition visuelle qui révèle progressivement la figure divinatoire.

Les grilles distinguent :
- **Yang** (trait plein) : énergie active, créatrice, masculine
- **Yin** (trait brisé) : énergie réceptive, nourricière, féminine
- **Mutations** : traits en transformation, porteurs du changement à venir

## Les 64 Hexagrammes en Animation

Contemplez le défilement des 64 hexagrammes avec leurs grilles superposées dans cette démonstration interactive :

<div style="text-align: center; margin: 40px 0;">
<a href="/demos/64-hexagrammes-animation.html" target="_blank" rel="noopener" style="display: inline-block; background: linear-gradient(135deg, #12121a, #1a1a25); border: 2px solid rgba(212, 175, 55, 0.4); color: #d4af37; padding: 25px 50px; font-size: 1.4rem; font-weight: bold; text-decoration: none; border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.4); transition: all 0.3s ease;">
☯ Voir l'Animation des 64 Hexagrammes
</a>
<p style="margin-top: 15px; color: #9a9a9a; font-size: 0.9rem;">
Touches : ← → navigation • Espace pause • Vitesse réglable
</p>
</div>

## L'Application PWA : Votre Oracle de Poche

J'ai développé une **Progressive Web App** complète permettant de consulter l'oracle selon la méthode traditionnelle des trois pièces. L'application est :

✨ **Multilingue** : Français, Anglais, Allemand, Espagnol, Chinois  
📱 **Installable** : Fonctionne comme une app native sur mobile et desktop  
🔌 **Hors-ligne** : Consultez l'oracle sans connexion internet  
🎨 **Visuelle** : Grilles animées de La Livrée d'Hermès  
📜 **Complète** : Jugement, Image et traits mutants pour chaque hexagramme

<div style="text-align: center; margin: 40px 0;">
<a href="https://gkerma.github.io/yiking/" target="_blank" rel="noopener" style="display: inline-block; background: linear-gradient(135deg, #d4af37, #996515); color: #0a0a0f; padding: 18px 40px; font-size: 1.3rem; font-weight: bold; text-decoration: none; border-radius: 10px; box-shadow: 0 5px 20px rgba(212, 175, 55, 0.4); transition: all 0.3s ease;">
☯ Accéder à l'Oracle Yi Jing
</a>
</div>

## Comment Consulter l'Oracle

La méthode des **trois pièces** est la plus accessible pour interroger le Yi Jing :

1. **Formulez votre question** avec clarté et sincérité
2. **Lancez les pièces** six fois pour construire l'hexagramme
3. **Interprétez** le Jugement et l'Image de l'hexagramme obtenu
4. Si des **traits mutants** apparaissent, consultez également l'hexagramme de transformation

Chaque lancer produit une valeur :
- **6** = Vieux Yin (mutation vers Yang)
- **7** = Jeune Yang (stable)
- **8** = Jeune Yin (stable)
- **9** = Vieux Yang (mutation vers Yin)

Les traits mutants (6 et 9) indiquent les points de transformation de votre situation.

## Aspects Techniques

L'application est construite en **HTML/CSS/JavaScript** pur, sans framework, pour une légèreté maximale :

- **Service Worker** pour le fonctionnement hors-ligne
- **24 grilles PNG** encodées en base64 (intégrées au HTML)
- **64 hexagrammes** avec textes complets en 5 langues
- **Animations CSS** avec cubic-bezier pour la fluidité
- **LocalStorage** pour l'historique des tirages

Le code source est disponible et l'application peut être déployée sur n'importe quel hébergement statique (GitHub Pages, Netlify, etc.).

## Réflexions sur l'Oracle

> *"Le Livre des Mutations enseigne que la seule constante est le changement."*

Le Yi Jing ne prédit pas l'avenir de façon déterministe. Il offre plutôt un miroir de la situation présente et des tendances en cours. Comme tout outil de réflexion, sa valeur réside dans la qualité de l'introspection qu'il suscite.

Les hexagrammes fonctionnent comme des archétypes universels — *Le Créateur*, *Le Réceptif*, *La Difficulté Initiale*, *L'Attente*... — qui résonnent avec nos propres expériences et nous invitent à considérer notre situation sous un angle nouveau.

---

<div style="background: rgba(212, 175, 55, 0.1); border-left: 4px solid #d4af37; padding: 20px; margin: 30px 0; border-radius: 0 10px 10px 0;">

**Ressources complémentaires :**

- [Accéder à l'Oracle Yi Jing (PWA)](https://gkerma.github.io/yiking/)
- Wilhelm, Richard. *Yi King, Le Livre des Mutations*. Éditions Médicis.
- Javary, Cyrille. *Yi Jing, Le Livre des Changements*. Albin Michel.
- Amiot, Anibal Eldeberto. *La Livrée d'Hermès*. Groupe Facebook [AXIS MUNDI](https://www.facebook.com/groups/axismundi/)
- [GANIMED.FR](https://ganimed.fr) — Archive Résurrection

</div>

*Que les hexagrammes éclairent votre chemin.* ☯
