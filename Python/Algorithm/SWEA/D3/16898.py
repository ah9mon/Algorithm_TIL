# SWEA D3
# 부분수열의 합 

import sys
sys.stdin = open('input_for_16898.txt')
def func(s,e):
    global counts
    if s == e:
        if sum(bit) == K:
            counts += 1
        return
    
    else:
        bit[s] = arr[s]
        func(s+1,e)
        bit[s] = 0
        func(s+1,e)

T = int(input())
for i in range(1,T+1):
    # 자연수의 개수, 부분집합의 합
    N,K = map(int,input().split())
    arr = list(map(int,input().split()))
    bit = [0]*N
    counts = 0
    func(0,N)
    print(f'#{i} {counts}')

