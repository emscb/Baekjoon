a = input().upper()
D = {}
for i in a:
    try:
        D[i] += 1
    except KeyError:
        D[i] = 1
d2 = list(D.items())
d2.sort(key=lambda x: x[1], reverse=True)
if len(d2) != 1:
    if d2[0][1] != d2[1][1]:
        print(d2[0][0])
    else:
        print("?")
else:
    print(d2[0][0])

# Done