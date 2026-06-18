numbers = [10, 20, 30, 40]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[-1])

numbers[0] = 50
print(numbers)
print(len(numbers))

numbers.insert(1,60)
print(numbers)
numbers.append(70)
print(numbers)

numbers.remove(50)
print(numbers)

numbers.append(70)
print(numbers)

if(80 in numbers):
    ind = numbers.index(60)
    numbers[ind] = 10

print(numbers)
print(80 in numbers)