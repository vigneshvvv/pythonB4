class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Developer(Employee):
    def __init__(self, id, name, language):
        super().__init__(id, name)
        self.language = language

class Manager(Employee):
    def __init__(self, id, name, teamSize):
        super().__init__(id, name)
        self.teamSize = teamSize

dev = Developer(1,"Vignesh", "PY")
print(dev.id)
print(dev.name)
print(dev.language)

manager = Manager(2,"Deva", 30)
print(manager.teamSize)