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


