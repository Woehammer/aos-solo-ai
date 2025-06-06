from game_state import GameState
from ai_controller import AIController

# Initialize game state and AI
game = GameState()
ai = AIController()

# Main Game Loop
while game.round <= game.max_rounds:
    print(f"\n=== Round {game.round} ===")

    # Hero Phase
    ai.hero_phase()

    # Movement Phase
    ai.movement_phase()

    # Shooting Phase
    ai.shooting_phase()

    # Charge Phase
    ai.charge_phase()

    # Combat Phase
    ai.combat_phase()

    # End of Round: Ask player for contested objective outcome
    result = input("Who controls contested objective? (ai/player/neutral): ").strip().lower()
    if result in ["ai", "player", "neutral"]:
        game.contested_objective = result
    else:
        print("Invalid input. Defaulting to neutral.")
        game.contested_objective = "neutral"

    # Score update
    game.update_scores()
    game.print_score()
    game.advance_round()

# End of Game Summary
print("\n=== Final Score ===")
game.print_score()
if game.ai_vp > game.player_vp:
    print("AI Wins!")
elif game.player_vp > game.ai_vp:
    print("Player Wins!")
else:
    print("It's a Draw!")
