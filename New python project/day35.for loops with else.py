for i in range(5):
    print(i)
    if i==2:
        break
else:
    print("Sorry, no i")
    print("\n")
print("\n")
p=0
while p<7:
    print(p)
    p= p+1
    if p==4:
        break
else:
    print("Sorry no p")
print("\n")

for x in range(5):
    print("Iteration no {} in for loop".format(x+1))
else:
    print("Else block in loop")
print("Out of loop")