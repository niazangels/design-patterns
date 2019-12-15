import random
import string


class User:
    """
        This class stores each name as an instance attribute
    """

    def __init__(self, name):
        self.name = name


class User2:
    """
        This class stores the names as a class variable which is shared among instances
    """

    known_names = []

    def __init__(self, full_name):
        def get_or_add(name):
            if name in self.known_names:
                return self.known_names.index(name)
            self.known_names.append(name)
            return len(self.known_names) - 1

        self.names = [get_or_add(x) for x in full_name.split(" ")]

    def __repr__(self):
        return " ".join(self.known_names[x] for x in self.names)


def random_string(length=1):
    chars = string.ascii_lowercase
    return "".join([random.choice(chars) for _ in range(length)])


if __name__ == "__main__":
    users = []

    first_names = [random_string() for _ in range(100)]
    last_names = [random_string() for _ in range(100)]

    for first in first_names:
        for last in last_names:
            users.append(User2(f"{first} {last}"))

    print("Created {len(users)} users")

    # Let's ensure that it's the class variable that's storing the name
    print(users[0].known_names)
    print(User2.known_names)

    # Just to be extra sure the memory locations are shared
    print(id(users[0].known_names))
    print(id(users[1].known_names))
    print(id(User2.known_names))
