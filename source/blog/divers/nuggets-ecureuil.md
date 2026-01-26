---
title: Nuggets d'Écureuil
subtitle: Petits carrés fondants choco-cacahuète
date: 2026-01-12
categories:
  - Recettes
tags:
  - chocolat
  - cacahuète
  - dessert
  - brownie
  - recette maison
cover: /images/recipes/nuggets-ecureuil-cover.jpg
thumbnail: /images/recipes/nuggets-ecureuil-thumb.jpg
---

<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=Bebas+Neue&display=swap" rel="stylesheet">
<style>
:root {
  --cream: #F5E6D3;
  --paper: #FDF8F0;
  --brown-dark: #3D2314;
  --brown-medium: #6B4423;
  --brown-light: #8B5A2B;
  --rust: #A0522D;
  --orange-vintage: #D2691E;
  --gold: #B8860B;
}
.vintage-recipe {
  font-family: 'Crimson Text', Georgia, serif;
  background: var(--paper);
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E"), linear-gradient(135deg, var(--paper) 0%, #EDE4D4 50%, var(--paper) 100%);
  background-blend-mode: soft-light, normal;
  color: var(--brown-dark);
  padding: 25px 30px;
  position: relative;
  border: 2px solid var(--brown-medium);
}
.vintage-recipe::before {
  content: '';
  position: absolute;
  top: 6px;
  left: 6px;
  right: 6px;
  bottom: 6px;
  border: 1px solid var(--brown-light);
  pointer-events: none;
}
.vintage-recipe::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(ellipse at 20% 80%, rgba(139, 90, 43, 0.08) 0%, transparent 50%), radial-gradient(ellipse at 80% 20%, rgba(139, 90, 43, 0.06) 0%, transparent 50%);
  pointer-events: none;
}
.magazine-header {
  text-align: center;
  border-bottom: 3px double var(--brown-medium);
  padding-bottom: 10px;
  margin-bottom: 15px;
  position: relative;
  z-index: 1;
}
.magazine-name {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 14px;
  letter-spacing: 8px;
  color: var(--rust);
  text-transform: uppercase;
  margin: 0;
}
.magazine-tagline {
  font-family: 'Crimson Text', serif;
  font-style: italic;
  font-size: 12px;
  color: var(--brown-light);
  margin-top: 3px;
}
.title-section {
  text-align: center;
  margin: 20px 0 25px;
  position: relative;
  z-index: 1;
}
.title-deco {
  font-family: 'Playfair Display', serif;
  font-size: 12px;
  letter-spacing: 4px;
  color: var(--gold);
  text-transform: uppercase;
  margin-bottom: 8px;
}
.main-title {
  font-family: 'Playfair Display', serif;
  font-weight: 900;
  font-size: 48px;
  line-height: 0.95;
  color: var(--brown-dark);
  text-transform: uppercase;
  letter-spacing: 2px;
  text-shadow: 2px 2px 0 var(--cream);
  margin: 0;
}
.main-title .highlight {
  color: var(--orange-vintage);
  font-style: italic;
  display: block;
  font-size: 54px;
}
.subtitle {
  font-family: 'Crimson Text', serif;
  font-style: italic;
  font-size: 18px;
  color: var(--brown-medium);
  margin-top: 10px;
}
.squirrel-deco {
  font-size: 32px;
  position: absolute;
  right: 15px;
  top: 50%;
  transform: translateY(-50%) rotate(15deg);
  opacity: 0.8;
}
.info-banner {
  display: flex;
  justify-content: center;
  gap: 25px;
  flex-wrap: wrap;
  background: var(--brown-dark);
  color: var(--cream);
  padding: 10px 20px;
  margin: 0 -30px 20px;
  font-family: 'Bebas Neue', sans-serif;
  font-size: 14px;
  letter-spacing: 2px;
  position: relative;
  z-index: 1;
}
.info-banner span {
  display: flex;
  align-items: center;
  gap: 5px;
}
.main-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 25px;
  position: relative;
  z-index: 1;
}
@media (max-width: 700px) {
  .main-layout {
    grid-template-columns: 1fr;
  }
}
.images-section {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.main-image {
  position: relative;
  border: 4px solid var(--brown-dark);
  box-shadow: 4px 4px 0 var(--brown-light);
  overflow: hidden;
}
.main-image img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  filter: sepia(20%) contrast(1.05) saturate(0.9);
  display: block;
}
.image-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(61, 35, 20, 0.85);
  color: var(--cream);
  font-family: 'Crimson Text', serif;
  font-style: italic;
  font-size: 12px;
  padding: 6px 10px;
  text-align: center;
}
.small-images {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}
.small-image {
  border: 3px solid var(--brown-medium);
  position: relative;
  overflow: hidden;
}
.small-image img {
  width: 100%;
  height: 100px;
  object-fit: cover;
  filter: sepia(25%) contrast(1.05) saturate(0.85);
  display: block;
}
.small-image .step-number {
  position: absolute;
  top: -1px;
  left: -1px;
  width: 24px;
  height: 24px;
  background: var(--orange-vintage);
  color: var(--cream);
  font-family: 'Bebas Neue', sans-serif;
  font-size: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0 0 8px 0;
}
.ingredients-section {
  background: linear-gradient(135deg, var(--cream) 0%, #EDE0CC 100%);
  border: 2px solid var(--brown-medium);
  padding: 18px 20px;
  position: relative;
}
.ingredients-section::before {
  content: '✦';
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--paper);
  padding: 0 10px;
  color: var(--gold);
  font-size: 18px;
}
.section-title {
  font-family: 'Playfair Display', serif;
  font-weight: 700;
  font-size: 20px;
  text-align: center;
  color: var(--brown-dark);
  text-transform: uppercase;
  letter-spacing: 3px;
  margin: 0 0 12px 0;
  border-bottom: 1px solid var(--brown-light);
  padding-bottom: 8px;
}
.ingredients-list {
  columns: 2;
  column-gap: 20px;
  font-size: 14px;
  line-height: 2;
  list-style: none;
  padding: 0;
  margin: 0;
}
.ingredients-list li {
  break-inside: avoid;
  padding-left: 15px;
  position: relative;
}
.ingredients-list li::before {
  content: '◆';
  position: absolute;
  left: 0;
  color: var(--orange-vintage);
  font-size: 8px;
  top: 5px;
}
.ingredients-list strong {
  color: var(--brown-dark);
  font-weight: 600;
}
.preparation-section {
  margin-top: 20px;
  grid-column: 1 / -1;
}
.prep-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 24px;
  letter-spacing: 4px;
  color: var(--brown-dark);
  text-align: center;
  margin: 0 0 15px 0;
}
.prep-title::before, .prep-title::after {
  content: '═══════';
  color: var(--gold);
  font-size: 10px;
  vertical-align: middle;
  margin: 0 12px;
}
.steps-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 15px;
}
@media (max-width: 700px) {
  .steps-grid {
    grid-template-columns: 1fr 1fr;
  }
}
@media (max-width: 500px) {
  .steps-grid {
    grid-template-columns: 1fr;
  }
}
.step {
  background: var(--cream);
  border: 1px solid var(--brown-light);
  padding: 12px;
  position: relative;
  font-size: 13px;
  line-height: 1.5;
}
.step-num {
  position: absolute;
  top: -10px;
  left: 10px;
  background: var(--rust);
  color: var(--cream);
  font-family: 'Bebas Neue', sans-serif;
  font-size: 16px;
  width: 26px;
  height: 26px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
}
.step-title {
  font-family: 'Playfair Display', serif;
  font-weight: 700;
  font-size: 13px;
  color: var(--brown-dark);
  margin: 8px 0 5px 0;
}
.tip-section {
  grid-column: 1 / -1;
  margin-top: 15px;
  display: flex;
  align-items: center;
  gap: 12px;
  background: linear-gradient(90deg, var(--orange-vintage), var(--rust));
  color: var(--cream);
  padding: 12px 18px;
}
.tip-icon {
  font-size: 30px;
  flex-shrink: 0;
}
.tip-text {
  font-style: italic;
  font-size: 14px;
  line-height: 1.5;
  margin: 0;
}
.tip-text strong {
  font-family: 'Bebas Neue', sans-serif;
  font-style: normal;
  letter-spacing: 1px;
  color: var(--cream);
}
.magazine-footer {
  margin-top: 20px;
  text-align: center;
  border-top: 2px solid var(--brown-medium);
  padding-top: 12px;
  position: relative;
  z-index: 1;
}
.footer-deco {
  font-family: 'Playfair Display', serif;
  font-style: italic;
  font-size: 24px;
  color: var(--brown-dark);
  margin: 0;
}
.footer-year {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 12px;
  letter-spacing: 3px;
  color: var(--brown-light);
  margin-top: 5px;
}
</style>
<div class="vintage-recipe">
<header class="magazine-header">
<p class="magazine-name">La Cuisine de Maurienne</p>
<p class="magazine-tagline">Les recettes authentiques du terroir alpin</p>
</header>
<section class="title-section">
<div class="title-deco">✦ Recette Originale ✦</div>
<h1 class="main-title">Nuggets<span class="highlight">d'Écureuil</span></h1>
<p class="subtitle">Petits carrés fondants choco-cacahuète</p>
<span class="squirrel-deco">🐿️</span>
</section>
<div class="info-banner">
<span>🕐 25-30 MIN</span>
<span>🔥 180°C</span>
<span>🍫 28 PIÈCES</span>
<span>⭐ FACILE</span>
</div>
<div class="main-layout">
<div class="images-section">
<div class="main-image">
<img src="cuisson-four.jpg" alt="Nuggets au four">
<div class="image-caption">Sortie du four, croustillant à souhait !</div>
</div>
<div class="small-images">
<div class="small-image">
<span class="step-number">1</span>
<img src="preparation-oeufs.jpg" alt="Les œufs">
</div>
<div class="small-image">
<span class="step-number">2</span>
<img src="ajout-cacahuetes.jpg" alt="Les cacahuètes">
</div>
</div>
</div>
<div class="ingredients-section">
<h2 class="section-title">Ingrédients</h2>
<ul class="ingredients-list">
<li><strong>225 g</strong> de beurre</li>
<li><strong>115 g</strong> de chocolat noir</li>
<li><strong>4</strong> œufs entiers</li>
<li><strong>300 g</strong> de sucre semoule</li>
<li><strong>115 g</strong> de farine</li>
<li><strong>1 c.</strong> à café de vanille</li>
<li><strong>200 g</strong> de cacahuètes moulues</li>
</ul>
</div>
<section class="preparation-section">
<h2 class="prep-title">Préparation</h2>
<div class="steps-grid">
<div class="step">
<span class="step-num">1</span>
<p class="step-title">Préparation</p>
Préchauffer le four à 180°C. Beurrer un moule de 22,5 × 30 cm.
</div>
<div class="step">
<span class="step-num">2</span>
<p class="step-title">Bain-marie</p>
Faire fondre au bain-marie le beurre et le chocolat. Retirer et laisser tiédir.
</div>
<div class="step">
<span class="step-num">3</span>
<p class="step-title">Mélange</p>
Fouetter œufs et sucre jusqu'à obtenir un mélange pâle et mousseux. Ajouter la vanille.
</div>
<div class="step">
<span class="step-num">4</span>
<p class="step-title">Incorporation</p>
Incorporer le chocolat fondu avec le beurre, bien mélanger intimement.
</div>
<div class="step">
<span class="step-num">5</span>
<p class="step-title">Finition</p>
Tamiser et incorporer la farine. Ajouter les cacahuètes moulues en dernier.
</div>
<div class="step">
<span class="step-num">6</span>
<p class="step-title">Cuisson</p>
Verser dans le moule. Cuire 25 min. Laisser refroidir 30 min puis découper.
</div>
</div>
</section>
<div class="tip-section">
<span class="tip-icon">💡</span>
<p class="tip-text"><strong>SECRET DU CHEF :</strong> Le milieu doit être tout juste cuit ! Un nugget légèrement sous-cuit au centre sera parfaitement fondant une fois refroidi. Attention à ne pas dessécher la pâte.</p>
</div>
</div>
<footer class="magazine-footer">
<p class="footer-deco">Bon Appétit !</p>
<p class="footer-year">RECETTE MAISON • COLLECTION GOURMANDE</p>
</footer>
</div>
