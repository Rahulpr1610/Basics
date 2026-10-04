class Student:
    school = "ABCD School"

    def __init__(self,name):
        self.name = name

s1 = Student("rahul")
s2 = Student("sam")

print(s1.name)
print(s2.name)

print(Student.school) 