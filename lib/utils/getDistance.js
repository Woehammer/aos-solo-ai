// lib/utils/getDistance.js

export function getDistance(pos1, pos2) { const dx = pos1.x - pos2.x; const dy = pos1.y - pos2.y; return Math.sqrt(dx * dx + dy * dy); }
