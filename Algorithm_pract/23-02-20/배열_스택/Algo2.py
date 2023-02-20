import sys
sys.stdin = open('algo2_sample_in.txt')

# 문제 2: 탐사 로봇

'''
탐색 구역 : N x N 
로봇이 움직일 수 있는 방향 
dx = [1,0,-1,0]
dy = [0,1,0,-1]

로봇의 출발 위치 (0,0)
로봇은 노란색 칸에서 방향 전환 후 멈춤 

이동 방향이 0 1 1 0 3 3 2 라면 
에너지 소비를 표시하는 방법은 연속으로 중복된 숫자를 제거하여 나타낸다. 따라서 0 1 0 3 2 이다 

각 테스트 케이스의 에너지 소비를 출력해라 
'''

def energy_use(N,area_info):
    '''
    로봇이 area_info에 따라 이동할때의 에너지 소비를 출력하는 함수

    # 시작 + 방향전환 할때마다 리스트에 담기
    # 방문체크할 리스트를 만들어서 방문한곳 다시 방문하지 않도록 함

    :param N: 구역의 크기 N x N
    :param area_info: 구역에서 각 칸의 이동방향 정보가 포함된 2차원 리스트
    :return: 에너지 소비 반환
    '''
    # 방문체크용 리스트
    visited = [[0]*N for _ in range(N)]
    # 시작 위치
    y,x = 0, 0
    # 에너지 소비
    energy = [area_info[y][x]] # 시작위치의 방향은 무조건 에너지 소비에 들어가므로 미리 넣고 시작
    # 이동방향
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    #이동 시작
    while True:
        # 현재위치 방문 체크
        visited[y][x] = 1
        # 현재 위치의 이동 방향
        d = area_info[y][x]
        # 다음 칸 위치
        ny, nx = y + dy[d], x + dx[d]

        if visited[ny][nx]: # 이미 방문 했다면 # 다음 칸으로 나아갈 수 없으므로 종료
            print(*energy)
            return
        else: # 방문한 적 없다면
            if energy[-1] == area_info[ny][nx]: # 방향 전환이 안됐으면
                y, x = ny, nx
            else: # 방향 전환이 됐으면
                energy.append(area_info[ny][nx]) # 에너지 소비에 추가함
                y, x = ny, nx

T = int(input())
for i in range(1,T+1):
    # 구역의 크기 N x N
    N = int(input())
    area_info = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{i}', end = ' ')
    energy_use(N,area_info)
