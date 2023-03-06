# 당근 포장하기 

import sys
sys.stdin = open('input_for_16811.txt')

'''
N개의 당근 -> 대 중 소 상자로 구분 포장 

같은 크기의 당근은 같은 상자로 

비어있는 상자 있으면 안됨 

한상자 당 N//2 이하 

+ 당근의 개수 차이가 최소가 되어야함
'''

T = int(input())
for i in range(1,T+1):
    N = int(input()) # 당근의 개수
    carrots = list(map(int,input().split()))
    max_size = max(carrots)
    carrots_counts = [0] * (max_size + 1)
    for carr in carrots:
        carrots_counts[carr] += 1
    
    min_d = 1000 # 최소개수차이
    # 소 상자 크기 제한 
    for s in range(1,max_size-1):
        for m in range(s+1,max_size):
                S = sum(carrots_counts[1:s+1])
                M = sum(carrots_counts[s+1:m+1])       
                L = sum(carrots_counts[m+1:])
        
                if S > N//2 or M > N//2 or L > N//2: # 한상자에 N//2 초과로 들어가면 실패
                    continue
                if not S or not M or not L: # 빈상자가 있으면 실패 
                    continue 
                
                d = max( abs(S-M), abs(S-L), abs(M-L))
                if d < min_d:
                    min_d = d

    if min_d == 1000:
        print(f'#{i} {-1}')
    else: 
        print(f'#{i} {min_d}')

    
