def divide(dividend, divisor):
    return dividend / divisor

print("mymodule.py: ", __name__) # the __name__ is a global variable in python that allows us to differentiate between the file you run and the file you import.
# returns "mymodule.py: __main__". 
# __<variable>__ is also called a "dunder".
# when this file is imported, it changes to "mymodule".

import libs.mylib