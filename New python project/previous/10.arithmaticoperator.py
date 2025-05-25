print(5+8)
print(5-8)
print(5*8)
print(5/8)
print(5//8)#duita divide sign deoar jonno decimal part ta remove hoye jay mane integer number print kore
print(5%2)
print(5**2)#power operator
#i=0
#i=i+2
#i+=2
#i-=2
#i*=2
#i*=2

#operator precedence
result= 2+ 3*5
print(result)#python BODMAS follow kore

#comparison operator
print(3>2)#ei operator boolean value return kore
print(3>=2)
print(3==2)
print(3!=2)

#logical operator
print(2>3 or 2>1)
print(2>1 and 4>5)
print(not 2>3)#not operator true ke false ar false ke true kore dey

#if else statement
age =4

if age>=18:#python e colon use kora hoy ei bujhanor jonno je colon er por ja ja likha hobe ta oi if er under e ekta block of statement
    print("you are an adult")
    print("You can vote")#if er under e ki ki statement ache ta bujhbo intendation (TAB) er maddhome
elif age<18 and age>3:#elif=elseif
    print("You are in school")
else:
    print("You are a child")
