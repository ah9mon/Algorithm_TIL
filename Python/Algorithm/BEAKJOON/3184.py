# 양 

'''
https://www.acmicpc.net/problem/3184

'''
from collections import deque

def bfs(y,x):
    global visited
    global counts_o
    global counts_v

    # 동서남북 
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    # 현재 위치 인큐 
    q = deque()
    q.append((y,x))
    visited[y][x] += 1
    # bfs 
    c_o = 0
    c_v = 0
    while q:
        r, c = q.popleft()
        # 현재 위치가 양이면 
        if graph[r][c] == 'o':
            c_o += 1
        # 현재 위치가 늑대면 
        if graph[r][c] == 'v':
            c_v += 1

        for i in range(4):
            ny,nx = r + dy[i], c + dx[i]
            # 범위 안에 있고 방문안했으며 울타리 아니면 
            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0 and graph[ny][nx] != '#':
                q.append((ny,nx))
                visited[ny][nx] += 1
    
    if c_o > c_v: # 양이 늑대보다 많으면 
        counts_o += c_o # 눅대 우리에서 쫒아내니까 양의 수를 더해줌 
    
    else: # 늑대가 양보다 많으면 
        counts_v += c_v # 양을 다 먹으니까 늑대의 수를 더해줌


N,M = map(int,input().split())
graph = [input() for _ in range(N)]

visited = [[0]*M for _ in range(N)]

counts_v = 0 
counts_o = 0

for row in range(N):
    for col in range(M):
        if visited[row][col] == 0 and graph[row][col] != '#': # 방문 안했고 울타리가 아니면 
            bfs(row,col)

# print(visited)
print(f'{counts_o} {counts_v}')