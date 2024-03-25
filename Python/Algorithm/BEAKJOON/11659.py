import sys

N, M = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))
commends = [[0,0] for _ in range(M)]

maxN = -1
for i in range(M) :
    a,b = map(int, sys.stdin.readline().strip().split())
    a -= 1
    b -= 1

    if (maxN < b) : maxN = b

    commends[i][0] = a
    commends[i][1] = b

sums = [0 for _ in range(N)]
sums[0] = nums[0]

for i in range(1, maxN + 1) :
    sums[i] = sums[i - 1] + nums[i]

for i in range(M) :
    a = commends[i][0]
    b = commends[i][1]
    if (a > 0) :
        print(sums[b] - sums[a - 1])
    else :
        print(sums[b])