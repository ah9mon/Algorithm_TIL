# 오목 판정 

'''
NxN크기의 판 
판에는 돌이 잇거나 없음 
주던에 돌이 가로 세로 대각선에  5개 이상 연속되는게 잇는지 없는지 판정해라 

5개이상 있으면 'YES'
없으면 'NO'
'''
import sys
sys.stdin = open("input_for_15155.txt")

def func():
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [1, -1 , 0, 0, -1, 1, 1, -1]

    for row in range(N):
        for col in range(N):
            for i in range(8): # 가로 세로 대각선 확인 
                counts = 0 # 연속된거 카운트 
                ny,nx = row,col # 현재위치 초기값
                while 0<= ny < N and 0<= nx < N:
                    if graph[ny][nx] == "o": # 돌이면 
                        counts += 1 # 카운트 + 1
                        if counts == 5: # 카운트가 5가되면 
                            return "YES" # yes반환 및 종료 
                    else: # 돌이 아니면 
                        counts = 0 # 카운트 초기화 
                    
                    # 다음칸 확인 
                    ny += dy[i] 
                    nx += dx[i]
    return "NO" # 연속 5개 없음 

T = int(input())
for i in range(1,T+1):
    N = int(input())
    graph = [input() for _ in range(N)]
    print(f'#{i} {func()}')

