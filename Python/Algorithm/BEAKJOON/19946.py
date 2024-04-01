import sys

N = int(sys.stdin.readline())
count = 0
str = bin(N)
n = len(str[3:].strip('1'))
print(64 - n)
