for i in range(11):
    print(" 5 X ", i+1, "=", 5*(i+1))
    if (i==5):
        break
print('\n\n')
for i in range(11):
    if (i==5):
        continue
    print(" 6 X ", i+1, "=", 6*(i+1))
    

#do while loop emulation
i= 0
while True:
    print(i)
    i=i+1
    if(i%11==0):
        break