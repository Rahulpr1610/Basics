class BankAccount:

    def __init__(self,name,account_no,balance=0):
        self.name=name
        self.account_no=account_no
        self.balance=balance

    def deposit(self,amount):
        if amount >0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("invalid amount")

    def withdraw(self,amount):
        if amount <= self.balance and amount >0:
            self.balance -= amount
            print(f"withdraw: {amount}")
        else:
            print("insufficient balance or valid amount")

    def show_detail(self):
        print(f"Name: {self.name}")
        print(f"Account No: {self.account_no}")
        print(f"Balance: {self.balance}")

a = BankAccount("Rahul",123445,5000)
a.show_detail()
a.deposit(120)
a.withdraw(509)
