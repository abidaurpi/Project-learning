countries=("Spain","Italy", "India","England","Germany")
temp=list(countries)
temp.append("Russia")  #add item
temp.pop(3)            #remove item
temp[2]="Finland"      #change item
countries=tuple(temp)
print(countries)

#concatenation
countries = ("Pakistan", "Afghanistan","Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China" )
southEastAsia = countries + countries2
print(southEastAsia)


#count method

tuple1=(0,1,2,3,2,3,1,31,2,64)
res=tuple1.count(3)
print('COunt of 3 in tuple 1 is:', res)
#index method
res1 = tuple1. index(31)
print( 'Index of 31 in tuple1 is: ', res1)

res1 = tuple1. index(64, 4, 8)
print( 'Count of 3 in tuple1 is: ', res1)

