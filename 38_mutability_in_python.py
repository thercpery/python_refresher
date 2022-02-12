a = []
b = a

a.append(35)

print(a)
print(b)

# In python a and b are names, the value is []
print(id(a))
print(id(b)) # this will return the same value as a

a = []
b = []

a.append(35)

print(a)
print(b)

print(id(a))
print(id(b)) # this will return different value

# In Python, all things are mutable because everything is an object, unless there are specifically no ways of changing the properties of the object itself.
a = ()
b = ()

# a.append(35) # you cannot do this on tuples
a = a + (15,)

print(id(a))
print(id(b))

a = 8597
b = 8597

print(id(a))
print(id(b)) # will return same values

a = 8598
print(id(a))
print(id(b))

a = "hello"
b = a

print(id(a))
print(id(b))

a += "world"
print(id(a))
print(id(b))