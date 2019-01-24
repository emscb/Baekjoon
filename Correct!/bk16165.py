N, M = input().split()
N = int(N)
M = int(M)

all = {}


for _ in range(N):
    group = input()
    member = int(input())
    member_list = []
    for _ in range(member):
        member_list.append(input())
    member_list = sorted(member_list)
    member_list = [group] + member_list
    all[group] = member_list

for _ in range(M):
    Q = input()
    Qn = int(input())
    if Qn == 0:
        for i in range(1, len(all[Q])):
            print(all[Q][i])
    elif Qn == 1:
        for v in all.values():
            if Q in v:
                print(v[0]); break

# Done