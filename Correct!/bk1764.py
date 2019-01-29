NM = input()
N, M = int(NM.split()[0]), int(NM.split()[1])
dms = set([])
bms = set([])
for _ in range(N):
    dms.add(input())
for _ in range(M):
    bms.add(input())

dbms = dms & bms
dbms = list(dbms)

print(len(dbms))
dbms.sort()
for i in dbms:
    print(i)

# Done
