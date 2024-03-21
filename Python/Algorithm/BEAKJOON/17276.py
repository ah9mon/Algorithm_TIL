import sys
def getNewRowCol(row, col, center) :
    global d
    v = -1 if (d > 0) else 1
    newR = -1
    newC = -1
    if (v < 0) :
        if (row < center and col <= center) :
            newR = row
            newC = col - (row - center)
        
        elif (row <= center and col > center) :
            newR = row - (center - col)
            newC = col
            
        elif (row > center and col >= center) :
            newR = row
            newC = col - (row - center)
            
        elif (row >= center and col < center) :
            newR = row - (center - col)
            newC = col
    elif (v > 0) :
        if (row <= center and col < center) :
            newR = row + (center - col)
            newC = col
        
        elif (row < center and col >= center) :
            newR = row
            newC = col + (row - center)
            
        elif (row >= center and col > center) :
            newR = row + (center - col)
            newC = col 
            
        elif (row > center and col <= center) :
            newR = row 
            newC = col + (row - center)


    return [newR, newC]

def rotate() :
    global n
    newArr = [["" for _ in range(n)] for _ in range(n)]
    center = n//2
    newArr[center][center] = arr[center][center]

    # 대각선 1
    for index in range(n) :
        if (index != center and index != center) :
            newCooldinate = getNewRowCol(index, index, center)
            newR = newCooldinate[0]
            newC = newCooldinate[1]
            newArr[newR][newC] = arr[index][index]


    # 대각선 2
    for index in range(n) :
        if (index != center and ((n-1) - index) != center) :
            newCooldinate = getNewRowCol(index, (n-1) - index, center)
            newR = newCooldinate[0]
            newC = newCooldinate[1]
            newArr[newR][newC] = arr[index][(n-1) - index]
    
    # 가운데 행 
    for index in range(n) :
        if (index != center):
            newCooldinate = getNewRowCol(center, index, center)
            newR = newCooldinate[0]
            newC = newCooldinate[1]
            newArr[newR][newC] = arr[center][index]
    
    # 가운데 열
    for index in range(n) :
        if (index != center):
            newCooldinate = getNewRowCol(index, center, center)
            newR = newCooldinate[0]
            newC = newCooldinate[1]
            newArr[newR][newC] = arr[index][center]


    for row in range(n) :
        for col in range(n) :
            if (newArr[row][col]) :
                arr[row][col] = newArr[row][col]


T = int(sys.stdin.readline())
for _ in range(T) :
    n, d = map(int, sys.stdin.readline().split())
    arr = [[] for _ in range(n)]
    for i in range(n) :
        line = list(sys.stdin.readline().strip().split())
        arr[i] = line

    if (d != 0 and d != 360 and d != -360) :
        for _ in range(abs(d // 45)):
            rotate()

    for j in range(n) :
        print(' '.join(arr[j]))