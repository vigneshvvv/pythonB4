t = (230,221, 1211, 24345)
print(t[0])

for n in t:
    print(n)

lst = list(t)
# print(lst)
lst.append(56335)
t = tuple(lst)
print(t)    