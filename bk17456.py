import re


def score(n):
    notes = bin(n)[2:]
    ones = re.findall("1+", notes)
    score = 0
    for o in ones:
        score += len(o)**2
    return score


N = int(input())
for _ in range(N):
    rank = 1
    a, b, c = map(int, input().split())
    cs = score(c)
    for i in range(a, b+1):
        if score(i) > cs:
            rank += 1
    print(rank)
