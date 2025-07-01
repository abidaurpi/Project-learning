ep1 = { 122:45, 123: 89,567:69, 670:69}
ep2= {222:67, 566:90}

ep1.update(ep2)
print(ep1)

ep1.clear()
print(ep1)

empt={}
print(empt)


ep3 = { 122:45, 123: 89,567:69, 670:69}
ep3.pop(122)

print(ep3)

ep3.popitem()
print(ep3)

#del ep3
del ep3[123]
print(ep3)
