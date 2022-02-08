from re import A


x = 15 # the value will be assigned first before it will be assigned to a variable.
price = 9.99 # float data types

discount = 0.2

result = price * (1 - discount) # it follows the PEMDAS rule

print(result) # print() is a function

# STRINGS - stores character(s)
name = "Rolf"
name = "Bob" # reassigning a value
print(name)
print(name * 2) # print multiple instances
print(name + name)

# Changing variable values
a = 25
b = a # equals to 25

print(a)
print(b)

b = 17
print(a)
print(b)