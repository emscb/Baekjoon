t = int(input())
T = input().split()
A = []
for a in T:
    A.append(int(a))
print(str(min(A)) + " " + str(max(A)))