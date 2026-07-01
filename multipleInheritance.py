class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Address:
    def __init__(self, country, state):
        self.country = country
        self.state = state

class Developer(Employee, Address):
    def __init__(self, id, name, country, state, language):
        Employee.__init__(self,id, name)
        Address.__init__(self, country, state)
        self.language = language

dev = Developer(1,"Vignesh", "India", "TN", "python")
print(dev.state)