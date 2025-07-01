def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)

print(factorial(3))
print(factorial(4))
print(factorial(5))

m=int(input("Please enter the sequence number: "))
def fibo(m):
    if(m==0):
        return 0
    elif(m==1):
        return 1
    else:
        return fibo(m-1)+fibo(m-2)
    
print(fibo(m))