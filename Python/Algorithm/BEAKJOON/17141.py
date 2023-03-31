# 백준 연구소 2
'''
https://www.acmicpc.net/problem/17141
'''
from collections import deque
def bfs(q):
    global rlt
    global rlt2
    visited = [[-1]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if graph[row][col] == 1:
                visited[row][col] = '-'
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    for x,y in q:
        visited[y][x] = 0

    while q:
        c,r = q.popleft()

        for v in range(4):
            nx,ny = c + dx[v], r + dy[v] # 바이러스 퍼지는 칸 
            # 범위 안에 있고
            if 0<= nx < N and 0<= ny < N:  
                if graph[ny][nx] != 1 and visited[ny][nx] == -1: # 벽이 아니고 방문 안했으면 
                    q.append((nx,ny)) 

                    visited[ny][nx] = visited[r][c] + 1

    # visited 탐색 
    max_time = 0

    for k in range(N):
        for l in range(N):
            if visited[k][l] == -1:
                return 
            
            if visited[k][l] == '-':
                continue

            if max_time < visited[k][l]:
                max_time = visited[k][l]

    if rlt > max_time:
        rlt = max_time
    
    rlt2 = True
    return

def func(i,c):
    
    if c == M: 
        q = deque()
        for index in range(len(bit)):
            if bit[index]:
                q.append(b[index])
        bfs(q)
        return
    
    if i == len(b):
        return
    bit[i] = 1
    func(i+1, c+1)
    bit[i] = 0
    func(i+1, c)

# 연구소의 크기 N, 바이러스의 개수 M
N ,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
rlt = N*N
b = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            b.append((j,i))
bit = [0]*len(b)
rlt2 = False
func(0,0)

if rlt2:
    print(rlt)
else:
    print(-1)
