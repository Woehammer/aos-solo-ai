// lib/ai/shootingLogic.js

import { getDistanceBetweenUnits, getObjectiveControlStatus } from '../utils/gameUtils'; import { resolveShooting } from './resolveShooting'; import { selectBestTarget } from './targeting/selectBestTarget'; import { getEligibleShootingUnits } from './unitFilters';

/**

Controls the AI's shooting phase logic

@param {Object} gameState - the current state of the game

@param {Object} aiPlayer - the AI player object

@returns {Array} logMessages - log of shooting actions taken */ export function shootingLogic(gameState, aiPlayer) { const logMessages = [];


// 1. Filter all AI units that are able to shoot const shooters = getEligibleShootingUnits(gameState.units, aiPlayer);

for (const unit of shooters) { // 2. Select the best target based on threat level, proximity, mission etc. const target = selectBestTarget(unit, gameState.units, gameState.objectives); if (!target) continue;

// 3. Execute the shooting sequence against that target
const result = resolveShooting({ shooter: unit, target, gameState });
logMessages.push(result.message);

// 4. Mark unit as having shot
unit.hasShot = true;

}

return logMessages; }


