#ATM Simulation (Object State Control)

class ATM:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def check_balance(self):
        print(f"{self.account_holder} Your available balance {self.balance}")

person = ATM("Rahul",200)
person.deposit(100)
person.deposit(90)
person.withdraw(10)
person.check_balance()
