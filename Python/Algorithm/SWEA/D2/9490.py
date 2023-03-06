#풍선파파파파ㅏㅍㅇ

'''


풍선의 A만큼 상하좌우로 A개 퍼짐 
총 4A + 1

N x M 행렬에서 풍선 터트렷을 때 날릴 수 있는 꽃가루의 합 중 최대값 출력 
'''

import sys
sys.stdin = open('input_for_9490.txt')

def func():
    global max_rlt
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for row in range(N):
        for col in range(M):
            # 가운데는 무조건 터지니까 + 1
            ny, nx = row, col
            counts = graph[row][col]  # 해당좌표의 꽃가루 개수 더라기 
            for i in range(4):
                # 체크하려는 좌표로 이동
                ny = row + dy[i] 
                nx = col + dx[i]
                move = 1 # 이동 횟수 카운트용 
                while 0<=ny<N and 0<=nx<M and move <= graph[row][col] : # 범위 내에 있고 이동횟수가 graph[row][col] 초과가 아니면 
                    counts += graph[ny][nx] # 해당 좌표의 꽃가루 개수 더하기 
                    # 체크하려는 좌표로 이동 
                    ny += dy[i]
                    nx += dx[i]
                    move += 1 
            
            if counts > max_rlt:
                max_rlt = counts

T = int(input())
for i in range(1,T+1):
    N,M = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(N)]
    max_rlt = -1
    func()
    print(f'#{i} {max_rlt}')

