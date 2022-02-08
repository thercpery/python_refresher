x, y = 5, 11 # shorthand on declaring two variables
print(x)
print(y)

t = 5, 11
x, y = t
print(x, y)

student_attendance = {
    "Rolf": 96,
    "Bob": 80,
    "Anne": 100
}

print(list(student_attendance.items())) # turns all the values of the dictionary into a list. Returns a tuple

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}%") # prints keys

# for t in student_attendance.items():
#     print(t) # returns a tuple

people = [
    ("Bob", 42, "Mechanic"),
    ("James", 24, "Artist"),
    ("Harry", 32, "Lecturer")
]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# Iterate using index
for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

# Ignoring one value in tuple with "_"
person = ("Bob", 42, "Mechanic")
name, _, profession = person
print(name, profession)

# Seperate into two lists / collecting destructured variables
*head, tail = [1,2,3,4,5]
print(head)
print(tail)