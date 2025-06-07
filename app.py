from flask import Flask, render_template, request, redirect, url_for
from game_state import GameState
from ai_controller import AIController

app = Flask(__name__)

# In-memory game state
game_state = GameState()
ai_controller = AIController(game_state)

battle_log = []

@app.route("/", methods=["GET", "POST"])
def index():
    global game_state, ai_controller, battle_log

    if request.method == "POST":
        game_state = GameState()
        ai_controller = AIController(game_state)
        battle_log = []
        return redirect(url_for("game"))
    return render_template("index.html")

@app.route("/game", methods=["GET", "POST"])
def game():
    global game_state, ai_controller, battle_log

    # Full AI turn
    log = []
    log += ai_controller.hero_phase()
    log += ai_controller.movement_phase()
    log += ai_controller.shooting_phase()
    log += ai_controller.charge_phase()
    log += ai_controller.combat_phase()

    battle_log.append({
        'round': game_state.round,
        'phase_log': log
    })

    if request.method == "POST":
        controller = request.form["controller"]
        if controller in ["ai", "player", "neutral"]:
            game_state.contested_objective = controller
        else:
            game_state.contested_objective = "neutral"

        game_state.update_scores()
        game_state.advance_round()

        if game_state.round > game_state.max_rounds:
            return redirect(url_for("end"))

        return redirect(url_for("game"))

    return render_template("game.html", game_state=game_state, battle_log=battle_log)

@app.route("/end")
def end():
    return render_template("end.html", game_state=game_state)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
