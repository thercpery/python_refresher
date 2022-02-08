friend_ages = {
    "Rolf": 24, # key is "Rolf", value is "24"
    "Adam": 30,
    "Anne": 27
}
# Hashable types - integers and strings

# Access a particular element
print(friend_ages["Adam"])

# Add something to dictionary
friend_ages["Bob"] = 20
print(friend_ages)

# Change a value to element
friend_ages["Rolf"] = 25
print(friend_ages)

# List of dictionaries
friends = [
    {
        "name": "Rolf",
        "age": 24
    },
    {
        "name": "Adam",
        "age": 30
    },
    {
        "name": "Anne",
        "age": 27
    }
]

print(friends)
print(friends[0]) # get by index
print(friends[1]["name"]) # get by dictionary key

student_attendance = {
    "Rolf": 96,
    "Bob": 80,
    "Anne": 100
}

# Iterate over a dictionary
for student in student_attendance:
    print(f"{student}: {student_attendance[student]}%") # prints keys

# Iterate over values of a dictionary
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}%") # prints keys

# "in" keyword - only checks the keys of the dictionary
if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not a student.")

# Getting the values of the dictionary
attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))