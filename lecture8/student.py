# CS50P lecture 8 - look for source code.
class Student:
    def __init__(self, name, house):
            self.name = name
            self.house = house
        
    def __str__(self):
        return print(f"a student called {self.name} from {self.house}")
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    @property
    def house(self):  # one argument
        return self._house
    
    @house.setter
    def house(self, house):  # two arguemns
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")  # will not let access the attr. directly.
        self._house = house

def main():
    student = get_student()
    student._house = "Number Four, Privet Drive"  # the setter did not prevent. DONT CHANGE anything with _ xD
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house) # Constructor code


if __name__ == "__main__":
    main()