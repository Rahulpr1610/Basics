class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def show_info(self):
        print(f"brand : {self.brand}")
        print(f"year : {self.year}")

class Car(Vehicle):
    def __init__(self,brand,year,fuel_type):
        super().__init__(brand,year)
        self.fuel_type = fuel_type

    def show_info(self):
        super().show_info()
        print(f"Fuel : {self.fuel_type}")

v = Car("BMW",2025,"Petrol")
v.show_info()