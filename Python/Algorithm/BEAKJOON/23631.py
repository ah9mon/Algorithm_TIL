'''
진심 좌우 반복 뛰기 

https://www.acmicpc.net/problem/23631
'''

T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    '''
    location  2 -2  4 -4  6 -6 ... 
    move      1  2  3  4  5  6 ... 
    i         0  1  2  3  4  5 ...
    i//2      0  0  1  1  2  2 ...
    distance = K * (n*(n+1) // 2)
    distance > N인 n을 구하자 (이진탐색으로)
    '''
    

