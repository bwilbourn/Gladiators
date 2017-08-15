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


def test_heal():
    assert core.heal(gladiator)
