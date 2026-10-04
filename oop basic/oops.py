class person:
    def __init__(self,name,age):
        self.name = name           #class
        self.age = age

    def greet(self):
        print(f"Hi my name is {self.name}",self.age)

p1 = person("rahul",25) #creating objects
p2 = person("sam",26)

# print(p1.name)
# print(p2.age)      #accessing object data

p1.greet()           #calling method
p2.greet()

