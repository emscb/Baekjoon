import re

A = input()
ans = ""
ans += A[0]

a = re.findall("-(\w)", A)
for i in a:
    ans += i
print(ans)

# Done
