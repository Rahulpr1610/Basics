class Employee:
    def __init__(self,name,basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def hra(self):
        return  self.basic_salary * 0.02

    def pf(self):
        return self.basic_salary * 0.12

    def net_salary(self):
        return self.basic_salary + self.hra() - self.pf()

    def show_salary(self):
        print("Employee name:",self.name)
        print("Basic Salary:",self.basic_salary)
        print("HRA (20%):",self.hra())
        print("PF(12%):",self.pf())
        print("Net Salary:",self.net_salary())

emp = Employee("Rahul",20000)
emp.show_salary()