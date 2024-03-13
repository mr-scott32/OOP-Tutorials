'''
Modules are like dictionaries.
'''

student = {"studentID": "Student Number"}
print(student["studentID"])

enemy ={"enemyID": "Enemy Number","enemyHP": 100}
print(enemy["enemyID"])
print(enemy["enemyHP"])



class Student():
    def __init__(self, studentID, studentName):
        self.studentID = studentID
        self.studentName = studentName
    def getStudentID(self):
        return self.studentID
    def getStudentName(self):
        return self.studentName
    
class Enemy():
    def __init__(self, enemyID, enemyHP):
        self.enemyID = enemyID
        self.enemyHP = enemyHP
    def getEnemyID(self):
        return self.enemyID
    def getEnemyHP(self):
        return self.enemyHP
    
student1 = Student("S001", "John")
print(student1.getStudentID())

enemy1 = Enemy("E001", 100)
print(enemy1.getEnemyID())
print(enemy1.getEnemyHP())

#create a dictionary of two students
students = {"studentID1": "S001", "studentName1": "John", "studentID2": "S002", "studentName2": "Jane"}

print(students)

#create a new student using the class
student2 = Student("S002", "Jane")
print(student2.getStudentID())

Student3 = Student("S003", "Jack")
print(Student3.getStudentID())


class mapLocations():
    def __init__(self, locationID, locationName, locationDescription, visited):
        self.locationID = locationID
        self.locationName = locationName
        self.locationDescription = locationDescription
        self.visited = visited
    def getLocationID(self):
        return self.locationID
    def getLocationName(self):
        return self.locationName
    def getLocationDescription(self):
        return self.locationDescription
    def getVisited(self):
        return self.visited
    
location1 = mapLocations("L001", "Home", "This is your home", "No")
location2 = mapLocations("L002", "School", "This is your school", "No")
location3 = mapLocations("L003", "Park", "This is the park", "No")
location4 = mapLocations("L004", "Shop", "This is the shop", "No")
location5 = mapLocations("L005", "Cafe", "This is the cafe", "No")


# The eval function in Python is a built-in function that parses and evaluates 
# a string as a Python expression and returns the result. 
# This function can be useful when you need to dynamically execute Python code.


result = eval("5 + 3")
print(result)  # Outputs: 8

#here we want to show location1, location2 etc, but we also want to use the i
# in the for loop to add to the end of the string location, to make location1, location2 etc
# we can use the eval function to do this. It's not the best way to do it, but it's a way to do it.

for i in range(1,6):
    print("Location ID: ", eval("location"+str(i)+".getLocationID()"))
    print("Location Name: ", eval("location"+str(i)+".getLocationName()"))