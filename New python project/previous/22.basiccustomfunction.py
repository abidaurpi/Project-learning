name= input("What is his name? ")
age=input("What is "+name+"'s age? ")

def age_in_one_year(name,age):
    age_next_year=int(age)+1
    print("In one year, "+name+" will be "+str(age_next_year)+" years old.")

age_in_one_year(name,age)
#age_in_one_year(age,name)#correct order e thakte hobe..ei line run korbe na..error dekhabe
age_in_one_year(age="51",name="Chris")#evabe define kore dile order maintain na korleo hobe
age_in_one_year("Chrise",51)
#age_in_one_year(str(51),"Chrise") ..........ei line tao bhul