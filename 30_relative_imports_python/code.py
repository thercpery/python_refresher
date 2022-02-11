# import mymodule # this will run first.
# This is an absolute import that you have to define the path that you are importing from.

from mymodule import divide
# from .mymodule import divide # This means from the current folder, look at the "mymodule" file and import the divine function.
# The "mymodule" file is in the same folder as "code.py"
# It will return an error because what it does is it tries to import __main__.mymodule.

# A relative import is one can import the current folder that the file is in, but it cannot import unless there is a folder name in the path in the module path.

print("code.py:", __name__)