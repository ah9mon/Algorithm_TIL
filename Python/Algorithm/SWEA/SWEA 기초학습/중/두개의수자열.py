import sys

sys.stdin = open('input.txt', 'r')

def max_sum_find(n,m,ai,bi):
    
    if n >= m :
        high, low, hi, li = n, m, ai, bi
        
    else:
        high, low, hi, li = m, n, bi, ai

    
    
    max_sum = 0
    for i in range(abs(n-m) + 1): # 한턴마다 위치 변경 
        sum1 = 0
        for j in range(low): # 마주보는 숫자들 곱하기
            sum1 += li[j] * hi[j + i] 
        
        if max_sum < sum1: # 만약 곱들의 합이 max_sum 보다 크면
            max_sum = sum1
    
    return max_sum
        


T = int(input())

for i in range(1,T+1):
    N,M = map(int,input().split())
    Ai = list(map(int,input().split()))
    Bi = list(map(int,input().split()))
    print(f'#{i} {max_sum_find(N,M,Ai,Bi)}')
    