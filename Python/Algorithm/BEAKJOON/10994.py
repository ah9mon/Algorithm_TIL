import sys 

def changeVector() :
    global dv
    dv += 1
    if (dv >= 4) :
        dv = 0

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
m_coordinate = [N // 2 + 1, N // 2 + 1]

snail = [[0 for _ in range(N)] for _ in range(N)]
x = y = N // 2
snail[y][x] = 1

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
dv = 0

distance = 1
turnCount = 0
count = 0

for i in range(2,N * N + 1) :
    nx = x + dx[dv]
    ny = y + dy[dv]
    snail[ny][nx] = i
    if (i == M) :
        m_coordinate[0] = ny + 1
        m_coordinate[1] = nx + 1

    x = nx
    y = ny
    count += 1

    if (count == distance) :
        changeVector()
        turnCount += 1
        count = 0

    if (turnCount == 2) :
        distance += 1
        turnCount = 0

for i in range(N) :
    print(' '.join(map(str,snail[i])).strip())

print(' '.join(map(str,m_coordinate)).strip())