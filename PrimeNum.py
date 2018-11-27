def primes(n:int):
    fir = [False, False] + [True] * (n-1)
    for k, l in enumerate(fir):
        if l:
            if (n+1-2*k) % k == 0:
                fir[2 * k::k] = [False] * ((n + 1 - 2 * k) // k)
            else:
                fir[2 * k::k] = [False] * ((n + 1 - 2 * k) // k + 1)
    return [x for x, y in enumerate(fir) if y]

m, n = input().split()
m=int(m)
n=int(n)
ans=0
p = primes(1000000)

for i in range(n-m+1):
    x = m+i
    a = 0
    while(1):
        k = p[a] ** 2
        if x < k:
            ans+=1
            break
        elif x % k == 0:
            break
        else:
            a+=1


print(ans)