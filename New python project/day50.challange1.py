contact_dict={}

def add_contact():
    prompts=["Enter name:",
             "Enter phone number:"]
    entries=[]
    for i in range(len(prompts)):
        entry=input(prompts[i]).strip()

        if i==0:
            if not entry.replace(" ","").isalpha():
                print("Invalid Name. Name should contain only alphabets.")
                return
            name=entry.title()

        else:

            if not entry.isdigit() or not entry.startswith("01") or len(entry)!=11:
                print("Invalid phone number. Must start with '01' and be 11v digits.")
                return
            
            number=entry
        
    contact_dict[name]={
        "Number": number
    }

    print(f"{name}'s number is added successfully.\n")       


def search_contact():
    name= input("Enter the name you want to search:").strip().title()
    if name in contact_dict:
        print(f"{name}'s number is: {contact_dict[name]['Number']}")
    else:
        print("Not found")

def show_numbers():
    if not contact_dict:
        print("No number is found")
        return
    print("\nAll Contact list")
    print("-"*40)
    for i,(name,number) in enumerate(contact_dict.items(),start=1):
        print(f"{i}.{name}:{number['Number']}")
    


while True:
    print("Welcome to Phonebook Pro!!!")
    a=int(input("""
            1. Add Contact
            2. Search Contact
            3. Show All Contacts
            4. Exit
            what do you want to do?
"""))
    if a==1:
        add_contact()
    elif a==2:
        search_contact()
    elif a==3:
        show_numbers() 
    else:
        break
