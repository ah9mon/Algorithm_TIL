import sys
from collections import deque

def bfs(r,c) :
    global alive
    q = deque()
    q.append([r,c])
    while(q):
        coordinate = q.pop()
        y = coordinate[0]
        x = coordinate[1]
        visited[y][x] = 1
        for dv in range(4):
            ny = y + dy[dv]
            nx = x + dx[dv]
            if (0 <= ny < R and 0 <= nx < C and visited[ny][nx] == 0) :
                if (farm[ny][nx] == 'S') :
                    if (farm[y][x] == 'W') :
                        alive = 0
                        return
                    elif (farm[y][x] == '.') :
                        farm[y][x] = 'D'

                elif (farm[ny][nx] == '.') :
                    q.append([ny,nx])

alive = 1
R, C = map(int, sys.stdin.readline().strip().split())
farm = [[] for _ in range(R)]
for i in range(R) :
    line = list(sys.stdin.readline().strip())
    farm[i] = line

dx = [0,0,1,-1]
dy = [1,-1,0,0]
visited = [[0 for _ in range(C)] for _ in range(R)]

for r in range(R) :
    for c in range(C) :
        if (farm[r][c] == 'W') :
            bfs(r,c)
        
        if (alive == 0) :
            break
    
    if (alive == 0) :
        break

print(alive)
if (alive) :
    for i in range(R) :
        print(''.join(farm[i]))