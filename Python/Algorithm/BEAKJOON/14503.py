# 로소기

'''
https://www.acmicpc.net/problem/14503

방 N x M 
각 칸은 벽 or 빈칸

방향
dx = [0,1,0,-1]
dy = [-1,0,1,0]

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

def cleanroom(r,c,0):
    global graph
    y,x = r,c
    # 현재 칸 청소
    graph[r][c] = 0
    # 청소되지 않은 칸 탐색 
    for i in range(4)    
        ny,nx = y+dy[i], x+dx[i] # 탐색하고 있는 칸의 좌표 
        






# 방의 크기 
N,M = map(int,input().split())

# 로봇좌표 , 방향
r,c,v = map(int,input().split())

# 방
graph = [list(map(int,input().split())) for _ in range(N)]

# 청소한 방의 개수 
counts = 0






