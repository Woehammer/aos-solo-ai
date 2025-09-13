// lib/ai/movementLogic.js

import { getUnitDistanceMatrix } from './unitDistanceMatrix'; import { resolveObjectiveDistances } from './objectiveDistanceResolver';

export function getNextMove(unit, gameState, objectiveMap) { const { units, objectives, playerTurn } = gameState; const isAIUnit = unit.controller === 'AI';

// Avoid trying to move if already in combat if (unit.inCombat) return unit.position;

// Get distance to all objectives const objectiveDistances = resolveObjectiveDistances(unit, objectiveMap);

// Choose objective based on battle tactic or proximity const targetObjective = chooseTargetObjective(unit, objectives, objectiveDistances);

// Determine closest enemy unit if applicable const enemyUnits = units.filter((u) => u.controller !== unit.controller); const closestEnemy = getClosestEnemy(unit, enemyUnits);

// Logic: move toward the most important thing if (targetObjective && !unit.holdsObjective) { return moveToward(unit.position, targetObjective.position, unit.movement); } else if (closestEnemy) { return moveToward(unit.position, closestEnemy.position, unit.movement); } else { return unit.position; // Hold current ground } }

function chooseTargetObjective(unit, objectives, objectiveDistances) { const validObjectives = objectives.filter((obj) => !obj.heldBy || obj.heldBy !== unit.controller); if (validObjectives.length === 0) return null;

validObjectives.sort((a, b) => { const distA = objectiveDistances[a.id] || Infinity; const distB = objectiveDistances[b.id] || Infinity; return distA - distB; });

return validObjectives[0]; }

function getClosestEnemy(unit, enemyUnits) { let minDist = Infinity; let closest = null;

for (const enemy of enemyUnits) { const dx = enemy.position.x - unit.position.x; const dy = enemy.position.y - unit.position.y; const dist = Math.sqrt(dx * dx + dy * dy); if (dist < minDist) { minDist = dist; closest = enemy; } }

return closest; }

function moveToward(currentPos, targetPos, maxDistance) { const dx = targetPos.x - currentPos.x; const dy = targetPos.y - currentPos.y; const distance = Math.sqrt(dx * dx + dy * dy);

if (distance <= maxDistance) return { x: targetPos.x, y: targetPos.y };

const ratio = maxDistance / distance; return { x: currentPos.x + dx * ratio, y: currentPos.y + dy * ratio, }; }


