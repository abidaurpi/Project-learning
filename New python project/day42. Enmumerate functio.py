marks = [12, 56, 32, 98, 12,  45, 1, 4]
# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Harry, awesome!")
#   index +=1

for index,mark in enumerate(marks,start=1): #start=1 → tells Python to start counting from 1 instead of 0
    print(mark)
    if(index==3):
        print("Harry, awesome!!")

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')



