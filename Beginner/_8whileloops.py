s = True
att = 3

while s:
    pw = "yesterday"
    i = input("Enter the Password:\n")
    if i == pw:
        print("Valid Password")
    else:
        att-=1
        print(f"Incorrect Password,Attempts left {att}")
        if att == 0:
            print(f"You are out of attempts")
            break


