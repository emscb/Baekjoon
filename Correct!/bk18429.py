def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)


def choice(day, list, history):
    ret = []
    sum = 0
    for h in history:
        sum += h

    for l in list:
        if sum + l >= K * (day+1):
            history_new = history + [l]
            list_new = list.copy()
            list_new.remove(l)
            ret.append((day+1, list_new, history_new))
            # print(ret)
    return ret


N, K = map(int, input().split())
Ns = input().split()
Ns = [int(x) for x in Ns]
Ns.sort()
Nset = set(Ns)
Nd = {}
for n in Nset:
    Nd[n] = Ns.count(n)

ans = []
count = 0
# print(N, K, Ns)
# print(Nd)
# 모두가 K보다 크면 모든 경우가 가능
if min(Ns) >= K:
    count = fac(N)
else:
    ans.append((0, Ns, []))
    while 1:
        ans2 = []
        for a in ans:
            if a[0] != N:
                ans2 += choice(a[0], a[1], a[2])
                # print(ans2)
            else:
                ans2.append(a)
        if ans2 == ans:
            break
        ans = ans2.copy()

if count == 0:
    print(len(ans))
else:
    print(count)
