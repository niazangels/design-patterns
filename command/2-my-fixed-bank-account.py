from abc import ABC
from enum import Enum


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, balance={self.balance}")

    def withdraw(self, amount):
        if self.balance - amount < self.OVERDRAFT_LIMIT:
            return False
        self.balance -= amount
        print(f"Withdrew {amount}, balance={self.balance}")
        return True

    def __str__(self):
        return f"Balance={self.balance}"


class Command(ABC):
    def invoke(self):
        pass

    def undo(self):
        pass


class BankAccountCommand(Command):
    def __init__(self, account, action, amount):
        self.account = account
        self.amount = amount
        self.action = action
        self.success = None

    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return
        if self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)
            self.action = self.Action.DEPOSIT
        elif self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
            self.action = self.Action.WITHDRAW


if __name__ == "__main__":
    ba = BankAccount()
    print("> Init")
    print(ba)

    print("> Add +100")
    cmd = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
    cmd.invoke()
    print(ba)

    print("> Undo")
    cmd.undo()
    print(ba)

    # Fixed broken undo
    print("> Fixed: Undo once again")
    cmd.undo()
    print(ba)

    # But now we cycle thorugh
    print("> Uh-ho: But now we cycle through lasy two steps")
    cmd.undo()
    print(ba)

    print("> Withdraw 500")
    illegal_cmd = BankAccountCommand(ba, BankAccountCommand.Action.WITHDRAW, 500)
    illegal_cmd.invoke()
    print(ba)

    print("> Withdraw too much")
    illegal_cmd = BankAccountCommand(ba, BankAccountCommand.Action.WITHDRAW, 5000)
    illegal_cmd.invoke()
    print(ba)
