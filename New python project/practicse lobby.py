# # # name = "Abhishek hossain"

# # # for i in name:
# # #     print(i, end="")  # print without newline
  
# # x="dsdj fflkj"
# # # reverse=x[ : : -1]
# # # print(reverse)
# # reverse=""
# # for char in x:
# #     reverse= char+ reverse
# # print(reverse)
# # i= len(x)-1
# # reverse=""
# # while i>=0:
# #     reverse= reverse + x[i]
# #     i-=1
# # print(reverse)
# # a=input("Enter your paragraph:")
# # print(a)
# # reverse=""
# # for i in a:
# #     reverse=i+ reverse
# # print(reverse)


# # a=input("Enter your paragraph:")
# # b=a.rsplit()
# # l="mew"
# # k="sfd"
# # print(type(b))
# # for i in b:
# #     m=i[1: ]
# #     print(l+m+i[0]+k,end=" ")

# # print("\n")
# # x11="is nuefefdf fdgfdgm"
# # x12=x11.split()
# # print(len(x12))

# # while True:
# #     a = input("""Do you want to Code or Decode? 
# # Write "code" if you want to code.
# # Write "decode" if you want to decode: """)

# #     if a != "code" and a != "decode":
# #         print("Invalid text. Please write it again.")
# #     else:
# #         if a == "code":
# #             m = input("Enter your message: ")
# #             print(f"Total words in your message: {len(m.split())}")
# #             x = m.split()
# #             message = ""

# #             for word in x:
# #                 if len(word) <= 2:
# #                     shortword = word[::-1]
# #                     message += shortword + " "
# #                 else:
# #                     p = "Halum"
# #                     q = "mew"
# #                     slice1 = word[1:]
# #                     coded = p + slice1 + word[0] + q
# #                     message += coded + " "
            
# #             print("Your coded message:")
# #             print(message.strip())

# # while True:
# #     a = input("""Do you want to Code or Decode? 
# # Write "code" if you want to code.
# # Write "decode" if you want to decode: """)

# #     if a != "code" and a != "decode":
# #         print("Invalid text. Please write it again.")
# #     else:
# #         if a == "code":
# #             m = input("Enter your message: ")
# #             print(f"Total words in your message: {len(m.split())}")
# #             x = m.split()
# #             message = ""

# #             for i in x:
# #                 if len(i) <= 2:
# #                     message += i[::-1] + " "
# #                 else:
# #                     p = "Halum"
# #                     q = "mew"
# #                     slice1 = i[1:]
# #                     coded = p + slice1 + i[0] + q
# #                     message += coded + " "

# #             message = message.strip()
# #             reversed_message = message[::-1]
# #             print("Your coded message:")
# #             print(reversed_message)

# #         elif a == "decode":
# #             m = input("Enter your coded message (reversed): ")

# #             # Step 1: Reverse back the entire message first
# #             original_coded = m[::-1]

# #             x = original_coded.split()
# #             message = ""

# #             for i in x:
# #                 if len(i) <= 2:
# #                     message += i[::-1] + " "
# #                 else:
# #                     z = i[5:-3]
# #                     decoded = z[-1] + z[:-1]
# #                     message += decoded + " "

# #             message = message.strip()
# # #             print("Your decoded message:
# # while True:
# #     a = int(input("""
# #             Welcome to Student Result Analyzer!
# #             1. Add student
# #             2. Show student reports
# #             3. Save results to file
# #             4. Load results from file
# #             5. Exit
# #                 Enter your number: """))

# #     if a == 1:
# #         def add_student():
# #             prompts = [
# #                 "Enter student name: ",
# #                 "Enter marks in Math: ",
# #                 "Enter marks in Physics: ",
# #                 "Enter marks in Biology: "
# #             ]
            
# #             entries = []

# #             for i in range(len(prompts)):
# #                 entry = input(prompts[i])
# #                 if i == 0:  # Name field
# #                     if not entry.isalpha():
# #                         print("Invalid name. Name cannot be a number.")
# #                        #return

# #                 if i > 0:  # For marks only
# #                     try:
# #                         mark = int(entry)
# #                         if mark < 0 or mark > 100:
# #                             raise ValueError("The number should be between 0 and 100.")
# #                     except ValueError:
# #                         print("Invalid input. Marks must be numbers between 0 and 100.")
# #                         return
# #                 entries.append(entry)

# #             with open("student_entry_file.txt", 'a') as f:
# #                 f.write(', '.join(entries) + "\n")

# #         add_student()  # ✅ Function is called here

# #     elif a == 5:
# #         print("Exiting program...")
# #         break

# students_dict = {}  # Global dictionary to store student data in memory

# def add_student():
#     prompts = ["Enter student name: ",
#                "Enter marks in Math: ",
#                "Enter marks in Physics: ",
#                "Enter marks in Biology: "]

#     entries = []

#     for i in range(len(prompts)):
#         entry = input(prompts[i]).strip().title()

#         if i == 0:
#             if not entry.replace(" ", "").isalpha():
#                 print(" Invalid name. Name should only contain letters.")
#                 return
#             name = entry
#         else:
#             try:
#                 mark = int(entry)
#                 if mark < 0 or mark > 100:
#                     raise ValueError
#             except ValueError:
#                 print("❌ Marks must be between 0 and 100.")
#                 return
#             entries.append(mark)

#     # Add to in-memory dictionary
#     students_dict[name] = {
#         "Math": entries[0],
#         "Physics": entries[1],
#         "Biology": entries[2]
#     }
#     print(f"✅ Student '{name}' added successfully.\n")


# def calculate_average(marks):
#     return sum(marks) / len(marks)


# def calculate_grade(avg):
#     if avg >= 90:
#         return "A"
#     elif avg >= 80:
#         return "B"
#     elif avg >= 70:
#         return "C"
#     else:
#         return "F"


# def show_all_reports():
#     if not students_dict:
#         print("❌ No student data loaded in memory.\n")
#         return

#     print("\n📋 Student Reports:")
#     print("-" * 40)

#     for i, (name, subjects) in enumerate(students_dict.items(), start=1):
#         print(f"{i}. {name}")
#         for subject, mark in subjects.items():
#             print(f"   {subject}: {mark}")
#         marks = list(subjects.values())
#         avg = calculate_average(marks)
#         grade = calculate_grade(avg)
#         print(f"   Average: {avg:.2f}")
#         print(f"   Grade: {grade}")
#         print("-" * 40)


# def save_results_to_file():
#     if not students_dict:
#         print("❌ No student data in memory to save.")
#         return

#     with open("Student_marks.txt", "w") as f:
#         for name, marks in students_dict.items():
#             line = [name] + [str(m) for m in marks.values()]
#             f.write(", ".join(line) + "\n")
#     print("✅ All student data saved to 'Student_marks.txt'\n")


# def load_results_from_file():
#     try:
#         with open("Student_marks.txt", "r") as f:
#             for line in f:
#                 split = line.strip().split(", ")
#                 name = split[0]
#                 marks = list(map(int, split[1:]))
#                 students_dict[name] = {
#                     "Math": marks[0],
#                     "Physics": marks[1],
#                     "Biology": marks[2]
#                 }
#         print("✅ Student data loaded from file successfully.\n")
#     except FileNotFoundError:
#         print("❌ File not found. Add and save students first.\n")


# # ---------------- MAIN LOOP ----------------

# while True:
#     try:
#         a = int(input("""
# Welcome to Student Result Analyzer!
# 1. Add student
# 2. Show student reports
# 3. Save results to file
# 4. Load results from file
# 5. Exit
# Enter your number: """))

#         if a == 1:
#             add_student()

#         elif a == 2:
#             show_all_reports()

#         elif a == 3:
#             save_results_to_file()

#         elif a == 4:
#             load_results_from_file()

#         elif a == 5:
#             print("👋 Exiting the program. Goodbye!")
#             break

#         else:
#             print("❌ Invalid option. Please select 1 to 5.\n")

#     except ValueError:
#         print("❌ Please enter a number (1 to 5).")

contact_dict={}
def add_contact():
    prompt=["Enter name:",
            "Enter phone number: "]
    entry=[]
    
    for i in range(len(prompt)):
        entries=input(prompt[i]).strip()

        if i==0:
            if not entries.replace(" ","").isalpha():
                print("Invalid Input of name.")
                return
            name=entries
        else:
            if not entries.isdigit() or not entries.startswith("01") or len(entries)!=11:
                    print("Invalid Number inputed.")
            
            number=entries


    contact_dict[name]={
        "Number": number , 
    }

    print(f"{name}'s contact number is successfully stored.")


add_contact()



