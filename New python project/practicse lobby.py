# # name = "Abhishek hossain"

# # for i in name:
# #     print(i, end="")  # print without newline
  
x="dsdj fflkj"
# # reverse=x[ : : -1]
# # print(reverse)
# reverse=""
# for char in x:
#     reverse= char+ reverse
# print(reverse)
i= len(x)-1
reverse=""
while i>=0:
    reverse= reverse + x[i]
    i-=1
print(reverse)