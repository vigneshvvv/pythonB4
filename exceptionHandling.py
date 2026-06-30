try:
    age = int(input("Enter your age: "))
    print("Age is: ", age)
except ValueError:
    print("Please enter valid number")
