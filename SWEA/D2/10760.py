# 우주선 착륙 2
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXSHJueab1oDFAQT

import sys
sys.stdin = open('input_for_10760.txt')

def check(area, N, M):
    # 위부터 시계방향으로 확인하기 위한 dx, dy
    dx = (0, 1, 1, 1, 0, -1, -1, -1)
    dy = (-1, -1, 0, 1, 1, 1, 0 , -1)
    count_candidate = 0 # 후보지 카운트 
    # 탐색
    for i in range(N): #행
        for j in range(M): #열
            y,x = i,j # 인공위성의 위치 
            # 주변확인 
            count_near = 0 # 현재 위치에서 주변을 확인할 카운트 
            for k in range(8):
                ny, nx = y + dy[k], x + dx[k]
                if 0 <= ny < N and 0 <= nx < M and area[ny][nx] < area[y][x]: # ny,nx가 범위안에 있고 현재 확인하고 있는 곳의 높이가 인공위성이 위치한 곳의 높이보다 낮다면
                    count_near += 1
                
            if count_near >= 4: # 사진을 찍을 수 있는 방향이 4방향 이상이면 
                count_candidate += 1 # 후보지로 추가 
            
    return count_candidate


T = int(input())
for i in range(1,T+1):
    # 구역의 크기 (행, 열)
    N,M = map(int,input().split())
    area = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{i} {check(area, N, M)}')
