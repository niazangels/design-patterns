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
    def age(self):
        return self._age

    @age.setter
    def age(self, x):
        if self._age != x:
            self._age = x
            self.property_changed("age", self._age)


class TrafficAuthority:
    def __init__(self, person):
        self.person = person
        self.person.property_changed.append(self.person_changed)

    def person_changed(self, name, value):
        if name == "age":
            if value < 18:
                print("⛔ Still too young to drive")
            else:
                print("🎉 You can drive now")
                self.person.property_changed.remove(self.person_changed)


if __name__ == "__main__":
    p = Person()
    t = TrafficAuthority(p)

    for age in range(16, 20):
        print(f"Setting age to {age}")
        p.age = age
