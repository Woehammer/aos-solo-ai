// lib/ai/targeting/selectBestTarget.js

import { getDistance } from '../utils/distance';

/**

Prioritizes targets based on threat level and distance

@param {Object} unit - The attacking unit

@param {Array} enemies - List of enemy units

@param {Object} battlefield - Current battlefield state

@returns {Object|null} - Best target or null */ export function selectBestTarget(unit, enemies, battlefield) { if (!unit || !enemies || enemies.length === 0) return null;


// Filter out dead units const aliveEnemies = enemies.filter(enemy => enemy.models > 0);

// Evaluate each target const scored = aliveEnemies.map(enemy => { const distance = getDistance(unit.position, enemy.position); const woundsRemaining = enemy.wounds * enemy.models; const priority = unit.keywords.includes('Hero') && enemy.keywords.includes('Hero') ? 3 : 1;

return {
  enemy,
  score: priority * 100 - distance * 2 - woundsRemaining * 0.5
};

});

// Sort by descending score scored.sort((a, b) => b.score - a.score);

return scored[0]?.enemy || null; }

