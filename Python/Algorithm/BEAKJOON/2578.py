import sys

def findBingo() :
    count = 0

    # 가로 탐색
    for row in range(5) :
        line_count = 0
        for col in range(5) :
            if (board[row][col] == 0) :
                line_count += 1
        
        if (line_count == 5) :
            count += 1
            if (count >= 3) :
                return True

    # 세로 탐색
    for col in range(5) :
        line_count = 0
        for row in range(5) :
            if (board[row][col] == 0) :
                line_count += 1
        
        if (line_count == 5) :
            count += 1
            if (count >= 3) :
                return True
    
    # 대각선 탐색 
    line_count = 0
    for i in range(5):
        if (board[i][i] == 0) :
            line_count += 1
    
    if (line_count == 5) :
        count += 1
        if (count >= 3) :
                return True

    line_count = 0
    for i in range(5):
        if (board[4 - i][i] == 0) :
            line_count += 1
    
    if (line_count == 5) :
        count += 1
        if (count >= 3) :
                return True
    
    return False


board = [[0 for _ in range(5)] for _ in range(5)]
board_info = [[0, 0] for _ in range(25 + 1)]
for row in range(5) :
    line = list(map(int,sys.stdin.readline().split()))
    for col in range(5):
        board_info[line[col]][0] = row
        board_info[line[col]][1] = col
        board[row][col] = line[col]

for i in range(5) :
    line2 = list(map(int,sys.stdin.readline().split()))
    for j in range(5) :
        num = line2[j]
        board[board_info[num][0]][board_info[num][1]] = 0
        
        if (findBingo()) : 
            print(i * 5 + (j + 1))
            sys.exit()
            
