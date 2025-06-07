import random

def roll_dice(number, success_threshold):
    rolls = [random.randint(1, 6) for _ in range(number)]
    successes = sum(1 for roll in rolls if roll >= success_threshold)
    return successes, rolls

def resolve_attack(weapon_profile, stationary_bonus=False):
    attacks = weapon_profile["attacks"]

    if stationary_bonus and weapon_profile.get("stationary_bonus", False):
        hit_threshold = weapon_profile["hit"] - 1
    else:
        hit_threshold = weapon_profile["hit"]

    wound_threshold = weapon_profile["wound"]
    rend = weapon_profile["rend"]
    damage = weapon_profile["damage"]
    crit_rule = weapon_profile.get("crit_rule", "none")
    mortal_on_crit = weapon_profile.get("mortal_on_crit", 0)

    hits, hit_rolls = roll_dice(attacks, hit_threshold)
    crit_hits = sum(1 for roll in hit_rolls if roll == 6)
    normal_hits = hits - crit_hits
    crit_mortal_wounds = crit_hits * mortal_on_crit if crit_rule == "mortal_on_crit" else 0
    wounds, wound_rolls = roll_dice(normal_hits, wound_threshold)

    return {
        "weapon": weapon_profile["weapon"],
        "attacks": attacks,
        "hit_rolls": hit_rolls,
        "normal_hits": normal_hits,
        "crit_hits": crit_hits,
        "wounds": wounds,
        "rend": rend,
        "damage": damage,
        "crit_mortal_wounds": crit_mortal_wounds
    }

def resolve_unit_attacks(unit_attack_profiles, stationary_bonus=False):
    results = []
    total_mortal_wounds = 0
    for weapon in unit_attack_profiles:
        outcome = resolve_attack(weapon, stationary_bonus)
        total_mortal_wounds += outcome["crit_mortal_wounds"]
        results.append(outcome)
    return {"weapon_results": results, "total_mortal_wounds": total_mortal_wounds}

def format_attack_output(result, unit_name):
    output = [f"{unit_name} attacks:"]
    for weapon in result["weapon_results"]:
        text = f"- {weapon['weapon']} makes {weapon['attacks']} attacks: "
        text += f"{weapon['normal_hits'] + weapon['crit_mortal_wounds']} hits ({weapon['normal_hits']} normal, {weapon['crit_mortal_wounds']} crit mortals). "
        if weapon['wounds'] > 0:
            text += f"{weapon['wounds']} wounds — {weapon['wounds']} saves at rend {weapon['rend']}, damage {weapon['damage']}. "
        if weapon['crit_mortal_wounds'] > 0:
            text += f"Apply {weapon['crit_mortal_wounds']} mortal wounds ({weapon['crit_mortal_wounds'] * weapon['damage']} damage)."
        output.append(text)
    return output
