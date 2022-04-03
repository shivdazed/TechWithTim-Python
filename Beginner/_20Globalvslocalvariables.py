var = 10
i = 27

def func(x):
    global i
    i = True
    if x == 5:
        return x

y = func(5)
print(y)
print(i)