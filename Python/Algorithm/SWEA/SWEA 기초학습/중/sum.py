import sys
sys.stdin = open('input2.txt')


def max_sum(list):
    # 각 행의 합 중에서 가장 큰 값을 max_sum_row에 할당 

    max_sum_row = -1 # 행 합 최댓값 max_sum_r 초기값

    for row in list:
        if max_sum_row < sum(row):
            max_sum_row = sum(row)

    # print(max_sum_row)
    
    # 각 열의 합 중에서 가장 큰 값을 max_sum_column 에 할당
 
    max_sum_column = -1 # 열 합 최댓값의 초기값 

    for i in range(100):
        sum_of_column = 0 

        for j in range(100):
            sum_of_column += list[j][i]

        if max_sum_column < sum_of_column:
            max_sum_column = sum_of_column
     
    # print(max_sum_column)
    
    # (0,0) 부터 (99,99) 대각선의 합 
    sum_of_di1 = 0
    for k in range(100):
        sum_of_di1 += list[k][k]

    # print(sum_of_di1)

    # (99,0) 부터 (0,99) 대각선의 합 
    sum_of_di2 = 0
    for k in range(100):
        sum_of_di2 += list[99-k][k]

    # print(sum_of_di2)

    # 각 행/ 각 열/ 각 대각선의 합 中 가장 큰거 반환 
    return max([max_sum_row, max_sum_column, sum_of_di1, sum_of_di2])
    

for i in range(1,11):
    tc = input()
    num_array = [list(map(int,input().split())) for j in range(100)]

    print(f'#{tc} {max_sum(num_array)}')


