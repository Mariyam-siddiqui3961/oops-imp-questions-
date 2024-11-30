# Inheritance:
# (i). Create a base class called “Animal” and two subclasses,
# “Dog” and “Cat.” Add methods and attributes specific to
# each subclass.
# (ii). Create a Bus child class that inherits from the Vehicle
# class. The default fare charge of any vehicle is seating
# capacity * 100. If Vehicle is Bus instance, we need to add an
# extra 10% on full fare as a maintenance charge. So total fare
# for bus instance will become the final amount = total fare +
# 10% of the total fare.
# Note: The bus seating capacity is 50. so the final fare
# amount should be 5500. You need to override the fare()
# method of a Vehicle class in Bus class.



# (i). Inheritance with Animal base class and Dog and Cat subclasses:

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Example usage
dog = Dog("Buddy")
print(dog.name, "says", dog.sound())

cat = Cat("Whiskers")
print(cat.name, "says", cat.sound())


# (ii). Inheritance with Bus child class inheriting from Vehicle class and overriding the fare() method:

class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self):
        super().__init__(seating_capacity=50)

    def fare(self):
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.1
        total_fare = base_fare + maintenance_charge
        return total_fare

# Example usage
bus = Bus()
print("Total fare for bus instance:", bus.fare())
