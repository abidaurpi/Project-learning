tup=(1,2,3,"green", True)
print(type(tup),tup)

tup1=(1)
print(type(tup1),tup1)

tup2=(1,)
print(type(tup2),tup2)

#tup[0]=90 error ashbe karon tuple change hoy na

print ( type( tup ), tup)
print(tup[0])
print(tup[1])
print(tup[2])
# print(tup[34]) #error ashbe

if 342 in tup:
    print("Yes.This number is in tuple")
else:
    print("No! This tuple isn't present in this tuple.")

tup= tup[12:41]  #observation:tuple e rang jai e dei na keno answer return kore..error ashe na

print(tup)

tup2= tup[1:4]
print(tup2)

tup3= tup[1:4]
print(tup3)
