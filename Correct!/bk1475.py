import re

A = input()
A = A.replace('6', '9')

N = []
for i in range(ord('0'), ord('9')):
    N.append(len(re.findall(chr(i), A)))
N.append(len(re.findall('9', A)) / 2)

N.sort(reverse=True)

if N[0] % 1 == 0:
    print(int(N[0]))
else:
    print(int(N[0]+1))

# Done
