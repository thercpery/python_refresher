from libs import mylib # this will run first
# from .libs import mylib # This will try to access the "libs" folder inside the current folder
# This is an absolute import that you have to define the path that you are importing from.

print("mymodule.py:", __name__)

def divide():
    pass