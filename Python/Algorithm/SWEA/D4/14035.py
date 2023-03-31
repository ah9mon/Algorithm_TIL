# 격자판의 숫자 이어 붙이기 
'''
동서남북 한방향으로만 6번? 

'''
import sys
sys.stdin = open('input_for_14035.txt')

def func(x,y,c,num):
    if c == 7:
        rlt.add(num)
        return
    
    for v in range(4):
        nx = x + dx[v]
        ny = y + dy[v]
        if 0<= nx < 4 and 0 <= ny < 4:
            func(nx,ny,c+1,num+str(graph[ny][nx]))

T = int(input())
for tc in range(1,T+1):
    graph = [list(map(int,input().split())) for _ in range(4)]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    rlt = set()
    for x in range(4):
        for y in range(4):
            func(x,y,1,str(graph[y][x]))
    # print(rlt)
    print(f'#{tc} {len(rlt)}')
    
