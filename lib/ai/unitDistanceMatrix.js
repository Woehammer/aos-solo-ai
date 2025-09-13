// lib/ai/unitDistanceMatrix.js

import { getDistance } from "./getDistance";

/**

Generates a matrix of distances between each unit and each other unit.

This is used by tactical AI to evaluate threats and support potential.

@param {Array} units - All units in the game, both AI and human.

@returns {Object} - A nested object matrix: distances[unitIdA][unitIdB] = distance */ export function generateUnitDistanceMatrix(units) { const matrix = {};


for (let i = 0; i < units.length; i++) { const unitA = units[i]; matrix[unitA.id] = {};

for (let j = 0; j < units.length; j++) {
  const unitB = units[j];
  const distance = getDistance(unitA.position, unitB.position);
  matrix[unitA.id][unitB.id] = distance;
}

}

return matrix; }

