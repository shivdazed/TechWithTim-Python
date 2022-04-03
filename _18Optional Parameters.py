"""
agility ag=35 out of 50, stamina st = 75 out of 100
"""
def Funk(ag=35,st=75):
    ag = int(input("input your guess for best agility to have awesoome funk:"))
    st = int(input("input your guess for best stamina to have awesoome funk:"))
    if ag ==35 and st == 75:
        print("These are the optional(BEST) parameters for this function!")
    else:
        print("Rerun function")

Funk()