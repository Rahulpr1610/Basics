class student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark

    def a(self):
        print(f"student name is {self.name} and mark are {self.mark}")

s1 = student("rahul",50)
s2 = student("sam",70)

s1.a()
s2.a()