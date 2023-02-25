# minmax

import sys
sys.stdin = open('input_for_4828.txt')

T = int(input())

for i in range(1,T+1):
    N = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    print(f'#{i} {nums[-1]-nums[0]}')