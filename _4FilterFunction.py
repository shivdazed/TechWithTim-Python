def add7(x):
    return x + 7

def isodd(x):
    return x % 2 == 0


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(filter(isodd, a))
#difference between map function and list
c = list(map(isodd, a))

d = list(filter(add7, a))

print(b)
print(a)
print(c)
print(d)