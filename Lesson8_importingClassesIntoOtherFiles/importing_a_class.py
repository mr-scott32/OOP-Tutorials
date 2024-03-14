from Lesson8.students import Student #import the Student class from the students.py file

# we are creating students using the Student class from the students.py file

#create 5 students
student1 = Student("S001", "John")
student2 = Student("S002", "Jane")
student3 = Student("S003", "Jack")
student4 =  Student("S004", "Jill")
student5 = Student("S005", "James")

for i in range(1,6):
    print("Student ID: ", student1.getStudentID())
    print("Student Name: ", student1.getStudentName())
    print()
