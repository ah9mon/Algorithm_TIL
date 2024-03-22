import sys
from collections import deque

def bfs(r,c) :
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    count = 1
    while(q) :
        y,x = q.popleft()
        for dv in range(4) :
            ny = y + dy[dv]
            nx = x + dx[dv]
            if (0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0 and villages[ny][nx] == '1') :
                q.append((ny,nx))
                visited[ny][nx] = 1
                count += 1

    village_info.append(count)


N = int(sys.stdin.readline())
villages = ["" for _ in range(N)]
for i in range(N) :
    villages[i] = sys.stdin.readline().strip()

visited = [[0 for _ in range(N)] for _ in range(N)]
village_info = []
for r in range(N) :
    for c in range(N) :
        if (villages[r][c] == '1' and visited[r][c] == 0) :
            bfs(r,c)

print(len(village_info))
village_info.sort()
for village in village_info :
    print(village)