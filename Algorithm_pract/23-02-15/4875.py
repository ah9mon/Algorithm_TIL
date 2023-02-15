# 미로
import sys
sys.stdin = open('input_for_4875.txt')

def miro(map1, visited, a, b):
    y, x = a, b
    visited[y][x] = 1 # 방문체크

    # 방문해야 하는 곳 리스트에 넣기
    stack = []
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]

        if 0<= ny < N and 0<= nx < N and map1[ny][nx] != 1 :
            stack.append((ny,nx)) # 가봐야 하는곳 스택에 추가

    while stack: # 스택이 빌때까지
        y,x = stack.pop()
        if not visited[y][x]: #방문 안했으면
            miro(map1, visited, y, x) # 방문

T = int(input())

for i in range(1,T+1):
    N = int(input())
    map1 = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    for j in range(N):
        if 2 in map1[j]:
            a,b = j, map1[j].index(2)
        elif 3 in map1[j]:
            c,d = j, map1[j].index(3)
    miro(map1, visited, a,b)
    # for k in range(N):
    #     print(visited[k])
    print(f'#{i} {visited[c][d]}')


