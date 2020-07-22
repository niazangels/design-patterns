class Memento:
    def __init__(self, balance):
        self.balance = balance


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return Memento(self.balance)

    def restore(self, memento):
        self.balance = memento.balance

    def __str__(self):
        return f"Balance = {self.balance}"


if __name__ == "__main__":
    ba = BankAccount(100)
    print(f"Init:{ba}")

    v1 = 50
    m1 = ba.deposit(v1)
    print(f"+{v1} (m1): {ba}")

    v2 = 25
    m2 = ba.deposit(v2)
    print(f"+{v2} (m2): {ba}")

    ba.restore(m1)
    print(f"Restore m1: {ba}")

    ba.restore(m2)
    print(f"Restore m2: {ba}")

