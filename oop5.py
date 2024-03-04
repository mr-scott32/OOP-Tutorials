# Able to: Explain the purpose and benefits of using classes in programming.
# Tutorial:

# Define a class representing a Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create an instance of the Rectangle class
rectangle = Rectangle(5, 3)

# Explain the purpose and benefits of using classes
print(rectangle.area())  # Output: 15
