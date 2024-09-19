# Problem Statement

Write a Python program that defines a base class named `Shape` with methods to calculate the area and perimeter. Then, implement subclasses such as `Circle`, `Rectangle`, and `Triangle`, each overriding the base class methods with their specific calculations. The program should demonstrate polymorphism by creating a list of different shape objects and calculating their areas and perimeters.

## Task to be Performed

### 1. Define the Base Class Shape:
- Create a base class `Shape` that includes methods to calculate the area and perimeter.
- Since the calculations will vary depending on the shape, define these methods to raise a `NotImplementedError`, indicating that they should be overridden in the subclasses.

### 2. Implement Subclasses:
Create subclasses for different shapes:
- **Circle**: Implement the methods to calculate the area (`π * r^2`) and perimeter (`2 * π * r`) for a circle.
- **Rectangle**: Implement the methods to calculate the area (`length * width`) and perimeter (`2 * (length + width)`) for a rectangle.
- **Triangle**: Implement the methods to calculate the area using **Heron's formula** and the perimeter by summing the lengths of the sides.

### 3. Override Methods:
In each subclass, override the `area` and `perimeter` methods to provide the specific calculations for that shape.

### 4. Demonstrate Polymorphism:
- Create a list containing objects of different shapes (e.g., a Circle, a Rectangle, and a Triangle).
- Use a loop to iterate through the list, and for each shape object, call the `area` and `perimeter` methods.
- Demonstrate that the correct method is called for each shape, illustrating **polymorphism**.

### 5. Display the Results:
The program should print the area and perimeter of each shape in a clear and formatted manner, demonstrating that the program can handle different shapes in a unified way.

## Implementation Guidelines

### 1. Inheritance:
- Utilize **inheritance** to create subclasses (`Circle`, `Rectangle`, `Triangle`) from the base class `Shape`.
- This will allow each subclass to inherit the structure of the base class while providing specific implementations for the methods.

### 2. Polymorphism:
- Demonstrate polymorphism by treating different shape objects uniformly in the list.
- When the `area` and `perimeter` methods are called in the loop, the appropriate method for each shape should be executed based on the object type.

### 3. Error Handling:
- Consider adding error handling for invalid inputs, such as negative values for the dimensions of shapes.
