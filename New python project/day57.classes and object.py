class Person:
    name="Harry"
    occupation="Software Developer."
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person()
b=Person()

a.name="Shubham"
a.occupation="Accountant"

b.name="Nitika"
b.occupation="Accountant"
a.info()
b.info()