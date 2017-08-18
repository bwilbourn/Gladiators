import core


def main():
    print('Prepare for total domination!!')
    gladiator_1 = core.new_gladiator(100, 0, 10, 20)
    gladiator_2 = core.new_gladiator(100, 0, 10, 20)
    while True:
        choice = input("""Gladiator1, what's your move?\n
        \t-heal
        \t-attack
        \t-power punch
        \t-pass
        \t-quit\n""")
        if choice == 'attack':
            core.attack(gladiator_1, gladiator_2)
            if core.is_dead(gladiator_2):
                print('Gladiator2 is dead, Gladiator1 wins.')
                break
        elif choice == 'power punch':
            core.punch(gladiator_1, gladiator_2)
            if core.is_dead(gladiator_2):
                print('Gladiator2 is dead, Gladiator1 wins.')
                break
        elif choice == 'heal':
            core.heal(gladiator_1)
        elif choice == 'pass':
            print('pass')
        elif choice == 'quit':
            exit()
        print('gladiator_1:', gladiator_1)
        print('gladiator_2:', gladiator_2)

        choice = input("""Gladiator2, what's your move?\n
        \t-heal
        \t-attack
        \t-power punch
        \t-pass
        \t-quit\n""")
        if choice == 'attack':
            core.attack(gladiator_2, gladiator_1)
            if core.is_dead(gladiator_1):
                print('Gladiator1 is dead, Gladiator2 wins.')
                break
        elif choice == 'power punch':
            core.punch(gladiator_2, gladiator_1)
            if core.is_dead(gladiator_1):
                print('Gladiator2 is dead, Gladiator1 wins.')
                break
        elif choice == 'heal':
            core.heal(gladiator_2)
        elif choice == 'pass':
            print('pass')
        elif choice == 'quit':
            exit()
        print('gladiator_1:', gladiator_1)
        print('gladiator_2:', gladiator_2)


if __name__ == '__main__':
    main()
