# How to use extrnal data with classes

This a Python script that demonstrates how JSON data can be used to create objects of a class.

The script starts by importing the **json module**, which provides methods for manipulating JSON data in Python.

Next, a class named **DogBreed** is defined. 

This class has a **constructor** that takes two parameters: **breed and sub_breeds**. 

These parameters represent the breed of a dog and its sub-breeds, respectively. 

Inside the constructor, these parameters are assigned to instance variables **self.breed** and **self.sub_breeds**.

The script then opens a JSON file named d**ogs.json in read mode**. The json.load function is used to load the JSON data from the file into a **Python dictionary**, which is stored in the variable data.

A **list** named **dog_breeds** is created to store DogBreed objects.

The script then **iterates** over the items in the message field of the data dictionary. 

For each item, a DogBreed object is created with the breed and sub-breeds from the item, and this object is appended to the dog_breeds list.

Finally, the script iterates over the DogBreed objects in the dog_breeds list and prints the breed and sub-breeds of each dog. If a dog breed does not have any sub-breeds, "Sub-breeds: None" is printed.