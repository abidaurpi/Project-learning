marks=[3,4,5, "Harry", True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])


print(marks[-3]) #negative indexing.. temon use kora hoy na.. majhe majhe negative indexing kora hoy.. eta advance developer ra kore
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])

if 7 in marks: #ekhane jodi "7"(string) hisebe likha hoto tahole ans no asto karon 7 ekhane string hisebe list e ase
    print("Yes")
else:
    print("No")

if "Harry" in marks:
    print("Yes")
else:
    print("No")

if "arry" in "Harry":
    print("Yes.string")

if "bid" in "Abid":
    print("Yes..abid")

lst=[i*i for i in range(5)]
print(lst)
lst1=[i*i for i in range(10) if i%2==0]
print(lst1)
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_0 = [item for item in names if "o" in item]
print(namesWith_0)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_0 = [item for item in names if (len(item) > 4)]
print(namesWith_0)

