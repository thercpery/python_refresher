from typing import List, Optional

class Student:
    # def __init__(self, name: str, grades: List[int] = []): # this is bad!
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        # The function default parameters evaluate when the function is defined, not when the function is called. 
        self.name = name,
        # self.grades = grades
        self.grades = grades or []

    def take_exam(self, result: int):
        # As long as you use the default parameter for all of your students, they will share the same grades.
        self.grades.append(result)

bob = Student("bob")
bob.take_exam(90)
rolf = Student("rolf")
print(bob.grades)
print(rolf.grades) # this will output [90] even though rolf did not take an exam