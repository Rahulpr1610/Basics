class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name: ",self.name)
        print("Marks: ",self.marks)

    def is_pass(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

    def grade(self):
        if self.marks >= 90:
            print("A")
        elif self.marks >= 75:
            print("B")
        elif self.marks >= 50:
            print("C")
        else:
            print("D")


s1 = Student("Rahul",90)
s1.display()
s1.is_pass()
s1.grade()
