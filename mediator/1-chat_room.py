class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room = None

    def receive(self, sender, message):
        xmessage = f"{sender}: {message}"
        print(f"{self.name}'s chat session > {xmessage}")
        self.chat_log.append(xmessage)

    def private_message(self, destination, message):
        self.room.message(self.name, destination, message)

    def say(self, message):
        self.room.broadcast(self.name, message)


class ChatRoom:
    def __init__(self):
        self.people = []

    def join(self, person: Person):
        join_msg = f"{person.name} joins the chat"
        self.broadcast("room", join_msg)
        person.room = self
        self.people.append(person)

    def broadcast(self, source, message):
        for person in self.people:
            if person.name != source:
                person.receive(source, message)

    def message(self, source, destination, message):
        for person in self.people:
            print(person.name)
            if person.name == destination:
                person.receive(source, message)


if __name__ == "__main__":
    room = ChatRoom()
    alice = Person("Alice")
    bob = Person("Bob")

    room.join(alice)
    room.join(bob)

    alice.say("Hi room")
    bob.say("Hi Alice")

    simon = Person("Simon")
    room.join(simon)

    simon.say("Hi everyone")

    alice.private_message(simon.name, "Hi Simon")
