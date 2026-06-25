attempt = 1

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



def login():
    username = input("Enter your userName: ")
    password = input("Enter your password: ")
    isloggedIn = False
    for user in userData:
        if(user["userName"] == username and user["password"] == password):
            isloggedIn = True

    if(isloggedIn):
        print("login successful")
    else:
        action = input("Either username or password incorrect. Do you want to reset your password. yes | No")
        if(action == "yes"):
            resetPassword()
        else:
            print("please try again") 


def resetPassword():
    global attempt
    
    if(attempt > 3):
        print("Max attemp reached")
    else:    
        userName =input("Enter your userName: ")
        password = input("Enter your password: ")
        reEnter = input("Re-Enter your password: ")

        if(password == reEnter):
            for user in userData:
                if(user["userName"] == userName):
                    user["password"] = password
        else:
            print("Either password doesn't match. please Try again")
            attempt += 1
            resetPassword()


operation = int(input("Enter operation to perform 1. Login 2.Reset Password"))

if(operation == 1):
    login()
elif(operation == 2):
    resetPassword()
else:
    print("Invalid operation")


