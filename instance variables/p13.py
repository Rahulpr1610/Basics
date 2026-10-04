class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"name:{self.name}")
        print(f"age:{self.age}")

class Student(Person):
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course = course

    def show_info(self):
        super().show_info()
        print(f"course : {self.course}")

s1 = Student("rahul",23,"python")
s1.show_info()