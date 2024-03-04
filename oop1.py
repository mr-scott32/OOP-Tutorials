# Can Do: 
# Understand the concept of objects, attributes, and methods.
# Tutorial:

# Define a simple class representing a car
class Car:
    def __init__(self, brand, model, color): # Constructor
        self.brand = brand # Attribute
        self.model = model # Attribute
        self.color = color # Attribute

    def drive(self):
        return f"{self.color} {self.brand} {self.model} is driving."

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", "blue")

# Accessing attributes and calling methods
print(my_car.brand)  # Output: Toyota
print(my_car.drive())  # Output: blue Toyota Camry is driving.

#modifying the colour of the car

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", "blue")

# Modify the color of the car
my_car.color = "red"

# after running my_car would be red!
# try it out!
