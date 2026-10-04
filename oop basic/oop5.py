class BankAccount:
    def __init__(self,name,balance=0):
        self.name = name                                #created a class
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance+amount              #Created method
        print(f"{amount} has been deposited")

    def withdraw(self,amount):
        self.balance = self.balance - amount
        print(f"{amount} has been withdrawed")

    def show_balance(self):
        print(self.balance)

account = BankAccount("Rahul",100)          #object created

account.deposit(2000)
account.withdraw(20)                                       #method called
account.show_balance()
