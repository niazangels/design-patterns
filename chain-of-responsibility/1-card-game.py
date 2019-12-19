class Creature:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"


class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttackModifer(CreatureModifier):
    def handle(self):
        print(f"Doubling {self.creature.name}'s attack")
        self.creature.attack *= 2
        super().handle()


class IncreaseDefenceModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            self.creature.defense += 50
        super().handle()


class NoBonuses(CreatureModifier):
    def handle(self):
        print("You have no Bonuses")
        # We don't call super.handle() intentionally


if __name__ == "__main__":
    pikachu = Creature("Pikachu", 1, 1)
    print(pikachu)

    root = CreatureModifier(pikachu)
    root.add_modifier(DoubleAttackModifer(pikachu))
    root.add_modifier(IncreaseDefenceModifier(pikachu))
    root.handle()
    print(pikachu)

    print("-" * 20)

    squirtle = Creature("Squirtle", 1, 1)
    print(squirtle)
    root = CreatureModifier(squirtle)
    root.add_modifier(NoBonuses(DoubleAttackModifer(squirtle)))
    root.handle()
    print(squirtle)

