#1st way to create a list
o = []
print(f"1st way")
j = int(input("Enter the number of elements in list:"))

for x in range(0,j):
    o.append(int(input("Enter a number: ")))
    o.sort()

print(o)
#2nd way to create a list
print("2nd way")
try:
    a = []
    status=True
    while status:
        a.append(int(input("Input a number:")))
except:
    a.sort()
    print(a)

#3rd way to create a list
print("3rd way")
r = int(input("Enter number of elements:"))
b = list(map(int,input(f"Input the {r} elements in string and press enter- ").strip().split()))[:r]
print(f'List is {b}')


#4th way to create a list, list of a list
print("4th way")
lt = []
y = int(input("Enter number of elements:"))

for t in range(0, y):
    e = [input(), int(input())]
    lt.append(e)

print(f'list is {lt}')

#5th way to print a list, using list comprehension and type casting
print("5th way")

l1 = [int(item) for item in input("Enter the list items").split()]

l2 = [item for item in input("Enter the list items:").split()]

print(f'list1 is {l1}')
print(f'list2 is {l2}')





