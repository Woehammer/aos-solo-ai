// combatResolver.js

import { gameState } from './gameState';
import { getCombatNarrative } from './narrativeGenerator';
import { calculateHits, calculateWounds, calculateSaves, applyDamage } from './diceUtils';
import { getUnitById } from './utils';

export function resolveCombat(attackerId, defenderId, weaponProfile) {
  const attacker = getUnitById(attackerId);
  const defender = getUnitById(defenderId);

  const { attacks, toHit, toWound, rend, damage, critEffect } = weaponProfile;

  const result = {
    hits: 0,
    crits: 0,
    wounds: 0,
    failedSaves: 0,
    totalDamage: 0,
    message: '',
  };

  const hits = calculateHits(attacks, toHit, critEffect);
  result.hits = hits.normal;
  result.crits = hits.crit;

  const wounds = calculateWounds(hits.normal + hits.crit, toWound, critEffect);
  result.wounds = wounds.total;

  const saves = calculateSaves(wounds.total, defender.save, rend, defender.ward);
  result.failedSaves = saves.failed;

  const totalDamage = applyDamage(saves.failed, damage, critEffect);
  result.totalDamage = totalDamage;

  // Update defender model count
  const modelsKilled = Math.floor(totalDamage / defender.wounds);
  defender.models -= modelsKilled;
  if (defender.models < 0) defender.models = 0;

  // Log narrative
  result.message = getCombatNarrative(attacker, defender, result, weaponProfile);
  gameState.combatLog.push(result.message);

  return result;
}

export function canFight(unit) {
  return unit.models > 0 && !unit.hasFought;
}
