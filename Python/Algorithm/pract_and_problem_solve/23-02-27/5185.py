# 이진수
import sys
sys.stdin = open('input_for_5185.txt')

T = int(input())
for i in range(1,T+1):
    # 자리수 , 16진수
    N, f = tuple(input().split())
    a = int(f,16)
    # print(type(bin(a)))
    print(f'#{i} {"0"+bin(a)[2:]}')