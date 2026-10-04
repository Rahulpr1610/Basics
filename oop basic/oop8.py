class Student:
    def __init__(self,name,present_days):
        self.name = name
        self.present_days = present_days

    def mark_present(self):
        self.present_days = self.present_days + 1
        print(f"{self.name} is present days {self.present_days}")

    def show_attendance(self):
        print(f"{self.name} attendance {self.present_days}")

student = Student("Rahul",15)
student.mark_present()
student.show_attendance()