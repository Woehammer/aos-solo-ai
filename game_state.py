class GameState:
    def __init__(self):
        self.round = 1
        self.max_rounds = 5
        self.ai_vp = 0
        self.player_vp = 0
        self.ai_objectives = 1
        self.player_objectives = 1
        self.contested_objective = "neutral"

    def update_scores(self):
        if self.contested_objective == "ai":
            self.ai_objectives = 2
            self.player_objectives = 1
        elif self.contested_objective == "player":
            self.ai_objectives = 1
            self.player_objectives = 2
        else:
            self.ai_objectives = 1
            self.player_objectives = 1

        self.ai_vp += self.ai_objectives
        self.player_vp += self.player_objectives

    def advance_round(self):
        self.round += 1

    def print_score(self):
        print(f"--- End of Round {self.round} ---")
        print(f"AI Victory Points: {self.ai_vp}")
        print(f"Player Victory Points: {self.player_vp}")
        print("--------------------------")
