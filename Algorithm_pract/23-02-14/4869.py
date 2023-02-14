# 종이붙이기

import sys
sys.stdin = open('input_for_4869.txt')

def pd(N):
    '''
    20xN 크기의 직사작형을 20x10, 10x20, 20x20의 테이프로 붙이는 경우의 수를 반환하는 함수

    #param
    N : 직사각형의 가로 크기 (10 <= N <= 300 / N % 10 == 0)
    '''

    d = [0] * (N//10 + 1) # 메모이제이션을 위한 리스트 생성

    #초기값 입력
    d[1] = 1
    d[2] = 3

    # d[i] = d[i-1] + d[i-2] * 2 인 점화식을 이용해서 d[i] 할당
    for i in range(3,N//10+1):
        d[i] = d[i-1] + d[i-2]*2
    return d[N//10]

T = int(input())

for i in range(1,T+1):
    N = int(input())
    print(f'#{i} {pd(N)}')