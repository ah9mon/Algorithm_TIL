import sys

A, B, C = map(int, sys.stdin.readline().strip().split())
if (C % 2) :
    print(A ^ B)
else :
    print(A)