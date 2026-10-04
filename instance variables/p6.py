# Function (outside class)
def add(a, b):
    return a + b


# Class with method
class Calculator:
    def method(self, a, b):
        return a - b


# Calling the function
result_function = add(12, 33)
print("Function result:", result_function)


# Creating object of class
calc = Calculator()

# Calling the method using object
result_method = calc.method(33, 12)
print("Method result:", result_method)
