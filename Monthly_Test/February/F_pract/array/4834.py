# 숫자 카드 

import sys
sys.stdin = open('input_for_4834.txt')

T = int(input())

for i in range(1,T+1):
    # 카드 장수 
    N = int(input())
    # 카드들 입력 받기 
    cards = list(map(int,input()))
    # 숫자 카운트용
    counts = [0]*10
    
    for j in range(N):
        counts[cards[j]] += 1
    
    # print(counts)

    max_count = max(counts)
    for index in range(10):
        if counts[index] == max_count:
            max_index = index
    
    print(f'#{i} {max_index} {counts[max_index]}')
