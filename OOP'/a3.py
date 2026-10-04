class Car:
    brand = "Toyata"

    def __init__(self,model):
        self.model = model

    @classmethod
    def change_brand(cls,new_brand):
        cls.brand = new_brand

a = Car("Helux")
a1 = Car("Corolla")
print(a.brand)
print(a1.brand)

Car.change_brand("Honda")

print(a.brand)
print(a1.brand)