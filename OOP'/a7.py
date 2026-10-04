class BankAccount:

    def __init__(self,balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:",self.__balance)

acc = BankAccount(5000)
acc.show_balance()
