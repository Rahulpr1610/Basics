#Mobile Phone Class

class Mobile:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def show_details(self):
        print(f"{self.model} has launch {self.model} at {self.price} rupees")

m1 = Mobile("Oneplus","One plus 12R",38000)
m2 = Mobile("Oneplus","One plus 13",50000)
m3 = Mobile("Oneplus","One plus 15",75000)

m1.show_details()
m2.show_details()
m3.show_details()