N = int(input())
def distance(A,B):
    ans = ord(B) - ord(A)
    if ans < 0:
        ans += 26
    return ans



ans = []
for _ in range(N):
    AB = input()
    A, B = AB.split()[0], AB.split()[1]

    t = []
    for i in range(len(A)):
        t.append(distance(A[i], B[i]))
    ans.append(t)


for k in ans:
    a = ''
    for j in k:
        a += ' ' + str(j)
        a.strip()
    print("Distances:%s" % a)

# Done
