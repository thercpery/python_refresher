friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# difference() method
local_friends = friends.difference(abroad) # returns the difference as a new set (filter function in Javascript)
print(local_friends)

local_friends = abroad.difference(friends) # returns the difference as a new set (filter function in Javascript)
print(local_friends)

# union() method
local = {"Rolf"}
abroad = {"Bob", "Anne"}

friends = local.union(abroad) # unites two sets
print(friends)

# intersection() method
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science) # gets the elements that are both present in two sets
print(both)