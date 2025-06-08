from flask import Flask, render_template, request, redirect, url_for
from game_state import GameState
from ai_controller import AIController
from battlefield_state import BattlefieldState

app = Flask(__name__)

game_state = GameState()
battlefield_state = BattlefieldState()
ai_controller = AIController(game_state, battlefield_state)

battle_log = []
@app.route("/", methods=["GET", "POST"])
def index():
    global game_state, battlefield_state, ai_controller, battle_log

    if request.method == "POST":
        game_state = GameState()
        battlefield_state = BattlefieldState()
        ai_controller = AIController(game_state, battlefield_state)
        battle_log.clear()
        return redirect(url_for("game"))

    return render_template("index.html")
@app.route("/game", methods=["GET", "POST"])
def game():
    global game_state, battlefield_state, ai_controller, battle_log

    if request.method == "POST":
        # Collect battlefield inputs
        battlefield_state.killaboss_enemy_distance = int(request.form["killaboss_enemy_distance"])
        battlefield_state.killaboss_objective_distance = int(request.form["killaboss_objective_distance"])
        battlefield_state.killaboss_charge = request.form["killaboss_charge"]

        # Same for other units (Murknob, Gutrippaz, Boltboyz, Killbow)
        battlefield_state.murknob_enemy_distance = int(request.form["murknob_enemy_distance"])
        battlefield_state.murknob_objective_distance = int(request.form["murknob_objective_distance"])
        battlefield_state.murknob_charge = request.form["murknob_charge"]

        battlefield_state.gutrippaz_enemy_distance = int(request.form["gutrippaz_enemy_distance"])
        battlefield_state.gutrippaz_objective_distance = int(request.form["gutrippaz_objective_distance"])
        battlefield_state.gutrippaz_charge = request.form["gutrippaz_charge"]

        battlefield_state.boltboyz_enemy_distance = int(request.form["boltboyz_enemy_distance"])
        battlefield_state.boltboyz_objective_distance = int(request.form["boltboyz_objective_distance"])
        battlefield_state.boltboyz_charge = request.form["boltboyz_charge"]

        battlefield_state.killbow_enemy_distance = int(request.form["killbow_enemy_distance"])
        battlefield_state.killbow_objective_distance = int(request.form["killbow_objective_distance"])
        battlefield_state.killbow_charge = request.form["killbow_charge"]

        # Run AI Turn
        log = ai_controller.run_turn()
        battle_log.append({
            'round': game_state.round,
            'phase_log': log
        })

        # After turn, collect contested objective control
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
