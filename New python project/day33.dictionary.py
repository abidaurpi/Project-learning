dic= {
    "Harry": "Human being",
    "Spoon": "Object"
}

print(dic["Harry"])

info = {'name' : 'Karan', 'age' : 19, 'eligible' : True}
print(info)
print(info['name']) #name2 dile eta error o/p asto.. jodi error ante cai tahole ei syntax use korte hobe
print(info.get('name')) #name2 dile "None" o/p asto.. jodi error na ante cai tahole ei syntax use korte hobe
print("\n")
print("Printing keys:")
print(info.keys())
print("Printing values:")
print(info.values())

print("\n")
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")
print("\n")

print(info.items())

print("\n")

for key,value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
    