# 사람의 수 N과 파티의 수 M
a = input()
N, M = int(a.split()[0]), int(a.split()[1])
truth = input().split()[1:]
truth = set(truth)
ans = 0
partyList = []
for i in range(M):
    party = input().split()
    partyList.append(party)
# partyList.sort(key=lambda row:row[0], reverse=True)
for l in partyList:
    appendence = l[1:]
    if list(truth & set(appendence)) != []:
        truth = truth | set(appendence)
for l2 in partyList:
    app2 = l2[1:]
    if list(truth & set(app2)) == []:
        ans += 1
print(ans)
