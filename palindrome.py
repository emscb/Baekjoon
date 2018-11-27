import time
# 출력 : #라인번호, 찾은 회문, 회문개수
# 입력 : 다중 라인
def isPalindrome(string):
    return string[::-1] == string

N = 1 # line 수 카운트
ekq = []
while(True):
    answer = ''
    a=input()
    if a == '':
        break
    a.strip()
    ans = [] # 출력할 답
    li = [] # 뜯어 넣기
    for i in a:
        li.append(i)
    index = 0
    for i in li:
        idx = [j for j, k in enumerate(li) if k == i]
        if len(idx) != 1:
            for p in idx:
                if index != p and isPalindrome(a[index:p+1]):
                    if len(a[index:p+1]) >= 3:
                        ans.append(a[index:p+1])
        index += 1
    ans.sort(key=lambda x: len(x))
    answer += '#' + str(N) + ' '
    for k in ans:
        answer += k + ' '
    answer += str(len(ans))
    ekq.append(answer)
    N += 1
for k in ekq:
    print(k)
time.sleep(5)