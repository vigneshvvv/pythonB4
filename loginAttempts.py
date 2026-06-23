userName = "vignesh"
password = "vignesh"

attempts = 3

while(attempts > 0):
    
    inputUserName = input("Enter the username: ")
    inputpassword = input("Enter your password: ")

    if( inputpassword == userName and password == inputpassword):
        print("login successful")
        break
    else:
        print("either username or password incorrect")
        attempts -= 1

    if(attempts == 0):
        print("Exceeded the number of retries. Pls try again later")
        break
    