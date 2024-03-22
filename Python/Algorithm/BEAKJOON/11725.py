import sys
from collections import deque

def bfs() :
    q = deque()
    q.append(1)
    visited[1] = 1
    while(q) :
        node = q.popleft()
        for next in links[node] :
            if (visited[next] == 0) :
                q.append(next)
                visited[next] = node


N = int(sys.stdin.readline())
links = [[] for _ in range(N + 1)]
for _ in range(N - 1) :
    a,b = map(int, sys.stdin.readline().strip().split())
    links[a].append(b)
    links[b].append(a)

visited = [0 for _ in range(N + 1)]
bfs()
for i in range(2, N + 1) :
    print(visited[i])