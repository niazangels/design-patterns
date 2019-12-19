"""
Proxy Coding Exercise

You are given the Person  class and asked to write a ResponsiblePerson  proxy that does the following:

Allows person to drink unless they are younger than 18 (in that case, return "too young")

Allows person to drive unless they are younger than 16 (otherwise, "too young")

In case of driving while drink, returns "dead", regardless of age"""


class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return "drinking"

    def drive(self):
        return "driving"

    def drink_and_drive(self):
        return "driving while drunk"


class ResponsiblePerson:
    def __init__(self, person):
        self.person = person

    @property
    def age(self):
        return self.person.age

    @age.setter
    def age(self, value):
        self.person.age = value

    def drink(self):
        if self.age <= 18:
            return "too young"
        return self.person.drink()

    def drive(self):
        if self.age <= 16:
            return "too young"
        return self.person.drive()

    def drink_and_drive(self):
        return "dead"


if __name__ == "__main__":
    p = ResponsiblePerson(15)
    print(p.drink())
    print(p.drive())
    print(p.drink_and_drive())

    p = ResponsiblePerson(17)
    print(p.drink())
    print(p.drive())
    print(p.drink_and_drive())

    p = ResponsiblePerson(19)
    print(p.drink())
    print(p.drive())
    print(p.drink_and_drive())
