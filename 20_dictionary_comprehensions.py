users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234")
]

username_mapping = {user[1]: user for user in users}
# user[1] = username, "user" is the whole tuple, do this in each iteration of user in the users list.
print(username_mapping)
print(username_mapping["Bob"])

# Traditional way (w/o mapping)
# for user in users:
#     if user[1] == "Bob":
#         print(user)

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

# Destructure variables using input
_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect.")