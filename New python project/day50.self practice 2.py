name={
    "Abid":{"Math": 90, "Physics": 85, "Biology": 88},
    "Nihal":{"Math": 75, "Physics": 80, "Biology": 78},
    "Arohi":{"Math": 82, "Physics": 90, "Biology": 91}
}
total_mark=[]

for i,(names,marks) in enumerate(name.items(),start=1):
    print(f"{i}.{names}")
    markss=0
    for subject,mark in marks.items(): 
        print(f"{subject}:{mark}")
        markss=markss+mark

    avg=markss/3
    print(f"Avg marks of {names}'s is: {(avg)}")
    
    print("\n")
    print("-"*20)

print("Students who scored above 80 in Math:")

for student,subjects in name.items():
    if subjects["Math"]>80:
        print(f"{student}")

name["Nihal"]["Biology"]=90
print("\n Updated Nihal's Biology Mark to 90.\n")

del name["Arohi"]
print("Deleted Arohi from database.")

print("Final list after update:")

for i,(name,subject) in enumerate(name.items(),start=1):
    print(f"{i}. {name}")

    for subjes,mark in subject.items():
        print(f"{subjes}: {mark}")

    print("\n")
    print("-"*40)
   



    