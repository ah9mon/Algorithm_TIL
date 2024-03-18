import sys

num = sys.stdin.readline()
num_10 = int(num, 8)
num_2 = bin(num_10)
print(num_2[2:])