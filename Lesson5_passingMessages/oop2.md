# Tutorial 2: Interacting with objects and passing messages

This tutorial defines a class Person and creates an instance of it. The concept of objects interacting by passing messages is demonstrated.

The Person class is defined with the **class** keyword. It has a constructor method __init__ which is automatically called when a new instance of the class is created. 

The constructor takes two arguments: **self** and **name**. The self argument is a reference to the instance of the class and is used to access variables that belong to the class. 

The **name** argument is used to initialise the instance attribute of the same name. Instance attributes are variables that are unique to each instance of a class. 

In this case, each person can have a different name.

The **Person class** also has a method **greet**. 

This method returns a **string** that includes the name of the person and a greeting message. 

The f before the string is used to embed expressions inside string literals, using curly braces {}. The expressions will be replaced with their values when the string is created. This is decoration only

After the class definition, an instance of the Person class is created with the line person = Person("Alice"). This line creates a new Person object and calls the __init__ method to initialize the name attribute.

Finally, the greet method of the person object is called with print(person.greet()). The greet method returns a string that is then printed. This is an example of objects interacting by passing messages. 

In this case, the person object is sending a message to the console to print the greeting.