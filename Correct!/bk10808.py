import re

A = input()
ans = []

for i in range(ord('a'), ord('z') + 1):
    n = len(re.findall(chr(i), A))
    ans.append(n)

for k in ans:
    print(k, end=' ')

# Done
