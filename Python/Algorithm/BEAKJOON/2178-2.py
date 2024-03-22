import sys
from collections import deque

def bfs() :
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    while(q) :
        y,x = q.popleft()
        for dv in range(4) :
            ny = y + dy[dv]
            nx = x + dx[dv]
            if (0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0 and maze[ny][nx] == '1') :
                q.append((ny,nx))
                visited[ny][nx] = visited[y][x] + 1

N, M = map(int, sys.stdin.readline().strip().split())
visited = [[0 for _ in range(M)] for _ in range(N)]
maze = ["" for _ in range(N)]
for i in range(N) :
    line = sys.stdin.readline().strip()
    maze[i] = line

bfs()
print(visited[N - 1][M - 1])


