# a= int(input("Enter your age: "))
# print("Your age is:",a)
# if(a>18):
#     print("You can drive")
# else:
#     print("You cannot drive")

a=int(input("Enter your number: "))
print("Your number is:",a)
if(a<0):
    print("The number is negative")
elif(a>0):
    if(a<=10):
        print("The number is between 1 to 10")
    elif(a>10 and a<=20):
        print("The number is between 11 to 20")
    else:
        print("The number is greater than 20")
else:
    print("The number is zero")
