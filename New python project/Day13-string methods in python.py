#Strings immtable
a="Harry"
b="Harry..!!!" #b="Harry!!!..." eta dile rstrip("!") command e ! mark ta jay na.. etar solution hocche !. duitai rstrip("!.") use kora
c="!!!...Harry!!"
d="Harry!!.."
e="Harry"
f="Harry......Harry"
g="Harry !!!! Harry"
print(len(a))
print(a.upper())
print(a.lower())
print(b.rstrip("!"))
print(c.rstrip("!")) 
print(d.rstrip("!."))  # !. duita eksathe dile strip kore fele. 
print(e.replace("Harry", "John"))
print(f.replace("Harry", "John"))
print(g.split(" "))# #split function use kore string ke list e convert kora jabe,, ekhane space diye split kora hoyeche

blogheading="introduction to js"
blogheading2="intrOduCtion tO jS"
print(blogheading.capitalize())
print(blogheading2.capitalize())  #capitalize function use kore first letter capital kora hoyeche
print(blogheading.title())  #title function use kore shob gula word er first letter capital kora hoyeche

str1="Welcome to the Console!!"
print(str1.center(50))
print(len(str1))
print(len(str1.center(50)))#center function use kore string ke center e rakha hoyeche, ekhane 50 ta character er space deya hoyeche
print(f.count("Harry"))
print(g.count("r"))
print(str1.endswith("!!"))
print(str1.endswith("to",4,10))  #endswith function use kore check kora hoyeche je string er end e !! ache kina, second parameter diye index range set kora hoyeche
str2=" He's name is Dan. He is an honest man."
print(str2.find("is"))
print(str2.find("ishh"))
print(str2.index("is"))

print(str2.isalnum())  #isalnum function use kore check kora hoyeche je string er shob character alphanumeric kina
print(str2.islower())  #isalnum function use kore check kora hoyeche je string er shob character alphanumeric kina
str3=" He's name is Dan. He is an honest man.\n"
print(str3.isprintable())  #isprintable function use kore check kora hoyeche je string printable kina   
print(str3.isspace())  #isspace function use kore check kora hoyeche je string er shob character space kina
str4="      "
print(str4.isspace()) 
print(str1.istitle()) #false dekhabe karon str1 er shob word er first letter capital na
print(str2.swapcase())
print(str2.title())  #title function use kore shob word er first letter capital kora hoyeche)