# 색칠하기
import sys

sys.stdin = open('sample_input (1).txt')

def purples(color_list, graph):
    
    purple_count = 0 # 3이면 보라색으로 인식 할건데 인식할때마다 카운트 + 1
    for info in color_list: 
        y1,x1,y2,x2,color = tuple(info)
        # print(y1,x1,y2,x2,color)
        dx = [0,0,1,0,-1] # 인덱스 순서대로 (현재 위치, 위, 우, 아래, 좌)
        dy = [0,-1,0,1,0] # 인덱스 순서대로 (현재 위치, 위, 우, 아래, 좌)
        for i in range(y1, y2+1): # 시작 y좌표 ~ 종료 y좌표
            for j in range(x1, x2+1): # 시작 x 좌표 ~ 종료 x 좌표
                for k in range(5): # 인덱스 순서대로 (현재 위치, 위, 우, 아래, 좌) 
                    ny, nx = i + dy[k], j + dx[k] # 인덱스 순서대로 (현재 위치, 위, 우, 아래, 좌)                 
                    if  y1<= ny <= y2 and x1 <= nx <= x2 and graph[ny][nx] != color: # 현재 칠하려는 곳이 현재 색상이랑 다르고 현재 위치가 범위안에 있으면 
                        graph[ny][nx] += color # 칠함
                        # print(f'현재 위치 {ny, nx}')
                        # print(f'현재 위치 색{graph[ny][nx]}')
                        if graph[ny][nx] == 3: # 칠햇는데 보라색이면 
                            purple_count += 1 # 카운트 + 1

    return purple_count
            

T = int(input())

# graph = [[0] * 10 for i in range(10)]

for j in range(1, T+1):
    graph = [[0] * 10 for i in range(10)]
    N = int(input())
    color_info = [list(map(int,input().split())) for k in range(N)]
    print(f'#{j} {purples(color_info, graph)}')

