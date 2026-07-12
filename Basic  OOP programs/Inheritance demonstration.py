#Inheritance demonstration
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def display_details(self):
        return f"Brand: {self.brand}, Color: {self.color}"

class Car(Vehicle):
    def __init__(self, brand, color, doors):
        super().__init__(brand, color)
        self.doors = doors
    
    def display_details(self):
        return f"{super().display_details()}, Doors: {self.doors}"

class Bike(Vehicle):
    def __init__(self, brand, color, bike_type):
        super().__init__(brand, color)
        self.bike_type = bike_type
    
    def display_details(self):
        return f"{super().display_details()}, Type: {self.bike_type}"


car_obj = Car("Toyota", "Red", 4)
bike_obj = Bike("Honda", "Black", "Sports")

print(car_obj.display_details())
print(bike_obj.display_details())
