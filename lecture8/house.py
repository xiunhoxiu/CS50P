name = input("Hat's your name? ")

match name:
    case "Harry" | "Hermone" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:  
        print("Who?")
