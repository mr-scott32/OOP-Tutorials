# Tutorial 5: The purpose and benefits of OOP example

This is a Python script that demonstrates the use of classes in programming. It defines a class Rectangle and creates an instance of it. The purpose and benefits of using classes in programming are also illustrated.

The **Rectangle class** is defined with the class keyword. It has a special method called __init__, which is the constructor method for the class. 

This method is automatically called when a new instance of the class is created. 

The __init__ method takes three parameters: **self, width, and height.** The self parameter is a reference to the current instance of the class and is used to access variables and methods that belongs to the class. 

The width and height parameters are used to initialise instance variables of the same names. These instance variables are unique to each instance of the class.

The Rectangle class also has a method area. This method calculates and returns the area of the rectangle by multiplying the width and height instance variables.

After the class definition, an instance of the Rectangle class is created with the line rectangle = Rectangle(5, 3). This line creates a new Rectangle object and calls the __init__ method to initialize the width and height instance variables.

Finally, the area method of the rectangle object is called with print(rectangle.area()). The area method calculates the area of the rectangle and returns it. The returned value is then printed.

The purpose of using classes in programming is to group related data and functions into a single unit, which is the class. This makes the code more organized and easier to understand and maintain. The benefits of using classes include code reuse, encapsulation, and inheritance. Code reuse is achieved by creating instances of the class. Encapsulation is achieved by hiding the internal details of the class and exposing only what is necessary. Inheritance allows new classes to be created based on existing ones, which promotes code reuse and logical structure.