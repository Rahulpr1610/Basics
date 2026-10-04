class student:
    def __init__(self,name,roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def student_details(self):
        print(f"Student name is {self.name} and roll name is {self.roll_number} and student scored mark{self.marks}")

s1 = student("rahul",41,100)
s2 = student("sam",11,90)
s3 = student("rahul",4,80)

s1.student_details()
s2.student_details()
s3.student_details()