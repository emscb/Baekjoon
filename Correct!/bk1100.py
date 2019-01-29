phan = [[0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0],
        [0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0]]
for x in range(8):
    l = input()
    for y in range(8):
        if l[y] == 'F':
            phan[x][y] += 1

ans = 0
for x in range(8):
    for y in range(8):
        if phan[x][y] == 1:
            ans += 1
print(ans)

# Done
