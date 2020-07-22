class Memento:
    def __init__(self, balance):
        self.balance = balance


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.changes = [Memento(self.balance)]
        self.current = len(self.changes) - 1

    def deposit(self, amount):
        self.balance += amount
        m = Memento(self.balance)
        self.changes.append(m)
        self.current += 1
        return m

    def restore(self, memento):
        if memento:
            self.balance = memento.balance
            self.changes.append(memento)
            self.current = len(self.changes) - 1

    def undo(self):
        if not (self.current > 0):
            print("Undo is not possible")
            return
        self.current -= 1
        m = self.changes[self.current]
        self.balance = m.balance
        return m

    def redo(self):
        if self.current + 1 >= len(self.changes):
            print("Redo is not possible")
            return
        self.current += 1
        m = self.changes[self.current]
        self.balance = m.balance

    def __str__(self):
        return f"Balance = {self.balance}"


if __name__ == "__main__":
    ba = BankAccount(100)
    print(f"Init:{ba}")

    v1 = 50
    m1 = ba.deposit(v1)
    print(f"+{v1} (m1): {ba}")

    ba.undo()
    print(f"Undo: {ba}")

    ba.undo()
    print(f"Undo: {ba}")

    ba.redo()
    print(f"Redo: {ba}")

    ba.redo()
    print(f"Redo: {ba}")

    v2 = 25
    m2 = ba.deposit(v2)
    print(f"+{v2} (m2): {ba}")

    ba.undo()
    print(f"Undo: {ba}")

    ba.redo()
    print(f"Redo: {ba}")
