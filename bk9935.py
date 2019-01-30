import re

A = input()
ptrn = input()

ans = ''
s = 0
e = 999999
anse = ''
while 1:
    s = A.find(ptrn[0])
    if s == -1: break
    F = re.findall('[' + ptrn[0] + ptrn[1] + ']', A[s+1]) == []
    if F:
        s = A[2:].find(ptrn[0]) + 2

    if A[::-1].find(ptrn[-1]) == -1: break
    e = len(A) - A[::-1].find(ptrn[-1]) - 1
    F2 = re.findall('[' + ptrn[-1] + ptrn[-2] + ']', A[e-1]) == []
    if F2:
        e = len(A[:-2]) - A[:-2][::-1].find(ptrn[-1]) - 1

    ans += A[0:s]
    anse = A[e+1:] + anse
    A = A[s:e+1]
    A = A.replace(ptrn, '')
    if A.find(ptrn) == -1: break
ans = ans + A + anse

if ans == '':
    print("FRULA")
else:
    print(ans)

# 시간 초과
