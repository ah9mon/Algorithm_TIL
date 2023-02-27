import sys
sys.stdin = open('algo1_sample_in.txt')

# 문제 1 : 봉우리의 수

'''
가장 높은 봉우리와 가장 낮은 봉우리의 차이를 반환하는 함수 만들기 

1. 한 구역을 중심으로 주변 8개 구역보다 높으면 봉우리임
2. 가장자리 구역은 봉우리 아님 
3. 봉우리가 하나만 있거나 없는 경우, 높이차는 -1 표시 
'''


def check_mountain(N,mountain_map):
    '''
    산의 높이 정보가 담긴 지도를 받아서 가장 높은 봉우리와 가장 낮은 봉우리의 높이 차이를 반환하는 함수

    # 일단 봉우리 위치랑 높이를 리스트에 담기
    # 그 후에 sort하고 첫번째 인덱스의 값과 마지막 인덱스 값의 차이를 반환
    # 근데 len == 1 이하이면 -1 반환

    :param N:지도의 크기
    :param mountain_map: 산의 높이 정보 2차원 리스트
    :return: 봉우리가 1개 이하이면 -1 반환 / 봉우리가 2개 이상이면 가장 높은 봉우리와 가장 낮은 봉우리의 높이 차이 반환
    '''

    # 현재 위치의 위부터 시계방향으로 확인하기 위한 dy,dx
    dx = [0,1,1,1,0,-1,-1,-1]
    dy = [-1,-1,0,1,1,1,0,-1]
    # 봉우리 정보를 담을 리스트
    top_list = []
    for i in range(1,N-1): # 행 (가장자리는 어차피 봉우리가 아니니까 보지 않음)
        for j in range(1,N-1): #열
            # 현재 위치
            y,x = i,j
            # 현재 위치보다 낮은 영역 세기위한 변수
            count_near = 0 # 초기값
            # 위부터 시계방향으로 탐색
            for k in range(8):
                ny,nx = y + dy[k], x + dx[k]
                if mountain_map[ny][nx] < mountain_map[y][x]: # 현재위치보다 탐색하고 있는 위치가 낮으면
                    count_near += 1

                if count_near == 8 : # 현재위치가 주변 8개 영역보다 높으면
                    # (y,x,높이)
                    top_list.append((i,j,mountain_map[j][i])) # 현재 위치를 리스트에 추가

    # print(top_list)
    # 결과 출력
    if len(top_list) <= 1: # 만약 봉우리가 1개거나 없다면
        return -1 # -1 반환

    else: # 봉우리가 2개 이상이면
        top_list.sort(key = lambda x: x[-1]) # 높이 순으로 정렬하고
        high = top_list[-1][-1] # 높은 봉우리의 높이
        low = top_list[0][-1] # 낮은 봉우리의 높이
        return high - low # 봉우리의 높이 차이 반환


T = int(input())
for i in range(1,T+1):
    # 지도의 크기 N x N
    N = int(input())
    # 산의 높이 정보 받기
    mountain_map = [list(map(int,input().split())) for _ in range(N)]
    # check_mountain(N,mountain_map)
    print(f'#{i} {check_mountain(N,mountain_map)}')


