# def titanic_sinking():
#     name= input("Who was in the Titanic? ")
#     sink=int(input("Which year is it currently?"))
#     sink2=sink-1912
#     print(name+ " were on the Titanic, which sunk "+str(sink2)+" years ago.")
# titanic_sinking()

name= input("Who was in the Titanic? ")
year=input("What year is currently? ")

def titanic_sinking(name,year):
    sink=int(year)-1912
    print(name+" were on the titanic, which sunk "+str(sink)+ " years ago")
titanic_sinking(name,year)


#duitai same output dey..2nd code tay parameter use kora hoise
 