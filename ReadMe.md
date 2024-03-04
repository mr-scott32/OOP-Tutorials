# Object Oriented Programming Unit

## Unit 1: Introduction to Object Oriented Programming (OOP)
- Can Do:
Understand the concept of objects, attributes, and methods.
Identify how objects interact by passing messages.
- Able to:
Classify objects based on their attributes and behaviors.
Create instances of classes to represent individual objects.
Explain the purpose and benefits of using classes in programming.

## Unit 2: Inheritance and Polymorphism
- Can Do:
Recognise the concept of inheritance and its role in code reuse.
Understand how polymorphism allows different objects to share code segments.
- Is Able to:
Implement inheritance to create new objects with shared attributes and behaviors.
Apply polymorphism to allow objects to utilize common code in different contexts.

## Unit 3: Encapsulation and Abstraction
- Can Do:
Describe the concept of encapsulation and its significance in hiding internal code.
Explain how abstraction simplifies programming by hiding irrelevant details.
- Able to:
Implement encapsulation to hide the implementation details of objects.
Utilise abstraction to focus on solving problems without being burdened by unnecessary details.

## Unit 4: Functions in Functional Programming
- Can Do:
Define functional programming and its emphasis on functions.
Understand the concept of recursion and its role in functional programming.
- Is Able to:
Create functions that return different data types based on requirements.
Utilise recursion to solve problems in a functional programming paradigm.

# HSC Theory

## Methods
An object is any item which can be described by specifying attributes and the procedures that can be performed on these attributes. E.g. picture box, report, drop down menu.
Objects contain methods which can be accessed by passing messages to them from the mainline of a program’s coded solution.
Method / operations / services: the instructions contained within an object.
A method is performed when a message is sent to that object. This is how different objects interact with each other.

## Classes
Classes are groups of objects with similar attributes and behaviours.
Classes form abstract (summary) data types as they share similar characteristics and processes. E.g. radio buttons, check box and push buttons can all be classified as one class.
Instances: structure and behaviour of the objects in the class.
Classes can inherit features from other classes to create superclasses

##v Inheritance
Inheritance is the ability to create new objects from another parent object which includes the same attributes and behaviours of an existing (parent or ancestor) object.
Allows one class to inherit methods and variables from another superclass (class with all common features to other classes). 
Inheritance allows a programmer to efficiently reuse attributes, variables, methods and behaviours on various objects and classes by only coding these ONCE throughout the entirely solution
Greater functionality can then easily be added by inheriting these existing features on new classes and objects while adding or coding new features into different objects and classes to quickly enhance functionality.

## Polymorphism
Polymorphism allows DIFFERENT types of objects to use the same segment of code, behaviour or method. E.g. a button can use the same colour as a picture box
The routines are encapsulated within a class of objects, so these routines can be used by any object within that class.

## Encapsulation
Encapsulation is the ability to contain and hide the source code behind an object, such as internal data structures and variables.
The user does not see this code. E.g. when the user clicks a button, they see a little button click animation, they do not need to know or see the coded solution.
The scripts are self-sufficient which means they stay hidden from the user and other objects and they always travel with their related object.
This means that their existing methods and attributes can be updated without affecting other classes or objects.

## Abstraction
Abstraction means to ‘take away’. With OOPs, abstraction means hiding the irrelevant characteristic code of objects from the programmer to let the programmer focus on the code of a solution to the problem, not every little detail of an object.
An example would be visual studio hiding the designer code in a separate tab for each object, rather than including it with the programmer’s source code, which could confuse the programmer.
Abstraction involves representing a complex task in a simple or symbolic way
All subprograms are process abstractions, they allow a large complex program to be viewed in a more simpler manner defined as many sub sections. This makes it easier for a programmer to read and modify the program’s code.
Data abstraction allows similar data and its operations to be syntactically grouped as one line or region.

## Functions
Functional languages allow a variety of data types to be returned from a function, unlike imperative which strictly only accepts what’s defined.
A function in PYTHON may return a single character or an entire list
Functional languages are not given a particular path to follow, so they can follow a multiple range of possibilities to arrive at the correct output or goal.
While this requires powerful parallel processors to work efficiently due to the slow execution rate of these fifth generation A.I languages. They are worth it, as they can provide a huge range of endless possibilities compared to other ‘not so expansive’ programming paradigms
Functions are built into modules meaning they can be reused together or used independently in other projects.
Use recursion (repeating an application until the correct solution is reached) rather than iteration (repeating loops to get the same outputs).
Modern functional languages allow the uses of variables and a range of data structures

# Examples in the world around you

## Online Shopping System:

**Objects**: Customer, Product, Cart, Order.
**Attributes**: Customer (name, email), Product (name, price, quantity), Order (order ID, date).
**Methods**: Customer (login, register), Product (add_to_cart, remove_from_cart), Order (place_order, cancel_order).
**Classes**: Customer class with methods for login and registration, Product class to handle product details and cart management, Order class to manage order placement and cancellation.


## Social Media Platform:

**Objects**: User, Post, Comment, Like.
**Attributes**: User (username, email), Post (content, timestamp), Comment (text, timestamp), Like (timestamp).
**Methods**: User (create_post, add_comment, like_post), Post (edit_post, delete_post), Comment (edit_comment, delete_comment).
**Classes**: User class with methods for posting, commenting, and liking, Post class to manage post content and interactions, Comment class to handle comments on posts, Like class to manage likes on posts.

## Bank Account Management System:

**Objects**: Account, Transaction, ATM, Customer.
**Attributes**: Account (account number, balance), Transaction (amount, type, timestamp), ATM (location, availability), **Customer** (name, address).
**Methods**: Account (deposit, withdraw, transfer), Transaction (record_transaction), ATM (withdraw_cash, check_balance), Customer (open_account, close_account).
**Classes**: Account class to manage account operations, Transaction class to record transactions, ATM class to handle ATM functionalities, Customer class to manage customer-related operations.


## Employee Management System:

**Objects**: Employee, Department, Project, Salary.
**Attributes**: Employee (name, id, designation), Department (name, head), Project (name, deadline), Salary (amount, bonuses).
**Methods**: Employee (update_details, assign_project), Department (add_employee, remove_employee), Project (update_deadline, assign_employee), Salary (calculate_salary, give_bonus).
**Classes**: Employee class to manage employee details and assignments, Department class to handle department-related operations, Project class to manage project details and assignments, Salary class to calculate salaries and bonuses.
