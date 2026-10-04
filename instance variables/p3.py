class Employee:
    company_name = "ABCD company"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

p1 = Employee("rahul",5900)
p2 = Employee("sam",8900)

print(p1.name)
print(p1.salary)

print(Employee.company_name)