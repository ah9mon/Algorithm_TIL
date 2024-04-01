import sys

N = int(sys.stdin.readline())
n = pow(2,32) + N

str1 = bin(pow(2, 32) + N)[4:]

str2 = bin(pow(2, 32) + ~N + 1)[3:]

count = 0
for i in range(len(str1)) :
    if (str1[i] != str2[i]) :
        count += 1

print(count + 1)