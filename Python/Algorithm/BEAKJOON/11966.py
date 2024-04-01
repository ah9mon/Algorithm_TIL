import sys

N = int(sys.stdin.readline())
if (N & (N - 1)) :
    print(0)
else :
    print(1)