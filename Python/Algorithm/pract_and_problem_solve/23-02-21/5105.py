# the street of maze z z
import sys
sys.stdin = open('input_for_5105.txt')

'''
N * N 크기의 미로
1 : 벽
0 : 통로
출발지(2)에서 도착지(3)까지의 지나간 칸수는 ?
'''

# from collections import deque

def bfs(Y,X):
    global min_distance
    visited = [[0]*N for _ in range(N)] # 인큐 체크용
    q = [] # 큐 생성
    q.append((Y,X)) # 시작점 인큐
    visited[Y][X] = 1 # 인큐 체크
    dx = [1,0,-1,0] # 주변길 확인용
    dy = [0,1,0,-1] # 주변길 확인용
    while q:
        y,x = q.pop(0)
        for i in range(4):
            ny,nx = y+dy[i], x+ dx[i]
            if 0 <= ny < N and 0 <= nx < N: # 범위 안에 있으면 
                if not maze[ny][nx] and not visited[ny][nx]: # 방문한적 없는 길이면
                    q.append((ny,nx)) # 인큐
                    visited[ny][nx] = visited[y][x] + 1
                    # print(visited[y][x], visited[ny][nx])
    
                if maze[ny][nx] == 3:
                    # print(f'도착까지 이동거리 : {visited[ny][nx]}')
                    if visited[y][x] - 1 < min_distance:
                        min_distance = visited[y][x] - 1

T = int(input())
for i in range(1,T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    for j in range(N):
        if 2 in maze[j]:
            x,y = maze[j].index(2), j
            break
    min_distance = N*N
    # print(y,x)
    bfs(y,x)
    if min_distance == N*N: # 초기값이랑 min값이 똑같으면
        min_distance = 0
    print(f'#{i} {min_distance}')




