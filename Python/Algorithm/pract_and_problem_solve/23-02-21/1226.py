# 미로 1

'''
16*16 행렬

시작점 miro(1,1) = 2
도착점 miro(3,3) = 3
길 miro[i][j] = 0
'''
import sys
sys.stdin = open('input_for_1226.txt')

from collections import deque

def bfs(Y,X,maze):
    # 인큐 체크용
    visited = [[0]* 16 for _ in range(16)]
    # 주변 탐색 용
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    q = deque()
    q.append((Y,X))
    visited[Y][X] = 1
    while q:
        y,x = q.popleft() # 디큐
        for i in range(4):
            ny,nx = y+dy[i], x+dx[i]
            # print(ny,nx)
            # print(maze[ny][nx])
            if not visited[ny][nx] and not maze[ny][nx] : # 길이면 and 안가본 길이면
                q.append((ny,nx)) # 인큐
                visited[ny][nx] = 1 # 인큐 체크

            if maze[ny][nx] == 3: # 도착하면
                return 1 # 1반환

    return 0 # 도착 못하면 -1 반환

for _ in range(10):
    tc = input()
    maze = [list(map(int,input())) for _ in range(16)]
    # print(maze)
    print(f'#{tc} {bfs(1,1,maze)}')
