class Person:
    def __init__(self, name, age):
        # methods with two underscores in the beginning and end are special methods because you do not have to call it.
        self.name = name
        self.age = age

    def __str__(self):
        # a magic method that will turn the object into a string
        return f"Person {self.name}, {self.age} years old."

    def __repr__(self):
        # a magic method that makes the object unambiguous and should return a string that allows us to recreate the original object very easily.
        # the __repr__() method is used in python debugger.
        return f"<Person({self.name}, {self.age})>"

bob = Person("Bob", 35)
print(bob) # returns a Person object and not its value without the __str__() method.