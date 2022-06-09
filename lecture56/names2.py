with open("names1.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())