a = int(input("Enter 1st value:"))
b = int(input("Enter 2nd value:"))

if not(a==b or a+b==12):
    print("Code ran")
else:
    print('didnt run')

if (a > 3 and a < 8):
    if (b > 6 and b < 13):
        print(f'a={a} and b={b}')
    else:
        print(f'a = {a} and b is not in the range of 6 and 13')
else:
    print(" a and b are not in the ranges of 3 and 13")
