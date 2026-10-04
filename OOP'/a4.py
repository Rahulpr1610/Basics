class BankAccount:
    bank_name = "State Bank"

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    @classmethod
    def change_bank(cls,new_name):
        cls.bank_name = new_name

x = BankAccount("Rahul",10000)
y = BankAccount("sam",110000)

print(x.bank_name)
print(y.bank_name)

BankAccount.change_bank("HDFC")

print(x.bank_name)
print(y.bank_name)
