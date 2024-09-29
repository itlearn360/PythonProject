import math

# Parent class
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement this method.")

# Child class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Child class Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Child class Square
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# A function to calculate area for any shape
def calculate_area(shape):
    print(f"The area of the shape is: {shape.area()}")

# Create objects for different shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
square = Square(3)

# Calculate area for each shape using polymorphism
calculate_area(circle)      # Output: The area of the shape is: 78.5398...
calculate_area(rectangle)   # Output: The area of the shape is: 24
calculate_area(square)      # Output: The area of the shape is: 9
