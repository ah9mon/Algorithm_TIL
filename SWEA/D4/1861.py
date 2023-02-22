# bfs 

import sys
sys.stdin = open('input_for_1861.txt')

from collections import deque

def bfs(a,b):
    global max_move
    global max_point
    global visited
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visited = [[0]*N for _ in range(N)]
    q = deque()
    q.append((a,b))
    visited[b][a] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x +dx[i], y+ dy[i]
            if 0 <= nx < N and 0 <= ny < N and list1[ny][nx] == list1[y][x] + 1 and not visited[ny][nx] :
                q.append((nx,ny))
                visited[ny][nx] = visited[y][x] + 1
                if visited[ny][nx] > max_move:
                    max_move = visited[ny][nx]
                    max_point = list1[b][a]
                elif visited[ny][nx] == max_move:
                    if max_point > list1[b][a]:
                        max_point = list1[b][a]        
    
T = int(input())

for i in range(1,T+1):
    N = int(input())   
    list1 = [list(map(int,input().split())) for _ in range(N)]
    max_move = 0
    max_point = 1000001
    for row in range(N):
        for col in range(N):
            # if not visited[row][col]:
            bfs(col,row)
    
    print(f'#{i} {max_point} {max_move}')
    