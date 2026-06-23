def loginOperation():
    userName = "vignesh"
    password = "vignesh"
    attempts = 3
    while(attempts > 0):
        inputUserName = input("Enter the username: ")
        inputpassword = input("Enter your password: ")
        if( inputUserName == userName and password == inputpassword):
            print("login successful")
            break
        else:
            print("either username or password incorrect")
            attempts -= 1
        if(attempts == 0):
            print("Exceeded the number of retries. Pls try again later")
            break

def registration():
    userName = input("Enter your userName: ")
    password = input("Enter your password: ")
    reEnterPassword = input("Re-Enter your password: ")
    print("registered successfully")


option = int(input("Select the operation 1. Login 2.Registration"))
if(option == 1):
    loginOperation()
elif(option == 2):
    registration()
else:
    print("Invalid operation")    
