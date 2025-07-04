students={}
def add_student():
    prompts=[
        "Enter student name:",
        "Math:",
        "Physics:",
        "Biology:"
    ]

    total_data_set=[]

    for i in range(len(prompts)):
        data=input(prompts[i])
        if i==0:
            if not data.replace(" ", "").isalpha():
                print("Invalid input of names. It should contain only alphabets.")

            name=data
        #students=name
        else:
            try:
                mark=int(data)
                if mark<0 or mark>100:
                    raise ValueError
            except ValueError:
                print("Number should be between 0 to 100.")
            
            total_data_set.append(mark)

    students[name]={
        "Math:": total_data_set[0],
        "Physics:": total_data_set[1],
        "Biology:": total_data_set[2],
    }
    print(f"Student name:{name} added successfully." )

def show_all_students():
    for i,(name,marks) in enumerate(students.items(),start=1):
        print(f"{i}.{name}")
        total=0
        for subject,mark in marks.items():
            print(f"{subject}: {mark}")
            total+=mark
        avg=total/3

        print(f"Average: {avg:.2f}")
        print("-"*20)

def top_3_students():
    score_list=[]
    for name, marks in students.items():
        total=sum(marks.values())
        score_list.append((name,total))        

    score_list.sort(key=lambda x:x[1],reverse=True)
    
    print("\n Top 3 students: ")
    for i,(name,total) in enumerate(score_list[:3],start=1):
        print(f"{i}. {name} (Total Marks: {total})")
    print()      
    
while True:
    a=int(input("""
Welcome to Student Rank Manager!
1. Add Student
2. Show All Students
3. Show Top 3 Students
4. Exit
Add the number:

"""))
    if a==1:
        add_student()
    elif a==2:
        show_all_students()
    elif a==3:
        top_3_students()
    else:
        break

         




