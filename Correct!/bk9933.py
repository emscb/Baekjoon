N = int(input())
D = {}

for _ in range(N):
    A = input()
    try:
        D[(len(A), A[len(A) // 2])].append(A)
    except KeyError:
        D[(len(A), A[len(A) // 2])] = []
        D[(len(A), A[len(A) // 2])].append(A)
for i in D.keys():
    lst = D[i]
    for k in range(len(lst)):
        let1 = lst[k]
        if let1 == let1[::-1]: # 자체 팰린드롬 생각하기
            print("%d %s" % (i[0], i[1])); break
        for let2 in lst[k+1:]:
            if let1 == let2[::-1]:
                print("%d %s" % (i[0], i[1])); break

# Done
