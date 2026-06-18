num1= int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
operation = int(input("Enter a operation to perform 1. Addition 2. Sub 3.Multiplication 4.Division: "))

if(operation == 1):
    print(num1+num2)
elif(operation == 2):
    print(num1-num2)
elif (operation == 3):
    print(num1*num2)
elif(operation == 4):
    print(num1/num2)
else:
    print("Invalid operation please choose correct one")