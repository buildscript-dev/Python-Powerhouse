# List - to store multip data 
# of multiple data types
# also with the duplicates
# and mutable in nature. a = [123] to a = [456]

# Syntax: list
# variableName = [this list]
#
# Indexing - starts from 0 till the last-1.

import copy


s = [10,20,30,40,50]
print(s[2])
print(s[-2])
print(s[:3:1])

s = [12,15,15,169]
s[0] = 123
print(s)


# Deep Copy and # Shalow Copy

a = [10, 12, 13, 14]
b = a # reference copy


c = [10, 20 ,30, 40, 50]
d = c.copy() # shalow copy

c[3] = 400
print(c)
print(d)

e = [123, 345, 567, 789]
f = copy.deepcopy(e) # deep copy

e[0] = 000

print(e)
print(f)

# traversing the list

travList= [10, 20, 30, 40, 50]

for i in travList:
  print(travList)