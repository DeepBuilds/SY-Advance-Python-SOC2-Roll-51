#6. Vehicle Showroom Management System
class Vehicle:
    def __init__(self, vehicle_number, brand, price, category):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price
        self.category = category

    def display(self):
        print("Vehicle Number:", self.vehicle_number)
        print("Brand:", self.brand)
        print("Price:", self.price)
        print("Category:", self.category)
        print("------------------------")


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self):
        number = input("Enter Vehicle Number: ")
        brand = input("Enter Brand: ")
        price = float(input("Enter Price: "))

        if price >= 1000000:
            category = "Luxury"
        else:
            category = "Economy"

        vehicle = Vehicle(number, brand, price, category)
        self.vehicles.append(vehicle)
        print("Vehicle added successfully.")

    def display_all(self):
        if not self.vehicles:
            print("No vehicles available.")
        else:
            print("\n--- All Vehicles ---")
            for vehicle in self.vehicles:
                vehicle.display()


# Main program
showroom = Showroom()

while True:
    print("\n1. Add Vehicle")
    print("2. Display All Vehicles")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        showroom.add_vehicle()

    elif choice == "2":
        showroom.display_all()

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")

'''

1. Add Vehicle
2. Display All Vehicles
3. Exit
Enter your choice: 1
Enter Vehicle Number: 100
Enter Brand: BMW
Enter Price: 1000000
Vehicle added successfully.

1. Add Vehicle
2. Display All Vehicles
3. Exit
Enter your choice: 2

--- All Vehicles ---
Vehicle Number: 100
Brand: BMW
Price: 1000000.0
Category: Luxury
------------------------
1. Add Vehicle
2. Display All Vehicles
3. Exit
Enter your choice: 3
Program ended.

1. Add Vehicle
2. Display All Vehicles
3. Exit
Enter your choice: 4
Invalid choice.

 '''