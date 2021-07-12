import unittest
from abc import ABC
from enum import Enum

class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, current balance is {self.balance}')
    
    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f'Withdrew {amount}, current balance is {self.balance}')
            return True
        return False
    
    def __str__(self):
        return f'Balance = {self.balance}'

class Command(ABC):
    def __init__(self):
        self.success = False

    def invoke(self):
        pass

    def undo(self):
        pass

class BankAccountCommand(Command):

    class Action(Enum):
        DEPOSIT = 1
        WITHDRAW = 2

    def __init__(self, account, action, amount):
        super().__init__()
        self.account = account
        self.action = action
        self.amount = amount
    
    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)
    
    def undo(self):
        if not self.success:
            return
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)

class CompositeBankAccountCommand(Command, list):
    def __init__(self, items=[]):
        super().__init__()
        for i in items:
            self.append(i)
    
    def invoke(self):
        for x in self:
            x.invoke()
    
    def undo(self):
        for x in reversed(self):
            x.undo()

class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_acc, to_acc, amount):
        super().__init__([
            BankAccountCommand(from_acc, BankAccountCommand.Action.WITHDRAW, amount),
            BankAccountCommand(to_acc, BankAccountCommand.Action.DEPOSIT, amount),
        ])

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False
        self.success = ok


class TestSuite(unittest.TestCase):
    def test_composite_deposit(self):
        ba = BankAccount()
        deposit1 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 1000)
        deposit2 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 1000)
        composite = CompositeBankAccountCommand([deposit1, deposit2])
        composite.invoke()
        print(ba)
        composite.undo()
        print(ba)

    def test_transfer_fail(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        # composite isn't so good because of failure
        amount = 1000  # try 1000: no transactions should happen
        wc = BankAccountCommand(ba1, BankAccountCommand.Action.WITHDRAW, amount)
        dc = BankAccountCommand(ba2, BankAccountCommand.Action.DEPOSIT, amount)

        transfer = CompositeBankAccountCommand([wc, dc])

        transfer.invoke()
        print('ba1:', ba1, 'ba2:', ba2)  # end up in incorrect state
        transfer.undo()
        print('ba1:', ba1, 'ba2:', ba2)

    def test_better_tranfer(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        amount = 1000

        transfer = MoneyTransferCommand(ba1, ba2, amount)
        transfer.invoke()
        print('ba1:', ba1, 'ba2:', ba2)
        transfer.undo()
        print('ba1:', ba1, 'ba2:', ba2)
        print(transfer.success)


if __name__ == '__main__':
    # ba = BankAccount()
    # cmd = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
    # cmd.invoke()
    # print(ba)

    # cmd.undo()
    # print(ba)

    # illegal_cmd = BankAccountCommand(ba, BankAccountCommand.Action.WITHDRAW, 1000)
    # illegal_cmd.invoke()
    # print(ba)
    # illegal_cmd.undo()
    # print(ba)
    unittest.main()