#MAP
def cube(x):
  return x * x * x
print(cube(2))

l = [1, 2, 4, 6, 4, 3]
# newl = []
# for item in l:
#   newl.append(cube(item))

newl=list(map(cube,l))

newl = list(map(lambda x: x*x*x, l))
print(newl)

#FILTER

def filter_function(a):
  return a>3

newnewl=list(filter(filter_function, l))
print(newnewl)





from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
# def mysum(x,y):
#   return x+y #etai lamba function e likha ase

sum = reduce(lambda x, y: x + y, numbers)

# Print the sum
print(sum)