# Lambda functions does not have a name and is only used to return value. (Arrow function in Javascript)

# Traditional functions
# def add(x, y):
#     return x + y

# Lambda functions
add = lambda x, y: x + y

# If you are going to use the lambda functions later, you should to use at the same line you have declared it.
# print((lambda x, y: x + y)(5, 7))

print(add(5, 7))

def double(x):
    return x * 2

sequence = [1, 3, 5, 9]

doubled = [double(x) * 2 for x in sequence]
print(doubled)
# Lambda functions with list comprehension
doubled = [(lambda x: x * 2)(x) for x in sequence]
print(doubled)

# map function - goes over each value in first array and applies a function declared
# You have to wrap maps in a list() function if you want to get its value because maps return objects.
# MOST PROGRAMMING LANGUAGES DOES NOT HAVE LIST COMPREHENSIONS.
doubled = list(map(double, sequence))
print(doubled)

doubled = list(map(lambda x: x * 2, sequence))
print(doubled)