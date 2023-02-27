# 부분집합의 합 

# 부분집합 구하기 
import sys

sys.stdin = open('sample_input (1).txt')

def num_of_part(N1,K):
    arr = list(range(1,13)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N = len(arr) # 12
    count = 0 
    
    for i in range(1<<N): # 2**N
        part = []
        for j in range(N):
            if i & (1<<j):
                part.append(arr[j])
                
        if len(part) == N1 and sum(part) == K:
            count += 1

    return count

T = int(input())

for i in range(1,T+1):

    N1, K = map(int, input().split())
    print(f'#{i} {num_of_part(N1,K)}')

