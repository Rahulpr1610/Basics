class Account:

    def __init__(self,balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        return 