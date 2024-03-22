import sys
from collections import deque

def bfs(n) :
    visited = [0 for _ in range(N + 1)]
    q= deque()
    q.append(n)
    visited[n] = 1

    while(q) :
        node = q.popleft()
        for nextNode in links[node] :
            if (visited[nextNode] == 0) :
                q.append(nextNode)
                visited[nextNode] = 1

    count[n] = sum(visited)

N, M = map(int,sys.stdin.readline().strip().split())
links = [[] for _ in range(N + 1)]
for _ in range(M) :
    a,b = map(int, sys.stdin.readline().strip().split())
    links[b].append(a)

count = [0 for _ in range(N + 1)]

for i in range(1, N + 1) :
    bfs(i)

max_count= max(count)
for i in range(N + 1) :
    if (count[i] == max_count) :
        if (i == N) :
            print(i)
        else :
            print(i, end = " ")