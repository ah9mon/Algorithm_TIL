'''
https://www.acmicpc.net/problem/14940
'''
from collections import deque

def bfs(y,x):
    global visited
    # 동서남북 탐색 
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    # 큐생성 
    q = deque()
    # 시작점 방문체크 및 인큐 
    q.append((y,x))
    while q: 
        r,c = q.popleft()
        for i in range(4):
            ny,nx = r + dy[i], c + dx[i]
            # 범위 안에 있고 visited == 0 이고 graph == 1이면 
            if 0<= nx < M and 0<= ny < N and visited[ny][nx] == 0 and graph[ny][nx] == '1':
                q.append((ny,nx))
                visited[ny][nx] = visited[r][c] + 1    

    return

N,M = map(int,input().split())
# 입력 받으면서 2 찾기 
graph = []
startx,starty = -1,-1 
for i in range(N):
    line = input().split()
    if '2' in line:
        startx = line.index('2')
        starty = i
    graph.append(line)

# 방문체크용 
visited = [[0]*M for _ in range(N)]
# print(starty,startx)
bfs(starty, startx)
# print(visited)
# print(graph)
for row in range(N):
    for col in range(M):
        #graph가 1인데 visited가 0이면 
        if graph[row][col] == '1' and visited[row][col] == 0:
            print(-1, end = ' ')
        else:
            print(visited[row][col], end=' ')
    print('')