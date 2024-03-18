import sys

N = int(sys.stdin.readline())
for _ in range(N) :
    a, b = sys.stdin.readline().split()
    a = int(a, 2)
    b = int(b, 2)
    c = a + b
    c = bin(c)
    print(c[2:])