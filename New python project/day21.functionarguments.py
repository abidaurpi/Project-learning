# There are four types of arguments that we can provide in a function:
# . Default Arguments
# . Keyword Arguments
# · Variable length Arguments
# . Required Arguments


def average(a=9,b=1):# eta defult argument
    print("The average value: ", (a+b)/2)

average(1,5)# default argument jai thakuk na keno, je value diyye function call kora hobe shei value diyei execute hobe

def average1(a=9,b=1):
    print("The average value: ", (a+b)/2)

average1(5)#ekhane a=5,b=1 hobe..

def average1(a=9,b=1):
    print("The average value: ", (a+b)/2)

average1(b=9)#ekhane a=9,b=9 hobe..

def name(fname, mname = "Jhon", lname ="Whatson"):
    print( "Hello,", fname, mname, lname)
name ("Amy")

def name( fname, mname = "Jhon", lname ="Whatson" ):
    print( "Hello,", fname, mname, lname)
name( "Amy", "Agarwal")

#keyword argument
def average(a=9, b=1):
    print("The average is ", (a+b)/2)
average(b=9, a=21)

def average3(*numbers):#argument as a tuple
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is: ", sum/len(numbers))
average3(5,6,6,2,5,7,4,2342)

def name(**name): #argument as dictionary
    print(type(name))
    print( "Hello, ", name[ "fname"],
name [ "mname" ], name[ "lname"] )
name(mname = "Buchanan", lname = "Barnes",
fname = "James" )

