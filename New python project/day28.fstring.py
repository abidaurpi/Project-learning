letter = "Hey my name is {1} and I am from {0}"
country="India"
name = "Harry"
print(letter.format(country, name))

print(f"Hey my name is {name} and I am from {country}")

price=49.25456
txt=f"For only {price: .2f} dollars!!"
print(type(txt))
print(txt)

print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}" )
