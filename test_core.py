import core


def test_new_gladiator():
    assert core.new_gladiator(17, 15, 10, 20) == {
        'rage': 15,
        'damage_high': 20,
        'health': 17,
        'damage_low': 10
    }


def test_is_dead():
    choice = {'rage': 15, 'damage_high': 20, 'health': -1, 'damage_low': 10}
    assert core.is_dead(choice) == True
    choice = {'rage': 15, 'damage_high': 20, 'health': 20, 'damage_low': 10}
    assert core.is_dead(choice) == False


def test_heal():
    choice = {'rage': 15, 'damage_high': 20, 'health': 100, 'damage_low': 10}
    assert core.heal(choice) == choice


def test_attack():
    attacker = {'health': 75, 'rage': 0, 'damage_low': 10, 'damage_high': 10}
    defender = {'health': 75, 'rage': 0, 'damage_low': 11, 'damage_high': 13}
    core.attack(attacker, defender)
    assert attacker['rage'] == 15
    assert defender['health'] == 65
    attacker = {'health': 75, 'rage': 100, 'damage_low': 10, 'damage_high': 10}
    defender = {'health': 65, 'rage': 100, 'damage_low': 11, 'damage_high': 13}
    core.attack(attacker, defender)
    assert attacker['rage'] == 0
    assert defender['health'] == 20
