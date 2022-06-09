students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # defining keys and values instead of leaving dictionary empty
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")