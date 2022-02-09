def multiply(*args): # what this means is a collection of arguments passed as a parameter as a tuple
    # with this, you can pass how many arguments you want.
    print(args) # prints a tuple of arguments.
    total = 1
    for arg in args:
        total = total * arg
    
    return total

print(multiply(1, 3, 5))
print(multiply(-1))

def add(x, y):
    return x + y

nums = [3, 5]
# Using asterisk to destructure arguments from a list into multiple parameters.
print(add(*nums))
# add(nums) # passing nums as a list. returns an error.

# Destructuring arguments from a dictionary
nums = {"x": 15, "y": 25}
print(add(nums["x"], nums["y"]))
print(add(x=nums["x"], y=nums["y"]))
# Passing values in a dictionary through double-asterisk.
print(add(**nums))

def apply(*args, operator): # what this means is collect all arguments and a named argument at the end of the declaration
    if operator == "*":
        # return multiply(args) # this will pass args as a tuple itself (1, 3, 6, 7)
        return multiply(*args) # this will pass a unpacked tuple passed as an argument.
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print(apply(1, 3, 6, 7, operator="+"))
print(apply(1, 3, 6, 7, operator="*"))
# print(apply(1, 3, 6, 7, "+")) # returns an error because there is no named argument "operator" passed.