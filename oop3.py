# Able to: Classify objects based on their attributes and behaviors.
# Able to: Create instances of classes to represent individual objects.
# Tutorial:

# Define a class representing a Dog
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

# Create instances of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

# Classify objects and create instances
print(dog1.name, dog1.breed)  # Output: Buddy Golden Retriever
print(dog2.name, dog2.breed)  # Output: Max German Shepherd
