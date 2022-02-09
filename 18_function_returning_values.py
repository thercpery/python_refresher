def add(x, y):
    # return # this will return None and the function is terminated.
    print(x + y)
    return x + y
    # print(x + y) # any statements after return will not run 

# add(5, 8) # this will not print out because it does not print something.
result = add(5, 8) # the result expects a value
print(result) # prints "None". It is python's equivalent of "null"
# print(add(5, 8)) # prints None unless it returns something.

# The "result" variable is assigned to None because the function add() does something but does not return any value.

# Functions return None by default.

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"

# It is not recommended to return multiple different types of data.

result = divide(dividend=15, divisor=3)
print(result) # prints 5.0

result = divide(dividend=15, divisor=0)
print(result) # prints "You fool!"

result = divide(dividend=15, divisor=0) * 5
print(result) # prints "You fool!" 5 times.