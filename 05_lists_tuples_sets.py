# A List is a collection which is ordered and changeable. Allows duplicate members.
l = ["Bob", "Rolf", "Anne"]

# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
t = ("Bob", "Rolf", "Anne")

# A Set is a collection which is unordered and unindexed. No duplicate members.
s = {"Bob", "Rolf", "Anne"}

# Accessing Lists
print(l[0])
print(l[2])

# Accessing Tuples
print(t[0])
print(t[2])

l[0] = "Smith"
print(l)

# ERROR
# t[0] = "Smith"
# print(t)

# Add element to list
l.append("Bob")
print(l)

# ERROR
# t.append("Smith")
# print(t)

# Remove element to list
l.remove("Bob")
print(l)

# Add element to set
s.add("Smith")
print(s)
s.add("Smith") # it will ignore because sets does not have duplicate
print(s)