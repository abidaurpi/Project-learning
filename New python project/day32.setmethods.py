s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))

print(s1,s2)

s1.update(s2)
print("Updated s1:")
print(s1,s2)

cities = {"Tokyo", "Madrid","Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul","Kabul", "Madrid"}

cities3=cities.intersection(cities2)
print(cities3 )
cities.intersection_update(cities2)
print("Updated Cities:")
print(cities)

cities3 = {"Tokyo", "Madrid","Berlin", "Delhi"}
cities4 = {"Tokyo", "Seoul","Kabul", "Madrid"}
cities5=cities3.symmetric_difference(cities4)
print("Symmetric difference: ")
print(cities5)

cities6 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities7 = {"Seoul", "Kabul", "Delhi","Berlin"}
cities8=cities6.difference(cities7)
print(cities8) #cities 7 er extra uncommon element gula kintu print hobe na

cities9 = {"Tokyo2", "Madrid2", "Berlin",
"Delhi"}
cities10 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities9. isdisjoint(cities10))

cities11 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities12= {"Seoul", "Kabul"}
print(cities11. issuperset(cities12) )
cities13 = { "Tokyo", "Madrid", "Delhi"}
print( cities11. issuperset( cities13) )
print( cities13. issubset( cities11) )

cities = {"Tokyo", "Madrid",
"Berlin", "Delhi"}
cities. add( "Helsinki")
print(cities)


cities = {"Tokyo", "Madrid", "Berlin",
"Delhi"}
cities. remove( "Tokyo" )
print(cities)

cities = {"Tokyo", "Madrid", "Berlin",
"Delhi"}
item = cities. pop( )
print(cities)
print(item)


cities15 = {"Tokyo", "Madrid", "Berlin",
"Delhi"}
del cities15

cities16 = {"Tokyo", "Madrid", "Berlin",
"Delhi"}
cities16.clear()
print(cities16)

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print ("Carla is present. ")
else:
    print("Carla is absent. ")




