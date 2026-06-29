class Users:
    id = 0
    name = ""
    city = ""
    mobileNo= ""

    def __init__(self, id, name, city, mobileNo):
        self.id = id
        self.name = name
        self.city = city
        self.mobileNo = mobileNo

    def printObject(self):
        print("function inside class",self.name)


user1 = Users(1,"vignesh", "chennai", "121232434")
user2 = Users(2,"Deva", "chennai", "121232434")
print(user1.name)
user1.printObject()

print(user2.name)
user2.printObject()
