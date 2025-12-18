/**
 * category-helpers.js - Helpers simples pour les catégories
 * 
 * Ce script ajoute uniquement des helpers utilisables dans les templates.
 * Toute la logique de filtrage est dans les templates EJS.
 */

'use strict';

// Configuration des catégories
const CATEGORIES = {
  'cybersecurity': { name: 'Cybersécurité', color: '#00ff88', icon: '🛡️' },
  'embedded': { name: 'Embarqué', color: '#ff6600', icon: '⚙️' },
  'linux': { name: 'Linux', color: '#ffcc00', icon: '🐧' },
  'creative': { name: 'Créativité', color: '#ff6699', icon: '🎨' },
  'philosophy': { name: 'Philosophie', color: '#9966ff', icon: '🧘' },
  'tutorials': { name: 'Tutoriels', color: '#66ccff', icon: '📖' },
};

// Helper simple pour obtenir les infos d'une catégorie
hexo.extend.helper.register('get_category_info', function(slug) {
  if (!slug) return { name: 'Catégorie', color: '#888888', icon: '📁' };
  const key = String(slug).toLowerCase();
  return CATEGORIES[key] || { name: slug, color: '#888888', icon: '📁' };
});

// Helper pour lister toutes les catégories
hexo.extend.helper.register('get_all_categories', function() {
  return Object.keys(CATEGORIES).map(slug => ({ slug, ...CATEGORIES[slug] }));
});

hexo.log.info('[category-helpers] Chargé - ' + Object.keys(CATEGORIES).length + ' catégories');
