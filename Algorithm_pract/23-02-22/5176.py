# 이진 탐색

# in_order

import sys
sys.stdin = open('input_for_5176.txt')

def dinary(n):
    global rlt
    if 2*n <= N: # 왼자식 있으면
        dinary(2*n)

    rlt.append(n)

    if 2*n+1 <= N: # 오른자식 있으면
        dinary(2*n+1)

T = int(input())

for i in range(1,T+1):
    N = int(input())
    rlt = []
    dinary(1)
    print(rlt)
    print(f'#{i} {rlt.index(1)+1} {rlt.index(N//2)+1}')

