from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    """dict -> dict"""
    return {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high
    }


def is_dead(gladiator):
    if gladiator['health'] <= 0:
        return True
    else:
        return False


def heal(gladiator):
    if gladiator['rage'] >= 10:
        gladiator['rage'] = max(gladiator['rage'] - 10, 0)
        gladiator['health'] = min(gladiator['health'] + 5, 100)
        return gladiator


def attack(attacker, defender):
    damage_dealt = randint(attacker['damage_low'], attacker['damage_high'])
    if randint(1, 100) <= attacker['rage']:
        defender['health'] -= damage_dealt * 2
        attacker['rage'] = 0
    else:
        defender['health'] -= damage_dealt
        attacker['rage'] += 15
    return attacker, defender


def punch(attacker, defender):
    super_punch = attacker['damage_high']
    defender['health'] -= super_punch * 2
    attacker['rage'] = 0
    attacker['health'] = attacker['health'] * .5