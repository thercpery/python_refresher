# from mymodule import divide
# # import divide

# print(divide(10, 2))
# print(__name__)

import sys

# print(sys.path) # this returns the list of paths to find files to import.
# If none of the paths contains the module that will be imported, it will return an error 

# Import something in a folder.
import mymodule
# returns "mylib.py libs.mylib"
print(sys.modules) # prints modules that are imported as a dictionary (including built-in modules).