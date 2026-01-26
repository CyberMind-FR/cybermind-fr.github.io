import React, { useState } from 'react';

const sections = [
  {
    id: 'formula',
    emoji: '⚡',
    title: 'Formule Universelle',
    content: {
      code: '[RÔLE] + [CONTEXTE] + [TÂCHE] + [FORMAT] + [CONTRAINTES]',
      note: 'Cette structure de base s\'applique à 90% des prompts efficaces.'
    }
  },
  {
    id: 'techniques',
    emoji: '🔥',
    title: 'Techniques Core',
    content: {
      table: [
        { tech: '🧠 CoT', pattern: '"Réfléchis étape par étape"', usage: 'Raisonnement complexe' },
        { tech: '🎭 Persona', pattern: '"Tu es un [expert] avec 20 ans en [X]"', usage: 'Expertise ciblée' },
        { tech: '📚 Few-Shot', pattern: '"Exemples: A→B, C→D. Traite: E"', usage: 'Format précis' },
        { tech: '🔄 Multi-Path', pattern: '"3 approches, puis synthèse"', usage: 'Exploration créative' },
        { tech: '🪞 Méta', pattern: '"Identifie les biais de ma question"', usage: 'Qualité de réflexion' }
      ]
    }
  },
  {
    id: 'recursion',
    emoji: '🌀',
    title: 'Niveaux de Récursion',
    content: {
      levels: [
        { level: 1, name: 'Auto-Critique Simple', status: '✅', code: 'Réponds, puis: "Qu\'est-ce qui est faible?"', fixpoint: '1 itération suffit pour 80% des cas' },
        { level: 2, name: 'Simulation d\'Expert', status: '✅', code: 'Réponds comme si [expert] allait critiquer', fixpoint: 'L\'expert simulé n\'a plus rien à dire' },
        { level: 3, name: 'Meta-Pattern', status: '⚠️', code: 'Observe tes patterns sur [N] échanges', fixpoint: 'Changement améliore vraiment' },
        { level: '4+', name: 'Éviter', status: '❌', code: 'Analyser l\'analyse de l\'analyse...', fixpoint: 'STOP après 3 boucles' }
      ]
    }
  },
  {
    id: 'secubox',
    emoji: '🛡️',
    title: 'Sécurité & SecuBox',
    content: {
      prompts: [
        { name: '🔐 Audit OpenWrt', code: 'Analyse cette config UCI comme un auditeur ANSSI.\nChecklist: firewall rules, services exposés, credentials.\nSortie: tableau [finding | criticité | remediation].' },
        { name: '🐝 Règles CrowdSec', code: 'Crée un scenario CrowdSec pour [pattern d\'attaque].\nFormat YAML: filter, groupby, blackhole, labels.' },
        { name: '📋 Doc ANSSI', code: 'Rédige section [X] du dossier de validation.\nStyle: formel, référencé ISO27001, preuves factuelles.' }
      ]
    }
  },
  {
    id: 'esoteric',
    emoji: '🔮',
    title: 'Création Ésotérique',
    content: {
      prompts: [
        { name: '☯️ Yi Jing', code: 'Hexagramme: [n°] [nom].\nInterprète avec: lignes mutantes, hexagramme dérivé,\nconseil actionnable pour [domaine].' },
        { name: '📐 Géométrie Sacrée', code: 'Génère SVG [Fleur de Vie/Métatron].\nProportions basées sur [Phi/π].' },
        { name: '✨ Poésie → Suno', code: 'Transforme en paroles Suno:\n- Structure: [couplet/refrain/bridge]\n- Style: [genre + mood + tempo]' }
      ]
    }
  },
  {
    id: 'formulas',
    emoji: '🎯',
    title: 'Formules Récursives',
    content: {
      formulas: [
        { name: '🔁 Triple Miroir', code: '[Requête]. Réponds. Critique (3 faiblesses). Version finale.' },
        { name: '🐍 Ouroboros', code: 'Génère [créatif]. "Si c\'était un hexagramme?" Transforme la ligne mutante.' },
        { name: '🔐 Pentest de Soi', code: 'Propose [solution]. Attaque-la. Défends. Livre version durcie.' },
        { name: '⚖️ Point Fixe', code: 'Itère jusqu\'à v(n) ≈ v(n-1). Max 5 itérations.' }
      ]
    }
  },
  {
    id: 'modifiers',
    emoji: '🎛️',
    title: 'Modificateurs',
    content: {
      mods: [
        { emoji: '🎯', mod: '"Pas de préambule"', effect: 'Direct au résultat' },
        { emoji: '📏', mod: '"Max [N] lignes"', effect: 'Concision forcée' },
        { emoji: '🔬', mod: '"Niveau expert"', effect: 'Profondeur technique' },
        { emoji: '🎨', mod: '"Safe → audacieux"', effect: 'Spectre créatif' },
        { emoji: '⚖️', mod: '"Avocat du diable"', effect: 'Contre-argumentation' },
        { emoji: '🔄', mod: '"Itère 3x"', effect: 'Raffinement' },
        { emoji: '🚫', mod: '"Sans jargon"', effect: 'Style épuré' }
      ]
    }
  },
  {
    id: 'stops',
    emoji: '🌟',
    title: 'Heuristiques d\'Arrêt',
    content: {
      signals: [
        { signal: '🟢', condition: 'Amélioration claire v(n) vs v(n-1)', action: 'Continue' },
        { signal: '🟡', condition: 'Changements cosmétiques', action: '1 dernière max' },
        { signal: '🔴', condition: 'Dégradation/sur-complexification', action: 'Reviens v(n-1)' },
        { signal: '⚫', condition: '3ème boucle sans gain', action: 'STOP + note' }
      ]
    }
  }
];

const hexagram = `
     ━━━━━━━  Clarté de l'arrêt
     ━━ ━━   Espace pour l'émergence
     ━━━━━━━  Boucle qui sait se borner
     ━━ ━━   Critique intégrée
     ━━━━━━━  Application concrète
     ━━━━━━━  Honnêteté sur les limites
`;

export default function ClaudeGodmodeQuicksheet() {
  const [activeSection, setActiveSection] = useState('formula');
  const [copiedCode, setCopiedCode] = useState(null);

  const copyToClipboard = (text, id) => {
    navigator.clipboard.writeText(text);
    setCopiedCode(id);
    setTimeout(() => setCopiedCode(null), 2000);
  };

  const renderContent = (section) => {
    const { content } = section;
    
    if (content.code) {
      return (
        <div className="space-y-4">
          <div 
            className="relative group cursor-pointer"
            onClick={() => copyToClipboard(content.code, 'main')}
          >
            <pre className="bg-slate-900 text-amber-300 p-4 rounded-lg font-mono text-sm overflow-x-auto border border-amber-500/30 hover:border-amber-400 transition-all">
              {content.code}
            </pre>
            <span className="absolute top-2 right-2 text-xs text-slate-400 group-hover:text-amber-400">
              {copiedCode === 'main' ? '✓ Copié!' : 'Cliquer pour copier'}
            </span>
          </div>
          {content.note && <p className="text-slate-300 italic text-sm">{content.note}</p>}
        </div>
      );
    }

    if (content.table) {
      return (
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="bg-gradient-to-r from-indigo-900 to-purple-900">
                <th className="p-3 text-left text-amber-300 font-semibold">Technique</th>
                <th className="p-3 text-left text-amber-300 font-semibold">Pattern</th>
                <th className="p-3 text-left text-amber-300 font-semibold">Usage</th>
              </tr>
            </thead>
            <tbody>
              {content.table.map((row, i) => (
                <tr key={i} className={`${i % 2 === 0 ? 'bg-slate-800/50' : 'bg-slate-900/50'} hover:bg-indigo-900/30 transition-colors`}>
                  <td className="p-3 font-medium">{row.tech}</td>
                  <td className="p-3 font-mono text-cyan-300 text-xs">{row.pattern}</td>
                  <td className="p-3 text-slate-300">{row.usage}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      );
    }

    if (content.levels) {
      return (
        <div className="space-y-3">
          {content.levels.map((lvl, i) => (
            <div key={i} className={`p-4 rounded-lg border ${
              lvl.status === '✅' ? 'border-green-500/30 bg-green-900/10' :
              lvl.status === '⚠️' ? 'border-yellow-500/30 bg-yellow-900/10' :
              'border-red-500/30 bg-red-900/10'
            }`}>
              <div className="flex items-center gap-2 mb-2">
                <span className="text-lg">{lvl.status}</span>
                <span className="font-bold text-white">Niveau {lvl.level}: {lvl.name}</span>
              </div>
              <pre 
                className="bg-slate-900 p-2 rounded text-cyan-300 font-mono text-xs cursor-pointer hover:bg-slate-800 transition-colors"
                onClick={() => copyToClipboard(lvl.code, `lvl-${i}`)}
              >
                {lvl.code}
                {copiedCode === `lvl-${i}` && <span className="ml-2 text-green-400">✓</span>}
              </pre>
              <p className="text-slate-400 text-xs mt-2">🎯 Point fixe: {lvl.fixpoint}</p>
            </div>
          ))}
        </div>
      );
    }

    if (content.prompts) {
      return (
        <div className="space-y-4">
          {content.prompts.map((p, i) => (
            <div key={i} className="group">
              <h4 className="font-semibold text-amber-300 mb-2">{p.name}</h4>
              <pre 
                className="bg-slate-900 p-3 rounded-lg text-cyan-300 font-mono text-xs whitespace-pre-wrap cursor-pointer border border-slate-700 hover:border-cyan-500 transition-all"
                onClick={() => copyToClipboard(p.code, `prompt-${i}`)}
              >
                {p.code}
                {copiedCode === `prompt-${i}` && <span className="block mt-2 text-green-400">✓ Copié!</span>}
              </pre>
            </div>
          ))}
        </div>
      );
    }

    if (content.formulas) {
      return (
        <div className="grid gap-3">
          {content.formulas.map((f, i) => (
            <div 
              key={i} 
              className="p-3 bg-gradient-to-r from-slate-800 to-slate-900 rounded-lg border border-slate-700 hover:border-amber-500 cursor-pointer transition-all"
              onClick={() => copyToClipboard(f.code, `formula-${i}`)}
            >
              <div className="flex justify-between items-start">
                <span className="font-bold text-white">{f.name}</span>
                {copiedCode === `formula-${i}` && <span className="text-green-400 text-xs">✓</span>}
              </div>
              <p className="text-cyan-300 font-mono text-xs mt-1">{f.code}</p>
            </div>
          ))}
        </div>
      );
    }

    if (content.mods) {
      return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
          {content.mods.map((m, i) => (
            <div 
              key={i} 
              className="flex items-center gap-3 p-2 bg-slate-800/50 rounded hover:bg-slate-700/50 cursor-pointer transition-all"
              onClick={() => copyToClipboard(m.mod, `mod-${i}`)}
            >
              <span className="text-xl">{m.emoji}</span>
              <div className="flex-1">
                <code className="text-amber-300 text-xs">{m.mod}</code>
                <p className="text-slate-400 text-xs">{m.effect}</p>
              </div>
              {copiedCode === `mod-${i}` && <span className="text-green-400 text-xs">✓</span>}
            </div>
          ))}
        </div>
      );
    }

    if (content.signals) {
      return (
        <div className="space-y-2">
          {content.signals.map((s, i) => (
            <div key={i} className="flex items-center gap-4 p-3 bg-slate-800/50 rounded-lg">
              <span className="text-2xl">{s.signal}</span>
              <div className="flex-1">
                <p className="text-white text-sm">{s.condition}</p>
              </div>
              <span className="text-amber-300 font-bold text-sm">{s.action}</span>
            </div>
          ))}
        </div>
      );
    }

    return null;
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-indigo-950 to-slate-950 text-white p-4 font-sans">
      {/* Decorative background elements */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-20 left-10 w-64 h-64 bg-purple-500/5 rounded-full blur-3xl"></div>
        <div className="absolute bottom-20 right-10 w-96 h-96 bg-cyan-500/5 rounded-full blur-3xl"></div>
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-amber-500/3 rounded-full blur-3xl"></div>
      </div>

      <div className="relative max-w-4xl mx-auto">
        {/* Header */}
        <header className="text-center py-8 mb-6">
          <div className="text-6xl mb-4 animate-pulse">🧙‍♂️</div>
          <h1 className="text-3xl md:text-4xl font-bold bg-gradient-to-r from-amber-300 via-yellow-200 to-amber-300 bg-clip-text text-transparent">
            CLAUDE GODMODE
          </h1>
          <h2 className="text-xl md:text-2xl text-indigo-300 mt-2">QUICKSHEET RÉCURSIF</h2>
          <p className="text-slate-400 mt-2 text-sm">Le Modèle qui se Modélise • Par Gandalf • CyberMind.FR</p>
          <div className="mt-4 text-amber-500/50 font-mono text-xs">
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
          </div>
        </header>

        {/* Navigation */}
        <nav className="flex flex-wrap justify-center gap-2 mb-6 p-2 bg-slate-900/50 rounded-xl backdrop-blur-sm border border-slate-800">
          {sections.map(s => (
            <button
              key={s.id}
              onClick={() => setActiveSection(s.id)}
              className={`px-3 py-2 rounded-lg text-sm font-medium transition-all ${
                activeSection === s.id 
                  ? 'bg-gradient-to-r from-amber-500 to-orange-500 text-slate-900 shadow-lg shadow-amber-500/25' 
                  : 'text-slate-300 hover:text-white hover:bg-slate-800'
              }`}
            >
              <span className="mr-1">{s.emoji}</span>
              <span className="hidden sm:inline">{s.title}</span>
            </button>
          ))}
        </nav>

        {/* Active Section Content */}
        <main className="bg-slate-900/70 backdrop-blur-sm rounded-2xl p-6 border border-slate-800 shadow-2xl">
          {sections.filter(s => s.id === activeSection).map(section => (
            <div key={section.id}>
              <h3 className="text-2xl font-bold mb-6 flex items-center gap-3">
                <span className="text-3xl">{section.emoji}</span>
                <span className="bg-gradient-to-r from-white to-slate-300 bg-clip-text text-transparent">
                  {section.title}
                </span>
              </h3>
              {renderContent(section)}
            </div>
          ))}
        </main>

        {/* Hexagram Philosophy */}
        <section className="mt-8 text-center">
          <h3 className="text-xl font-bold text-amber-300 mb-4">💎 Philosophie Gandalf</h3>
          <pre className="inline-block text-left bg-gradient-to-br from-indigo-900/50 to-purple-900/50 p-6 rounded-xl text-amber-200/80 font-mono text-xs border border-amber-500/20">
{hexagram}
          </pre>
          <p className="mt-6 text-lg italic text-slate-300">
            "La récursion parfaite sait quand devenir action."
          </p>
          <div className="mt-2 text-2xl">🐍♾️→🎯</div>
        </section>

        {/* Footer */}
        <footer className="mt-8 text-center text-slate-500 text-xs py-4 border-t border-slate-800">
          <p>🧙‍♂️ CyberMind.FR • 2025 • v1.0</p>
          <p className="mt-1">Consultant Cybersécurité • Poète • Explorateur du Yi Jing</p>
        </footer>
      </div>
    </div>
  );
}
