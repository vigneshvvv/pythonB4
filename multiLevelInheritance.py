class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Address(Employee):
    def __init__(self, id, name, state, country):
        super().__init__(id, name)
        self.state = state
        self.country = country

class Developer(Address):
    def __init__(self, id, name, state, country, language):
        super().__init__(id, name, state, country)
        self.language = language

dev = Developer(1, "vignesh", "TN", "INDIA", "python")
print(dev.name)