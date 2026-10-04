class Employee:
    def __init__(self,name,emp_id,salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        print(f"Employee name is {self.name} and Employee id {self.emp_id} and salary {self.salary}")

p1 = Employee("Rahul",1234,2000)
p2 = Employee("sam",12234,2500)

p1.show_details()
p2.show_details()