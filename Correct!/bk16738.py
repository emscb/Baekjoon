def new(X, Y, room, team, num):
    if room.find("1") == -1: # 방이 다 비었을 때
        room = "1"*Y + room[Y:]
        team[num] = "%d:%d:%d" % (X, 0, Y)
        print("%d %d" % (1, Y))
        return room, team, 0
    elif room.find("0") == -1 or room.find("%s" % "0"*Y) == -1: # 모든 방이 사용중일 때, 원하는 평수의 방이 없을 때
        print("REJECTED"); return room, team, -1
    else:
        start = room.find("%s" % "0"*Y)
        if start != 0:
            room = room[0:start] + "1"*Y + room[start+Y:]
        else:
            room = "1"*Y + room[Y:]
        team[num] = "%d:%d:%d" % (X, start, start+Y)
        print("%d %d" % (start+1, start+Y))
        return room, team, 0


def out(A, B, room, team):
    n, L, R = int(team[A].split(":")[0]), int(team[A].split(":")[1]), int(team[A].split(":")[2])
    n -= B
    if n == 0:
        print("CLEAN %d %d" % (L+1, R))
        if L == 0:
            room = "0"*(R) + room[R:]
        else:
            room = room[0:L] + "0"*(R-L) + room[R:]
        return room, team
    else:
        team[A] = "%d:%d:%d" % (n, L, R)
        return room, team


NQ = input()
N, Q = int(NQ.split()[0]), int(NQ.split()[1])
# Room number : 1 ~ N -> 0 ~ N-1
roomStat = "0" * N
teamMem = {}
teamNum = 1
for i in range(Q):
    line = input().split()
    if line[0] == "new":
        roomStat, teamMem, status = new(int(line[1]), int(line[2]), roomStat, teamMem, teamNum)
        if status == 0:
            teamNum += 1
    elif line[0] == "in":
        A, B = int(line[1]), int(line[2])
        n, L, R = int(teamMem[A].split(":")[0]), int(teamMem[A].split(":")[1]), int(teamMem[A].split(":")[2])
        n += B
        teamMem[A] = "%d:%d:%d" % (n, L, R)
    elif line[0] == "out":
        A, B = int(line[1]), int(line[2])
        roomStat, teamMem = out(A, B, roomStat, teamMem)
