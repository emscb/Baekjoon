N = int(input())
light = [] # List of tuple (spotlight)
for i in range(N):
    xn, yn = input().split()
    xn = int(xn)
    yn = int(yn)
    light.append((xn,yn))

P = int(input())
spot = [] # List of tuple (spot)
spotlight = [] # light weight
for i in range(P):
    xp, yp = input().split()
    xp = int(xp)
    yp = int(yp)
    spot.append((xp,yp))
    spotlight.append(0)

# Compare

for i in range(len(light)):
    xl = light[i][0]
    yl = light[i][1]
    for j in range(len(spot)):
        xs = spot[j][0]
        ys = spot[j][1]

        if ys < yl: continue
        elif ys == yl and xs == xl: spotlight[j]+=1
