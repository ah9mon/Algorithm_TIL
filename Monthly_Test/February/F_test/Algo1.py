
# 문제 1 정원에 나무 심기

'''
나무 0부터 짝수로 col 한줄로 심음
정원에 나무 심기 총 비용과 심은 나무의 수 
심은 나무 중 가장 비싼 나무의 가격과 해당 col의 인덱스를 출력  
가장 비싼 나무가 여러개 심어져 있으면 가장 큰 열의 번호를 계산 
'''

def cost(N,M,garden):
    '''
    각 행을 탐색해서
    총 나무 심기 비용,
    총 나무 수,
    가장 가격이 높은 나무,
    가장 가격 높은 나무가 있는 열의 위치
    찾는 함수

    :param N: 정원 행의 개수
    :param M: 정원 열의 개수
    :param garden: 정원의 나무 가격 정보
    :return: print(총 나무 심기 비용, 총 나무 수, 가장 가격이 높은 나무의 가격, 가장 가격 높은 나무가 있는 열의 위치 )
    '''
    global max_cost_namu # 가장 가격이 높은 나무의 가격
    global max_cost_namu_col # 가장 가격 높은 나무가 있는 열의 위치
    total_cost = 0 # 총 나무 심기 비용
    total_namu = 0 # 총 나무 수

    for row in range(N): #행 탐색
        # 0부터 격열 == 나무 심는 곳 == garden[row][0::2]
        total_cost += sum(garden[row][0::2]) # 현재 행에 심는 나무의 총 비용 더해주기
        total_namu += len(garden[row][0::2]) # 현재 행에 심는 나무의 수를 총 나무수에 더해주기
        for index in range(0,M,2): # 나무가 심어진 열을 탐색하여 최대값(최대 가격)을 꺼내 할당
            if garden[row][index] >= max_cost_namu: # 현재 [행][열]의 나무를 심는 비용이 최대 값보다 크면
                max_cost_namu = garden[row][index] # 전체 최대 가격으로 할당
                max_cost_namu_col = index + 1 # 최대가격의 column인덱스를 할당

    print(total_cost,total_namu,max_cost_namu,max_cost_namu_col)

T = int(input())

for i in range(1,T+1):
    # 정원의 크기 행, 열
    N,M = map(int,input().split())
    # 정원 맵 2차원 리스트로 입력 받기
    garden = [list(map(int,input().split())) for _ in range(N)]
    max_cost_namu = 0 # 가장 가격이 높은 나무의 가격
    max_cost_namu_col = 0 # 가장 가격 높은 나무가 있는 열의 위치
    print(f'#{i}', end=' ')
    cost(N,M,garden)

