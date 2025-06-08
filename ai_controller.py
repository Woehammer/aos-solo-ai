from combat_engine import resolve_unit_attacks, format_attack_output
import movement_logic

class AIController:
    def __init__(self, game_state, battlefield_state):
        self.state = game_state
        self.battlefield = battlefield_state

    def run_turn(self):
        log = []

        log.append(f"=== Round {self.state.round} Tactical AI Turn ===")

        # Movement phase decisions based on inputs:
        log.append(movement_logic.killaboss_decision(
            self.battlefield.killaboss_enemy_distance,
            self.battlefield.killaboss_objective_distance,
            self.battlefield.killaboss_charge))

        log.append(movement_logic.murknob_decision(
            self.battlefield.murknob_enemy_distance,
            self.battlefield.murknob_objective_distance,
            self.battlefield.murknob_charge))

        log.append(movement_logic.gutrippaz_decision(
            self.battlefield.gutrippaz_enemy_distance,
            self.battlefield.gutrippaz_objective_distance,
            self.battlefield.gutrippaz_charge))

        log.append(movement_logic.boltboyz_decision(
            self.battlefield.boltboyz_enemy_distance,
            self.battlefield.boltboyz_objective_distance,
            self.battlefield.boltboyz_charge))

        log.append(movement_logic.killbow_decision(
            self.battlefield.killbow_enemy_distance,
            self.battlefield.killbow_objective_distance,
            self.battlefield.killbow_charge))

        # After movement, we still resolve attacks fully
        log.append("=== Shooting Phase ===")
        log += self.shooting_phase()

        log.append("=== Combat Phase ===")
        log += self.combat_phase()

        return log

    def shooting_phase(self):
        from combat_engine import resolve_unit_attacks, format_attack_output

        boltboyz_attack_profile = [
            {"weapon": "Man-Skewer Crossbows", "attacks": 2, "hit": 4, "wound": 3, "rend": 1, "damage": 2, "crit_rule": "none", "stationary_bonus": True}
        ]

        killbow_attack_profile = [
            {"weapon": "Beast-Skewer Bolts", "attacks": 2, "hit": 4, "wound": 2, "rend": 2, "damage": 6, "crit_rule": "none"}
        ]

        log = []
        result = resolve_unit_attacks(boltboyz_attack_profile, stationary_bonus=True)
        log += format_attack_output(result, "Boltboyz")

        result = resolve_unit_attacks(killbow_attack_profile)
        log += format_attack_output(result, "Killbow")

        return log

    def combat_phase(self):
        from combat_engine import resolve_unit_attacks, format_attack_output

        killaboss_attack_profile = [
            {"weapon": "Jagged Boss-Stikka", "attacks": 4, "hit": 3, "wound": 3, "rend": 1, "damage": 1, "crit_rule": "mortal_on_crit", "mortal_on_crit": 1},
            {"weapon": "Gnashtoof’s Fangs", "attacks": 5, "hit": 4, "wound": 3, "rend": 1, "damage": 2, "crit_rule": "none"}
        ]

        gutrippaz_attack_profile = [
            {"weapon": "Wicked Hacka", "attacks": 2, "hit": 4, "wound": 3, "rend": 0, "damage": 1, "crit_rule": "mortal_on_crit", "mortal_on_crit": 1}
        ]

        murknob_attack_profile = [
            {"weapon": "Murknob Cleaver", "attacks": 4, "hit": 4, "wound": 3, "rend": 1, "damage": 2, "crit_rule": "mortal_on_crit", "mortal_on_crit": 1}
        ]

        log = []

        if not self.state.kruleboyz_waaagh_used:
            log.append("Kruleboyz Waaagh! activated.")
            self.state.kruleboyz_waaagh_used = True

        result = resolve_unit_attacks(killaboss_attack_profile)
        log += format_attack_output(result, "Killaboss")

        result = resolve_unit_attacks(murknob_attack_profile)
        log += format_attack_output(result, "Murknob")

        result = resolve_unit_attacks(gutrippaz_attack_profile)
        log += format_attack_output(result, "Gutrippaz")

        return log
