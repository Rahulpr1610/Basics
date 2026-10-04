# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age =age
#
# s1 = Student("rahul",24)
# s2 = Student("sam",34)
#
# print(s1.name)
# print(s1.age)

class Student:
    def __init__(self,name):
        self.name = name

class School:
    def show_student(self,student):
        print("student name :", student.name)

s1 = Student("rahul")
school = School()

school.show_student(s1)