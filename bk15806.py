def wmdtlr(pos, fna):
    if pos == []:
        return pos, fna
    pos2 = []
    N=len(fna)-1
    for i in pos:
        fna[i[0]][i[1]] = False

    for i in pos:
        # try:
            if i[0]+2 <= N and i[1]+2 <= N and i[0]-2 >= 0 and i[1]-2 >= 0: # 8개 다
                # 1
                fna[i[0] - 2][i[1] + 1] = True
                pos2.append((i[0] - 2, i[1] + 1))
                # 2
                fna[i[0] - 1][i[1] + 2] = True
                pos2.append((i[0] - 1, i[1] + 2))
                # 3
                fna[i[0] + 1][i[1] + 2] = True
                pos2.append((i[0] + 1, i[1] + 2))
                # 4
                fna[i[0] + 2][i[1] + 1] = True
                pos2.append((i[0] + 2, i[1] + 1))
                # 5
                fna[i[0] + 2][i[1] - 1] = True
                pos2.append((i[0] + 2, i[1] - 1))
                # 6
                fna[i[0] + 1][i[1] - 2] = True
                pos2.append((i[0] + 1, i[1] - 2))
                # 7
                fna[i[0] - 1][i[1] - 2] = True
                pos2.append((i[0] - 1, i[1] - 2))
                # 8
                fna[i[0] - 2][i[1] - 1] = True
                pos2.append((i[0] - 2, i[1] - 1))

            elif i[0]+1 == N and i[1]+2 <= N and i[1]-2 >= 0: # 밑에 2개 빼고
                # 1
                fna[i[0] - 2][i[1] + 1] = True
                pos2.append((i[0] - 2, i[1] + 1))
                # 2
                fna[i[0] - 1][i[1] + 2] = True
                pos2.append((i[0] - 1, i[1] + 2))
                # 3
                fna[i[0] + 1][i[1] + 2] = True
                pos2.append((i[0] + 1, i[1] + 2))
                # 6
                fna[i[0]+1][i[1]-2] = True
                pos2.append((i[0]+1,i[1]-2))
                # 7
                fna[i[0]-1][i[1]-2] = True
                pos2.append((i[0]-1,i[1]-2))
                # 8
                fna[i[0]-2][i[1]-1] = True
                pos2.append((i[0]-2,i[1]-1))

            elif i[0]+2 <= N and i[1]+2 == N and i[0]-2 >= 0: # 오른쪽 2개 빼고
                # 1
                fna[i[0] - 2][i[1] + 1] = True
                pos2.append((i[0] - 2, i[1] + 1))
                # 4
                fna[i[0] + 2][i[1] + 1] = True
                pos2.append((i[0] + 2, i[1] + 1))
                # 5
                fna[i[0] + 2][i[1] - 1] = True
                pos2.append((i[0] + 2, i[1] - 1))
                # 6
                fna[i[0] + 1][i[1] - 2] = True
                pos2.append((i[0] + 1, i[1] - 2))
                # 7
                fna[i[0] - 1][i[1] - 2] = True
                pos2.append((i[0] - 1, i[1] - 2))
                # 8
                fna[i[0] - 2][i[1] - 1] = True
                pos2.append((i[0] - 2, i[1] - 1))

            elif i[0]+1 == N and i[1]+1 == N: # 밑, 오른쪽 2개씩 빼고
                # 1
                fna[i[0] - 2][i[1] + 1] = True
                pos2.append((i[0] - 2, i[1] + 1))
                # 6
                fna[i[0] + 1][i[1] - 2] = True
                pos2.append((i[0] + 1, i[1] - 2))
                # 7
                fna[i[0] - 1][i[1] - 2] = True
                pos2.append((i[0] - 1, i[1] - 2))
                # 8
                fna[i[0] - 2][i[1] - 1] = True
                pos2.append((i[0] - 2, i[1] - 1))

            elif i[0]+1 == N and i[1] == N: # 오른쪽 4개, 밑 2개 빼고
                # 6
                fna[i[0] + 1][i[1] - 2] = True
                pos2.append((i[0] + 1, i[1] - 2))
                # 7
                fna[i[0] - 1][i[1] - 2] = True
                pos2.append((i[0] - 1, i[1] - 2))
                # 8
                fna[i[0] - 2][i[1] - 1] = True
                pos2.append((i[0] - 2, i[1] - 1))

            elif i[0] == N and i[1]+1 == N: # 밑 4개, 오른쪽 2개 빼고
                # 1
                fna[i[0] - 2][i[1] + 1] = True
                pos2.append((i[0] - 2, i[1] + 1))
                # 7
                fna[i[0] - 1][i[1] - 2] = True
                pos2.append((i[0] - 1, i[1] - 2))
                # 8
                fna[i[0] - 2][i[1] - 1] = True
                pos2.append((i[0] - 2, i[1] - 1))

            elif i[0] == i[1] == N: # 좌상 2개만
                # 7
                fna[i[0] - 1][i[1] - 2] = True
                pos2.append((i[0] - 1, i[1] - 2))
                # 8
                fna[i[0] - 2][i[1] - 1] = True
                pos2.append((i[0] - 2, i[1] - 1))

            elif i[0]-1 == 0 and i[1]-2 >= 0 and i[1]+2 <= N: # 위 2개 빼고
                # 2
                fna[i[0] - 1][i[1] + 2] = True
                pos2.append((i[0] - 1, i[1] + 2))
                # 3
                fna[i[0] + 1][i[1] + 2] = True
                pos2.append((i[0] + 1, i[1] + 2))
                # 4
                fna[i[0] + 2][i[1] + 1] = True
                pos2.append((i[0] + 2, i[1] + 1))
                # 5
                fna[i[0] + 2][i[1] - 1] = True
                pos2.append((i[0] + 2, i[1] - 1))
                # 6
                fna[i[0] + 1][i[1] - 2] = True
                pos2.append((i[0] + 1, i[1] - 2))
                # 7
                fna[i[0] - 1][i[1] - 2] = True
                pos2.append((i[0] - 1, i[1] - 2))

            elif i[0]-2 >= 0 and i[1]-1 == 0 and i[0]+2 <= N: # 왼쪽 2개 빼고
                # 1
                fna[i[0] - 2][i[1] + 1] = True
                pos2.append((i[0] - 2, i[1] + 1))
                # 2
                fna[i[0] - 1][i[1] + 2] = True
                pos2.append((i[0] - 1, i[1] + 2))
                # 3
                fna[i[0] + 1][i[1] + 2] = True
                pos2.append((i[0] + 1, i[1] + 2))
                # 4
                fna[i[0] + 2][i[1] + 1] = True
                pos2.append((i[0] + 2, i[1] + 1))
                # 5
                fna[i[0] + 2][i[1] - 1] = True
                pos2.append((i[0] + 2, i[1] - 1))
                # 8
                fna[i[0] - 2][i[1] - 1] = True
                pos2.append((i[0] - 2, i[1] - 1))

            elif i[0]-1 == 0 and i[1]-1 == 0: # 왼쪽 2개, 위 2개 빼고
                # 2
                fna[i[0] - 1][i[1] + 2] = True
                pos2.append((i[0] - 1, i[1] + 2))
                # 3
                fna[i[0] + 1][i[1] + 2] = True
                pos2.append((i[0] + 1, i[1] + 2))
                # 4
                fna[i[0] + 2][i[1] + 1] = True
                pos2.append((i[0] + 2, i[1] + 1))
                # 5
                fna[i[0] + 2][i[1] - 1] = True
                pos2.append((i[0] + 2, i[1] - 1))

            elif i[0] == 0 and i[1]-1 == 0: # 위 4개, 왼쪽 2개 빼고
                # 3
                fna[i[0] + 1][i[1] + 2] = True
                pos2.append((i[0] + 1, i[1] + 2))
                # 4
                fna[i[0] + 2][i[1] + 1] = True
                pos2.append((i[0] + 2, i[1] + 1))
                # 5
                fna[i[0] + 2][i[1] - 1] = True
                pos2.append((i[0] + 2, i[1] - 1))

            elif i[0]-1 == 0 and i[1] == 0: # 왼쪽 4개, 위 2개 뺴고
                # 2
                fna[i[0] - 1][i[1] + 2] = True
                pos2.append((i[0] - 1, i[1] + 2))
                # 3
                fna[i[0] + 1][i[1] + 2] = True
                pos2.append((i[0] + 1, i[1] + 2))
                # 4
                fna[i[0] + 2][i[1] + 1] = True
                pos2.append((i[0] + 2, i[1] + 1))

            elif i[0] == i[1] == 0: # 우하 2개만
                # 3
                fna[i[0] + 1][i[1] + 2] = True
                pos2.append((i[0] + 1, i[1] + 2))
                # 4
                fna[i[0] + 2][i[1] + 1] = True
                pos2.append((i[0] + 2, i[1] + 1))

            elif i[0]-1 == 0 and i[1]+1 == N: # 위 2개, 오른쪽 2개 뺴고
                # 4
                fna[i[0] + 2][i[1] + 1] = True
                pos2.append((i[0] + 2, i[1] + 1))
                # 5
                fna[i[0] + 2][i[1] - 1] = True
                pos2.append((i[0] + 2, i[1] - 1))
                # 6
                fna[i[0] + 1][i[1] - 2] = True
                pos2.append((i[0] + 1, i[1] - 2))
                # 7
                fna[i[0] - 1][i[1] - 2] = True
                pos2.append((i[0] - 1, i[1] - 2))

            elif i[0]-1 == 0 and i[1] == N: # 오른쪽 4개, 위 2개 빼고
                # 5
                fna[i[0] + 2][i[1] - 1] = True
                pos2.append((i[0] + 2, i[1] - 1))
                # 6
                fna[i[0] + 1][i[1] - 2] = True
                pos2.append((i[0] + 1, i[1] - 2))
                # 7
                fna[i[0] - 1][i[1] - 2] = True
                pos2.append((i[0] - 1, i[1] - 2))

            elif i[0] == 0 and i[1]+1 == N: # 위 4개, 오른쪽 2개 빼고
                # 4
                fna[i[0] + 2][i[1] + 1] = True
                pos2.append((i[0] + 2, i[1] + 1))
                # 5
                fna[i[0] + 2][i[1] - 1] = True
                pos2.append((i[0] + 2, i[1] - 1))
                # 6
                fna[i[0] + 1][i[1] - 2] = True
                pos2.append((i[0] + 1, i[1] - 2))

            elif i[0] == 0 and i[1] == N: # 좌하 2개만
                # 5
                fna[i[0] + 2][i[1] - 1] = True
                pos2.append((i[0] + 2, i[1] - 1))
                # 6
                fna[i[0] + 1][i[1] - 2] = True
                pos2.append((i[0] + 1, i[1] - 2))

            elif i[0]+1 == N and i[1]-1 == 0: #1238
                # 1
                fna[i[0] - 2][i[1] + 1] = True
                pos2.append((i[0] - 2, i[1] + 1))
                # 2
                fna[i[0] - 1][i[1] + 2] = True
                pos2.append((i[0] - 1, i[1] + 2))
                # 3
                fna[i[0] + 1][i[1] + 2] = True
                pos2.append((i[0] + 1, i[1] + 2))
                # 8
                fna[i[0] - 2][i[1] - 1] = True
                pos2.append((i[0] - 2, i[1] - 1))

            elif i[0]+1 == N and i[1] == 0: # 123
                # 1
                fna[i[0] - 2][i[1] + 1] = True
                pos2.append((i[0] - 2, i[1] + 1))
                # 2
                fna[i[0] - 1][i[1] + 2] = True
                pos2.append((i[0] - 1, i[1] + 2))
                # 3
                fna[i[0] + 1][i[1] + 2] = True
                pos2.append((i[0] + 1, i[1] + 2))

            elif i[0] == N and i[1]-1 == 0: #128
                # 1
                fna[i[0] - 2][i[1] + 1] = True
                pos2.append((i[0] - 2, i[1] + 1))
                # 2
                fna[i[0] - 1][i[1] + 2] = True
                pos2.append((i[0] - 1, i[1] + 2))
                # 8
                fna[i[0] - 2][i[1] - 1] = True
                pos2.append((i[0] - 2, i[1] - 1))

            elif i[0] == N and i[1] == 0: # 12
                # 1
                fna[i[0] - 2][i[1] + 1] = True
                pos2.append((i[0] - 2, i[1] + 1))
                # 2
                fna[i[0] - 1][i[1] + 2] = True
                pos2.append((i[0] - 1, i[1] + 2))

        # except Exception as e:
        #     print(e, i[0], i[1])
        #     exit(-1)
    return pos2, fna

N,M,K,t = input().split()
N=int(N)
M=int(M)
K=int(K)
t=int(t)

if N <= 3 or M == 0 or K == 0:
    print("NO")
    exit()

pang=[]
badak=[]

for i in range(M):
    x1, y1 = input().split()
    pang.append((int(x1)-1, int(y1)-1))

for i in range(K):
    x1, y1 = input().split()
    badak.append([int(x1)-1, int(y1)-1])

# 방의 크기는 N*N
room = [ [False] * N for i in range(N) ]
for i in pang:
    room[i[0]][i[1]] = True

for i in range(t):
    pangs = set(pang)
    pang = list(pangs)
    pang, room = wmdtlr(pang, room)
#    print("증식됨")

for i in badak:
    x, y = i[0], i[1]
    if room[x][y]:
        print("YES")
        exit()

print("NO")