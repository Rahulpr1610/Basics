class ATM:
    def __init__(self,account_holder,pin,balance):
        self.account_holder = account_holder
        self.pin = pin
        self.balance = balance

    def check_pin(self,entered_pin):
        if self.pin == entered_pin:
            return True
        else:
            print("Incorrect Pin")
            return False

    def withdraw(self,entered_pin, amount):
        self.check_pin(entered_pin)
        self.balance -= amount
        if self.pin == entered_pin:
            print("Check Balance:",self.balance)
            print("Deduct Amount:",amount)
        else:
            print("Stop operation")

    def show_balance(self, entered_pin):
        if self.pin == entered_pin:
            return  True
        else:
            print("Balance:",self.balance)

p = ATM("rahul",12345,50000)
p.show_balance()
