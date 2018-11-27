N = int(input())
for i in range(N):
    a = input().split('X')
    score = 0
    for i in a:
        if i == '':
            pass
        else:
            b = len(i)
            score += b*(b+1)/2
    print(int(score))

# Done