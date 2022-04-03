li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

# 1st and usual way to make a list
newList = []
for i in li:
    newList.append(func(i))

print(newList)

# using map function
print(list(map(func, li)))

# using list comprehensions
print([func(x) for x in li])