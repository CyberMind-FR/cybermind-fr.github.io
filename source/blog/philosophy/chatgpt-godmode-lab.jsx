import React, { useState, useEffect, useCallback, useMemo } from 'react';

// ═══════════════════════════════════════════════════════════════════
// 🤖 CHATGPT GODMODE LAB - L'Application Récursive pour OpenAI
// ═══════════════════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────────────────────
// DATA LAYER - Les Modèles Fondamentaux OpenAI
// ─────────────────────────────────────────────────────────────────────

const OPENAI_MODELS = {
  'gpt-4o': { name: 'GPT-4o', speed: 'fast', reasoning: 'good', creative: 'excellent', cost: '$$' },
  'gpt-4-turbo': { name: 'GPT-4 Turbo', speed: 'medium', reasoning: 'good', creative: 'excellent', cost: '$$$' },
  'o1-preview': { name: 'o1-preview', speed: 'slow', reasoning: 'excellent', creative: 'good', cost: '$$$$' },
  'o1': { name: 'o1', speed: 'slow', reasoning: 'superior', creative: 'good', cost: '$$$$$' },
  'gpt-4o-mini': { name: 'GPT-4o Mini', speed: 'very-fast', reasoning: 'moderate', creative: 'good', cost: '$' }
};

const PROMPT_PATTERNS = {
  system: {
    id: 'system',
    name: 'System Role',
    emoji: '⚙️',
    template: 'You are a [ROLE] with expertise in [DOMAIN]. Your task is to [OBJECTIVE].',
    variables: ['role', 'domain', 'objective'],
    color: '#10A37F',
    connections: ['persona', 'constraints'],
    bestFor: ['gpt-4o', 'gpt-4-turbo']
  },
  persona: {
    id: 'persona',
    name: 'Expert Persona',
    emoji: '🎭',
    template: 'You are a senior [EXPERT] with [N] years of experience. You specialize in [SPECIALTY]. Your communication style is [STYLE].',
    variables: ['expert', 'years', 'specialty', 'style'],
    color: '#8B5CF6',
    connections: ['system', 'fewshot'],
    bestFor: ['gpt-4o', 'gpt-4-turbo']
  },
  cot: {
    id: 'cot',
    name: 'Chain of Thought',
    emoji: '🧠',
    template: 'Let\'s think through this step by step:\n1. First, [STEP1]\n2. Then, [STEP2]\n3. Finally, [STEP3]',
    variables: ['step1', 'step2', 'step3'],
    color: '#06B6D4',
    connections: ['tot', 'reflection'],
    bestFor: ['gpt-4o', 'gpt-4-turbo', 'o1-preview']
  },
  tot: {
    id: 'tot',
    name: 'Tree of Thought',
    emoji: '🌳',
    template: 'Explore [N] different reasoning paths for this problem. For each path:\n- State the approach\n- Work through the logic\n- Evaluate likelihood of success\nThen synthesize the best solution.',
    variables: ['paths'],
    color: '#F59E0B',
    connections: ['cot', 'o1native'],
    bestFor: ['o1-preview', 'o1']
  },
  o1native: {
    id: 'o1native',
    name: 'o1 Native Reasoning',
    emoji: '🔮',
    template: '[COMPLEX_PROBLEM]\n\nTake your time to reason through this thoroughly. Show your complete thinking process.',
    variables: ['problem'],
    color: '#EC4899',
    connections: ['tot', 'adversarial'],
    bestFor: ['o1', 'o1-preview']
  },
  fewshot: {
    id: 'fewshot',
    name: 'Few-Shot Examples',
    emoji: '📚',
    template: 'Here are examples of the expected format:\n\nExample 1:\nInput: [IN1]\nOutput: [OUT1]\n\nExample 2:\nInput: [IN2]\nOutput: [OUT2]\n\nNow process:\nInput: [QUERY]',
    variables: ['in1', 'out1', 'in2', 'out2', 'query'],
    color: '#14B8A6',
    connections: ['persona', 'json'],
    bestFor: ['gpt-4o', 'gpt-4-turbo']
  },
  json: {
    id: 'json',
    name: 'JSON Mode',
    emoji: '📋',
    template: 'Respond ONLY with valid JSON in this exact structure:\n```json\n{\n  "analysis": "...",\n  "recommendation": "...",\n  "confidence": 0.0-1.0,\n  "next_steps": ["..."]\n}\n```\nNo markdown outside JSON. No explanations.',
    variables: [],
    color: '#EAB308',
    connections: ['fewshot', 'constraints'],
    bestFor: ['gpt-4-turbo', 'gpt-4o']
  },
  constraints: {
    id: 'constraints',
    name: 'Constraints & Rules',
    emoji: '📏',
    template: 'CONSTRAINTS:\n- Maximum [N] words\n- No [FORBIDDEN]\n- Always include [REQUIRED]\n- Format: [FORMAT]\n- Tone: [TONE]',
    variables: ['maxWords', 'forbidden', 'required', 'format', 'tone'],
    color: '#EF4444',
    connections: ['system', 'json'],
    bestFor: ['gpt-4o', 'gpt-4-turbo', 'gpt-4o-mini']
  },
  reflection: {
    id: 'reflection',
    name: 'Self-Reflection',
    emoji: '🪞',
    template: 'Before answering:\n1. What assumptions am I making?\n2. What could I be missing?\n3. What are potential biases?\n\nNow, with these considerations in mind: [TASK]',
    variables: ['task'],
    color: '#A855F7',
    connections: ['cot', 'adversarial'],
    bestFor: ['o1-preview', 'o1', 'gpt-4o']
  },
  adversarial: {
    id: 'adversarial',
    name: 'Adversarial Review',
    emoji: '⚔️',
    template: 'Propose a solution for: [PROBLEM]\n\nThen:\n1. Attack your solution as a hostile critic\n2. Identify the 3 strongest objections\n3. Address each objection\n4. Deliver the hardened solution',
    variables: ['problem'],
    color: '#DC2626',
    connections: ['reflection', 'o1native'],
    bestFor: ['o1', 'o1-preview', 'gpt-4o']
  },
  recursive: {
    id: 'recursive',
    name: 'Recursive Improvement',
    emoji: '🔄',
    template: 'Task: [TASK]\n\nExecute this loop:\n- V1: Initial attempt\n- V2: Critique V1, improve\n- V3: If V2 ≈ V1, stop. Else improve.\n\nMax 5 iterations. Show only final with confidence score.',
    variables: ['task'],
    color: '#7C3AED',
    connections: ['adversarial', 'system'],
    bestFor: ['gpt-4o', 'gpt-4-turbo']
  }
};

const CUSTOM_INSTRUCTIONS_TEMPLATE = {
  about: `PROFESSIONAL CONTEXT:
- Role: [your job/expertise]
- Domains: [technical specialties]
- Current projects: [active work]
- Tech stack: [languages, frameworks, tools]

PREFERENCES:
- Language: [preferred language]
- Level: Expert, no oversimplification
- Style: Direct, concise, actionable`,
  
  response: `RESPONSE FORMAT:
- No preamble, straight to the point
- Code: Commented, production-ready
- Length: Concise unless complexity requires more

BEHAVIOR:
- Constructive criticism welcome
- Flag edge cases and risks
- Suggest alternatives when relevant
- Don't repeat the question in response`
};

const API_PARAMS = {
  temperature: { min: 0, max: 2, default: 0.7, description: 'Creativity vs determinism' },
  max_tokens: { min: 1, max: 128000, default: 4096, description: 'Maximum output length' },
  top_p: { min: 0, max: 1, default: 1, description: 'Nucleus sampling' },
  frequency_penalty: { min: -2, max: 2, default: 0, description: 'Penalize repetition' },
  presence_penalty: { min: -2, max: 2, default: 0, description: 'Encourage new topics' }
};

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
    } catch {}
  }, [key, value]);

  return [value, setValue];
};

// ─────────────────────────────────────────────────────────────────────
// VISUALIZATION COMPONENTS
// ─────────────────────────────────────────────────────────────────────

const ModelSelector = ({ selected, onSelect }) => {
  return (
    <div className="grid grid-cols-2 md:grid-cols-5 gap-2">
      {Object.entries(OPENAI_MODELS).map(([id, model]) => (
        <button
          key={id}
          onClick={() => onSelect(id)}
          className={`p-3 rounded-lg border transition-all text-left ${
            selected === id
              ? 'border-emerald-500 bg-emerald-500/20 shadow-lg shadow-emerald-500/20'
              : 'border-slate-700 bg-slate-800/50 hover:border-slate-600'
          }`}
        >
          <div className="font-medium text-sm">{model.name}</div>
          <div className="text-xs text-slate-400 mt-1">{model.cost}</div>
        </button>
      ))}
    </div>
  );
};

const PatternNode = ({ pattern, x, y, isActive, onClick, connections, allPatterns, selectedModel }) => {
  const [hover, setHover] = useState(false);
  const isOptimal = pattern.bestFor?.includes(selectedModel);
  
  return (
    <g>
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
      
      <circle
        cx={x}
        cy={y}
        r={hover ? 38 : 32}
        fill={isActive ? pattern.color : '#1a1a1a'}
        stroke={isOptimal ? '#10A37F' : pattern.color}
        strokeWidth={isActive ? 3 : isOptimal ? 2 : 1}
        style={{ cursor: 'pointer', transition: 'all 0.3s ease' }}
        onClick={onClick}
        onMouseEnter={() => setHover(true)}
        onMouseLeave={() => setHover(false)}
      />
      
      {isOptimal && (
        <circle
          cx={x + 22}
          cy={y - 22}
          r={8}
          fill="#10A37F"
        />
      )}
      
      <text
        x={x}
        y={y + 6}
        textAnchor="middle"
        fontSize="18"
        style={{ pointerEvents: 'none' }}
      >
        {pattern.emoji}
      </text>
      
      {hover && (
        <text
          x={x}
          y={y + 55}
          textAnchor="middle"
          fill="#fff"
          fontSize="11"
          fontWeight="bold"
        >
          {pattern.name}
        </text>
      )}
    </g>
  );
};

const PatternGraph = ({ patterns, activePattern, onSelect, selectedModel }) => {
  const patternList = Object.values(patterns);
  const centerX = 220;
  const centerY = 220;
  const radius = 170;
  
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
    <svg width="440" height="440" viewBox="0 0 440 440">
      <defs>
        <radialGradient id="bgGradGpt">
          <stop offset="0%" stopColor="#1a1a1a" />
          <stop offset="100%" stopColor="#0d0d0d" />
        </radialGradient>
        <filter id="glowGpt">
          <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
          <feMerge>
            <feMergeNode in="coloredBlur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>
      </defs>
      
      <circle cx={centerX} cy={centerY} r="210" fill="url(#bgGradGpt)" stroke="#10A37F" strokeWidth="1" strokeOpacity="0.3"/>
      
      <text x={centerX} y={centerY + 8} textAnchor="middle" fontSize="36" filter="url(#glowGpt)">
        🤖
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
          selectedModel={selectedModel}
        />
      ))}
      
      <text x={centerX} y={centerY + 195} textAnchor="middle" fill="#10A37F" fontSize="10">
        🟢 = Optimal pour {OPENAI_MODELS[selectedModel]?.name}
      </text>
    </svg>
  );
};

const TemperatureSlider = ({ value, onChange }) => {
  const getLabel = (v) => {
    if (v === 0) return '❄️ Déterministe';
    if (v < 0.5) return '🎯 Factuel';
    if (v < 1) return '⚖️ Équilibré';
    if (v < 1.5) return '🎨 Créatif';
    return '🌈 Très créatif';
  };

  return (
    <div className="space-y-2">
      <div className="flex justify-between text-sm">
        <span>Temperature: {value.toFixed(1)}</span>
        <span className="text-emerald-400">{getLabel(value)}</span>
      </div>
      <input
        type="range"
        min="0"
        max="2"
        step="0.1"
        value={value}
        onChange={(e) => onChange(parseFloat(e.target.value))}
        className="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-emerald-500"
      />
      <div className="flex justify-between text-xs text-slate-500">
        <span>0 (Code)</span>
        <span>0.7 (Default)</span>
        <span>2 (Wild)</span>
      </div>
    </div>
  );
};

const APIConfigPanel = ({ config, onChange }) => {
  return (
    <div className="space-y-4">
      <TemperatureSlider 
        value={config.temperature} 
        onChange={(v) => onChange({ ...config, temperature: v })} 
      />
      
      <div className="grid grid-cols-2 gap-4">
        <div>
          <label className="text-xs text-slate-400">Max Tokens</label>
          <input
            type="number"
            value={config.max_tokens}
            onChange={(e) => onChange({ ...config, max_tokens: parseInt(e.target.value) })}
            className="w-full mt-1 p-2 bg-slate-800 border border-slate-600 rounded text-sm"
          />
        </div>
        <div>
          <label className="text-xs text-slate-400">Top P</label>
          <input
            type="number"
            step="0.1"
            min="0"
            max="1"
            value={config.top_p}
            onChange={(e) => onChange({ ...config, top_p: parseFloat(e.target.value) })}
            className="w-full mt-1 p-2 bg-slate-800 border border-slate-600 rounded text-sm"
          />
        </div>
      </div>

      <div className="p-3 bg-slate-800 rounded-lg">
        <div className="text-xs text-slate-400 mb-2">API Preview</div>
        <pre className="text-xs text-emerald-300 font-mono overflow-x-auto">
{JSON.stringify({
  model: config.model,
  temperature: config.temperature,
  max_tokens: config.max_tokens,
  top_p: config.top_p
}, null, 2)}
        </pre>
      </div>
    </div>
  );
};

// ─────────────────────────────────────────────────────────────────────
// PROMPT BUILDER COMPONENT
// ─────────────────────────────────────────────────────────────────────

const PromptBuilder = ({ pattern, model, onGenerate }) => {
  const [variables, setVariables] = useState({});
  const [generated, setGenerated] = useState('');
  const [copied, setCopied] = useState(false);

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
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const isOptimal = pattern.bestFor?.includes(model);

  return (
    <div className="space-y-4">
      <div className="flex items-center gap-3 mb-4">
        <span className="text-3xl">{pattern.emoji}</span>
        <div className="flex-1">
          <h3 className="font-bold text-lg">{pattern.name}</h3>
          <div className="flex items-center gap-2 mt-1">
            {isOptimal ? (
              <span className="text-xs px-2 py-0.5 bg-emerald-500/20 text-emerald-400 rounded">
                ✓ Optimal pour {OPENAI_MODELS[model]?.name}
              </span>
            ) : (
              <span className="text-xs px-2 py-0.5 bg-amber-500/20 text-amber-400 rounded">
                ⚠️ Mieux adapté à: {pattern.bestFor?.map(m => OPENAI_MODELS[m]?.name).join(', ')}
              </span>
            )}
          </div>
        </div>
      </div>

      <div className="p-3 bg-slate-900 rounded-lg border border-slate-700">
        <pre className="text-emerald-300 text-sm whitespace-pre-wrap font-mono">
          {pattern.template}
        </pre>
      </div>

      {pattern.variables.length > 0 && (
        <div className="space-y-3">
          <h4 className="text-sm font-semibold text-emerald-400">Variables</h4>
          <div className="grid grid-cols-2 gap-3">
            {pattern.variables.map(v => (
              <div key={v}>
                <label className="text-xs text-slate-400 uppercase">{v}</label>
                <input
                  type="text"
                  value={variables[v] || ''}
                  onChange={e => handleChange(v, e.target.value)}
                  placeholder={`[${v.toUpperCase()}]`}
                  className="w-full mt-1 p-2 bg-slate-800 border border-slate-600 rounded text-white text-sm focus:border-emerald-500 focus:outline-none"
                />
              </div>
            ))}
          </div>
        </div>
      )}

      <button
        onClick={generate}
        className="w-full py-3 bg-gradient-to-r from-emerald-500 to-teal-500 text-white font-bold rounded-lg hover:from-emerald-400 hover:to-teal-400 transition-all"
      >
        ⚡ Générer le Prompt
      </button>

      {generated && (
        <div className="relative">
          <div 
            className="p-4 bg-slate-900 rounded-lg border border-emerald-500/30 cursor-pointer hover:border-emerald-500"
            onClick={copyToClipboard}
          >
            <pre className="text-green-300 text-sm whitespace-pre-wrap font-mono">
              {generated}
            </pre>
          </div>
          <span className="absolute top-2 right-2 text-xs text-slate-500">
            {copied ? '✓ Copié!' : 'Cliquer pour copier'}
          </span>
        </div>
      )}
    </div>
  );
};

// ─────────────────────────────────────────────────────────────────────
// CUSTOM INSTRUCTIONS EDITOR
// ─────────────────────────────────────────────────────────────────────

const CustomInstructionsEditor = () => {
  const [about, setAbout] = useState(CUSTOM_INSTRUCTIONS_TEMPLATE.about);
  const [response, setResponse] = useState(CUSTOM_INSTRUCTIONS_TEMPLATE.response);
  const [copied, setCopied] = useState(null);

  const copySection = (section, text) => {
    navigator.clipboard.writeText(text);
    setCopied(section);
    setTimeout(() => setCopied(null), 2000);
  };

  return (
    <div className="space-y-6">
      <div>
        <div className="flex justify-between items-center mb-2">
          <label className="text-sm font-semibold text-emerald-400">
            📝 "What would you like ChatGPT to know about you?"
          </label>
          <button
            onClick={() => copySection('about', about)}
            className="text-xs px-2 py-1 bg-slate-700 rounded hover:bg-slate-600"
          >
            {copied === 'about' ? '✓ Copié' : 'Copier'}
          </button>
        </div>
        <textarea
          value={about}
          onChange={(e) => setAbout(e.target.value)}
          className="w-full h-48 p-3 bg-slate-900 border border-slate-600 rounded-lg text-white font-mono text-sm focus:border-emerald-500 focus:outline-none resize-none"
        />
      </div>

      <div>
        <div className="flex justify-between items-center mb-2">
          <label className="text-sm font-semibold text-emerald-400">
            📝 "How would you like ChatGPT to respond?"
          </label>
          <button
            onClick={() => copySection('response', response)}
            className="text-xs px-2 py-1 bg-slate-700 rounded hover:bg-slate-600"
          >
            {copied === 'response' ? '✓ Copié' : 'Copier'}
          </button>
        </div>
        <textarea
          value={response}
          onChange={(e) => setResponse(e.target.value)}
          className="w-full h-48 p-3 bg-slate-900 border border-slate-600 rounded-lg text-white font-mono text-sm focus:border-emerald-500 focus:outline-none resize-none"
        />
      </div>

      <div className="p-4 bg-emerald-900/20 border border-emerald-500/30 rounded-lg">
        <p className="text-sm text-emerald-300">
          💡 <strong>Tip:</strong> Ces instructions persistent à travers toutes vos conversations ChatGPT.
          Accédez-y via Settings → Personalization → Custom Instructions.
        </p>
      </div>
    </div>
  );
};

// ─────────────────────────────────────────────────────────────────────
// COMPARISON TABLE
// ─────────────────────────────────────────────────────────────────────

const ModelComparison = () => {
  const comparisons = [
    { case: 'Conversation rapide', 'gpt-4o': '✅', 'gpt-4-turbo': '✅', 'o1-preview': '❌', 'o1': '❌' },
    { case: 'Rédaction créative', 'gpt-4o': '✅', 'gpt-4-turbo': '✅', 'o1-preview': '⚠️', 'o1': '⚠️' },
    { case: 'Code simple', 'gpt-4o': '✅', 'gpt-4-turbo': '✅', 'o1-preview': '❌', 'o1': '❌' },
    { case: 'Algorithmes complexes', 'gpt-4o': '⚠️', 'gpt-4-turbo': '⚠️', 'o1-preview': '✅', 'o1': '✅' },
    { case: 'Mathématiques', 'gpt-4o': '⚠️', 'gpt-4-turbo': '⚠️', 'o1-preview': '✅', 'o1': '✅' },
    { case: 'Raisonnement multi-étapes', 'gpt-4o': '⚠️', 'gpt-4-turbo': '⚠️', 'o1-preview': '✅', 'o1': '✅' },
    { case: 'Analyse profonde', 'gpt-4o': '⚠️', 'gpt-4-turbo': '⚠️', 'o1-preview': '✅', 'o1': '✅' },
    { case: 'Latence < 5s', 'gpt-4o': '✅', 'gpt-4-turbo': '⚠️', 'o1-preview': '❌', 'o1': '❌' }
  ];

  const getColor = (val) => {
    if (val === '✅') return 'text-emerald-400';
    if (val === '❌') return 'text-red-400';
    return 'text-amber-400';
  };

  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="bg-slate-800">
            <th className="p-3 text-left">Cas d'usage</th>
            <th className="p-3 text-center">GPT-4o</th>
            <th className="p-3 text-center">GPT-4 Turbo</th>
            <th className="p-3 text-center">o1-preview</th>
            <th className="p-3 text-center">o1</th>
          </tr>
        </thead>
        <tbody>
          {comparisons.map((row, i) => (
            <tr key={i} className={i % 2 === 0 ? 'bg-slate-900/50' : ''}>
              <td className="p-3 font-medium">{row.case}</td>
              <td className={`p-3 text-center ${getColor(row['gpt-4o'])}`}>{row['gpt-4o']}</td>
              <td className={`p-3 text-center ${getColor(row['gpt-4-turbo'])}`}>{row['gpt-4-turbo']}</td>
              <td className={`p-3 text-center ${getColor(row['o1-preview'])}`}>{row['o1-preview']}</td>
              <td className={`p-3 text-center ${getColor(row['o1'])}`}>{row['o1']}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

// ─────────────────────────────────────────────────────────────────────
// MAIN APPLICATION
// ─────────────────────────────────────────────────────────────────────

export default function ChatGPTGodmodeLab() {
  const [activeTab, setActiveTab] = useState('graph');
  const [selectedPattern, setSelectedPattern] = useState('system');
  const [selectedModel, setSelectedModel] = useState('gpt-4o');
  const [apiConfig, setApiConfig] = useState({
    model: 'gpt-4o',
    temperature: 0.7,
    max_tokens: 4096,
    top_p: 1
  });
  const [savedPrompts, setSavedPrompts] = useLocalStorage('chatgpt-godmode-prompts', []);

  useEffect(() => {
    setApiConfig(prev => ({ ...prev, model: selectedModel }));
  }, [selectedModel]);

  const handleSavePrompt = (prompt) => {
    setSavedPrompts(prev => [...prev, {
      id: Date.now(),
      prompt,
      pattern: selectedPattern,
      model: selectedModel,
      timestamp: new Date().toISOString()
    }]);
  };

  const tabs = [
    { id: 'graph', label: '🕸️ Patterns' },
    { id: 'builder', label: '⚡ Builder' },
    { id: 'custom', label: '⚙️ Custom Instructions' },
    { id: 'api', label: '🔧 API Config' },
    { id: 'compare', label: '📊 Comparaison' },
    { id: 'library', label: '📚 Librairie' }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 text-white">
      {/* Ambient background */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-emerald-500/5 rounded-full blur-3xl animate-pulse" />
        <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-teal-500/5 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '1s' }} />
      </div>

      <div className="relative max-w-6xl mx-auto p-4">
        {/* Header */}
        <header className="text-center py-8">
          <div className="text-5xl mb-4">🤖</div>
          <h1 className="text-3xl font-bold bg-gradient-to-r from-emerald-300 via-teal-200 to-emerald-300 bg-clip-text text-transparent">
            CHATGPT GODMODE LAB
          </h1>
          <p className="text-emerald-400 mt-2">GPT-4 • GPT-4o • o1 • Custom GPTs</p>
          <p className="text-slate-400 text-sm mt-1">Par Gandalf • CyberMind.FR</p>
        </header>

        {/* Model Selector */}
        <div className="mb-6">
          <h3 className="text-sm font-semibold text-slate-400 mb-3">Sélectionner le modèle</h3>
          <ModelSelector selected={selectedModel} onSelect={setSelectedModel} />
        </div>

        {/* Navigation */}
        <nav className="flex flex-wrap justify-center gap-2 mb-6 p-2 bg-slate-900/50 rounded-xl backdrop-blur-sm border border-slate-800">
          {tabs.map(tab => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                activeTab === tab.id
                  ? 'bg-gradient-to-r from-emerald-500 to-teal-500 text-white shadow-lg shadow-emerald-500/25'
                  : 'text-slate-300 hover:text-white hover:bg-slate-800'
              }`}
            >
              {tab.label}
            </button>
          ))}
        </nav>

        {/* Main content */}
        <main className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Left panel */}
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
                  selectedModel={selectedModel}
                />
              </>
            )}

            {activeTab === 'builder' && (
              <>
                <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                  <span>⚡</span> Pattern Builder
                </h2>
                <PromptBuilder 
                  pattern={PROMPT_PATTERNS[selectedPattern]}
                  model={selectedModel}
                  onGenerate={handleSavePrompt}
                />
              </>
            )}

            {activeTab === 'custom' && (
              <>
                <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                  <span>⚙️</span> Custom Instructions
                </h2>
                <CustomInstructionsEditor />
              </>
            )}

            {activeTab === 'api' && (
              <>
                <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                  <span>🔧</span> Configuration API
                </h2>
                <APIConfigPanel config={apiConfig} onChange={setApiConfig} />
              </>
            )}

            {activeTab === 'compare' && (
              <>
                <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                  <span>📊</span> Comparaison des Modèles
                </h2>
                <ModelComparison />
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
                      Utilisez le Builder pour créer et sauvegarder.
                    </p>
                  ) : (
                    savedPrompts.slice().reverse().map(sp => (
                      <div key={sp.id} className="p-3 bg-slate-800/50 rounded-lg">
                        <div className="flex items-center gap-2 mb-2">
                          <span>{PROMPT_PATTERNS[sp.pattern]?.emoji}</span>
                          <span className="text-sm font-medium">{PROMPT_PATTERNS[sp.pattern]?.name}</span>
                          <span className="text-xs text-emerald-400 ml-auto">{sp.model}</span>
                        </div>
                        <pre className="text-xs text-emerald-300 font-mono whitespace-pre-wrap">
                          {sp.prompt.slice(0, 150)}...
                        </pre>
                      </div>
                    ))
                  )}
                </div>
              </>
            )}
          </div>

          {/* Right panel */}
          <div className="space-y-6">
            {/* Pattern details */}
            <div className="bg-slate-900/70 backdrop-blur-sm rounded-2xl p-6 border border-slate-800">
              <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                <span>{PROMPT_PATTERNS[selectedPattern].emoji}</span>
                {PROMPT_PATTERNS[selectedPattern].name}
              </h2>
              
              <div className="space-y-4">
                <div className="p-3 bg-slate-800 rounded-lg">
                  <pre className="text-emerald-300 text-sm font-mono whitespace-pre-wrap">
                    {PROMPT_PATTERNS[selectedPattern].template}
                  </pre>
                </div>

                <div>
                  <h4 className="text-sm font-semibold text-emerald-400 mb-2">Meilleur pour</h4>
                  <div className="flex flex-wrap gap-2">
                    {PROMPT_PATTERNS[selectedPattern].bestFor?.map(m => (
                      <span
                        key={m}
                        className={`px-2 py-1 rounded text-xs ${
                          m === selectedModel 
                            ? 'bg-emerald-500 text-white' 
                            : 'bg-slate-700 text-slate-300'
                        }`}
                      >
                        {OPENAI_MODELS[m]?.name}
                      </span>
                    ))}
                  </div>
                </div>

                <div>
                  <h4 className="text-sm font-semibold text-emerald-400 mb-2">Connexions</h4>
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

            {/* Quick tips */}
            <div className="bg-slate-900/70 backdrop-blur-sm rounded-2xl p-6 border border-slate-800">
              <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                <span>💡</span> Tips pour {OPENAI_MODELS[selectedModel]?.name}
              </h2>
              <div className="space-y-3 text-sm">
                {selectedModel.startsWith('o1') ? (
                  <>
                    <p className="text-slate-300">• Pas besoin de "think step by step" - c'est natif</p>
                    <p className="text-slate-300">• Laissez le modèle raisonner sans contraintes de temps</p>
                    <p className="text-slate-300">• Idéal pour problèmes complexes multi-étapes</p>
                    <p className="text-slate-300">• Temperature fixée à 1, pas modifiable</p>
                  </>
                ) : (
                  <>
                    <p className="text-slate-300">• Utilisez Chain of Thought pour raisonnement complexe</p>
                    <p className="text-slate-300">• Few-shot examples améliorent la précision du format</p>
                    <p className="text-slate-300">• Temperature 0 pour code, 0.7+ pour créativité</p>
                    <p className="text-slate-300">• JSON mode disponible avec response_format</p>
                  </>
                )}
              </div>
            </div>

            {/* Philosophy */}
            <div className="bg-gradient-to-br from-emerald-900/20 to-teal-900/20 backdrop-blur-sm rounded-2xl p-6 border border-emerald-500/20">
              <div className="text-center">
                <p className="text-lg font-medium text-slate-300 mb-2">
                  "The best prompt makes the model think<br/>
                  it already knows exactly what you want."
                </p>
                <div className="text-2xl mt-4">🤖 → 🧠 → 💡 → ✨</div>
              </div>
            </div>
          </div>
        </main>

        {/* Footer */}
        <footer className="text-center py-8 mt-8 border-t border-slate-800">
          <p className="text-slate-500 text-sm">
            🤖 ChatGPT Godmode Lab • CyberMind.FR • 2025
          </p>
        </footer>
      </div>
    </div>
  );
}
