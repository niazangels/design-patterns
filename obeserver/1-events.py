class Event(list):
    def __call__(self, *a, **kw):
        for item in self:
            item(*a, **kw)


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        self.falls_ill(name=self.name, address=self.address)


def call_a_doctor(name, address):
    print(f"Doctor needed: {name} living in {address}")


if __name__ == "__main__":
    person = Person("Sherlock", "221B Baker St.")
    person.falls_ill.append(lambda name, address: print(f"{name} has fallen ill"))
    person.falls_ill.append(call_a_doctor)

    person.catch_a_cold()

    person.falls_ill.remove(call_a_doctor)

    person.catch_a_cold()
