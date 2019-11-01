N = int(input())
n = 0
if N % 5 == 0:
    print(N // 5)
else:
    if N % 3 == 0:
        f = N // 3
        n += 1
        N -= 5
        while N % 3 != 0 and N > 0:
            n += 1
            N -= 5
        if N < 0:
            print(f); exit(0)
        else:

        n += N // 3
        print(n)
    else:
        while N % 3 != 0 and N > 0:
            n += 1
            N -= 5
        n += N // 3
        if N < 0:
            print(-1); exit(-1)
        print(n)
