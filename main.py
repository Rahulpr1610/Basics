# even = 0
# odd = 0
#
# print("Enter 10 number")
#
# for i in range(10):
#     num = int(input("Enter number: "))
#
#     if num%2 == 0:
#         even = even+1
#     else:
#         odd = odd+1
#
# print("Result: ")
# print("total even",even)
# print("total odd",odd)

# class Student:
#     school = "ABC School"   # class variable
#
#     def __init__(self, name):
#         self.name = name
# s1 = Student("Rahul")
# s2 = Student("Sam")
#
# print(s1.name)
# print(Student.school)
# print(s1.school)
#

class Student:
    school = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name    # instance variable

s1 = Student("Rahul")
s2 = Student("Sam")

print(s1.name)        # Rahul
print(s2.name)        # Sam

print(Student.school) # ABC School
