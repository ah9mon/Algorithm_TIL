import sys
from collections import deque

def dfs(n) :
    dfs_order.append(n)
    visited[n] = 1
    links[n].sort()
    for node in links[n] :
        if (visited[node] == 0) :
            dfs(node)

def bfs(n) :
    q = deque()
    q.append(n)
    visited[n] = 1
    while(q) :
        node = q.popleft()
        bfs_order.append(node)
        links[node].sort()
        for newNode in links[node] :
            if (visited[newNode] == 0) :
                q.append(newNode)
                visited[newNode] = 1

N, M, V = map(int, sys.stdin.readline().strip().split())
links = [[] for _ in range(N + 1)]

dfs_order = []
bfs_order = []
for i in range(M) :
    a,b = map(int, sys.stdin.readline().strip().split())
    links[a].append(b)
    links[b].append(a)

visited = [0 for _ in range(N + 1)]
dfs(V)
print(" ".join(map(str,dfs_order)))

visited = [0 for _ in range(N + 1)]
bfs(V)
print(" ".join(map(str,bfs_order)))