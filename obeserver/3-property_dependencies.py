class Event(list):
    def __call__(self, *a, **kw):
        for item in self:
            item(*a, **kw)


class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, age=0):
        super().__init__()
        self._age = age

    @property
    def can_vote(self):
        return self._age >= 18

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, x):
        if self._age != x:
            old_can_vote = self.can_vote
            self._age = x
            self.property_changed("age", self._age)
            if old_can_vote != self.can_vote:
                self.property_changed("can_vote", self.can_vote)


if __name__ == "__main__":

    def person_changed(name, value):
        if name == "can_vote":
            print(f"🎫 Voting ability changed to {value}")

    p = Person()
    p.property_changed.append(person_changed)
    for age in range(16, 20):
        print(f"Setting age to {age}")
        p.age = age
