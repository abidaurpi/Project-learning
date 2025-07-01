# f=open('day49.txt', 'r')
# # print(f)
# text=f.read()
# print(text)
# f.close()

f=open('day49.txt', 'w')
f=open('day49.txt', 'a')
f.write('Hello, world!\n')
f.close() #close obosshoi korte hobe..

with open('day49.1.txt','a') as f:
    f.write("Hey. I am inside with.")