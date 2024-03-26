import sys

N, X = map(int,sys.stdin.readline().strip().split())
visited = list(map(int, sys.stdin.readline().strip().split()))
start = 0
end = X - 1
s = sum(visited[start: end + 1])

m = 0
count = 0
while (end < N) :
    if (start != 0) :
        s = s - visited[start - 1] + visited[end]

    if (s > m) :
        m = s
        count = 1
    elif (s == m) :
        count += 1
    
    start += 1
    end += 1

if (m > 0) :
    print(f'{m}\n{count}')
else :
    print('SAD')
