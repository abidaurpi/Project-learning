a=int(input("""Enter any value between 5 and 9.Type \"quit" to quit: """))
if(str(a)=="quit"):
    print("You are quiting.")
elif(int(a)<5 or int(a)>9):
    raise ValueError("Value should be between 5 and 9")
else:
    print(a)
5