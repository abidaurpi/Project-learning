l = [11, 45, 1, 2, 4, 6,1,1]
print(1)
l.append(7)
l. sort(reverse=True)
l.reverse( )
print(l. index(1))
print(l.count(1) )
# m =l
# m[0] = 0
# print(l)  #ei method ta recommended na
m=l.copy()
m[0]=0
print(l)
print(m)

n=[100,55,885,454]
l.extend(n)
print(l)

k=n+m+l
print(k)