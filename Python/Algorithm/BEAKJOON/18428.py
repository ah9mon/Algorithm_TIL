# 감시 피하기 

'''
https://www.acmicpc.net/problem/18428

N x N 크기의 복도 
특정 위치에 선생님, 학생, 장애물이 위치해 있음 

T(선생님) : 상 하 좌 우 4방향 감시
S(학생)
O(장애물)
선생님은 장애물 뒤편에 숨어있는 학생은 볼 수 없음 

3개의 장애물을 설치하면 모든 학생이 모든 선생님들의 감시를 피할 수 있는지 출력

how? 

수열 만드는 것처럼 장애물 설치 후
bfs돌림 
학생 안만나면 rlt = true
-> "yes"
'''

from collections import deque

def bfs():
    visited = [[0]*N for _ in range(N)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque()
    for t in T:
        q.append(t)
        y, x = t
        visited[y][x] = 1

    while q:
        # print(q)
        y,x = q.popleft()
        for index in range(4):
            ny,nx = y + dy[index], x + dx[index]
            if 0 <= ny < N and 0 <= nx < N and visited == 0:
                if corridor[ny][nx] == "S": 
                    return False
                if corridor[ny][nx] == "T" or corridor[ny][nx] == "O":
                    pass
                elif corridor[ny][nx] == "X":
                    visited[ny][nx] = 1
                    q.append((ny,nx))
    return True   

def set_block(cnt):
    global corridor
    global rlt
    if cnt == 3: # 장애물 설치 
        # print("설치완료")
        # print(corridor)
        if bfs():
            rlt = True 
            return
    else:
        for row in range(N):
            for col in range(N):
                if corridor[row][col] == "X":
                    corridor[row][col] = "O"
                    set_block(cnt + 1)
                    corridor[row][col] = "X"

N = int(input()) # 복도의 크기 
corridor = [input().split() for _ in range(N)]
T = []
for i in range(N):
    for j in range(N):
        if corridor[i][j] == "T":
            T.append((i,j))

set_block(0)
rlt = False
if rlt: # true면
    print("YES")
else:
    print("NO")



    







        


