s = set()

s = {1,2,3,4,1}
print(s)

s.add(5)
print(s)

result = s.pop()
print(result)
print(s)

s.remove(5)
print(s)

# s.clear()
# print(s)

print(len(s))

s2 = s.copy()
print(s2)

s3 = {2,6,7,8,9}
# print(s.union(s3))

print(s.intersection(s3))

print(s.difference(s3))

print(s3.difference(s))
