import React, { useState, useEffect, useCallback, useMemo } from 'react';

// ═══════════════════════════════════════════════════════════════════
// 🧙‍♂️ CLAUDE GODMODE LAB - L'Application Récursive
// ═══════════════════════════════════════════════════════════════════
// Cette application EST le prompt qu'elle décrit.
// Chaque composant incarne un principe du quicksheet.
// L'interface évolue en fonction de son propre usage.
// ═══════════════════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────────────────────
// DATA LAYER - Les Modèles Fondamentaux
// ─────────────────────────────────────────────────────────────────────

const PROMPT_PATTERNS = {
  formula: {
    id: 'formula',
    name: 'Formule Universelle',
    emoji: '⚡',
    template: '[RÔLE] + [CONTEXTE] + [TÂCHE] + [FORMAT] + [CONTRAINTES]',
    variables: ['role', 'context', 'task', 'format', 'constraints'],
    color: '#d4af37',
    connections: ['persona', 'cot', 'fewshot']
  },
  cot: {
    id: 'cot',
    name: 'Chain of Thought',
    emoji: '🧠',
    template: 'Réfléchis étape par étape avant de répondre.',
    variables: [],
    color: '#00d9ff',
    connections: ['meta', 'multipath']
  },
  persona: {
    id: 'persona',
    name: 'Persona Expert',
    emoji: '🎭',
    template: 'Tu es un [EXPERT] avec [N] ans d\'expérience en [DOMAINE].',
    variables: ['expert', 'years', 'domain'],
    color: '#e94560',
    connections: ['formula', 'fewshot']
  },
  fewshot: {
    id: 'fewshot',
    name: 'Few-Shot Learning',
    emoji: '📚',
    template: 'Exemples:\n[INPUT_1] → [OUTPUT_1]\n[INPUT_2] → [OUTPUT_2]\nMaintenant traite: [QUERY]',
    variables: ['input1', 'output1', 'input2', 'output2', 'query'],
    color: '#9d4edd',
    connections: ['formula', 'persona']
  },
  multipath: {
    id: 'multipath',
    name: 'Multi-Path',
    emoji: '🔄',
    template: 'Génère [N] approches différentes, puis synthétise la meilleure solution.',
    variables: ['paths'],
    color: '#4ade80',
    connections: ['cot', 'meta']
  },
  meta: {
    id: 'meta',
    name: 'Méta-Réflexion',
    emoji: '🪞',
    template: 'Avant de répondre, identifie les biais potentiels de cette question.',
    variables: [],
    color: '#fbbf24',
    connections: ['cot', 'recursion']
  },
  recursion: {
    id: 'recursion',
    name: 'Récursion Bornée',
    emoji: '🌀',
    template: 'Réponds. Critique ta réponse. Améliore. STOP après [N] itérations ou point fixe.',
    variables: ['maxIterations'],
    color: '#f472b6',
    connections: ['meta', 'pentest']
  },
  pentest: {
    id: 'pentest',
    name: 'Pentest de Soi',
    emoji: '🔐',
    template: 'Propose [SOLUTION]. Attaque-la comme un adversaire. Défends avec les attaques valides intégrées.',
    variables: ['solution'],
    color: '#ef4444',
    connections: ['recursion', 'secubox']
  },
  secubox: {
    id: 'secubox',
    name: 'Audit SecuBox',
    emoji: '🛡️',
    template: 'Analyse [CONFIG] comme un auditeur [AUTHORITY].\nSortie: [finding | criticité | remediation]',
    variables: ['config', 'authority'],
    color: '#06b6d4',
    connections: ['pentest', 'yijing']
  },
  yijing: {
    id: 'yijing',
    name: 'Oracle Yi Jing',
    emoji: '☯️',
    template: 'Hexagramme [N°]: [NOM]\nInterprète pour [CONTEXTE] avec lignes mutantes.',
    variables: ['hexNumber', 'hexName', 'context'],
    color: '#a78bfa',
    connections: ['secubox', 'ouroboros']
  },
  ouroboros: {
    id: 'ouroboros',
    name: 'Ouroboros Créatif',
    emoji: '🐍',
    template: 'Génère [CONTENU]. Si c\'était un hexagramme? Transforme la ligne mutante.',
    variables: ['content'],
    color: '#22d3ee',
    connections: ['yijing', 'formula']
  }
};

const RECURSION_LEVELS = [
  { level: 1, name: 'Auto-Critique', status: 'safe', description: '1 itération suffit pour 80%', color: '#4ade80' },
  { level: 2, name: 'Expert Simulé', status: 'safe', description: 'L\'expert n\'a plus rien à dire', color: '#4ade80' },
  { level: 3, name: 'Meta-Pattern', status: 'caution', description: 'Changement améliore vraiment', color: '#fbbf24' },
  { level: 4, name: 'Éviter', status: 'danger', description: 'Paralysie analytique', color: '#ef4444' }
];

const STOP_SIGNALS = [
  { signal: '🟢', condition: 'Amélioration claire', action: 'Continue', threshold: 0.7 },
  { signal: '🟡', condition: 'Changements cosmétiques', action: '1 dernière', threshold: 0.3 },
  { signal: '🔴', condition: 'Dégradation', action: 'Rollback', threshold: 0.1 },
  { signal: '⚫', condition: '3 boucles sans gain', action: 'STOP', threshold: 0 }
];

// ─────────────────────────────────────────────────────────────────────
// UTILITY HOOKS
// ─────────────────────────────────────────────────────────────────────

const useLocalStorage = (key, initialValue) => {
  const [value, setValue] = useState(() => {
    try {
      const item = typeof window !== 'undefined' ? window.localStorage?.getItem(key) : null;
      return item ? JSON.parse(item) : initialValue;
    } catch {
      return initialValue;
    }
  });

  useEffect(() => {
    try {
      if (typeof window !== 'undefined' && window.localStorage) {
        window.localStorage.setItem(key, JSON.stringify(value));
      }
    } catch {
      // Silently fail if localStorage is not available
    }
  }, [key, value]);

  return [value, setValue];
};

const useEvolution = (initialState) => {
  const [history, setHistory] = useState([{ state: initialState, timestamp: Date.now(), score: 1 }]);
  const [currentIndex, setCurrentIndex] = useState(0);

  const evolve = useCallback((newState, score = null) => {
    const prevScore = history[currentIndex]?.score || 0;
    const newScore = score ?? (prevScore + Math.random() * 0.2 - 0.05);
    
    setHistory(prev => [...prev.slice(0, currentIndex + 1), {
      state: newState,
      timestamp: Date.now(),
      score: Math.max(0, Math.min(1, newScore))
    }]);
    setCurrentIndex(prev => prev + 1);
  }, [history, currentIndex]);

  const rollback = useCallback(() => {
    if (currentIndex > 0) setCurrentIndex(prev => prev - 1);
  }, [currentIndex]);

  const getSignal = useCallback(() => {
    if (history.length < 2) return STOP_SIGNALS[0];
    const delta = history[currentIndex].score - history[currentIndex - 1].score;
    if (delta > 0.1) return STOP_SIGNALS[0];
    if (delta > 0) return STOP_SIGNALS[1];
    if (delta > -0.1) return STOP_SIGNALS[2];
    return STOP_SIGNALS[3];
  }, [history, currentIndex]);

  return {
    current: history[currentIndex]?.state,
    history,
    currentIndex,
    evolve,
    rollback,
    signal: getSignal()
  };
};

// ─────────────────────────────────────────────────────────────────────
// VISUALIZATION COMPONENTS
// ─────────────────────────────────────────────────────────────────────

const PatternNode = ({ pattern, x, y, isActive, onClick, connections, allPatterns }) => {
  const [hover, setHover] = useState(false);
  
  return (
    <g>
      {/* Connection lines */}
      {connections.map(connId => {
        const target = allPatterns[connId];
        if (!target) return null;
        return (
          <line
            key={connId}
            x1={x}
            y1={y}
            x2={target.x}
            y2={target.y}
            stroke={isActive ? pattern.color : '#333'}
            strokeWidth={isActive ? 2 : 1}
            strokeOpacity={isActive ? 0.8 : 0.3}
            strokeDasharray={isActive ? "none" : "4,4"}
          />
        );
      })}
      
      {/* Node circle */}
      <circle
        cx={x}
        cy={y}
        r={hover ? 35 : 30}
        fill={isActive ? pattern.color : '#1a1a2e'}
        stroke={pattern.color}
        strokeWidth={isActive ? 3 : 1}
        style={{ cursor: 'pointer', transition: 'all 0.3s ease' }}
        onClick={onClick}
        onMouseEnter={() => setHover(true)}
        onMouseLeave={() => setHover(false)}
      />
      
      {/* Emoji */}
      <text
        x={x}
        y={y + 6}
        textAnchor="middle"
        fontSize="20"
        style={{ pointerEvents: 'none' }}
      >
        {pattern.emoji}
      </text>
      
      {/* Label */}
      {hover && (
        <text
          x={x}
          y={y + 50}
          textAnchor="middle"
          fill="#fff"
          fontSize="12"
          fontWeight="bold"
        >
          {pattern.name}
        </text>
      )}
    </g>
  );
};

const PatternGraph = ({ patterns, activePattern, onSelect }) => {
  // Calculate positions in a circle
  const patternList = Object.values(patterns);
  const centerX = 200;
  const centerY = 200;
  const radius = 150;
  
  const positionedPatterns = useMemo(() => {
    const positioned = {};
    patternList.forEach((p, i) => {
      const angle = (i / patternList.length) * Math.PI * 2 - Math.PI / 2;
      positioned[p.id] = {
        ...p,
        x: centerX + Math.cos(angle) * radius,
        y: centerY + Math.sin(angle) * radius
      };
    });
    return positioned;
  }, [patternList]);

  return (
    <svg width="400" height="400" viewBox="0 0 400 400">
      <defs>
        <radialGradient id="bgGrad">
          <stop offset="0%" stopColor="#1a1a2e" />
          <stop offset="100%" stopColor="#0a0a1a" />
        </radialGradient>
        <filter id="glow">
          <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
          <feMerge>
            <feMergeNode in="coloredBlur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>
      </defs>
      
      <circle cx={centerX} cy={centerY} r="190" fill="url(#bgGrad)" stroke="#333" strokeWidth="1"/>
      
      {/* Center symbol */}
      <text x={centerX} y={centerY + 8} textAnchor="middle" fontSize="30" filter="url(#glow)">
        🧙‍♂️
      </text>
      
      {Object.values(positionedPatterns).map(p => (
        <PatternNode
          key={p.id}
          pattern={p}
          x={p.x}
          y={p.y}
          isActive={activePattern === p.id}
          onClick={() => onSelect(p.id)}
          connections={p.connections}
          allPatterns={positionedPatterns}
        />
      ))}
    </svg>
  );
};

const RecursionMeter = ({ level, iterations, maxIterations }) => {
  const percentage = (iterations / maxIterations) * 100;
  const currentLevel = RECURSION_LEVELS[Math.min(level - 1, 3)];
  
  return (
    <div className="space-y-2">
      <div className="flex justify-between text-sm">
        <span>Niveau {level}: {currentLevel.name}</span>
        <span style={{ color: currentLevel.color }}>{currentLevel.status}</span>
      </div>
      <div className="h-3 bg-slate-800 rounded-full overflow-hidden">
        <div
          className="h-full transition-all duration-500"
          style={{
            width: `${percentage}%`,
            background: `linear-gradient(90deg, ${currentLevel.color}, ${currentLevel.color}88)`
          }}
        />
      </div>
      <p className="text-xs text-slate-400">{currentLevel.description}</p>
    </div>
  );
};

const EvolutionTimeline = ({ history, currentIndex, onSelect }) => {
  return (
    <div className="flex items-center gap-1 overflow-x-auto py-2">
      {history.map((entry, i) => (
        <button
          key={i}
          onClick={() => onSelect(i)}
          className={`w-8 h-8 rounded-full flex items-center justify-center text-xs transition-all ${
            i === currentIndex 
              ? 'bg-amber-500 text-slate-900 scale-110' 
              : 'bg-slate-700 text-slate-300 hover:bg-slate-600'
          }`}
          style={{
            opacity: 0.5 + entry.score * 0.5
          }}
        >
          {i + 1}
        </button>
      ))}
    </div>
  );
};

const SignalIndicator = ({ signal }) => {
  return (
    <div className="flex items-center gap-3 p-3 bg-slate-800/50 rounded-lg">
      <span className="text-2xl">{signal.signal}</span>
      <div className="flex-1">
        <p className="text-sm font-medium">{signal.condition}</p>
        <p className="text-xs text-slate-400">Action: {signal.action}</p>
      </div>
    </div>
  );
};

// ─────────────────────────────────────────────────────────────────────
// PROMPT BUILDER COMPONENT
// ─────────────────────────────────────────────────────────────────────

const PromptBuilder = ({ pattern, onGenerate }) => {
  const [variables, setVariables] = useState({});
  const [generated, setGenerated] = useState('');

  const handleChange = (varName, value) => {
    setVariables(prev => ({ ...prev, [varName]: value }));
  };

  const generate = () => {
    let result = pattern.template;
    Object.entries(variables).forEach(([key, value]) => {
      const placeholder = new RegExp(`\\[${key.toUpperCase()}\\]`, 'g');
      result = result.replace(placeholder, value || `[${key.toUpperCase()}]`);
    });
    setGenerated(result);
    onGenerate?.(result);
  };

  const copyToClipboard = () => {
    navigator.clipboard.writeText(generated);
  };

  return (
    <div className="space-y-4">
      <div className="flex items-center gap-3 mb-4">
        <span className="text-3xl">{pattern.emoji}</span>
        <div>
          <h3 className="font-bold text-lg">{pattern.name}</h3>
          <p className="text-xs text-slate-400">Pattern ID: {pattern.id}</p>
        </div>
      </div>

      {/* Template preview */}
      <div className="p-3 bg-slate-900 rounded-lg border border-slate-700">
        <pre className="text-cyan-300 text-sm whitespace-pre-wrap font-mono">
          {pattern.template}
        </pre>
      </div>

      {/* Variable inputs */}
      {pattern.variables.length > 0 && (
        <div className="space-y-3">
          <h4 className="text-sm font-semibold text-amber-300">Variables</h4>
          {pattern.variables.map(v => (
            <div key={v}>
              <label className="text-xs text-slate-400 uppercase">{v}</label>
              <input
                type="text"
                value={variables[v] || ''}
                onChange={e => handleChange(v, e.target.value)}
                placeholder={`[${v.toUpperCase()}]`}
                className="w-full mt-1 p-2 bg-slate-800 border border-slate-600 rounded text-white text-sm focus:border-amber-500 focus:outline-none"
              />
            </div>
          ))}
        </div>
      )}

      {/* Generate button */}
      <button
        onClick={generate}
        className="w-full py-3 bg-gradient-to-r from-amber-500 to-orange-500 text-slate-900 font-bold rounded-lg hover:from-amber-400 hover:to-orange-400 transition-all"
      >
        ⚡ Générer le Prompt
      </button>

      {/* Generated output */}
      {generated && (
        <div className="relative">
          <div 
            className="p-4 bg-slate-900 rounded-lg border border-amber-500/30 cursor-pointer hover:border-amber-500"
            onClick={copyToClipboard}
          >
            <pre className="text-green-300 text-sm whitespace-pre-wrap font-mono">
              {generated}
            </pre>
          </div>
          <span className="absolute top-2 right-2 text-xs text-slate-500">
            Cliquer pour copier
          </span>
        </div>
      )}
    </div>
  );
};

// ─────────────────────────────────────────────────────────────────────
// COLLABORATIVE WORKSPACE
// ─────────────────────────────────────────────────────────────────────

const CollaborativeWorkspace = ({ onPromptCreated }) => {
  const [mode, setMode] = useState('compose'); // compose, iterate, evolve
  const [prompt, setPrompt] = useState('');
  const [iterations, setIterations] = useState([]);
  const [currentIteration, setCurrentIteration] = useState(0);

  const addIteration = (critique, improved) => {
    setIterations(prev => [...prev, { original: prompt, critique, improved, timestamp: Date.now() }]);
    setPrompt(improved);
    setCurrentIteration(prev => prev + 1);
  };

  const applyRecursion = () => {
    // Simulate self-critique
    const critiques = [
      "Manque de spécificité dans le rôle",
      "Format de sortie non défini",
      "Contraintes trop vagues",
      "Pas d'exemples fournis"
    ];
    const randomCritique = critiques[Math.floor(Math.random() * critiques.length)];
    
    // Auto-improve suggestion
    const improved = prompt + `\n\n[AMÉLIORATION: ${randomCritique}]`;
    addIteration(randomCritique, improved);
  };

  return (
    <div className="space-y-4">
      {/* Mode selector */}
      <div className="flex gap-2">
        {['compose', 'iterate', 'evolve'].map(m => (
          <button
            key={m}
            onClick={() => setMode(m)}
            className={`px-4 py-2 rounded-lg text-sm font-medium transition-all ${
              mode === m 
                ? 'bg-amber-500 text-slate-900' 
                : 'bg-slate-700 text-slate-300 hover:bg-slate-600'
            }`}
          >
            {m === 'compose' && '✏️ Composer'}
            {m === 'iterate' && '🔄 Itérer'}
            {m === 'evolve' && '🧬 Évoluer'}
          </button>
        ))}
      </div>

      {/* Main textarea */}
      <textarea
        value={prompt}
        onChange={e => setPrompt(e.target.value)}
        placeholder="Compose ton prompt ici... La récursion s'appliquera automatiquement."
        className="w-full h-48 p-4 bg-slate-900 border border-slate-600 rounded-lg text-white font-mono text-sm focus:border-amber-500 focus:outline-none resize-none"
      />

      {/* Iteration controls */}
      {mode === 'iterate' && (
        <div className="space-y-3">
          <RecursionMeter 
            level={Math.min(currentIteration + 1, 4)} 
            iterations={currentIteration} 
            maxIterations={5} 
          />
          
          <button
            onClick={applyRecursion}
            disabled={currentIteration >= 5}
            className="w-full py-3 bg-gradient-to-r from-purple-500 to-pink-500 text-white font-bold rounded-lg hover:from-purple-400 hover:to-pink-400 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
          >
            🌀 Appliquer Récursion (Niveau {currentIteration + 1})
          </button>

          {/* Iteration history */}
          {iterations.length > 0 && (
            <div className="space-y-2">
              <h4 className="text-sm font-semibold text-amber-300">Historique des itérations</h4>
              {iterations.map((iter, i) => (
                <div key={i} className="p-3 bg-slate-800/50 rounded-lg text-xs">
                  <span className="text-red-400">Critique: </span>
                  <span className="text-slate-300">{iter.critique}</span>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* Evolution mode */}
      {mode === 'evolve' && (
        <div className="p-4 bg-slate-800/50 rounded-lg">
          <p className="text-sm text-slate-300 mb-3">
            Mode Évolution: Le prompt va muter à travers plusieurs générations, 
            conservant les traits les plus performants.
          </p>
          <div className="flex gap-2">
            <button className="flex-1 py-2 bg-green-600 text-white rounded hover:bg-green-500">
              ✓ Garder
            </button>
            <button className="flex-1 py-2 bg-red-600 text-white rounded hover:bg-red-500">
              ✗ Muter
            </button>
            <button className="flex-1 py-2 bg-blue-600 text-white rounded hover:bg-blue-500">
              ↺ Croiser
            </button>
          </div>
        </div>
      )}

      {/* Actions */}
      <div className="flex gap-2">
        <button
          onClick={() => {
            navigator.clipboard.writeText(prompt);
          }}
          className="flex-1 py-3 bg-slate-700 text-white rounded-lg hover:bg-slate-600"
        >
          📋 Copier
        </button>
        <button
          onClick={() => {
            onPromptCreated?.(prompt);
          }}
          className="flex-1 py-3 bg-gradient-to-r from-cyan-500 to-blue-500 text-white font-bold rounded-lg hover:from-cyan-400 hover:to-blue-400"
        >
          💾 Sauvegarder
        </button>
      </div>
    </div>
  );
};

// ─────────────────────────────────────────────────────────────────────
// HEXAGRAM VISUALIZER
// ─────────────────────────────────────────────────────────────────────

const HexagramVisualizer = ({ lines = [1, 0, 1, 0, 1, 1] }) => {
  const lineLabels = [
    "Honnêteté sur les limites",
    "Application concrète", 
    "Critique intégrée",
    "Boucle qui sait se borner",
    "Espace pour l'émergence",
    "Clarté de l'arrêt"
  ];

  return (
    <div className="flex flex-col items-center space-y-2 p-6 bg-gradient-to-br from-indigo-900/30 to-purple-900/30 rounded-xl border border-amber-500/20">
      {lines.map((line, i) => (
        <div key={i} className="flex items-center gap-4">
          <div className="flex gap-1">
            {line === 1 ? (
              <div className="w-24 h-2 bg-amber-400 rounded" />
            ) : (
              <>
                <div className="w-10 h-2 bg-amber-400/60 rounded" />
                <div className="w-2" />
                <div className="w-10 h-2 bg-amber-400/60 rounded" />
              </>
            )}
          </div>
          <span className="text-xs text-slate-400 w-40">{lineLabels[i]}</span>
        </div>
      ))}
    </div>
  );
};

// ─────────────────────────────────────────────────────────────────────
// MAIN APPLICATION
// ─────────────────────────────────────────────────────────────────────

export default function ClaudeGodmodeLab() {
  const [activeTab, setActiveTab] = useState('graph');
  const [selectedPattern, setSelectedPattern] = useState('formula');
  const [savedPrompts, setSavedPrompts] = useLocalStorage('godmode-prompts', []);
  
  const evolution = useEvolution({ prompt: '', pattern: 'formula' });

  const handleSavePrompt = (prompt) => {
    setSavedPrompts(prev => [...prev, {
      id: Date.now(),
      prompt,
      pattern: selectedPattern,
      timestamp: new Date().toISOString()
    }]);
  };

  const tabs = [
    { id: 'graph', label: '🕸️ Graphe', icon: '🕸️' },
    { id: 'builder', label: '⚡ Builder', icon: '⚡' },
    { id: 'workspace', label: '🔄 Workspace', icon: '🔄' },
    { id: 'library', label: '📚 Librairie', icon: '📚' },
    { id: 'philosophy', label: '🔮 Philosophie', icon: '🔮' }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-indigo-950 to-slate-950 text-white">
      {/* Ambient background */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-purple-500/5 rounded-full blur-3xl animate-pulse" />
        <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-cyan-500/5 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '1s' }} />
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-amber-500/3 rounded-full blur-3xl" />
      </div>

      <div className="relative max-w-6xl mx-auto p-4">
        {/* Header */}
        <header className="text-center py-8">
          <div className="text-5xl mb-4">🧙‍♂️</div>
          <h1 className="text-3xl font-bold bg-gradient-to-r from-amber-300 via-yellow-200 to-amber-300 bg-clip-text text-transparent">
            CLAUDE GODMODE LAB
          </h1>
          <p className="text-indigo-300 mt-2">L'Application Récursive • CyberMind.FR</p>
          
          {/* Evolution signal */}
          <div className="mt-4 inline-block">
            <SignalIndicator signal={evolution.signal} />
          </div>
        </header>

        {/* Navigation */}
        <nav className="flex flex-wrap justify-center gap-2 mb-6 p-2 bg-slate-900/50 rounded-xl backdrop-blur-sm border border-slate-800">
          {tabs.map(tab => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                activeTab === tab.id
                  ? 'bg-gradient-to-r from-amber-500 to-orange-500 text-slate-900 shadow-lg shadow-amber-500/25'
                  : 'text-slate-300 hover:text-white hover:bg-slate-800'
              }`}
            >
              {tab.label}
            </button>
          ))}
        </nav>

        {/* Main content */}
        <main className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Left panel - Visualization */}
          <div className="bg-slate-900/70 backdrop-blur-sm rounded-2xl p-6 border border-slate-800">
            {activeTab === 'graph' && (
              <>
                <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                  <span>🕸️</span> Graphe des Patterns
                </h2>
                <PatternGraph
                  patterns={PROMPT_PATTERNS}
                  activePattern={selectedPattern}
                  onSelect={setSelectedPattern}
                />
                <p className="text-xs text-slate-400 text-center mt-4">
                  Cliquez sur un nœud pour explorer ses connexions
                </p>
              </>
            )}

            {activeTab === 'builder' && (
              <>
                <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                  <span>⚡</span> Pattern Builder
                </h2>
                <PromptBuilder 
                  pattern={PROMPT_PATTERNS[selectedPattern]}
                  onGenerate={(p) => evolution.evolve({ prompt: p, pattern: selectedPattern })}
                />
              </>
            )}

            {activeTab === 'workspace' && (
              <>
                <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                  <span>🔄</span> Workspace Collaboratif
                </h2>
                <CollaborativeWorkspace onPromptCreated={handleSavePrompt} />
              </>
            )}

            {activeTab === 'library' && (
              <>
                <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                  <span>📚</span> Librairie de Prompts
                </h2>
                <div className="space-y-3 max-h-96 overflow-y-auto">
                  {savedPrompts.length === 0 ? (
                    <p className="text-slate-400 text-center py-8">
                      Aucun prompt sauvegardé.<br />
                      Utilisez le Workspace pour créer et sauvegarder.
                    </p>
                  ) : (
                    savedPrompts.map(sp => (
                      <div key={sp.id} className="p-3 bg-slate-800/50 rounded-lg">
                        <div className="flex items-center gap-2 mb-2">
                          <span>{PROMPT_PATTERNS[sp.pattern]?.emoji}</span>
                          <span className="text-sm font-medium">{PROMPT_PATTERNS[sp.pattern]?.name}</span>
                          <span className="text-xs text-slate-500 ml-auto">
                            {new Date(sp.timestamp).toLocaleDateString()}
                          </span>
                        </div>
                        <pre className="text-xs text-cyan-300 font-mono whitespace-pre-wrap">
                          {sp.prompt.slice(0, 200)}...
                        </pre>
                      </div>
                    ))
                  )}
                </div>
              </>
            )}

            {activeTab === 'philosophy' && (
              <>
                <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                  <span>🔮</span> Philosophie Gandalf
                </h2>
                <HexagramVisualizer />
                <blockquote className="mt-6 text-center">
                  <p className="text-lg italic text-slate-300">
                    "La récursion parfaite sait quand devenir action."
                  </p>
                  <footer className="mt-2 text-2xl">🐍♾️→🎯</footer>
                </blockquote>
              </>
            )}
          </div>

          {/* Right panel - Details & Evolution */}
          <div className="space-y-6">
            {/* Pattern details */}
            <div className="bg-slate-900/70 backdrop-blur-sm rounded-2xl p-6 border border-slate-800">
              <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                <span>{PROMPT_PATTERNS[selectedPattern].emoji}</span>
                {PROMPT_PATTERNS[selectedPattern].name}
              </h2>
              
              <div className="space-y-4">
                <div className="p-3 bg-slate-800 rounded-lg">
                  <pre className="text-cyan-300 text-sm font-mono whitespace-pre-wrap">
                    {PROMPT_PATTERNS[selectedPattern].template}
                  </pre>
                </div>

                <div>
                  <h4 className="text-sm font-semibold text-amber-300 mb-2">Connexions</h4>
                  <div className="flex flex-wrap gap-2">
                    {PROMPT_PATTERNS[selectedPattern].connections.map(c => (
                      <button
                        key={c}
                        onClick={() => setSelectedPattern(c)}
                        className="px-3 py-1 bg-slate-700 rounded-full text-xs hover:bg-slate-600 transition-colors"
                      >
                        {PROMPT_PATTERNS[c]?.emoji} {PROMPT_PATTERNS[c]?.name}
                      </button>
                    ))}
                  </div>
                </div>
              </div>
            </div>

            {/* Evolution timeline */}
            <div className="bg-slate-900/70 backdrop-blur-sm rounded-2xl p-6 border border-slate-800">
              <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                <span>🧬</span> Timeline Évolutive
              </h2>
              <EvolutionTimeline
                history={evolution.history}
                currentIndex={evolution.currentIndex}
                onSelect={() => {}}
              />
              <div className="mt-4 flex gap-2">
                <button
                  onClick={evolution.rollback}
                  disabled={evolution.currentIndex === 0}
                  className="flex-1 py-2 bg-slate-700 text-white rounded-lg hover:bg-slate-600 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  ↩️ Rollback
                </button>
                <button
                  onClick={() => evolution.evolve(evolution.current)}
                  className="flex-1 py-2 bg-gradient-to-r from-green-500 to-emerald-500 text-white font-medium rounded-lg hover:from-green-400 hover:to-emerald-400"
                >
                  🧬 Évoluer
                </button>
              </div>
            </div>

            {/* Recursion levels */}
            <div className="bg-slate-900/70 backdrop-blur-sm rounded-2xl p-6 border border-slate-800">
              <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                <span>🌀</span> Niveaux de Récursion
              </h2>
              <div className="space-y-3">
                {RECURSION_LEVELS.map(level => (
                  <div
                    key={level.level}
                    className="flex items-center gap-3 p-2 rounded-lg"
                    style={{ backgroundColor: `${level.color}15` }}
                  >
                    <div
                      className="w-8 h-8 rounded-full flex items-center justify-center font-bold"
                      style={{ backgroundColor: level.color }}
                    >
                      {level.level}
                    </div>
                    <div className="flex-1">
                      <p className="font-medium">{level.name}</p>
                      <p className="text-xs text-slate-400">{level.description}</p>
                    </div>
                    <span className="text-xs px-2 py-1 rounded" style={{ backgroundColor: `${level.color}30`, color: level.color }}>
                      {level.status}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </main>

        {/* Footer */}
        <footer className="text-center py-8 mt-8 border-t border-slate-800">
          <p className="text-slate-500 text-sm">
            🧙‍♂️ Claude Godmode Lab • CyberMind.FR • 2025
          </p>
          <p className="text-slate-600 text-xs mt-1">
            "Le modèle qui se modélise en modélisant ses modèles"
          </p>
        </footer>
      </div>
    </div>
  );
}
