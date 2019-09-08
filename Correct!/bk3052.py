N = []
T = []
for _ in range(10):
    N.append(int(input()))
for n in N:
    T.append(n % 42)
T = set(T)
print(len(T))
