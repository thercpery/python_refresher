# While loops
# number = 7

# while True:
#     user_input = input("Would you like to play? (Y/n) ")

#     # Terminates the program if user types "n" 
#     if user_input == "n":
#         break

#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You guessed correctly!")
#     elif abs(number - user_number) == 1:
#         print("You were off by one.")
#     else:
#         print("Sorry, it's wrong!")

# For loops
friends = ["Rolf", "Jen", "Bob", "Anne"]

# print(f"{friends[0]} is my friend.")
# print(f"{friends[1]} is my friend.")
# print(f"{friends[2]} is my friend.")
# print(f"{friends[3]} is my friend.")

for friend in friends:
    print(f"{friend} is my friend.") # prints the elements.

for friend in range(4):
    print(f"{friend} is my friend.") # prints the index.

grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)

# sum() function
total = sum(grades)
print(total / amount)