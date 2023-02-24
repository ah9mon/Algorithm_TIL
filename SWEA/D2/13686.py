# 백만 장자 프로젝트

import sys
sys.stdin = open('input_for_13686.txt')





T = int(input())
for i in range(1,T+1):
    N = int(input())
    price = list(map(int,input().split()))
    sum1 = 0
    max_price = price[-1]
    for j in range(N-1,-1,-1):
        if price[j] < max_price:
            sum1 += max_price - price[j]
        else:
            max_price = price[j]

    print(f'#{i} {sum1}')
