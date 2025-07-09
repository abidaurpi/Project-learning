student_dict={}
def add_student():
    prompt=["Student name:",
            "Math:",
            "Physics:",
            "Biology:"]
    entries=[]
    for i in range(len(prompt)):
        entry=input(prompt[i])

        if i==0:
            if not entry.replace(" ","").isalpha():
                print("Name should contain only alphabet.")
            name=entry
        else:
            try:
                mark=int(entry)
                if mark<0 or mark>100:
                    raise ValueError
            except ValueError:
                print("Marks should be in between 0 to 100.")
            entries.append(mark)
    
    student_dict[name]={
        "Math:":entries[0],
        "Physics:":entries[1],
        "Biology:":entries[2],
        
    }
    with open("self_practice_5.txt",'a') as f:
        for name,marks in student_dict.items():
            line=[name] +[str(m) for m in marks.values()]
            f.write(", ".join(line) +"\n")
            
def show_all_student():
    try:
        with open("self_practice_5.txt",'r') as f:
            lines=f.readlines()

            for i, line in enumerate(lines,start=1):
                parts=line.strip().split(", ")
                name=parts[0]
                marks=list(map(int, parts[1:]))
                avg=sum(marks)/len(marks)
                print(f"{i}.{name}")
                print(f"Math: {marks[0]}")
                print(f"Physics: {marks[1]}")
                print(f"Biology: {marks[2]}")
                print(f"Average: {avg:.2f}")
                print("-"*20)
    except FileNotFoundError:
        print("File not found.")

def search_student():
    name_to_find=input("Enter student name to serach:").strip().title()

    found=False
    try:
        with open("self_practice_5.txt",'r') as f:
            for line in f:
                parts=line.strip().split(", ")
                if name_to_find==parts[0]:
                    marks=list(map(int,parts[1:]))
                    avg=sum(marks)/len(marks)
                    print(f"{name_to_find}'s Record:")
                    print(f"Math: {marks[0]}")
                    print(f"Physics: {marks[1]}")
                    print(f"Biology: {marks[2]}")
                    print(f"Average: {avg:.2f}")
                    print("-"*20)

                    found=True
                    break

        if not found:
            print(f"{name_to_find} not found in the record.")
    except FileNotFoundError:
        print("File not found.")

def update_student():
    name_to_update=input("Enter the student name you want to update:").strip().title()
    updated_lines=[]
    found= False

    try:
        with open("self_practice_5.txt",'r') as f:
            lines=f.readlines()

        for line in lines:
            parts=line.strip().split(", ")
            name=parts[0]

            if name==name_to_update:
                print(f"\n{name} found. Enter new marks:")
                try:
                    math=int(input("New math mark: "))
                    physics=int(input("New Physics mark:"))
                    biology=int(input("New Biology mark:"))

                    if not (0 <=math <=100 and 0 <=physics <=100 and 0 <=biology <=100 ):
                        print("Marks should be between 0 to 100.")
                        return
                    
                    updated_line=f"{name}, {math}, {physics}, {biology}\n"
                    updated_lines.append(updated_line)

                    found=True
                except ValueError:
                    print("Invalid Input. Marks should be numbers.")
                    return
            
            else:
                updated_lines.append(line)

        if found:
            with open("self_practice_5.txt",'w') as f:
                f.writelines(updated_lines)
            print(f"{name_to_update}'s record updated successfully.")

        else:
            print(f"{name_to_update} not found.")

    except FileNotFoundError:
        print("File not found.")


while True:
    a=int(input("""Student File Manager:
1. Add Student
2. Show All Students
3. Search Student 
4. Update Student
5. Exit
Enter your choice
"""))       
    if a==1:
        add_student()
    elif a==2:
        show_all_student()
    elif a==3:
        search_student()
    elif a==4:
        update_student()
    else:
        break
                  



###