# def cross(info, array, num):
def findIndex(list):
    ans = []
    i = 0
    while i >= 0:
        try:
            i = list.index(1)
        except ValueError:
            break
        else:
            if i != -1:
                ans.append(i)
                list[i] = 0
    return ans





NM = input().split()
N, M = int(NM[0]), int(NM[1])
L = input().split()
R = input().split()
K = int(input())
info = [[0 for _ in range(M)] for _ in range(N)]
array = [[0 for _ in range(M)] for _ in range(N)]
num = 0
for _ in range(K):
    l = input().split()
    info[L.index(l[0])][R.index(l[1])] = 1
print(findIndex(info[num]))

# 두 좌표을 이은 직선의 기울기가 양수면 교차하지 않음