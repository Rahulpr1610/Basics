class BankAccount :
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw: {amount}")
        else:
            print("Insufficient balance or valid amount")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Rahul",1000)
acc.deposit(100)
acc.withdraw(200)
print("Current Balance: ",acc.get_balance())