# 로소기

'''
https://www.acmicpc.net/problem/14503

방 N x M 
각 칸은 벽 or 빈칸

방향

1. 현재 칸 청소 
2. 현재 칸 주변 탐색 
  1. 청소되지 않은 칸이 없는 경우 
    1. 현재 바라보는 방향을 유지한 채 후진할 수 있다면 후진하고 1번으로 돌아감 
    2. 바라보는 방향의 뒤쪽 칸이 벽이면 작동을 멈춤 (out of range == 벽)
  2. 있는 경우 
    1. 반시계로 회전 
    2. 회전한 곳이 청소해야하는 칸이면 청소해야하는 칸으로 전진 
    3. 1번으로 돌아감 

청소하는 영역의 개수는 ? 
'''
def turn():
    global v
    v -= 1
    if v < 0:
        v = 3

def cleanroom(r,c):
    global graph
    global counts
    y,x = r,c
    # 현재 칸 청소안되어있으면 청소 
    if not graph[r][c]:
        graph[r][c] = 2
        counts += 1
    # 현재 위치의 동서남북에 청소되지 않은 칸 탐색
    stack = [] 
    for i in range(4):  
        ny,nx = y+dy[i], x+dx[i] # 탐색하고 있는 칸의 좌표
        # 청소 안되어 있으면 stack에 넣기 
        if not graph[ny][nx]: 
            stack.append((ny,nx))
    
    # 현재 칸 동서남북에 청소되지 않은 빈칸이 없는 경우
    if not stack:
        ny,nx = y-dy[v], x-dx[v] # 후진한 좌표
        # 바라보는 방향을 유지한 채 한칸 후진할 수 있으면 후진
        if 0<= ny < N and 0<= nx < M and graph[ny][nx] != 1: # 범위안에 있고 벽이 아니면 
            y,x = ny,nx # v 변경없이 후진
            cleanroom(y,x)
        elif 0<= ny < N and 0<= nx < M and graph[ny][nx] == 1: # 벽이라 후진 못하면 
            return 
        
    else: # 주변에 청소되지 않은 곳이 있다면
        while True: # 전진할때까지 반복 
            turn() # 반시계로 회전 
            # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈칸인 경우 한칸 전진
            ny,nx = y+dy[v], x+dx[v] # 전진한 좌표
            if (ny,nx) in stack: # 청소 안되어잇으면 
                # 한칸 전진 
                y,x = ny,nx 
                cleanroom(y,x)
                return                   

# 방의 크기 
N,M = map(int,input().split())

# 로봇좌표 , 방향
r,c,v = map(int,input().split())

# 방
graph = [list(map(int,input().split())) for _ in range(N)]

# 청소한 방의 개수 
counts = 0

# 북 동 남 서
dx = [0,1,0,-1]
dy = [-1,0,1,0]

cleanroom(r,c)
print(counts)




