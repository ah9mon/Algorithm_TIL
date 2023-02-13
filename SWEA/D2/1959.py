# 두개의 숫자열 
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PpoFaAS4DFAUq&categoryId=AV5PpoFaAS4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2
# 
#
import sys
sys.stdin = open('input_for_1959.txt')

def func(N, A, M, B):
    # 원소의 개수가 적거나 같은쪽이 N,A
    # 원소의 개수가 큰쪽이 M,B

    if N <= M :
        n, a, m ,b = N, A, M, B
    else: 
        n, a, m ,b = M, B, N, A
    

    max_sum = 0 # 최댓값의 초기값

    
    '''
    위치 변경을 for문으로 구현 a를 한칸씩 미는 것
    == 한칸 앞의 b의 원소와 곱하는 것
    i : a가 몇칸을 움직였는지 표현
    j : a의 현재 인덱스 
    a[j] * b[j+i] 를 통해 '이동 후 마주보는 칸을 곱한다'를 구현 
    '''
    for i in range(m - n + 1):  
        sum_1 = 0
        for j in range(n):
            sum_1 += a[j] * b[j+i] 
        
        if max_sum < sum_1:
            max_sum = sum_1 
    
    return max_sum

T = int(input())

for i in range(1,T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(f'#{i} {func(N,A,M,B)}')

