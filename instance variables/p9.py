class MobileRecharge:
    def __init__(self,mobile_number,balance):
        self.mobile_number = mobile_number
        self.balance = balance

    def recharge(self,amount):
        self.balance += amount
        print("Recharge success")

    def use_balance(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Balance used successfully!")
        else:
            print("Insufficient balance!!!")

    def show_balance(self):
        print("Number",self.mobile_number)
        print("Balance",self.balance)

p = MobileRecharge(8129731534,500)
p.recharge(350)
p.use_balance(120)
p.show_balance()