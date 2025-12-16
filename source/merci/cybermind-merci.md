---
title: Merci !
date: 2026-01-01
layout: page
permalink: /merci/
description: Votre demande a bien été envoyée - CyberMind
---

<style>
.cm-thanks {
    --cm-bg-primary: #000000;
    --cm-bg-secondary: #0a0a0f;
    --cm-accent-cyan: #00d4ff;
    --cm-accent-green: #00ff88;
    --cm-text-primary: #e8e8ed;
    --cm-text-secondary: #9898a6;
    --cm-text-muted: #5a5a6e;
    --cm-border-subtle: rgba(255,255,255,0.08);
    --cm-glow-cyan: rgba(0,212,255,0.15);
    
    font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--cm-text-primary);
    line-height: 1.7;
    background: var(--cm-bg-primary);
    padding: 3rem 2rem;
    border-radius: 16px;
    margin: -1rem;
    text-align: center;
    min-height: 60vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Space+Grotesk:wght@400;500;600;700&display=swap');

.cm-thanks-icon {
    width: 100px;
    height: 100px;
    background: linear-gradient(135deg, var(--cm-accent-cyan), var(--cm-accent-green));
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
    margin-bottom: 2rem;
    animation: cm-success-pop 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

@keyframes cm-success-pop {
    0% { transform: scale(0); opacity: 0; }
    50% { transform: scale(1.2); }
    100% { transform: scale(1); opacity: 1; }
}

.cm-thanks h1 {
    font-size: clamp(1.8rem, 4vw, 2.5rem);
    font-weight: 700;
    margin: 0 0 1rem 0;
    background: linear-gradient(135deg, var(--cm-accent-cyan), var(--cm-accent-green));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.cm-thanks-message {
    font-size: 1.1rem;
    color: var(--cm-text-secondary);
    max-width: 500px;
    margin: 0 0 2rem 0;
}

.cm-thanks-details {
    background: var(--cm-bg-secondary);
    border: 1px solid var(--cm-border-subtle);
    border-radius: 12px;
    padding: 1.5rem 2rem;
    margin-bottom: 2rem;
    text-align: left;
    max-width: 400px;
}

.cm-thanks-details h3 {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: var(--cm-accent-cyan);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin: 0 0 1rem 0;
}

.cm-thanks-item {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    padding: 0.5rem 0;
    font-size: 0.9rem;
    color: var(--cm-text-secondary);
}

.cm-thanks-item span:first-child {
    color: var(--cm-accent-green);
}

.cm-thanks-cta {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    justify-content: center;
}

.cm-btn {
    padding: 0.9rem 1.8rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    font-weight: 500;
    text-decoration: none;
    border-radius: 6px;
    transition: all 0.3s ease;
    cursor: pointer;
    border: none;
    display: inline-block;
}

.cm-btn-primary {
    background: linear-gradient(135deg, var(--cm-accent-cyan), var(--cm-accent-green));
    color: var(--cm-bg-primary);
}

.cm-btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px var(--cm-glow-cyan);
    color: var(--cm-bg-primary);
}

.cm-btn-secondary {
    background: transparent;
    color: var(--cm-text-primary);
    border: 1px solid var(--cm-border-subtle);
}

.cm-btn-secondary:hover {
    border-color: var(--cm-accent-cyan);
    color: var(--cm-accent-cyan);
}

.cm-thanks-footer {
    margin-top: 3rem;
    padding-top: 2rem;
    border-top: 1px solid var(--cm-border-subtle);
}

.cm-thanks-footer p {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: var(--cm-text-muted);
}

.cm-terminal-mini {
    background: var(--cm-bg-secondary);
    border: 1px solid var(--cm-border-subtle);
    border-radius: 8px;
    padding: 1rem;
    margin-top: 1rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    text-align: left;
    max-width: 350px;
}

.cm-terminal-mini .prompt { color: var(--cm-accent-green); }
.cm-terminal-mini .cmd { color: var(--cm-accent-cyan); }
.cm-terminal-mini .success { color: var(--cm-accent-green); }
</style>

<div class="cm-thanks">
    <div class="cm-thanks-icon">✓</div>
    
    <h1>Message Envoyé !</h1>
    
    <p class="cm-thanks-message">
        Votre demande a bien été reçue. Je reviendrai vers vous dans les plus brefs délais 
        pour discuter de votre projet de sécurité.
    </p>
    
    <div class="cm-thanks-details">
        <h3>Prochaines étapes</h3>
        <div class="cm-thanks-item">
            <span>→</span>
            <span>Analyse de votre demande sous 24-48h</span>
        </div>
        <div class="cm-thanks-item">
            <span>→</span>
            <span>Prise de contact pour préciser vos besoins</span>
        </div>
        <div class="cm-thanks-item">
            <span>→</span>
            <span>Proposition personnalisée avec devis</span>
        </div>
    </div>
    
    <div class="cm-terminal-mini">
        <div><span class="prompt">gandalf@cybermind</span>:<span class="cmd">~</span>$ mail --status</div>
        <div class="success">[✓] Message received. Processing...</div>
    </div>
    
    <div class="cm-thanks-cta" style="margin-top: 2rem;">
        <a href="/" class="cm-btn cm-btn-primary">Retour à l'accueil</a>
        <a href="/blog" class="cm-btn cm-btn-secondary">Lire le blog</a>
    </div>
    
    <div class="cm-thanks-footer">
        <p>CyberMind — Sécurité offensive, éthique défensive.</p>
    </div>
</div>
