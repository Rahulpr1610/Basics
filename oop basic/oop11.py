class Student:
    def __init__(self,name,subject1,subject2,subject3):
        self.name = name
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3

    def total_marks(self):
        return self.subject1 + self.subject2 +self.subject3

    def average_mark(self):
        return self.total_marks()/3

    def show_result(self):
        print(f"{self.name}'s Total mark is {self.total_marks()} and average mark is {self.average_mark()}")

student = Student("Rahul",89,34,22)
student.show_result()