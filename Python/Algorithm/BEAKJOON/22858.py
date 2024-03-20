import sys

N, K = map(int, sys.stdin.readline().split())
S = list(map(int, sys.stdin.readline().split()))
D = list(map(int, sys.stdin.readline().split()))

for _ in range(K) :
    P = [0 for _ in range(N)]
    for i in range(N) :
        P[D[i] - 1] = S[i]
    S = P

print(' '.join(map(str, S)))