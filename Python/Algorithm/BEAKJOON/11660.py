import sys

N, M = map(int, sys.stdin.readline().strip().split())
nums = []

for _ in range(N) :
    line = list(map(int, sys.stdin.readline().strip().split()))
    nums.append(line)

commends = []
maxX = -1
maxY = -1
for _ in range(M) :
    line = list(map(lambda x : int(x) - 1, sys.stdin.readline().strip().split()))
    if (maxY < line[2]) : maxY = line[2]
    if (maxX < line[3]) : maxX = line[3]
    commends.append(line)

sums = [[0 for _ in range(N)] for _ in range(N)]
sums[0][0] = nums[0][0]
for row in range(maxY + 1) :
    for col in range(maxX + 1) :
            
        if (row == 0 and col != 0) :
            sums[0][col] = sums[0][col - 1] + nums[0][col]
        elif (col == 0 and row != 0) :
            sums[row][0] = sums[row - 1][0] + nums[row][0]
        elif (row != 0 and col != 0) :
            sums[row][col] = sums[row - 1][col] + sums[row][col - 1] - sums[row - 1][col - 1] + nums[row][col]


for i in range(M) :
    
    r1= commends[i][0]
    c1= commends[i][1]
    r2= commends[i][2]
    c2= commends[i][3]
    if (r1 == r2 and c1 == c2) :
        print(nums[r2][c2])
    elif (r1 == 0 and c1 == 0) :
        print(sums[r2][c2])
    elif (r1 == 0 and c1 != 0) :
        s = sums[r2][c2] - sums[r2][c1 - 1]
        print(s)
    elif (r1 != 0 and c1 == 0) :
        s = sums[r2][c2] - sums[r1 - 1][c2]
        print(s)
    else :
        s = sums[r2][c2] - sums[r2][c1 - 1] - sums[r1 - 1][c2] + sums[r1 - 1][c1 - 1]
        print(s)