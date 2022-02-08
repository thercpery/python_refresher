def add(x, y): # variables declared here is called parameters
    # pass # "do nothing" in python
    result = x + y
    print(result)

add(5, 3) # variables that will be used when calling a function is called arguments

# Function without parameters
def say_hello(name, surname):
    print(f"Hello, {name} {surname}.")

# say_hello("Bob") # will return an error because one argument is passed to a function that has no parameters declared.
# say_hello() # will return an error because no argument is passed to a function that needs parameters.

# Positional arguments
say_hello("Bob", "Smith") # the first argument will take first parameter, the second argument will take second parameter and so on...

# Named / Keyword arguments
say_hello(surname="Bob", name="Smith") # as long as the parameter is declared on the calling of the function as an argument, the order will not matter.
# Keyword arguments are easily readable to which argument is for each parameter.

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")

divide(dividend=15, divisor=0)
# The keyword argument cannot be followed by a positional argument, and it will return an error
# The positional arguments come first and keyword arguments later.