class employee:
    id = 0
    name = ""
    __department = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def setDepartment(self, d):
        self.__department = d

    def getDepartment(self):
        return self.__department
    
emp = employee(1, "guru")
# emp.__department = "IT"
emp.setDepartment("Development")
print(emp.getDepartment())