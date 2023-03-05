# 농작물 수확하기 

'''
N x N 크기의 농장 

농장의 크기는 항상 홀수 (N이 홀수)

농작의 크기에 맞게 마름모 모양으로 수확함 
그만큼 탐색해서 총 수확량을 구하기 
'''
import sys 
sys.stdin = open('input_for_15002.txt')


T = int(input())
for i in range(1,T+1):
    N = int(input())
    center = N // 2
    rlt = 0
    for row in range(N):
        arr = list(map(int,input()))
        if (center - row) >= 0: 
            earn = sum(arr[center-row : center+row+1])
            rlt += earn
        else:
            earn = sum(arr[center-(N-1-row) : center+(N-row)])
            rlt += earn
    print(f'#{i} {rlt}')
        

