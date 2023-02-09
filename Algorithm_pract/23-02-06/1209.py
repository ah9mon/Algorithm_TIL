# SUM
# import sys

# sys.stdin = open('input (3).txt')

def sum_func(n_list):
    max_sum = -1

    # 각 행에서 최댓값 찾기 
    for i1 in range(100): # 행
        if max_sum < sum(n_list[i1]): # i번 째 행의 합이 max_sum보다 크면
            max_sum = sum(n_list[i1])
    
    # print(max_sum)
    
    # 행의 합 최댓값과 각 열 최대값 비교 
    for j2 in range(100): # 열
        sum_column = 0
        for i2 in range(100):
            sum_column += n_list[i2][j2]
        if max_sum < sum_column:
            max_sum = sum_column
         
    # print(max_sum)

    # 오른쪾아래 방향 대각선 합과 비교 
    sum_right_diagonal = 0
    for i3 in range(100):
        sum_right_diagonal += n_list[0+i3][0+i3]
    
    if max_sum < sum_right_diagonal:
        max_sum = sum_right_diagonal

    # print(max_sum)

    # 왼쪽 아래 방향 대각선 합과 비교 
    sum_left_diagonal = 0
    for i3 in range(100):
        sum_left_diagonal += n_list[0+i3][99-i3]
    
    if max_sum < sum_left_diagonal:
        max_sum = sum_left_diagonal

    # print(max_sum)

    return max_sum

for i in range(1,11):
    tc = int(input())
    num_list = [list(map(int,input().split())) for j in range(100)]

    print(f'#{i} {sum_func(num_list)}')