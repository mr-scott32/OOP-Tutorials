# Modules and dictionaries refresher

Before learning about 'classes' make sure you have become familair with using dictionaries and modules

## Modules

**1. Create a Module (calculations.py):**

```python
def add(x, y):
  """Adds two numbers and returns the sum."""
  return x + y

def subtract(x, y):
  """Subtracts two numbers and returns the difference."""
  return x - y
```

This module defines two functions: `add` and `subtract` for performing basic arithmetic operations.

**2. Import and Use the Module (main.py):**

```python
# Import the calculations module
import calculations

# Use the add function
result = calculations.add(5, 3)
print(f"5 + 3 = {result}")  # Output: 5 + 3 = 8

# Use the subtract function
difference = calculations.subtract(10, 2)
print(f"10 - 2 = {difference}")  # Output: 10 - 2 = 8
```

**Explanation:**

- We import the `calculations` module using `import calculations`.
- Then, we call the `add` and `subtract` functions from the imported module using dot notation (`calculations.add`, `calculations.subtract`).
- The results are stored in variables (`result`, `difference`) and printed.

This example demonstrates how modules promote code organization and reusability. You can create modules for specific functionalities and import them into other scripts as needed.

## Let's walk through the code

```
student = {"studentID": "Student Number"}
print(student["studentID"])

enemy ={"enemyID": "Enemy Number","enemyHP": 100}
print(enemy["enemyID"])
print(enemy["enemyHP"])
```

At the beginning, two dictionaries are created: student and enemy. These have no particular meaning, just examples.

Each dictionary contains key-value pairs that represent attributes of a student and an enemy, respectively. The print function is then used to display the values of specific keys in these dictionaries.

## Introducing Classes

In the next code block, we are creating two classes.

These classes have __init__ methods, which are **special methods** in Python classes that are automatically called when an object of the class is instantiated. 

The __init__ methods here are used to **initialise the attributes o**f a Student or Enemy object. The classes also contain getter methods, which are used to retrieve the values of the attributes.

Objects of the Student and Enemy classes are then created and their attributes are printed out. 

A dictionary of students is then created and printed.

The mapLocations class is defined next. This class represents a location on a map, with attributes for the location's ID, name, description, and whether it has been visited. Five mapLocations objects are created, each representing a different location.

The eval function is then introduced. This built-in Python function evaluates a string as a Python expression and returns the result. In this case, it's used to evaluate a mathematical expression, "5 + 3", and print the result.

Finally, a for loop is used to print out the ID and name of each location. The eval function is used here to dynamically generate the name of each mapLocations object and call its getter methods. This is done by concatenating the string "location" with the string representation of the loop variable i, and the method name. The eval function then evaluates this string as a Python expression, effectively calling the method on the desired object.