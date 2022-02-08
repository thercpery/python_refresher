print(5 == 5)
print(5 > 5)
print(10 != 10)

# Comparisons: ==, !=, >, <, >=, <=

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad)
print(friends is abroad) # returns false because the two lists has a different memory id
print(abroad is abroad) 

friends = ["Rolf", "Bob"]
abroad = friends

print(friends is abroad) # returns true because the memory id of friends variable is passed to abroad variable
