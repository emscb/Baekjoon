import re

cro = {"c=" : '1', "c-" : '2', "dz=" : '3', "d-" : '4', "lj" : '5', "nj" : '6', "s=" : '7',
       "z=" : '8'}

A = input()
for i in cro.keys():
    A = re.sub(i, cro[i], A)
print(len(A))

# Done
