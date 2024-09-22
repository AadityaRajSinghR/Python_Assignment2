"""
Write a Python program that defines a base class named Shape with methods to calculate the area and perimeter. Then, implement subclasses such as Circle, Rectangle, and Triangle, each overriding the base class methods with their specific calculations. The program should demonstrate polymorphism by creating a list of different shape objects and calculating their areas and perimeters.
"""

PI = 3.14

# Base Class
class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def perimeter(self):
        raise NotImplementedError("This method should be overridden in subclasses.")

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.radius = radius

    def area(self):
        return PI * (self.radius ** 2)

    def perimeter(self):
        return 2 * PI * self.radius

# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative.")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Subclass for Triangle
class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        if side_a < 0 or side_b < 0 or side_c < 0:
            raise ValueError("Sides cannot be negative.")
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("The given sides do not form a triangle.")
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        # Using Heron's formula
        s = (self.side_a + self.side_b + self.side_c) / 2
        #A = √s(s−a)(s−b)(s−c)
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

# Demonstrating Polymorphism
def main():
    while True: 
        try:       
            radius = int(input("Enter the radius of the circle: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        break


    while True:
        try:
            length = int(input("Enter the length of the rectangle: "))
            width = int(input("Enter the width of the rectangle: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        break


    while True:
        try:
            side_a = int(input("Enter the first side of the triangle: "))
            side_b = int(input("Enter the second side of the triangle: "))
            side_c = int(input("Enter the third side of the triangle: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        break
        
    
    
    shapes = [
        Circle(radius),
        Rectangle(length, width),
        Triangle(side_a, side_b, side_c)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__}:")
        print(f"Area: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}\n")

if __name__ == "__main__":
    main()
