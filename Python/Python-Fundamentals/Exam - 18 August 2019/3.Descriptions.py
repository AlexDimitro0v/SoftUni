class Wizard:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = int(health)
        self.damage = int(damage)


def main():
    wizards = []
    data = input()
    while data != 'fight':
        wizard_names = list(map(lambda w: w.name, wizards))
        command, name, health, damage = data.split()
        if command == 'new':
            if name not in wizard_names:
                obj = Wizard(name, health, damage)
                wizards.append(obj)
            else:
                print("Wizard already exists!")
        elif command == 'edit':
            if name not in wizard_names:
                print("Wizard does not exist!")
            else:
                current_wizard = list(filter(lambda w: w.name == name, wizards))[0]
                current_wizard.health += int(health)
                current_wizard.damage += int(damage)

        data = input()

    battle(wizards)
    for wizard in sorted(wizards, key=lambda w: -w.health):
        print(f"Wizard: {wizard.name}. Health: {wizard.health}. Damage power: {wizard.damage}")


def battle(wizards):
    data = input()
    while data != 'end':
        w1, w2 = data.split(' <=> ')
        wizard_names = list(map(lambda w: w.name, wizards))
        if w1 in wizard_names and w2 in wizard_names:
            attacker = list(filter(lambda w: w.name == w1, wizards))[0]
            attacked = list(filter(lambda w: w.name == w2, wizards))[0]
            attacked.health -= int(attacker.damage)
            attacker.health += 50
            if attacked.health <= 0:
                print(f"Fatality - {attacker.name} wins!")
                wizards.remove(attacked)
            else:
                print(f"Next time {attacked.name}!")
        else:
            print("Cannot place a fight with non-existing wizards!")
        data = input()


if __name__ == '__main__':
    main()
