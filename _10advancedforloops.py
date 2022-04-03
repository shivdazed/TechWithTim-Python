fruits = [i for i in input("Enter four fruits:").split()]
print(fruits)
for _ in fruits:
    if _ == 'pears':
        print(_)
    else:
        print("Not a pear")

print("\n")

for _ in range(len(fruits)):
    if fruits[_] == 'pears':
        print(fruits[_])
    else:
        print("not a pear")