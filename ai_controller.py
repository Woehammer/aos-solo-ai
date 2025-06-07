from combat_engine import resolve_unit_attacks, format_attack_output

# Killaboss attack profile (expandable to other units)
killaboss_attack_profile = [
    {
        "weapon": "Jagged Boss-Stikka",
        "attacks": 4,
        "hit": 3,
        "wound": 3,
        "rend": 1,
        "damage": 1,
        "crit_rule": "mortal_on_crit",
        "mortal_on_crit": 1
    },
    {
        "weapon": "Gnashtoof’s Fangs",
        "attacks": 5,
        "hit": 4,
        "wound": 3,
        "rend": 1,
        "damage": 2,
        "crit_rule": "none"
    }
]

class AIController:
    def __init__(self, game_state):
        self.name = "Swampskulka Gang"
        self.state = gme_state

    def hero_phase(self):
        print("AI Hero Phase: Killaboss uses 'All Part of Da Plan' on Gutrippaz (+3 Control).")

    def movement_phase(self):
        print("AI Movement Phase: Units reposition toward objectives.")

    def shooting_phase(self):
        print("AI Shooting Phase: (No targets in test mode)")

    def charge_phase(self):
        print("AI Charge Phase: Killaboss charges.")

    def combat_phase(self):
        print("AI Combat Phase:")
        result = resolve_unit_attacks(killaboss_attack_profile)
        report = format_attack_output(result, "Killaboss on Great Gnashtoof")
        for line in report:
            print(line)
