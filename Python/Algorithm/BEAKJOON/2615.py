import sys

def isWin(row, col, v) : 
    color = board[row][col] # 검은색 : 1 / 흰색 : 2

    for i in range(1, 5) :
        nextCooldinate = getNextCooldinate(row, col, i, v)
        nextR = nextCooldinate[0]
        nextC = nextCooldinate[1]

        if (0 <= nextR < 19 and 0 <= nextC < 19 and visited[nextR][nextC] == 0) :
            if (board[nextR][nextC] == color) :
                visited[nextR][nextC] = 1
            else :
                break

            if (i == 4) :
                
                if (0 <= nextR + 1 < 19 and 0 <= nextC + 1 < 19) :
                    if (board[nextR + 1][nextC + 1] != color) :
                        return True
                else :
                    return True
        else :
            break
    
    
    return False

def getNextCooldinate(row, col, i, v) :
    nextR = -1
    nextC = -1

    if (v == 1) : # 대각선 1
        nextR = row + i
        nextC = col + i
    elif (v == 2) : # 대각선 2
        nextR = row - i
        nextC = col + i
    elif (v == 3) : # 가로
        nextR = row
        nextC = col + i
    elif (v == 4) : # 세로
        nextR = row + i
        nextC = col

    return [nextR, nextC]

board = [[] for _ in range(19)]
for i in range(19) :
    line = list(sys.stdin.readline().strip().split())
    board[i] = line

visited = [[0 for _ in range(19)] for _ in range(19)]
whiteWin = False
blackWin = False

for v in range(1,5) :
    
    if (v == 2) :
        for row in range(18, -1, -1) :
            for col in range(19) :
                if (board[row][col] != '0' and visited[row][col] == 0) :
                    if (board[row][col] == '1') :
                        blackWin = isWin(row, col, v)
                    else :
                        whiteWin = isWin(row, col, v)
                    visited[row][col] = 1
                
                if (blackWin) :
                    print(1)
                    print(row + 1, col + 1)
                    break
                elif (whiteWin) :
                    print(2)
                    print(row + 1,col + 1)
                    break
            if (blackWin or whiteWin) :
                break
        
        if (blackWin or whiteWin) :
                break
            
    else :
        for row in range(19) :
            for col in range(19) :
                if (board[row][col] != '0' and visited[row][col] == 0) :
                    if (board[row][col] == '1') :
                        blackWin = isWin(row, col, v)

                    else :
                        whiteWin = isWin(row, col, v)
                    visited[row][col] = 1
                
                if (blackWin) :
                    print(1)
                    print(row + 1, col + 1)
                    break
                elif (whiteWin) :
                    print(2)
                    print(row + 1, col + 1)
                    break

            if (blackWin or whiteWin) :
                break
        
        if (blackWin or whiteWin) :
                break
    
    visited = [[0 for _ in range(19)] for _ in range(19)]

