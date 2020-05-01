class Event(list):
    def __call__(self, *a, **kw):
        for item in self:
            item(*a, **kw)


class Game:
    def __init__(self):
        self.event = Event()

    def fire(self, args):
        self.event(args)


class GoalScoredInfo:
    def __init__(self, who, how_many):
        self.who = who
        self.how_many = how_many


class Player:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.goals_scored = 0

    def score(self):
        self.goals_scored += 1
        args = GoalScoredInfo(who=self.name, how_many=self.goals_scored)
        self.game.fire(args)


class Coach:
    def __init__(self, game):
        game.event.append(self.celebrate)

    def celebrate(self, args):
        if not isinstance(args, GoalScoredInfo):
            return
        if args.how_many < 3:
            print(f"Coach says: Well done {args.who}")


if __name__ == "__main__":
    game = Game()
    player = Player("Sam", game)
    coach = Coach(game)

    player.score()
    player.score()
    player.score()
