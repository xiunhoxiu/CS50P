with open("students.csv") as file:
    for line in file:
        row = line.rstip().split(",")
        print(f"{row[0] is in {row[1]}}")