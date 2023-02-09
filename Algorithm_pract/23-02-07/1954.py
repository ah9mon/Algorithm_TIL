# 달팽이
# 시계 방향 턴 함수 만들기 
# try except 로 
# out of range 뜨면 turn 

def snail(n):
    graph = [[0]*n for i in range(n)]
    v = 0 # 방향 
    dx = [1, 0, -1, 0] # v인덱스에 따른 dx
    dy = [0, 1, 0, -1] # v인덱스에 따른 dy
    x,y = 0, 0 # 시작지점 
    for i in range(1, n**2 + 1): # 1 ~ n^2
        graph[y][x] = i # 그래프에 숫자 넣기   
        nx, ny = x + dx[v], y + dy[v] # 앞으로 갈 블럭좌표       
        if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 0 : # 전진할 블럭이 범위안에 있고 0이면 
            x,y = nx, ny # 전진
        else : # 범위 밖에 있거나 0이 아니면
            # 방향 전환
            if v < 3: 
                v += 1
            else:
                v = 0
            # 전진 
            nx, ny = x + dx[v], y + dy[v]   
            x, y =nx, ny
    
    for index in graph:
        print(' '.join(str(x) for x in index))

T = int(input())

for i in range(1,T+1):
    N = int(input())
    print(f'#{i}')
    snail(N)
