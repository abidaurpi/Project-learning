while True:
    a=input("""Do you want to Code or Decode. 
            Write "code" if you want to code.
            Write "decode" if you want to decode: """)
    if(a!="code" and a!="decode"):
        print("Invallid text. Please write it again.")
    else:
        if(a=="code"):
            m=input("Enter you message: ")
            print(f"Total words in your message: {len(m.split())}")
            x=m.split()
            #shortword=""
            message=" "
            for i in x:
                if len(i)<=2:
                    #shortword=i[: : -1]
                    #message=message+shortword+ " "
                    message=message+ i +" "
                    
                else:
                    p="Halum"
                    q="mew"
                    slice1=i[1: ]
                    coded=p+slice1+i[0]+q
                    message=message+coded+" "

            print("your coded message:")
            message=message.strip()
            reversed_message=message[ : : -1]   
            print(reversed_message)
        
        elif(a=="decode"):
            m=input("Enter you message: ")
            original_code=m[ : : -1]
            x=original_code.split()
            message=""
            for i in x:
                if len(i)<=2:
                    message=message+ i +" "
                else:
                    z=i[5:-3]
                    l=z[: -1]
                    #print(z[len(z)-1])
                    decoded=z[-1]+z[ : -1]
                    message=message+decoded+" "
            print("your decoded message:")
            message=message.strip()
           
            print(message)

            #done and dusted!!!!!!!


            

            
