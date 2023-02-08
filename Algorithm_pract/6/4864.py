# 문자열 비교 
import sys
sys.stdin = open("input (3).txt")

T = int(input())

for i in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    num_list.sort()
    print(f'#{i} {" ".join(str(x) for x in num_list)}')
