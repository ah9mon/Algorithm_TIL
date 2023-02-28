import sys
sys.stdin = open('input_for_5185.txt')

T = int(input())

for i in range(1,T+1):
    N, arr = tuple(input().split())
    N = int(N)
    print(f'#{i}', end=' ')
    for x in arr:
        num = int(x, 16)
        for j in range(3, -1, -1):
            bit = 1 if num & (1 << j) else 0
            print(bit, end='')

    print('')






