# The purpose of object-oriented programming is to allow us to write code that looks like what we would work with in the real-world. (Real world objects such as tables, chairs, books, users, etc.)

# Functional programming

# student = {
#     "name": "Rolf",
#     "grades": (89, 90, 93, 78, 90)
# }

# def average(sequence):
#     return sum(sequence) / len(sequence)

# print(average(student["grades"]))

# Object-oriented programming

class Student: # a class is a definition of something, but it does not create a particular student. It's just defining how the student behaves.
    def __init__(self, name, grades):
        # Define the properties you want.
        # We use the __init__() method to create the object and assign whatever property with a value.
        # All parameters inside a class need to have a parameter (self) so that they can take in the object that you are constructing. You can declare as many parameters.
        # self.name = "Rolf"
        self.name = name
        # self.grades = (90, 90, 93, 78, 90)
        self.grades = grades

    # You can define another method inside a class that will pass "self" as a parameter
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (100, 100, 93, 78, 90)) # it creates a new empty container, and it runs the __init__ method inside of the Student.
student2 = Student("Rolf", (90, 90, 93, 78, 90))
print(student.name)
print(student.grades)
print(student2.name)
print(student2.grades)
# print(Student.average_grade(student)) # too verbose
print(student.average_grade())
print(student2.average_grade())