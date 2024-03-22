import sys

def dfs(start) :
    visited[start] = 1
    for node in links[start] :
        if (visited[node] == 0) :
            dfs(node)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
links = [[] for _ in range(N + 1)]
for _ in range(M) :
    a, b = map(int, sys.stdin.readline().strip().split())
    links[a].append(b)
    links[b].append(a)

visited = [0 for _ in range(N + 1)]
dfs(1)
print(sum(visited) - 1)