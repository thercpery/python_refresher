# First-class functions are just variables, you can pass them as an arguments to functions and use them in the same way you would use any other variable.

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

def calculate(*values, operator):
    return operator(*values) # the "operator" parameter is used as a function that will function the same way as the function above. 

result = calculate(20, 4, operator=divide) # the "divide" function is passed as an argument by the use of the variable "operator"
print(result)

# result = calculate(20, 0, operator=divide)
# print(result)


# result = calculate(20, 4, 5, operator=divide) # returns an error because it exceeds positional arguments
# print(result)

from operator import itemgetter

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem

    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
]

def get_friend_name(friend): # this will be the "finder" argument defined in search() function
    return friend["name"]

# print(search(friends, "Bob Smith", get_friend_name)) # returns an error because there is no "Bob Smith" found.
print(search(friends, "Rolf Smith", get_friend_name))
# Lambda functions in first-class functions
print(search(friends, "Rolf Smith", lambda friend: friend["name"]))
print(search(friends, "Rolf Smith", itemgetter("name")))