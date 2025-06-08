def killaboss_decision(enemy_distance, objective_distance, charge):
    if charge == "Yes":
        return "Killaboss attempts to charge the enemy."
    elif objective_distance <= 3:
        return "Killaboss holds position on objective."
    else:
        return "Killaboss advances towards enemy."

def murknob_decision(enemy_distance, objective_distance, charge):
    if charge == "Yes":
        return "Murknob charges to support Killaboss."
    elif objective_distance <= 3:
        return "Murknob holds objective."
    else:
        return "Murknob advances behind Killaboss."

def gutrippaz_decision(enemy_distance, objective_distance, charge):
    if objective_distance <= 3:
        return "Gutrippaz secure objective."
    elif charge == "Yes":
        return "Gutrippaz attempt to charge enemy."
    else:
        return "Gutrippaz advance towards objective."

def boltboyz_decision(enemy_distance, objective_distance, charge):
    if enemy_distance <= 24:
        return "Boltboyz stay stationary and fire with Pick 'Em Off."
    else:
        return "Boltboyz advance to shooting range."

def killbow_decision(enemy_distance, objective_distance, charge):
    if enemy_distance <= 36:
        return "Killbow holds position to shoot."
    else:
        return "Killbow advances to get line of sight."
