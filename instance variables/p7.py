class Student:
    def __init__(self,name,m1,m2,m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total_marks(self):
        return self.m1 + self.m2 + self.m3

    def average_marks(self):
        return self.total_marks()/3

    def show_result(self):
        print("name: ",self.name)
        print("Total_marks: ",self.total_marks())
        print("Average_marks: ",self.average_marks())

t = Student("Rahul",122,33,34)
t1 = Student("Rahul",122,33,34)
t.show_result()
t1.show_result()