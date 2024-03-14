# Can Do: 

#Identify how objects interact by passing messages.
# Tutorial:

# Define another class representing a person
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}."

# Create an instance of the Person class
person = Person("Alice")

# Interacting with objects by passing messages
print(person.greet())  # Output: Hello, I'm Alice.
