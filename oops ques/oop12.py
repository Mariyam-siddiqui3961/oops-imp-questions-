# Method Overriding:
# Create a base class called “Vehicle” with a method called
# “drive.” Implement two subclasses, “Car” and “Bicycle,” that
# inherit from “Vehicle” and override the “drive” method with
# their own implementations.


class Vehicle:
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Car is being driven on the road."

class Bicycle(Vehicle):
    def drive(self):
        return "Bicycle is being ridden on the street."

# Example usage
car = Car()
print(car.drive())  # Output: Car is being driven on the road.

bicycle = Bicycle()
print(bicycle.drive())  # Output: Bicycle is being ridden on the street.
