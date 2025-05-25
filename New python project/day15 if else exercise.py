a=float(input("Enter your time(12 hour format):"))
b=input("Is it am or pm?(Enter am or pm): ")
if(a>12):
    print("Your input is invalid")
elif(b=="am"):
    if(a>=0 and a<4):
        print("Happy mid night")
    elif(a>=4 and a< 6):
        print("Its dawn bro!! Wake up")
    else:
        print("Good morning")
elif(b=="pm"):
    if(a>=0 and a<4):
        print("Good afternoon")
    elif(a>=4 and a<7):
        print("Good evening.")
    else:
        print("Good night.")
else:
    print("Your input is invalid.")
