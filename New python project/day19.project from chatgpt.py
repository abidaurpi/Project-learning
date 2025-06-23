a=input("Please enter an input(Paragraph): ")
while True:
    print("""What do you want to do?
    1. Count total characters (excluding spaces)
    2. Count total vowels and consonants
    3. Reverse the sentence
    4. Extract substring using slicing
    5. Convert to UPPERCASE/lowercase/title case
    6. Remove spaces or count words
    7. Exit""")
    b=int(input("What do you want to do?(Please select the corresponding number.)"))
    match b:
        case 1:
            x1=a.count(" ")
            print(f"Number of spaces in your paragraph: {a.count(" ")}")
            print(f"Total characters are in your paragraph(Excluding spaces): {int(len(a)-x1)}")
        case 2:
            count=0
            numcount=0
            numcons=0
            for i in a:
                #print(i, end="") # end="" diye dile input er moto kore ekline e string er moto kore output dey
                #if (i=="a" or "e" or "i" or "o" or "u" or "A" OR "E" OR "I" OR "O" OR "U"):
                if i in "aeiouAEIOU":
                    count+=1

                elif i.isdigit():
                    numcount+=1
            
                elif i.isalpha(): #isalpha kintu vowel o count kore. but ekhane just consonant gula count korse karon age vowel count hoye gese. ekhane main kotha hocche order matters. age jodi vowel count na kore isalpha diye consonant count korte caitam tahole output wrong ashto.
                    numcons+=1
            print(f"Total vowels are: {count}")
            print(f"Total numbers are: {numcount}")
            print(f"Total consonants are: {numcons}")
        
        # case 3:
        #     x2= len(a)
        #     for i in range(len(a)):
        #         x2-=1
        #         print(x2, end="")

        case 4:
            a1=int(input("Enter the starting postion of your slicing the text: "))
            b1=int(input("Enter the ending postion of your slicing the text: "))
            if (a1<b1):
                print("The starting index should be less than ending index")
            elif(a1==b1):
                print("The starting index should be less than ending index")
            print(f"Your text is: {a}")
            print(a[a1:b1])


                


                
                

        