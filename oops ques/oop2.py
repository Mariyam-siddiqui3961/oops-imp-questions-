# Class with constructor:
# Write a program find Euclidean distance between two points
# in a three-dimensional space using class and objects. Class
# called point consists of a constructor (__init__()) and two
# functions # distancefromorgin() and distance().



import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def distance(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        dz = self.z - other_point.z
        return math.sqrt(dx**2 + dy**2 + dz**2)

# Example usage
point1 = Point(1, 2, 3)
point2 = Point(4, 5, 6)

print("Distance of point1 from origin:", point1.distance_from_origin())
print("Distance of point2 from origin:", point2.distance_from_origin())
print("Distance between point1 and point2:", point1.distance(point2))
