# 침투 
'''
https://www.acmicpc.net/problem/13565
'''
from sys import stdin
input = stdin.readline
from collections import deque

def bfs():
    # direction
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    while q:
        y,x = q.popleft() 
        
        # 종료 조건 
        if y == M-1: # 마지막 줄 도착하면 
            return True # True 반환 
        
        # 4방향 탐색 
        for v in range(4):
            ny, nx = y + dy[v], x + dx[v]
            # 범위 안에 있고 방문 안했고 전류 통하는 물질이면 
            if 0 <= ny < M and 0 <= nx < N and (not visited[ny][nx]) and (graph[ny][nx] == '0'):
                q.append((ny,nx))
                visited[ny][nx] = 1
    
    return False
                 
M, N = map(int,input().split()) # 2 <= row, column <= 1000
visited = [[0]*N for _ in range(M)] # 방문 체크용 
graph = [] # 섬유 물질

q = deque() # input 받으면서 시작점 넣어주기 위해 함수 바깥에서 queue 만듬 

for m in range(M): 
    line = input()
    graph.append(line)
    
    if not m: # 첫줄이면 
        # 출발 인덱스 찾기 
        for i in range(N): 
            if line[i] == '0':
                q.append((0,i))
                visited[0][i] = 1

if bfs():
    print('YES')
else:
    print('NO')
