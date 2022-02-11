def divide(dividend, divisor):
    if divisor == 0:
        # print("Divisor cannot be 0.")
        # return
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor

# divide(15, 0) 
grades = [78, 99, 85, 100]
# grades = []

print("Welcome to hte average grade program.")

# if len(grades) == 0:
#     print("You don't have grades yet.")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e: # this creates a variable to store errors
    print("There are no grades yet in your list.")
else: # this is to catch specific errors in specific code.
    print(f"The average grade is {average}")
finally: # this will run with or without error.
    print("Thank you.")

students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": [50]},
    {"name": "Jen", "grades": [100, 90]}
]

try:
    for student in students:
        name = student["name"]
        grades=  student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation --")
