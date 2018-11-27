N = int(input())
for i in range(N):
    a = input().split()
    r, s = int(a[0]), a[1]
    ans = ''
    for k in s:
        ans += k*r
    print(ans)

# Done