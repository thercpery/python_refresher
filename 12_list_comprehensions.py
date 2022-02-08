numbers = [1, 3, 5]
# List comprehensions
doubled = [x * 2 for x in numbers]

# Traditional way
# for num in numbers:
#     doubled.append(num * 2)

print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]
# starts_s = friends # will have the same memory address.


# Traditional way
# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(friends)
print(starts_s)
print(friends is starts_s) # return false because they have different memory ids with the same contents
# Check ids of the list
print(f"friends: {id(friends)} starts_s: {id(starts_s)}") # returns memory address.