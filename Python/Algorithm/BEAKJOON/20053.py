import sys

t = int(sys.stdin.readline())
for _ in range(t) :
    n = sys.stdin.readline()
    num_list = list(map(int, sys.stdin.readline().split()))
    num_list.sort()
    print(f"{num_list[0]} {num_list[-1]}")