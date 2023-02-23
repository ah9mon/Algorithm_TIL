# 탈주범 검거 
import sys
sys.stdin = open('input_for_13984.txt')

from collections import deque

def bfs(r,c):
    # 인덱스 순서대로 상하좌우 탐색 
    # 탐색    [상하좌우]  [상하 x x] [x x좌우] [상 x x우] [x하x우]   [x하좌x]    [상x좌x] 
    dx = [[],[0,0,-1,1],[0,0,0,0],[0,0,-1,1],[0,0,0,1],[0,0,0,1],[0,0,-1,0],[0,0,-1,0]]
    dy = [[],[-1,1,0,0],[-1,1,0,0],[0,0,0,0],[-1,0,0,0],[0,1,0,0],[0,1,0,0],[-1,0,0,0]]
    # 상성 
    '''
    상 탐색 i = 0 일때 nv != 3, 4, 7  
    하 탐색 i = 1 일때 nv != 3, 5, 6 
    좌 탐색 i = 2 일때 nv != 2, 6, 7
    우 탐색 i = 3 일때 nv != 2, 4, 5 
    '''
    dont_go = [[3,4,7],[3,5,6],[2,6,7],[2,4,5]]
    
    q = deque()
    visited = [[0]*M for _ in range(N)]
    q.append((r,c))
    visited[r][c] = 1
    counts = 1

    while q:
        y,x = q.popleft()
        v = tunul[y][x]
        # print(v)
        if visited[y][x] < L: # L시간 이전 까지만 아래 실행 가능             
             for i in range(len(dx[v])): # 터널 타입에 따라 탐색                 
                if (dy[v][i],dx[v][i]) != (0,0): # 탐색할수 없으면 아래 실행 안함 / 예를 들어 좌우 터널는 상하 탐색 못함
                    ny, nx = y + dy[v][i], x + dx[v][i] # 탐색 위치 
                    if  0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and tunul[ny][nx]: # 범위에 있고 방문한적 없고 터널 구조물이면  
                        # 구조물 모양(상성)에 따라 못가는 경우를 반영 
                        nv = tunul[ny][nx]
                        if nv in dont_go[i]:
                            continue
                        
                        q.append((ny,nx))
                        counts += 1
                        visited[ny][nx] = visited[y][x] + 1
    return counts
    

T = int(input())
for i in range(1,T+1):
    # 세로, 가로, 맨홀 뚜껑이 위치한 장소의 세로위치, 가로위치, 탈출 후 소요된 시간
    N,M,R,C,L = map(int,input().split())
    tunul = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{i} {bfs(R, C)}')
    