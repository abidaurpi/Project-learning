name="Harry"
friend="Rohan"
apple='He said, "Apple is red"' #using single quotes
apple2="He said, \"Apple is red\"" #using double quotes.jar jonno backslash use kora hoitese

print("Hello, " +name)
print("\n")

print(apple)
print("\n")

print(apple2)
print("\n")

#multiline line string
apple3='''Hello Harry,
Ki obostha?
habijabi habijabi''' #triple single or double quotes use kora jabe
print(apple3)
print("\n")
print(name[0])
print(name[1])
print(name[2])
#print(name[5])  index error dekhabe
print(name[0:3]) #0,1,2 index er value dekhabe
print("\n")
print("Lets use a for loop\n")
for character in name:
    print(character)