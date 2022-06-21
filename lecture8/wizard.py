class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name

class Student(Wizard): # inheritance
    def __init__(self, name, house):
        super().__init__(name)  # access super class and pass only the name
        self.house = house
    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    ...



wizard = Wizard("Albus")
student = Student("Harry")
professor = Professor("Severus")