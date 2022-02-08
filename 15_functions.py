# def hello():
#     print("Hello!")

# # Calling a function
# hello()

# Defining a code
# def user_age_in_seconds():
#     user_age = int(input("Enter your age: "))
#     age_seconds = user_age * 365 * 24 * 60 * 60
#     print(f"Your age in seconds is {age_seconds}.")

# Running the code
# print("Welcome to the age in seconds program!")
# user_age_in_seconds()
# print("Goodbye!")

# IMPORTANT: DO NOT RENAME BUILT-IN FUNCTIONS IN PYTHON!!
# def print():
#     print("Hello world")

# print()

# friends = ["Rolf", "Bob"] # global friends

# def add_friend():
#     friend_name = input("Enter your friend name: ")
#     # friends = friends + [friend_name] # local friends - will return error because it is defined inside the function and "friends" instance is not declared
#     f = friends + [friend_name]

# add_friend()

# Do not run functions before they are declared - Returns error
# say_hello()
# def say_hello():
#     print("Hello")

friends = []
def add_friend():
    friends.append("Rolf")

# friends = []
add_friend()
add_friend()
add_friend()

print(friends) # ["Rolf"]