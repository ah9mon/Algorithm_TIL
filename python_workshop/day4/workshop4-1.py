#N의 약수

N = int(input())

for n in range(2,N+1):
    if N % n == 0:
        print(n, end = ' ')
        