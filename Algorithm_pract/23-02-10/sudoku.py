# 스도쿠 중복없는지 확인하는거 ㅇㅇ
#
import sys
sys.stdin = open("s_input.txt")

def sudoku_check(sudoku):
    set_1_to_9 = set(range(1,10))
    # 행 확인
    # print('행')
    for low1 in range(9): # 행
        # print(sudoku[low1])
        if set(sudoku[low1]) != set_1_to_9:
            # print(set(sudoku[low1]) , set_1_to_9 )
            # print(f'{low1}행 실패')
            return 0

    # 열 확인
    # print('열')
    for column1 in range(9):
        column_set = set()
        for low2 in range(9):
            column_set.add(sudoku[low2][column1])
        # print(column_set)
        if column_set != set_1_to_9:
            # print(column_set, set_1_to_9)
            # print(f'{column1}열 실패')
            return 0

    # 3X3 확인
    # print('nXn')
    for low3 in range(0,7,3):
        for column2 in range(0,7,3):
            nXn_set = set()
            for i in range(low3,low3+3):
                for j in range(column2,column2+3):
                    nXn_set.add(sudoku[i][j])
            # print(nXn_set)
            if nXn_set != set_1_to_9:
                # print(f'{low3} X {column2} 실패')
                return 0


    return 1


T = int(input())

for i in range(1,T+1):
    sudoku = [list(map(int,input().split())) for _ in range(9)]
    print(f'#{i} {sudoku_check(sudoku)}')
