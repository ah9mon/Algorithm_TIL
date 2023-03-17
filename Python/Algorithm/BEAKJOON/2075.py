# N번째 큰 수 

'''
https://www.acmicpc.net/problem/2075
'''

N = int(input())
d = [0]*(N**2)

for j in range(N):
    arr = list(map(int, input().split()))
    for i in range(N):
        n = arr[i]
        d[i+(j*N)] += n

d.sort(reverse=True)
print(d[N-1])







    

    
