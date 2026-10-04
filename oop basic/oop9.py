class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"{self.name} has {self.price} rupee")

p1 = Product("car",12345)
p2 = Product("bus",20003)
p3 = Product("van",4990)

p1.show_info()
p2.show_info()
p3.show_info()

total = p1.price+p2.price+p3.price
print(f"Cart Total: {total}")