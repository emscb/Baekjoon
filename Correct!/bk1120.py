def diff(A, B):
    l = len(A)
    n = 0
    for i in range(l):
        if A[i] != B[i]:
            n += 1
    return n


AB = input()
A, B = AB.split()[0], AB.split()[1]
d = len(A)
for i in range(len(B) - len(A) + 1):
    d2 = diff(A, B[i:i + len(A)])
    if d2 < d:
        d = d2
print(d)

# Done
