
# 문제 2 별자리 사진 찍기

'''
최대 크기로 사진찍기 위해 몇번 확인?
하늘의 전체 크기 N * N
카메라 초점 (A,B) 영역 K * K

한번 확대할 때 마다 영역 -> K - 2*n (n은 확대 횟수)

초점과 별들의 거리 재서 가장 멀리있는 별과의 x,y거리를 알면 될듯?
'''

def zoom(k,y,x):
    '''
    초점과 별과의 최대거리를 구하고
    카메라영역의 크기와 비교해서
    별을 카메라에 다 담을 수 있을 때까지
    zoom을 하고 그 zoom횟수를 반환하는 함수

    :param k: 카메라 촬영 영역의 크기 k*k
    :param y: 초점의 y좌표
    :param x: 초점의 x좌표
    :return: 카메라 최대 확대(zoom) 수
    '''
    K = k//2 # 초점의 중심과 카메라 촬영 영역 가장자리와의 수직/수평거리
    max_dy = -1 # 별과 초점의 최대 수직거리 초기값
    max_dx = -1 # 별과 초점의 최대 수평거리 초기값
    # 초점과 별과의 최대 거리 구하기
    for row in range(N): # 행
        for col in range(N): # 열
            if sky[row][col] == '*': # 별이면
                if abs(row - y) > max_dy: # 별과 초점의 수직거리가 그것의 최댓값보다 크면
                    max_dy = abs(row - y) # 새로운 최댓값으로 할당
                if abs(col - x) > max_dx: # 별과 초점의 수평거리가 그것의 최댓값보다 크면
                    max_dx = abs(col - x) # 새로운 최댓값으로 할당

    max_distance = max(max_dy, max_dx) # 별과의 최대 거리를 변수에 할당
    if max_distance == -1: # 에초에 하늘에 별이 없었을 경우 
        return -1

    # 확대 횟수 구하기
    # 카메라 zoom 할때마다 초점과 카메라 촬영역영 가장자리와의 수직/수평거리는 -1이됨
    # 따라서 결국 별과의 최대거리와 K간의 차이가 zoom의 최대카운트가됨
    cnt = K - max_distance

    # print(f'max_d : {max_distance}')
    # print(f'cnt : {cnt} K : {K}')

    if cnt < 0: # 에초에 K의 초기값으로 별을 다 담지 못하면
        return -1
    else:
        return cnt

T = int(input())
for i in range(1,T+1):
    # 하늘 크기, 초기 카메라 영역 크기, 카메라 초점 y,x
    N, K, A, B = map(int,input().split())
    # 하늘 별자리 정보 2차원 리스트로 입력 받기
    sky = [input().split() for _ in range(N)]
    print(f'#{i} {zoom(K,A,B)}')