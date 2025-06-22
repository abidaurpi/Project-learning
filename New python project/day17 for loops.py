name="Abhishek"
for i in name:
    print(i)
    if(i=="b"):
        print("This is something special")

colors=["red", "green", "blue", "yellow"] # List of colors
for color in colors:
    print(color)
    for i in color:
        print(i)

for k in range(5):
    print(k+1)

print("another loop")

for k in range(1,9):
    print(k)

print("ANOTHER LOOP")
k=float(k)
for k in range(1, 10, 2):  # Start at 1, end before 10, step by 2 arekta kotha, ekhane for k in range(1, 10, 2.5) dile error dekhabe, karon range function e step float value nite pare na.ejonno while loop use korte hobe
    print(k)