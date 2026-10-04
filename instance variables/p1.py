class Employee:
    company_name = "RP Hardware"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

p1 = Employee("rahul",5000)
p2 = Employee("sam",2000)

print(f"Name: {p1.name}, Salary: {p1.salary}, Company: {Employee.company_name}")
print(f"Name: {p2.name}, Salary: {p2.salary}, Company: {Employee.company_name}")