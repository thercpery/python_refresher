# Class composition is a counterpart to class inheritance to build out classes that uses other classes.
# This is more common than class inheritance.

class BookShelf:
    # This will take in book objects.
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."

# shelf = BookShelf(300)

# print(shelf)

# Traditional inheritance.
# When you do inheritance, you are essentially treating it as evolutionary inheritance.
# All bookshelves have books, but a book is not a bookshelf.
# class Book(BookShelf):
#     def __init__(self, name, quantity):
#         super().__init__(quantity)
#         self.name = name

#     def __str__(self):
#         return f"Book {self.name}"

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book("Harry Potter")
book2 = Book("Python 101")
# print(book) # prints "BookShelf with 120 books."
shelf = BookShelf(book, book2)

print(shelf)