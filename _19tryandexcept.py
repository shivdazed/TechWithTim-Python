password = 123456
pass_att = input("Enter password:")

try:
    if password == int(pass_att):
        print("Valid Password")
    else:
        print("Incorrect Password")
except:
    print("Invalid Password!!!!")