class Creature:
    def __init__(self):
        self.strength = 10
        self.agility = 10
        self.intelligence = 10

    @property
    def sum_of_stats(self):
        return self.strength + self.intelligence + self.agility

    @property
    def max_stat(self):
        return max(self.strength, self.agility, self.intelligence)

    @property
    def avg_stat(self):
        return sum(self.strength, self.agility, self.intelligence) / 3


class Creature2ListBacked:
    _strength = 0
    _agility = 1
    _intelligence = 2

    def __init__(self):
        self.stats = [10, 10, 10]

    @property
    def strength(self):
        return self.stats[Creature2._strength]

    @strength.setter
    def strength(self, x):
        self.stats[Creature2._strength] = x

    @property
    def agility(self):
        return self.stats[Creature2._agility]

    @agility.setter
    def agility(self, x):
        self.stats[Creature2._agility] = x

    @property
    def intelligence(self):
        return self.stats[Creature2._intelligence]

    @intelligence.setter
    def intelligence(self, x):
        self.stats[Creature2._intelligence] = x

    @property
    def sum_of_stats(self):
        return sum(self.stats)

    @property
    def max_stat(self):
        return max(self.stats)

    @property
    def avg_stat(self):
        return sum(self.stats) / len(self.stats)


from typing import NamedTuple


class Stats(NamedTuple):
    strength: int = 10
    agility: int = 10
    intelligence: int = 10


class Creature3NamedTuple:
    def __init__(self):
        self.stats = Stats()

    @property
    def sum_of_stats(self):
        return sum(self.stats)


from typing import NamedTuple


class Stats(NamedTuple):
    strength: int = 10
    agility: int = 10
    intelligence: int = 10


class Creature3NamedTuple:
    def __init__(self):
        self.stats = Stats()

    @property
    def strength(self):
        return self.stats.strength

    @strength.setter
    def strength(self, x):
        self.stats.strength = x

    @property
    def sum_of_stats(self):
        return sum(self.stats)


if __name__ == "__main__":
    pikachu = Creature3NamedTuple()
    print(pikachu.strength)
    pikachu.strength = 100
    print(pikachu.strength)
