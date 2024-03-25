import sys

N, K = map(int, sys.stdin.readline().strip().split())
temps = list(map(int, sys.stdin.readline().strip().split()))
rlt = [0 for _ in range(N)]
rlt[0] = temps[0]

for i in range(1, N) :
    if (i >= K) :
        rlt[i] = rlt[i - 1] + temps[i] - temps[i - K]
    else :
        rlt[i] = rlt[i - 1] + temps[i]

print(max(rlt[K-1 :]))