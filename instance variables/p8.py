class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("Amount deposit successfully,",amount)

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("withdraw successful")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Account Holder Name: ",self.name)
        print("Balance: ",self.balance)

p = BankAccount("Rahul",4342)
p.deposit(50000)
p.withdraw(1223)
p.show_balance()

