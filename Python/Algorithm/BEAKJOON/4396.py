import sys

def findBombs(y,x) :
    global N
    count = 0
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= nx < N and 0 <= ny < N) :
            if (bombs[ny][nx] == '*') :
                count += 1
    
    return count

def revealBombs() :
    for row in range(N) :
        for col in range(N) :
            if (bombs[row][col] == '*') :
                player[row][col] = '*'

N = int(sys.stdin.readline())
bombs = [[] for _ in range(N)]
for i in range(N) :
    line = list(sys.stdin.readline())
    bombs[i] = line

player = [[] for _ in range(N)]
for i in range(N) :
    line = list(sys.stdin.readline())
    player[i] = line

dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]


for row in range(N) :
    for col in range(N) :
        if (player[row][col] == 'x') :
            if (bombs[row][col] == '*' and player[row][col] != '*') :
                revealBombs()
            else :
                player[row][col] = str(findBombs(row, col))

for i in range(N) :
    print(''.join(player[i]).strip())