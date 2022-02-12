class ClassTest:
    def instance_method(self):
        # instance methods are used if you want to produce an action that used the data inside the object. It is also used to modify the data in the object.
        print(f"Called instance_method of {self}")

    @classmethod # you can define another method
    def class_method(cls): # the cls parameter will be the class itself
        # class methods are used often as factories.
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        # static methods does not have a parameter.
        # static methods are used to just place a method in a class.
        print("Called static_method.")

# test = ClassTest() # creating instance_method()
# test.instance_method() # we call it instance_method because we call it on a class instance
# ClassTest.instance_method(test) # creating instance_method
ClassTest.class_method() # in calling @classmethod, you don't need to initialize the class object.
ClassTest.static_method() # @staticmethod is a separate function inside a classs

# why is @classmethod used?
class Book:
    TYPES = ("hardcover", "paperback") # you can also put variables and this becomes class properties

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        # __repr__ is commonly used as a representation of an object.
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
        # use cls for more flexibility and for inheritance purposes.

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

print(Book.TYPES)
book = Book("Harry Potter", "hardcover", 1500)
print(book.name)
print(book)

# since we don't want to hard-code the book type because of the TYPE variable in Book class, we need to call hardcover when instantiating a book object.

book = Book.hardcover("Harry Potter", 1500)
print(book)

light = Book.paperback("Python 101", 600)
print(light)