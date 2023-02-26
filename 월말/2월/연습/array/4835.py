# 구간합 

'''
N 개의 정수가 들어있는 배열에서 
이웃한 M개의 합을 계산 

M 개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력
'''

import sys
sys.stdin = open('input_for_4835.txt')

def func(n,m,arr):
    max_sum = 0
    min_sum = 123456789
    for i in range(N-M+1):
        sum_now = sum(arr[i:i+M])
        if sum_now > max_sum:
            max_sum = sum_now
        
        if sum_now < min_sum:
            min_sum = sum_now
    
    return max_sum - min_sum

T = int(input())

for i in range(1,T+1):
    # 정수의 개수, 구간의 개수 
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))
    print(f'#{i} {func(N,M,arr)}')
