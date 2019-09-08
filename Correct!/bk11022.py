T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    print("Case #" + str(t+1) + ": " + str(a) + " + " + str(b) + " = " + str(a+b))
