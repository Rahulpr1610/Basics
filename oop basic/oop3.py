class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add_numbers(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 *self.num2

    def divide(self):
        return self.num1 / self.num2

a = Calculator(13,12)

b = a.add_numbers()
s = a.subtract()
m = a.multiply()
d = a.divide()

print(f"The sum is : {b}")
print(f"The sum is : {s}")
print(f"The sum is : {m}")
print(f"The sum is : {d}")