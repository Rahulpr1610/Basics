num1 = int(input("Enter number: "))
operator = input("Enter the operator: ")
num2 = int(input("Enter number: "))

if operator == "+":
    print(num1+num2)

elif  operator == "*":
    print(num1*num2)

elif operator == "-":
    print(num1-num2)

elif operator == "/":
    print(num1/num2)

else:
    print("Invalid operator")