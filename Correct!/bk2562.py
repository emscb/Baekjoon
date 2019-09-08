a = []
for _ in range(9):
    a.append(int(input()))
m = max(a)
n = a.index(m)+1

print(m)
print(n)
