# Polymorphism:
# Create a function that takes an animal object as input and
# calls its “sound” method. Test it with both a dog and a cat
# object and utilize base class called “Animal” and two
# subclasses, “Dog” and “Cat.” Add methods and attributes
# specific to each subclass.



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

def make_sound(animal):
    print(animal.name, "says", animal.sound())

# Test with Dog object
dog = Dog("Buddy")
make_sound(dog)

# Test with Cat object
cat = Cat("Whiskers")
make_sound(cat)
