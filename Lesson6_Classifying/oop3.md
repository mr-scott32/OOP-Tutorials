# Tutorial 3: Classifying Objects and Creating Instances

## Walk through the example
The active selection is an example of Object-Oriented Programming (OOP) in Python. It defines a class Dog and creates two instances of it. The concepts of classifying objects based on their attributes and behaviors, and creating instances of classes to represent individual objects are demonstrated.

The **Dog class** is defined with the class keyword. It has a constructor method __init__ which is automatically called when a new instance of the class is created. 

The **constructor** takes three arguments: **self, name, and breed.** The self argument is a reference to the instance of the class and is used to access variables that belong to the class. The name and breed arguments are used to initialise instance attributes of the same names. 

**Instance attributes are variables that are unique to each instance of a class. In this case, each dog can have a different name and breed.**

The Dog class also has a **method** bark. 

This method returns a string "Woof!" which represents the behavior of a dog.

After the class definition, two instances of the Dog class are created with the lines dog1 = Dog("Buddy", "Golden Retriever") and dog2 = Dog("Max", "German Shepherd"). These lines create new Dog objects and call the __init__ method to initialize the name and breed attributes.

Finally, the name and breed attributes of the dog1 and dog2 objects are printed with print(dog1.name, dog1.breed) and print(dog2.name, dog2.breed). 

**This is an example of classifying objects based on their attributes. In this case, the dogs are classified by their names and breeds.**