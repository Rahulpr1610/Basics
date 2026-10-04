class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls,new_school):
        cls.school = new_school
Student.change_school("XYZ SCHOOL")
print(Student.school)