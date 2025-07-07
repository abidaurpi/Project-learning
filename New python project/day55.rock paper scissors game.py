
def play_game_rock():

    import random
    a=[1, 2, 3]
    #b=[1, 2, 3]
    c=int(random.choice(a))
    #d=["Rock","Paper","Scissors"]
     
    if c==1:
        print("Your opponent choose Rock")
        print("Its draw")
    elif c==2:
        print("Your opponent choose Paper.")
        print("You loose")
    else:
        print("Your opponent choose Scissors.")
        print("Its Win")
def play_game_paper():

    import random
    a=[1, 2, 3]
    #b=[1, 2, 3]
    c=int(random.choice(a))
    #d=["Rock","Paper","Scissors"]
     
    if c==1:
        print("Your opponent choose Rock")
        print("Its Win")
    elif c==2:
        print("Your opponent choose Paper.")
        print("You Draw")
    else:
        print("Your opponent choose Scissors.")
        print("Its Loose")
def play_game_Scissors():

    import random
    a=[1, 2, 3]
    #b=[1, 2, 3]
    c=int(random.choice(a))
    #d=["Rock","Paper","Scissors"]
     
    if c==1:
        print("Your opponent choose Rock")
        print("You loose")
    elif c==2:
        print("Your opponent choose Paper.")
        print("You Win")
    else:
        print("Your opponent choose Scissors.")
        print("Its Draw")
    

    
while True:
   a=int(input("""What do you want to play",
   "1. Rock " 
   "2. Paper" 
   "3. Scissors
    "4.exit"
    Enter the number:"""))
   if a==1:
       play_game_rock()
   elif a==2:
       play_game_paper()
   elif a==3:
       play_game_Scissors()
   else:
       break