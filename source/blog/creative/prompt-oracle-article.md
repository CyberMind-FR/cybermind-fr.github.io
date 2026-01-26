---
title: "L'Oracle du Prompt - Générateur Initiatique"
date: 2025-01-23
categories:
  - creative
  - tutorials
tags:
  - prompt-engineering
  - LLM
  - Claude
  - ChatGPT
  - outil
thumbnail: /images/thumbnails/prompt-oracle.png
description: "Un outil interactif pour apprendre et générer des prompts optimisés pour Claude et ChatGPT, avec une approche pédagogique par niveaux d'initiation."
---

## L'Art du Prompt Engineering

Le prompt engineering est devenu une compétence essentielle pour exploiter pleinement les LLMs comme Claude et ChatGPT. Cet outil interactif vous guide à travers les techniques fondamentales jusqu'aux patterns avancés, avec des prompts adaptés à chaque modèle.

### Comment utiliser l'Oracle

1. **Choisissez votre modèle** - Claude (XML tags) ou ChatGPT (Markdown)
2. **Sélectionnez votre niveau** - De Néophyte à Maître
3. **Explorez les techniques** - Chaque niveau débloque de nouvelles approches
4. **Décrivez votre objectif** - L'Oracle génère un prompt optimisé
5. **Apprenez** - Consultez l'explication pour comprendre la structure

---

<div id="prompt-oracle-app">

<style>
#prompt-oracle-app {
    --gold: #c9a227;
    --gold-light: #f0d060;
    --blue: #6b8cae;
    --green: #4a9079;
    --purple: #8b5cf6;
    --bg-dark: #0a0a0f;
    --bg-mid: #1a1a2e;
    --text: #e0e0e0;
    --text-muted: rgba(224, 224, 224, 0.6);
    
    font-family: 'Crimson Text', Georgia, serif;
    background: linear-gradient(135deg, var(--bg-dark) 0%, var(--bg-mid) 50%, var(--bg-dark) 100%);
    color: var(--text);
    padding: 2rem;
    border-radius: 12px;
    margin: 2rem 0;
    line-height: 1.6;
}

#prompt-oracle-app * {
    box-sizing: border-box;
}

#prompt-oracle-app .oracle-header {
    text-align: center;
    margin-bottom: 2rem;
}

#prompt-oracle-app .symbols {
    font-size: 2rem;
    letter-spacing: 0.8rem;
    color: var(--gold);
    margin-bottom: 0.5rem;
}

#prompt-oracle-app h2.oracle-title {
    font-size: 1.8rem;
    font-weight: 700;
    background: linear-gradient(135deg, var(--gold), var(--gold-light), var(--gold));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 0 0.5rem 0;
    border: none;
    padding: 0;
}

#prompt-oracle-app .subtitle {
    color: var(--text-muted);
    font-style: italic;
    font-size: 1rem;
}

#prompt-oracle-app .section-title {
    color: var(--gold);
    font-size: 1.1rem;
    margin: 1.5rem 0 1rem 0;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    border: none;
    padding: 0;
}

#prompt-oracle-app .model-selector {
    display: flex;
    gap: 1rem;
    justify-content: center;
    margin-bottom: 1rem;
    flex-wrap: wrap;
}

#prompt-oracle-app .model-card {
    background: linear-gradient(145deg, rgba(30, 30, 45, 0.9), rgba(20, 20, 35, 0.95));
    border: 2px solid rgba(100, 100, 120, 0.3);
    border-radius: 12px;
    padding: 1rem 2rem;
    cursor: pointer;
    transition: all 0.3s ease;
    text-align: center;
    min-width: 140px;
}

#prompt-oracle-app .model-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
}

#prompt-oracle-app .model-card.selected {
    border-color: var(--gold);
    box-shadow: 0 0 25px rgba(201, 162, 39, 0.3);
}

#prompt-oracle-app .model-card[data-model="claude"].selected {
    border-color: #d97706;
    box-shadow: 0 0 25px rgba(217, 119, 6, 0.3);
}

#prompt-oracle-app .model-card[data-model="chatgpt"].selected {
    border-color: #10a37f;
    box-shadow: 0 0 25px rgba(16, 163, 127, 0.3);
}

#prompt-oracle-app .model-icon {
    font-size: 2rem;
    margin-bottom: 0.3rem;
}

#prompt-oracle-app .model-name {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text);
}

#prompt-oracle-app .model-hint {
    font-size: 0.7rem;
    color: var(--text-muted);
}

#prompt-oracle-app .model-tips {
    background: rgba(0, 0, 0, 0.3);
    border-radius: 8px;
    padding: 1rem;
    margin-top: 1rem;
    border-left: 3px solid var(--gold);
    font-size: 0.85rem;
}

#prompt-oracle-app .model-tips h4 {
    margin: 0 0 0.5rem 0;
    font-size: 0.9rem;
    border: none;
    padding: 0;
}

#prompt-oracle-app .model-tips ul {
    margin: 0;
    padding-left: 1.2rem;
    list-style: disc;
}

#prompt-oracle-app .model-tips li {
    padding: 0.15rem 0;
    color: var(--text-muted);
}

#prompt-oracle-app .levels-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 0.75rem;
}

#prompt-oracle-app .level-card {
    background: linear-gradient(145deg, rgba(30, 30, 45, 0.9), rgba(20, 20, 35, 0.95));
    border: 1px solid rgba(201, 162, 39, 0.3);
    border-radius: 10px;
    padding: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    text-align: center;
}

#prompt-oracle-app .level-card:hover {
    border-color: rgba(201, 162, 39, 0.7);
    transform: translateY(-3px);
}

#prompt-oracle-app .level-card.selected {
    border-color: var(--gold);
    box-shadow: 0 0 20px rgba(201, 162, 39, 0.3);
}

#prompt-oracle-app .level-card .symbol {
    font-size: 1.5rem;
    margin-bottom: 0.3rem;
}

#prompt-oracle-app .level-card .name {
    font-size: 1rem;
    font-weight: 600;
}

#prompt-oracle-app .level-card .desc {
    color: var(--text-muted);
    font-size: 0.75rem;
}

#prompt-oracle-app .techniques-list {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

#prompt-oracle-app .technique-card {
    background: linear-gradient(145deg, rgba(25, 25, 40, 0.9), rgba(15, 15, 30, 0.95));
    border: 1px solid rgba(107, 140, 174, 0.3);
    border-radius: 8px;
    padding: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
}

#prompt-oracle-app .technique-card:hover {
    border-color: rgba(107, 140, 174, 0.7);
    transform: translateX(4px);
}

#prompt-oracle-app .technique-card.selected {
    border-color: var(--blue);
    background: linear-gradient(145deg, rgba(35, 35, 55, 0.95), rgba(25, 25, 45, 0.98));
}

#prompt-oracle-app .technique-card .trigram {
    font-size: 1.5rem;
    line-height: 1;
}

#prompt-oracle-app .technique-card .tech-name {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 0.2rem;
}

#prompt-oracle-app .technique-card .principle {
    color: var(--blue);
    font-style: italic;
    font-size: 0.85rem;
}

#prompt-oracle-app .technique-card .description {
    color: var(--text-muted);
    font-size: 0.8rem;
    margin-top: 0.3rem;
}

#prompt-oracle-app textarea {
    width: 100%;
    background: rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(201, 162, 39, 0.3);
    border-radius: 8px;
    color: var(--text);
    font-family: 'Crimson Text', Georgia, serif;
    font-size: 1rem;
    padding: 0.75rem;
    resize: vertical;
    min-height: 80px;
    margin-bottom: 1rem;
}

#prompt-oracle-app textarea:focus {
    outline: none;
    border-color: var(--gold);
}

#prompt-oracle-app textarea::placeholder {
    color: rgba(224, 224, 224, 0.4);
}

#prompt-oracle-app .btn {
    background: linear-gradient(145deg, var(--gold), #a08020);
    color: var(--bg-dark);
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 8px;
    font-family: 'Crimson Text', serif;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}

#prompt-oracle-app .btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 20px rgba(201, 162, 39, 0.4);
}

#prompt-oracle-app .btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
    transform: none;
}

#prompt-oracle-app .btn-secondary {
    background: transparent;
    border: 1px solid rgba(107, 140, 174, 0.5);
    color: var(--blue);
    padding: 0.4rem 0.8rem;
    font-size: 0.9rem;
}

#prompt-oracle-app .result-box {
    background: linear-gradient(145deg, rgba(20, 20, 35, 0.95), rgba(10, 10, 20, 0.98));
    border: 1px solid rgba(201, 162, 39, 0.4);
    border-radius: 12px;
    padding: 1.5rem;
    margin-top: 1.5rem;
    box-shadow: 0 0 30px rgba(201, 162, 39, 0.2);
    display: none;
}

#prompt-oracle-app .result-box.visible {
    display: block;
}

#prompt-oracle-app .result-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 1rem;
    flex-wrap: wrap;
    gap: 0.75rem;
}

#prompt-oracle-app .result-title {
    color: var(--gold);
    font-size: 1.2rem;
    margin: 0;
    border: none;
    padding: 0;
}

#prompt-oracle-app .result-principle {
    color: var(--text-muted);
    font-style: italic;
    font-size: 0.9rem;
    margin: 0.25rem 0 0 0;
}

#prompt-oracle-app .model-badge {
    display: inline-block;
    padding: 0.15rem 0.5rem;
    border-radius: 4px;
    font-size: 0.7rem;
    font-weight: 600;
    margin-left: 0.5rem;
    vertical-align: middle;
}

#prompt-oracle-app .model-badge.claude {
    background: rgba(217, 119, 6, 0.2);
    color: #d97706;
    border: 1px solid rgba(217, 119, 6, 0.4);
}

#prompt-oracle-app .model-badge.chatgpt {
    background: rgba(16, 163, 127, 0.2);
    color: #10a37f;
    border: 1px solid rgba(16, 163, 127, 0.4);
}

#prompt-oracle-app .code-block {
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid rgba(139, 92, 246, 0.3);
    border-radius: 8px;
    padding: 1rem;
    font-family: 'Fira Code', 'Courier New', monospace;
    font-size: 0.8rem;
    line-height: 1.5;
    white-space: pre-wrap;
    overflow-x: auto;
    margin-bottom: 1rem;
}

#prompt-oracle-app .explanation {
    background: rgba(0, 0, 0, 0.3);
    border-radius: 8px;
    padding: 1rem;
    border-left: 3px solid var(--blue);
    margin-top: 1rem;
    display: none;
}

#prompt-oracle-app .explanation.visible {
    display: block;
}

#prompt-oracle-app .explanation h4 {
    color: var(--blue);
    margin: 0 0 0.75rem 0;
    font-size: 1rem;
    border: none;
    padding: 0;
}

#prompt-oracle-app .explanation .tips-title {
    color: var(--green);
    margin: 1rem 0 0.5rem 0;
}

#prompt-oracle-app .explanation .pattern-title {
    color: var(--purple);
}

#prompt-oracle-app .tips {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
}

#prompt-oracle-app .tip {
    display: inline-block;
    background: rgba(74, 144, 121, 0.2);
    border: 1px solid rgba(74, 144, 121, 0.4);
    color: var(--green);
    padding: 0.2rem 0.6rem;
    border-radius: 15px;
    font-size: 0.75rem;
}

#prompt-oracle-app .reference {
    background: linear-gradient(145deg, rgba(15, 15, 25, 0.9), rgba(10, 10, 20, 0.95));
    border-radius: 10px;
    border: 1px solid rgba(74, 144, 121, 0.3);
    padding: 1.5rem;
    margin-top: 2rem;
}

#prompt-oracle-app .reference h3 {
    color: var(--green);
    margin: 0 0 1rem 0;
    font-size: 1.1rem;
    border: none;
    padding: 0;
}

#prompt-oracle-app .reference-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1rem;
}

#prompt-oracle-app .reference-col h4 {
    color: var(--gold);
    font-size: 0.9rem;
    margin: 0 0 0.5rem 0;
    border: none;
    padding: 0;
}

#prompt-oracle-app .reference-col.blue h4 { color: var(--blue); }
#prompt-oracle-app .reference-col.purple h4 { color: var(--purple); }

#prompt-oracle-app table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.8rem;
}

#prompt-oracle-app td {
    padding: 0.4rem;
    border-bottom: 1px solid rgba(201, 162, 39, 0.1);
}

#prompt-oracle-app td:first-child {
    color: var(--gold);
    font-family: 'Fira Code', monospace;
    font-size: 0.75rem;
}

#prompt-oracle-app .ref-list {
    list-style: none;
    padding: 0;
    margin: 0;
    font-size: 0.8rem;
}

#prompt-oracle-app .ref-list li {
    padding: 0.25rem 0;
    color: var(--text-muted);
}

#prompt-oracle-app .ref-list li::before {
    content: "→ ";
    color: var(--blue);
}

#prompt-oracle-app .hidden {
    display: none !important;
}

#prompt-oracle-app .oracle-footer {
    text-align: center;
    margin-top: 2rem;
    padding-top: 1rem;
    color: var(--text-muted);
    border-top: 1px solid rgba(201, 162, 39, 0.1);
    font-size: 0.85rem;
}

#prompt-oracle-app .oracle-footer .symbols {
    font-size: 1rem;
    letter-spacing: 0.3rem;
}
</style>

<link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;0,700;1,400&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">

<div class="oracle-header">
    <div class="symbols">☰ ☷ ☵</div>
    <h2 class="oracle-title">L'Oracle du Prompt</h2>
    <p class="subtitle">Générateur Initiatique — Apprends en Créant</p>
</div>

<!-- Model Selection -->
<div class="section-title"><span>⚙</span> Choisis ton Modèle</div>
<div class="model-selector">
    <div class="model-card selected" data-model="claude" onclick="OracleApp.selectModel('claude')">
        <div class="model-icon" style="color: #d97706">🅲</div>
        <div class="model-name">Claude</div>
        <div class="model-hint">Anthropic • XML</div>
    </div>
    <div class="model-card" data-model="chatgpt" onclick="OracleApp.selectModel('chatgpt')">
        <div class="model-icon" style="color: #10a37f">🅶</div>
        <div class="model-name">ChatGPT</div>
        <div class="model-hint">OpenAI • Markdown</div>
    </div>
</div>
<div class="model-tips" id="oracle-model-tips"></div>

<!-- Level Selection -->
<div class="section-title"><span>☽</span> Niveau d'Initiation</div>
<div class="levels-grid" id="oracle-levels"></div>

<!-- Technique Selection -->
<div class="section-title hidden" id="oracle-tech-title"><span>☿</span> Techniques</div>
<div class="techniques-list hidden" id="oracle-techniques"></div>

<!-- Input -->
<div class="hidden" id="oracle-input-section">
    <div class="section-title"><span>☿</span> Décris ta Quête</div>
    <textarea id="oracle-context" placeholder="Décris ton objectif... Ex: Créer un script Python pour scanner les vulnérabilités réseau"></textarea>
    <button class="btn" onclick="OracleApp.generate()">☉ Consulter l'Oracle</button>
</div>

<!-- Result -->
<div class="result-box" id="oracle-result">
    <div class="result-header">
        <div>
            <h3 class="result-title" id="oracle-result-title">Révélation</h3>
            <p class="result-principle" id="oracle-result-principle"></p>
        </div>
        <button class="btn" onclick="OracleApp.copy()">⎘ Copier</button>
    </div>
    <div class="code-block" id="oracle-prompt"></div>
    <button class="btn-secondary" onclick="OracleApp.toggleExplanation()">▶ Révéler l'Enseignement</button>
    <div class="explanation" id="oracle-explanation">
        <h4>☿ Pourquoi cette Structure ?</h4>
        <p id="oracle-explain-text"></p>
        <h4 class="tips-title">✦ Conseils du Maître</h4>
        <div class="tips" id="oracle-tips"></div>
        <h4 class="pattern-title">♄ Pattern Original</h4>
        <div class="code-block" id="oracle-pattern"></div>
    </div>
</div>

<!-- Reference -->
<div class="reference">
    <h3><span>☵</span> Grimoire de Référence</h3>
    <div class="reference-grid">
        <div class="reference-col">
            <h4>☰ Paramètres API</h4>
            <table>
                <tr><td>temperature</td><td>0-0.3 factuel, 0.7+ créatif</td></tr>
                <tr><td>max_tokens</td><td>Adapter + 20% marge</td></tr>
                <tr><td>top_p</td><td>0.9-0.95 typique</td></tr>
            </table>
        </div>
        <div class="reference-col blue">
            <h4>☷ Erreurs Communes</h4>
            <ul class="ref-list">
                <li>Instructions vagues → Être explicite</li>
                <li>Trop de tâches → Décomposer</li>
                <li>Format imprécis → Fournir exemple</li>
            </ul>
        </div>
        <div class="reference-col purple">
            <h4>☴ Balises</h4>
            <div class="code-block" style="font-size:0.7rem;padding:0.5rem;">&lt;instructions&gt;
&lt;context&gt;
&lt;constraints&gt;
&lt;output_format&gt;</div>
        </div>
    </div>
</div>

<div class="oracle-footer">
    <div class="symbols">☰ ☱ ☲ ☳ ☴ ☵ ☶ ☷</div>
    <p>L'Oracle du Prompt — CyberMind.FR</p>
</div>

<script>
const OracleApp = (function() {
    const models = {
        claude: {
            name: 'Claude', icon: '🅲', color: '#d97706',
            tips: ['Balises XML recommandées', 'Instructions positives', 'Extended thinking disponible', 'Artifacts pour code/docs']
        },
        chatgpt: {
            name: 'ChatGPT', icon: '🅶', color: '#10a37f',
            tips: ['Markdown et headers ###', 'System/user/assistant roles', 'Code Interpreter intégré', 'Function calls natives']
        }
    };

    const levels = [
        { id: 1, name: 'Néophyte', symbol: '☽', description: 'Fondamentaux', color: '#4a9079' },
        { id: 2, name: 'Initié', symbol: '☿', description: 'Techniques structurées', color: '#6b8cae' },
        { id: 3, name: 'Adepte', symbol: '☉', description: 'Patterns avancés', color: '#c9a227' },
        { id: 4, name: 'Maître', symbol: '♄', description: 'Orchestration complexe', color: '#8b5cf6' }
    ];

    const techniques = {
        1: [
            { id: 'zero-shot', name: 'Zero-Shot', trigram: '☰', principle: 'La clarté sans exemple',
              description: 'Instruction directe sans exemples préalables.',
              pattern: { claude: '[RÔLE] {role}\n[TÂCHE] {tache}\n[FORMAT] {format}',
                        chatgpt: '**Role:** {role}\n**Task:** {tache}\n**Format:** {format}' },
              tips: ['Format explicite', 'Une instruction = une action', 'Éviter ambiguïté'] },
            { id: 'persona', name: 'Persona', trigram: '☱', principle: "L'incarnation de l'expertise",
              description: 'Définir un rôle expert pour orienter les réponses.',
              pattern: { claude: 'Tu es un {expert} avec {experience}.\nTon style est {style}.\nTu dois {objectif}.',
                        chatgpt: 'You are a {expert} with {experience}.\nYour style is {style}.\nYour task: {objectif}.' },
              tips: ['Niveau expertise', 'Ton attendu', 'Domaine contextualisé'] },
            { id: 'delimiter', name: 'Délimiteurs', trigram: '☲', principle: 'Les frontières du sens',
              description: 'Balises pour séparer instructions, contexte et données.',
              pattern: { claude: '<instructions>\n{directives}\n</instructions>\n\n<input>\n{donnees}\n</input>\n\n<output_format>\n{format_attendu}\n</output_format>',
                        chatgpt: '### Instructions\n{directives}\n\n### Input\n```\n{donnees}\n```\n\n### Output Format\n{format_attendu}' },
              tips: { claude: ['XML tags natifs', 'Nesting possible'], chatgpt: ['Headers ###', 'Code blocks ```'] } }
        ],
        2: [
            { id: 'few-shot', name: 'Few-Shot', trigram: '☳', principle: "Enseigner par l'exemple",
              description: 'Fournir 2-5 exemples pour guider le pattern.',
              pattern: { claude: '<examples>\n<example>\n<input>{ex_in_1}</input>\n<output>{ex_out_1}</output>\n</example>\n</examples>\n\nMaintenant:\n<input>{input_reel}</input>',
                        chatgpt: '**Examples:**\n- Input: {ex_in_1} → Output: {ex_out_1}\n\n**Now process:**\n- Input: {input_reel}' },
              tips: ['Exemples variés', 'Cas limites', 'Format cohérent'] },
            { id: 'constraints', name: 'Contraintes', trigram: '☴', principle: 'Définir les limites',
              description: 'Spécifier ce qui est permis et interdit.',
              pattern: { claude: '<task>{objectif}</task>\n\n<constraints>\n<do>\n- {do_1}\n- {do_2}\n</do>\n<avoid>\n- {dont_1}\n</avoid>\n</constraints>',
                        chatgpt: '## Task\n{objectif}\n\n## Rules\n✅ DO: {do_1}, {do_2}\n❌ DON\'T: {dont_1}' },
              tips: ['Positif d\'abord', 'Interdits spécifiques', 'Validation incluse'] },
            { id: 'structured', name: 'Output Structuré', trigram: '☵', principle: 'La forme précède le fond',
              description: 'Imposer un format de sortie précis (JSON, etc.).',
              pattern: { claude: 'Analyse {sujet}. Retourne UNIQUEMENT:\n\n<output>\n{\n  "summary": "...",\n  "points": [...],\n  "risk": "low|medium|high"\n}\n</output>',
                        chatgpt: 'Analyze {sujet}. Return ONLY:\n\n```json\n{\n  "summary": "...",\n  "points": [...],\n  "risk": "low|medium|high"\n}\n```' },
              tips: ['Schéma exact', 'Types définis', 'Pas de texte superflu'] }
        ],
        3: [
            { id: 'cot', name: 'Chain of Thought', trigram: '☶', principle: 'Le chemin révèle la destination',
              description: 'Raisonnement étape par étape.',
              pattern: { claude: '{probleme}\n\n<instructions>\n1. ANALYSE: éléments clés\n2. DÉCOMPOSITION: sous-problèmes\n3. RAISONNEMENT: résoudre\n4. SYNTHÈSE: solution\n5. VÉRIFICATION\n</instructions>\n\nMontre ton raisonnement dans <thinking>.',
                        chatgpt: '{probleme}\n\n### Step-by-step:\n1. **Analysis:** key elements\n2. **Decomposition:** sub-problems\n3. **Reasoning:** solve each\n4. **Synthesis:** combine\n5. **Verification:** check' },
              tips: ['Étapes numérotées', 'Vérification finale', 'Problèmes complexes'] },
            { id: 'react', name: 'ReAct', trigram: '☷', principle: 'Penser puis Agir',
              description: 'Alternance réflexion/action.',
              pattern: { claude: 'Pour {objectif}, utilise ce cycle:\n\n<cycle>\n<thought>[Réflexion]</thought>\n<action>[Action]</action>\n<observation>[Résultat]</observation>\n</cycle>\n\nRépète jusqu\'à complétion.',
                        chatgpt: 'For {objectif}, use this cycle:\n\n**Thought:** [Reflection]\n**Action:** [Action]\n**Observation:** [Result]\n\nRepeat until done.' },
              tips: ['Multi-étapes', 'Debugging possible', 'Raisonnement explicite'] },
            { id: 'critique', name: 'Auto-Critique', trigram: '☰', principle: 'Le doute constructif',
              description: 'Critiquer et améliorer sa réponse.',
              pattern: { claude: '{tache}\n\n<process>\n1. Réponse initiale dans <draft>\n2. Critique dans <critique> (3 faiblesses)\n3. Version finale dans <final>\n</process>',
                        chatgpt: '{tache}\n\n### Draft\n[Initial answer]\n\n### Self-Critique\n- Weakness 1...\n- Weakness 2...\n\n### Final Answer\n[Improved]' },
              tips: ['Qualité améliorée', 'Angles morts révélés', 'Plus de tokens'] }
        ],
        4: [
            { id: 'meta', name: 'Meta-Prompting', trigram: '☱', principle: 'Le prompt qui crée des prompts',
              description: 'Utiliser le LLM pour générer des prompts.',
              pattern: { claude: '<role>Expert en prompt engineering pour Claude.</role>\n\n<request>\n<objective>{objectif_final}</objective>\n<context>{contexte}</context>\n</request>\n\n<task>Génère un prompt optimisé.</task>\n\n<output_format>\n<generated_prompt>[...]</generated_prompt>\n<explanation>[...]</explanation>\n</output_format>',
                        chatgpt: 'You are a prompt engineering expert for GPT.\n\n## Request\n- Objective: {objectif_final}\n- Context: {contexte}\n\n## Task\nGenerate an optimized prompt.\n\n## Output\n```prompt\n[...]\n```\n**Explanation:** [...]' },
              tips: ['Itération prompts', 'Capture expertise', 'Automatisation'] },
            { id: 'multiagent', name: 'Multi-Agent', trigram: '☲', principle: 'La sagesse des perspectives',
              description: 'Simuler plusieurs experts débattant.',
              pattern: { claude: '<simulation>\n<agents>\n<agent role="Pragmatique"/>\n<agent role="Critique"/>\n<agent role="Innovateur"/>\n</agents>\n<topic>{sujet}</topic>\n</simulation>\n\nSimule le débat, puis:\n<consensus>[...]</consensus>\n<divergences>[...]</divergences>',
                        chatgpt: '**Simulate 3 experts:**\n- Pragmatist\n- Critic  \n- Innovator\n\n**Topic:** {sujet}\n\n### Debate\n[...]\n\n### Consensus\n[...]\n\n### Divergences\n[...]' },
              tips: ['Perspectives opposées', 'Forcer synthèse', 'Révèle complexité'] },
            { id: 'constitutional', name: 'Constitutional AI', trigram: '☳', principle: 'Les règles qui gouvernent',
              description: 'Principes hiérarchiques à respecter.',
              pattern: { claude: '<constitution>\n<principles>\n1. {principe_1}\n2. {principe_2}\n</principles>\n<hierarchy>Sécurité > Exactitude > Utilité</hierarchy>\n</constitution>\n\n<task>{tache}</task>\n\nVérifie conformité avant de répondre.',
                        chatgpt: '# CONSTITUTION\n\n## Principles\n1. {principe_1}\n2. {principe_2}\n\n## Hierarchy\nSecurity > Accuracy > Utility\n\n---\n**Task:** {tache}\n\nVerify compliance before responding.' },
              tips: ['Hiérarchie claire', 'Conflits prévus', 'Systèmes critiques'] }
        ]
    };

    let state = { model: 'claude', level: null, technique: null };

    function init() {
        renderLevels();
        updateModelTips();
    }

    function selectModel(modelId) {
        state.model = modelId;
        document.querySelectorAll('#prompt-oracle-app .model-card').forEach(c => c.classList.remove('selected'));
        document.querySelector(`#prompt-oracle-app .model-card[data-model="${modelId}"]`).classList.add('selected');
        updateModelTips();
        document.getElementById('oracle-result').classList.remove('visible');
    }

    function updateModelTips() {
        const m = models[state.model];
        document.getElementById('oracle-model-tips').innerHTML = 
            `<h4 style="color:${m.color}">${m.icon} Tips ${m.name}</h4><ul>${m.tips.map(t=>`<li>${t}</li>`).join('')}</ul>`;
        document.getElementById('oracle-model-tips').style.borderLeftColor = m.color;
    }

    function renderLevels() {
        document.getElementById('oracle-levels').innerHTML = levels.map(l => 
            `<div class="level-card" data-level="${l.id}" onclick="OracleApp.selectLevel(${l.id})">
                <div class="symbol" style="color:${l.color}">${l.symbol}</div>
                <div class="name" style="color:${l.color}">${l.name}</div>
                <div class="desc">${l.description}</div>
            </div>`
        ).join('');
    }

    function selectLevel(id) {
        state.level = levels.find(l => l.id === id);
        state.technique = null;
        document.querySelectorAll('#prompt-oracle-app .level-card').forEach(c => c.classList.remove('selected'));
        document.querySelector(`#prompt-oracle-app .level-card[data-level="${id}"]`).classList.add('selected');
        
        document.getElementById('oracle-tech-title').classList.remove('hidden');
        document.getElementById('oracle-tech-title').innerHTML = `<span>${state.level.symbol}</span> Techniques ${state.level.name}`;
        renderTechniques(id);
        
        document.getElementById('oracle-input-section').classList.add('hidden');
        document.getElementById('oracle-result').classList.remove('visible');
    }

    function renderTechniques(levelId) {
        const container = document.getElementById('oracle-techniques');
        container.classList.remove('hidden');
        container.innerHTML = techniques[levelId].map(t => 
            `<div class="technique-card" data-tech="${t.id}" onclick="OracleApp.selectTechnique('${t.id}')">
                <span class="trigram" style="color:${state.level.color}">${t.trigram}</span>
                <div>
                    <div class="tech-name">${t.name}</div>
                    <div class="principle">"${t.principle}"</div>
                    <div class="description">${t.description}</div>
                </div>
            </div>`
        ).join('');
    }

    function selectTechnique(id) {
        state.technique = techniques[state.level.id].find(t => t.id === id);
        document.querySelectorAll('#prompt-oracle-app .technique-card').forEach(c => c.classList.remove('selected'));
        document.querySelector(`#prompt-oracle-app .technique-card[data-tech="${id}"]`).classList.add('selected');
        document.getElementById('oracle-input-section').classList.remove('hidden');
        document.getElementById('oracle-result').classList.remove('visible');
    }

    function generate() {
        const context = document.getElementById('oracle-context').value.trim();
        if (!context || !state.technique) return;

        const pattern = typeof state.technique.pattern === 'object' 
            ? state.technique.pattern[state.model] 
            : state.technique.pattern;
        
        const filled = fillTemplate(pattern, context);
        const m = models[state.model];

        document.getElementById('oracle-result-title').innerHTML = 
            `${state.technique.trigram} ${state.technique.name} <span class="model-badge ${state.model}">${m.icon} ${m.name}</span>`;
        document.getElementById('oracle-result-principle').textContent = 
            `${state.level.name} — "${state.technique.principle}"`;
        document.getElementById('oracle-prompt').textContent = filled;
        document.getElementById('oracle-explain-text').textContent = state.technique.description;
        document.getElementById('oracle-pattern').textContent = pattern;

        const tips = typeof state.technique.tips === 'object' && !Array.isArray(state.technique.tips)
            ? state.technique.tips[state.model] || Object.values(state.technique.tips)[0]
            : state.technique.tips;
        document.getElementById('oracle-tips').innerHTML = tips.map(t => `<span class="tip">${t}</span>`).join('');

        document.getElementById('oracle-result').classList.add('visible');
        document.getElementById('oracle-explanation').classList.remove('visible');
    }

    function fillTemplate(tpl, ctx) {
        const isEN = state.model === 'chatgpt';
        const r = {
            '{role}': isEN ? 'domain expert' : 'expert du domaine',
            '{expert}': isEN ? 'senior consultant' : 'consultant senior',
            '{experience}': isEN ? 'deep expertise' : 'expertise approfondie',
            '{style}': isEN ? 'professional, accessible' : 'professionnel, accessible',
            '{format}': isEN ? 'Structured response' : 'Réponse structurée',
            '{tache}': ctx, '{objectif}': ctx, '{sujet}': ctx, '{probleme}': ctx,
            '{directives}': ctx, '{input_reel}': ctx, '{objectif_final}': ctx,
            '{donnees}': isEN ? '[Your data]' : '[Vos données]',
            '{format_attendu}': isEN ? 'Appropriate format' : 'Format adapté',
            '{ex_in_1}': 'Example A', '{ex_out_1}': 'Output A',
            '{do_1}': isEN ? 'Follow best practices' : 'Bonnes pratiques',
            '{do_2}': isEN ? 'Document reasoning' : 'Documenter',
            '{dont_1}': isEN ? 'Make assumptions' : 'Suppositions',
            '{contexte}': isEN ? 'Production' : 'Production',
            '{principe_1}': isEN ? 'Data security' : 'Sécurité données',
            '{principe_2}': isEN ? 'Accuracy' : 'Exactitude'
        };
        let out = tpl;
        for (const [k,v] of Object.entries(r)) out = out.split(k).join(v);
        return out;
    }

    function copy() {
        navigator.clipboard.writeText(document.getElementById('oracle-prompt').textContent);
        event.target.textContent = '✓ Copié!';
        setTimeout(() => event.target.textContent = '⎘ Copier', 2000);
    }

    function toggleExplanation() {
        const el = document.getElementById('oracle-explanation');
        const btn = event.target;
        if (el.classList.contains('visible')) {
            el.classList.remove('visible');
            btn.textContent = '▶ Révéler l\'Enseignement';
        } else {
            el.classList.add('visible');
            btn.textContent = '▼ Masquer';
        }
    }

    document.addEventListener('DOMContentLoaded', init);
    if (document.readyState !== 'loading') init();

    return { selectModel, selectLevel, selectTechnique, generate, copy, toggleExplanation };
})();
</script>

</div>

---

## Niveaux d'Initiation

| Niveau | Symbole | Techniques |
|--------|---------|------------|
| ☽ Néophyte | Lune | Zero-shot, Persona, Délimiteurs |
| ☿ Initié | Mercure | Few-shot, Contraintes, Output structuré |
| ☉ Adepte | Soleil | Chain-of-Thought, ReAct, Auto-critique |
| ♄ Maître | Saturne | Meta-prompting, Multi-agent, Constitutional AI |

## Différences Claude vs ChatGPT

| Aspect | Claude 🅲 | ChatGPT 🅶 |
|--------|----------|-----------|
| Structure | Balises XML `<tag>` | Markdown `### Headers` |
| Langue | Français natif | English patterns |
| Raisonnement | `<thinking>` tags | `### Reasoning:` |
| Output | `<output>` tags | Code blocks ``` |

## Pour aller plus loin

- [Documentation Anthropic](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Prompting Guide](https://www.promptingguide.ai/)

*"Le sage maîtrise le prompt comme l'archer maîtrise son arc"*
