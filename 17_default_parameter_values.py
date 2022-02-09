def add(x, y=8): # adding a value to a parameter makes a parameter optional to be called as an argument
    print(x + y)

# you cannot have a default parameter followed by a non-default parameter.
# Incorrect:
# def add_2(x=5, y):
#     print(x + y)


add(5, 8)
add(x=5)
# add(y=5) # returns an error because "x" is a required argument.
add(x=5, y=8)

# DO NOT DO THIS!!!
default_y = 3
def add_default(x, y=default_y): # the value of "default_y" is ALWAYS 3 because it is declared before the function.
    sum = x + y
    print(sum)

add_default(2)
default_y=4
add_default(2)
