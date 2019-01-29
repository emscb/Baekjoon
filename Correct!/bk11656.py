A = input()
ans2 = []
ans = []
A = A[::-1]
for i in range(len(A)+1):
    ans2.append(A[0:i])

for i in ans2:
    ans.append(i[::-1])

ans.sort()
for i in ans:
    if i != '':
        print(i)

# Done
