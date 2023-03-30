# 최소 생산 비용 
# SWEA D3

'''
일단 다 완성하는 데
종료조건을 주자
'''
import sys
sys.stdin = open('input_for_14013.txt')


def func(start,end,sum_s):
    '''
    param
    start : 생산할 제품을 결정해야하는 공장 번호 (0 ~ N-1)
    end : 공장 수 & 제품 수
    sum_s : 현재까지 생산할 제품을 결정한 공장들의 생산 비용의 합
    '''
    global min_sum

    # 최소값보다 커지면 다음줄 더해볼 것 없이 실패이므로 종료 
    if min_sum <= sum_s:
        return

    # 마지막 줄까지 다 더했으면 
    if start == end:
        # print(f'공장 현황 : {used} / 총액 : {sum_s}')
        min_sum = sum_s
        return

    for i in range(N):
        if not used[i]: # 생산하지 않고 있는 제품이면  
            used[i] = 1
            func(start+1, end, sum_s + prices[start][i]) 
            used[i] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 제품의 가지수 
    prices = [list(map(int,input().split())) for _ in range(N)]
    min_sum = 99*15
    used = [0]*N # 생산 제품 현황 1이면 생산중인거 0이면 생산 안하고 있는거 
    func(0,N,0)
    print(f'#{tc} {min_sum}')