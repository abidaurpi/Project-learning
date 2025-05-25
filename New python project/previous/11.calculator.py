num1= input("enter the first number: ")
a= input("Enter the operation method(+-*/%) ")
num2= input("Enter the second number: ")


if a=='+':
    print(int(num1)+int(num2))
elif a=='-':
    print(int(num1)-int(num2))
elif a=='*':
    print(int(num1)*int(num2))
elif a=='/':
    print(int(num1)/int(num2))
elif a=='%':
    print(int(num1)%int(num2))
else:
    print("This calculator can't proceed")