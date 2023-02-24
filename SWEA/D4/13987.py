# 홈 방범 서비스

# 탐색 방법 -> K는 비용 계산의 파라미터이자 bfs시 이동 횟수임
# 탐색하면서 집을 카운트 하면 됨

import sys
sys.stdin = open('input_for_13987.txt')

from collections import deque

def bfs(a,b):
    global max_counts
    # 상하좌우 탐색
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    # 방문 체크 및 거리 체크
    visited = [[0]*N for _ in range(N)]

    # 시작점 큐에 넣기
    q = deque()
    q.append((a,b))
    visited[a][b] = 1

    # 시작점이 집이 있는 위치인지 확인
    if maap[a][b]: # 시작점에 집이 있으면 카운트 하고 시작
        counts = 1
    else: # 없으면 카운트 0으로 시작
        counts = 0

    while q:
        cost = K**2 + (K-1)**2 # 방범 비용
        y,x = q.popleft()
        if visited[y][x] < K: # 방범범위 안에 있는 곳만 탐색
            for i in range(4): # 상하좌우 체크
                ny,nx = y+dy[i], x+dx[i] # 현재의 탐색 위치
                if 0 <= ny < N and 0<= nx < N and not visited[ny][nx]: # 범위안에 있고 방문한적 없으면 탐색
                    q.append((ny,nx))
                    visited[ny][nx] = visited[y][x] + 1 # 거리체크
                    if maap[ny][nx]: # 집이 있으면
                        counts += 1 # 카운트

    if cost <= counts*M and max_counts < counts: # 수지타산 맞고 최댓값이면
        max_counts = counts # 할당

T = int(input())
for i in range(1,T+1):
    # 도시의 크기 , 집이 지불할 수 있는 비용
    N, M = map(int,input().split())
    # 도시정보 (집위치)
    maap = [list(map(int,input().split())) for _ in range(N)]
    max_counts = 0 # 최댓값의 초기 값
    K = 0 # 방범 범위
    while K < N+1:
        K += 1
        # 완전 탐색
        for row in range(N):
            for col in range(N):
                bfs(row,col)

    print(f'#{i} {max_counts}')