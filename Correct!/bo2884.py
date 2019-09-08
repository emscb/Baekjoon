h, m = map(int, input().split())
if m - 45 < 0:
    m = m - 45 + 60
    h -= 1
else:
    m -= 45

if h < 0:
    h += 24

print(str(h) + " " + str(m))