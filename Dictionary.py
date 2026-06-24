student = {
    "s.no": 1,
    "Name": "vignesh",
    "city": "chennai"
}

print(student["city"])

studentN = dict(name = "deva", age= 25)
print(studentN)

student["State"] = "TN"
print(student)
student["city"] = "Madurai"
print(student)
print(student.get("Name"))

del student["State"]
print(student)

student.pop("city")
print(student)

student.clear()
print(student)