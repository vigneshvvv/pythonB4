userName = "Deva"
password = "Deva"

inputUserName = input("Enter userName: ")
inputPassword = input("Enter password: ")

if(userName == inputUserName and password == inputPassword):
    print("logged in")
else:
    print("Either userName or password is incorrect")