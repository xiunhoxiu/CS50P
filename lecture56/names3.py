with open("names1.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())