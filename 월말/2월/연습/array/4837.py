# 부분집합의 합 

import sys
sys.stdin = open('input_for_4837.txt')

def func(i,n,s):
    global arr
    global counts
    if n == N: # 원소의 수가 N개가 됏을때
        if s == K: # 집합의 합이 K면 
            counts += 1
            # print(arr)
        
        return
        
    if s > K: # 집합의 합이 K를 넘었을 때 조기 종료 
        return
    
    if i == 11: # 11번쨰 인덱스 까지 부분집합 만들었을 때
        return
    
    # print(i)
    arr[i] = A[i]
    func(i+1, n+1, s + A[i])
    arr[i] = 0
    func(i+1, n, s)

T = int(input())

for i in range(1,T+1):
    A = list(range(1,13))
    # 부분집합 원소의 수 , 부분 집합의 합 
    N, K = map(int,input().split())
    arr = [0]*12
    counts = 0
    func(0,0,0)
    print(f'#{i} {counts}')
    