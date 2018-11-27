# 다시 해야 합니다.
def count(l): # list내의 서로 다른 숫자의 수를 반환
    ls = set(l)
    return len(ls)
def sorting(l): # list에서 중복제거해주고 오름차순 정렬
    ls = set(l)
    ll = list(ls)
    ll.sort()
    return ll
def check(N,K): # 받은 string 속 숫자의 개수가 K와 같은지 bool을 return
    li = []
    for k in N:
        li.append(k)
    return count(li) == K

a = input()
N, K = int(a.split()[0]), int(a.split()[1])

M = str(N) # 다 붙어있는 string
li = [] # 각 자리 수가 순서대로 들어있는 list
for i in range(len(M)):
    li.append(M[i])
if count(li) < K:
    while(True):
        N+=1
        if check(str(N), K):
            print(N); break
    exit()

# 앞에서부터 서로 다른 숫자를 K개 뽑는다.
ans = [] # 답을 넣을 list
for i in li:
    ans.append(i)
    if count(ans) == K:
        break
# 마지막으로 뽑은 자리 수와 다음 자리 수를 비교
# 다음 자리 수보다 크지만 뽑힌 수 중 가장 작은걸로 선택
ansl = len(ans)
try:
    b = li[ansl]
    for j in sorting(ans):
        j = int(j)
        if j >= int(b):
            ans.append(str(j))
            break
    if len(ans) == ansl:
        a2 = int(ans[-1]) + 1
        ans.pop()
        ans.append(str(a2))
    # 나머지 뒤는 뽑은 수 중 가장 작은 수로 채움
    bb = sorting(ans)[0]
    answer = ""
    for k in ans:
        answer += k
    while (True):
        answer += bb
        if len(answer) == len(M):
            break
    print(answer)
except IndexError:
    if count(ans) == K:
        answer = ""
        for k in ans:
            answer += k
        print(answer)
    else:
        c = count(ans)
        ans = ans[0:c]
        p = ['0','1','2','3','4','5','6','7','8','9']
        p2 = set(p); ans2 = set(ans)
        pans = p2 - ans2
        pans = list(pans)
        pans.sort()
        # 여기부터 고쳐야함
        for i in range(K-count(ans)+1):
            ans.append(pans[i])
        answer = ""
        for k in ans:
            answer += k
        print(answer)