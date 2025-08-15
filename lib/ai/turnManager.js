import { resolveCombat } from '@/lib/ai/combatResolver';
import { resolveShooting } from '@/lib/ai/shootingResolver';
import { resolveMovement } from '@/lib/ai/movementLogic';
// import other phase logic as needed

export async function runAIPhase(gameState, currentPhase) {
  switch (currentPhase) {
    case 'hero':
      // Placeholder: implement hero phase logic (spells, commands)
      console.log('[AI PHASE] Hero Phase not implemented yet.');
      return gameState;

    case 'movement':
      return await resolveMovement(gameState);

    case 'shooting':
      return await resolveShooting(gameState);

    case 'combat':
      return await resolveCombat(gameState); // ✅ Plugged in here

    case 'battleshock':
      // Placeholder: could check unit losses etc.
      console.log('[AI PHASE] Battleshock not implemented yet.');
      return gameState;

    default:
      console.warn(`[AI PHASE] Unknown phase: ${currentPhase}`);
      return gameState;
  }
}
