from flask import Flask, render_template, request, redirect, url_for, session
from game_state import GameState
from ai_controller import AIController

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with random string for production use

# In-memory game state per session
games = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        game_id = "solo_game"
        games[game_id] = {
            "state": GameState(),
            "ai": None
        }
        games[game_id]["ai"] = AIController(games[game_id]["state"])
        return redirect(url_for("game"))
    return render_template("index.html")

@app.route("/game", methods=["GET", "POST"])
def game():
    game_id = "solo_game"
    game_data = games[game_id]
    state = game_data["state"]
    ai = game_data["ai"]

    output = []

    # Run full AI turn for the round
    ai.hero_phase()
    ai.movement_phase()
    ai.shooting_phase()
    ai.charge_phase()
    ai.combat_phase()

    output.append(f"=== Round {state.round} ===")
    output.append("--- AI Turn Complete ---")

    if request.method == "POST":
        controller = request.form["controller"]
        if controller in ["ai", "player", "neutral"]:
            state.contested_objective = controller
        else:
            state.contested_objective = "neutral"

        state.update_scores()
        state.advance_round()

        if state.round > state.max_rounds:
            return redirect(url_for("end"))

        return redirect(url_for("game"))

    return render_template("game.html", output=output, state=state)

@app.route("/end")
def end():
    game_id = "solo_game"
    state = games[game_id]["state"]
    return render_template("end.html", state=state)

if __name__ == "__main__":
    app.run(debug=True)
