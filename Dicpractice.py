userData = [
    {
        "userName": "Vignesh",
        "password": "Vignesh"
    },
    {
        "userName": "Abdul",
        "password": "Abdul"
    },
    {
        "userName": "Revanth",
        "password": "Revanth"
    }
]

username = input("Enter your userName: ")
password = input("Enter your password: ")

isPresent = False
for i in range(len(userData)):
    user = userData[i]
    if(user["userName"] == username and user["password"] == password):
        isPresent = True
        break

for user in userData:
    if(user["userName"] == username and user["password"] == password):
        isPresent = True
        break

if isPresent:
    print("login Successful")
else:
    print("Either userName or password incorrect")
