// lib/utils/objectiveDistanceResolver.js

import { getDistance } from './getDistance';

/**

Calculates distance from each unit to each objective on the battlefield.

@param {Array} units - Array of unit objects with id and position ({ x, y })

@param {Object} objectives - Object with named objectives and their positions

@returns {Object} distancesByUnitId */ export function resolveObjectiveDistances(units, objectives) { const distancesByUnitId = {};


for (const unit of units) { const distances = {}; let nearestObjective = null; let nearestDistance = Infinity;

for (const [name, position] of Object.entries(objectives)) {
  const dist = getDistance(unit.position, position);
  distances[name] = dist;

  if (dist < nearestDistance) {
    nearestDistance = dist;
    nearestObjective = name;
  }
}

distancesByUnitId[unit.id] = {
  ...distances,
  nearest: nearestObjective,
  nearestDistance,
};

}

return distancesByUnitId; }

/**

Example objective positions:

const objectives = {

dracothionDias: { x: 10, y: 20 },

ignaxDias: { x: 25, y: 10 },

vulcatrixDias: { x: 5, y: 35 },

behematDias: { x: 40, y: 15 },

agendaDias: { x: 20, y: 30 },

}; */


