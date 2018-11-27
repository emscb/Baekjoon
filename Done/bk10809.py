import re

a = ord('a')
z = a+25
S = input()
D = {}
for i in range(a,z+1):
    try:
        r = re.search(chr(i), S).start()
    except AttributeError:
        D[chr(i)] = -1
    else:
        D[chr(i)] = r
ans = ''
for j in D.keys():
    ans += str(D[j]) + ' '
print(ans.strip())

# Done