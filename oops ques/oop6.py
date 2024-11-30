# Abstract Base Classes:
# Create an abstract base class called “Shape” with an abstract
# method called “area.” Implement two subclasses, “Circle”
# and “Rectangle,” that inherit from “Shape” and provide their
# own implementations of the “area” method.



from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example usage
circle = Circle(5)
print("Area of the circle:", circle.area())

rectangle = Rectangle(4, 6)
print("Area of the rectangle:", rectangle.area())
