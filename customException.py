class AgeException(Exception):
    pass

try:
    age = int(input("Enter your Age: "))
    if age < 18:
        raise AgeException("you are not eligible")
    print("login successfull")
except AgeException as e:
    print(e)