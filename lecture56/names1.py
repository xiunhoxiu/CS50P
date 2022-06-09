name = input("What's your name? ")

with open("names1.txt", "a") as file:
    file.write(f"{name}\n")