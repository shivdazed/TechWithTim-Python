#ex1
def func(x):
    return x + 5


func2 = lambda x: x + 5
print("Lambda function:", func2(5))
print("Ordinary function:", func(5))

#ex2 lambda function inside another ordinary function

def func1(x):
    func3 = lambda x: x + 5
    return func3(x) + 85


print("Lambda inside another ordinary function:", func1(2))

#ex3 multiple parameters
func4 = lambda x, y=4: x + y

print("Multiple parameter lambda function:", func4(5, 9))

#ex4 with map and filter functions

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newList = list(map(lambda x: x + 2, a))
print("Lambda in map function:", newList)

l = list(filter(lambda x: x % 3 == 0, a))
print("Lambda in filter function:", l)




