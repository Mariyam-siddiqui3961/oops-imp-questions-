# Creating a Class and Object:
# (i). Create a Python class called “Car” with attributes like
# make, model, and year. Then, create an object of the “Car”
# class and print its details.
# (ii). Write Python program to simulate a car dealership's
# inventory management system. The system aims to model
# cars and their attributes accurately.
# Task-1. You are tasked with creating a Python program to
# represent vehicles using a class. Each car should have
# attributes for maximum speed and mileage.
# Task-2. Update the class with the default color for all
# vehicles," white".
# Task-3. Additionally, you need to create methods in the
# Vehicle class to assign seating capacity to a vehicle.
# Task-4. Create a method to display all the properties of an
# object of the class.
# Task-5. Additionally, you need to create two objects of the
# Vehicle class object that should have a max speed of 200kph
# and mileage of 50000kmpl with five seating capacities, and
# another car object should have a max speed of 180kph and
# 75000kmpl with four seating capacities.



class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = "white"
        self.seating_capacity = None

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_details(self):
        print("Max Speed:", self.max_speed, "kph")
        print("Mileage:", self.mileage, "kmpl")
        print("Color:", self.color)
        print("Seating Capacity:", self.seating_capacity)


car1 = Vehicle(max_speed=200, mileage=50000)
car1.assign_seating_capacity(5)

car2 = Vehicle(max_speed=180, mileage=75000)
car2.assign_seating_capacity(4)

print("Car 1 Details:")
car1.display_details()
print("\nCar 2 Details:")
car2.display_details()
