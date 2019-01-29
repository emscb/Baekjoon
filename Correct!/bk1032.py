N = int(input())
lst = []
ans = ''

for _ in range(N):
    lst.append(input())

l = len(lst[0])

for i in range(l):
    st = lst[0][i]
    for j in lst:
        if st == j[i]:
            continue
        else:
            ans += '?'
            st = ''
            break
    if st != '':
        ans += st
print(ans)

# Done
