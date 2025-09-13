// /lib/ai/resolveShooting.js

import { getUnitsInRange, getVisibleEnemies } from '@/lib/gameUtils'; import { rollHit, rollWound, calculateDamage, buildSaveText } from '@/lib/ai/diceRollers'; import { logMessage } from '@/lib/ai/aiLogger'; import { chooseTarget } from '@/lib/ai/targetingLogic';

export async function resolveShooting(gameState) { const { aiArmy, humanArmy, log } = gameState;

const shooters = aiArmy.units.filter( unit => unit.models > 0 && unit.shootingAttacks && unit.shootingAttacks.length > 0 );

for (const shooter of shooters) { const validTargets = getVisibleEnemies(shooter, humanArmy.units); if (validTargets.length === 0) continue;

const target = chooseTarget(shooter, validTargets);
if (!target) continue;

for (const attack of shooter.shootingAttacks) {
  const numAttacks = attack.attacks * shooter.models;
  const hits = rollHit(numAttacks, attack.toHit);
  const wounds = rollWound(hits, attack.toWound);
  const unsaved = wounds; // Save rolls are done by player

  const damageTotal = calculateDamage(unsaved, attack.damage);

  const saveText = buildSaveText(target, attack.rend, attack.damage, unsaved);
  const message = `${shooter.name} unleashes ${attack.name} at ${target.name}! ${saveText}`;
  logMessage(log, message);

  target.pendingWounds = (target.pendingWounds || 0) + damageTotal;
}

}

return gameState; }

