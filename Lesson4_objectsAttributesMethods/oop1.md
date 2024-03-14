# Tutorial 1: Understanding Objects, Attributes, and Methods

this is a simple example of Object-Oriented Programming (OOP) in Python. 

It defines a class Car and creates an instance of it.

The Car class is defined with the class keyword. It has a constructor method __init__ which is automatically called when a new instance of the class is created. 
The constructor takes four arguments: self, brand, model, and color. 

The self argument is a reference to the instance of the class and is used to access variables that belongs to the class. It does not have to be named "self" , you can call it whatever you like, but it has to be the first parameter of any function in the class.

The "brand", "model", and "colour" arguments are used to initialize instance attributes of the same names. Instance attributes are variables that are unique to each instance of a class. In this case, each car can have a different brand, model, and color.

The Car class also has a method "drive". 

This method returns a string that includes the color, brand, and model of the car, and a message saying the car is driving. 

The f before the string is used to embed expressions inside string literals, using curly braces {}. The expressions will be replaced with their values when the string is created. It's formatting

After the class definition, an instance of the Car class is created with the line my_car = Car("Toyota", "Camry", "blue"). This line creates a new Car object and calls the '__init__' method to initialise the brand, model, and color attributes.

Finally, the brand attribute of the my_car object is printed with print(my_car.brand), and the drive method is called with print(my_car.drive()).

