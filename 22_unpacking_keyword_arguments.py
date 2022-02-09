def named(**kwargs): # this collects keyword arguments and put into a dictionary where the dictionary key is the name of the keyword argument(name and age), and the value is the values of those arguments that are passed.
    print(kwargs)

named(name="Bob", age=25)

def named2(name, age):
    print(name, age)

details = {
    "name": "Bob",
    "age": 25
}

# Unpacking the dictionary into two named arguments using **.
named2(**details)
# Same can be said for first function.
named(**details)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items(): # iterate items in kwargs. "arg" is key, "value" is the value
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)

def both(*args, **kwargs): # this is normally used to accept unlimited number of arguments
    print(args) # collection of positional arguments as tuple
    print(kwargs) # collection of named arguments as dictionary

both(1, 3, 5, name="Bob", age=25)

""" 
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
"""

def myfunction(**kwargs):
    print(kwargs)

# myfunction(**"Bob") # Error, must be mapping
# myfunction(**None) # Error, cannot destructure None