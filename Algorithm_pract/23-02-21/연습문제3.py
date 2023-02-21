a = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
V = max(a)
E = len(a)//2
graph = [[] for _ in range(V+1)]

for i in range(0,len(a), 2):
    graph[a[i]].append(a[i+1])

print(graph)

def bfs(v,N):
    visited = [0]*(N+1)
    # 큐 생성
    q = []
    q.append(v)
    visited[v] = 1 # 시작점 인큐표시
    while q: # 큐가 비어있지 않으면
        t = q.pop(0) # 디큐
        print(t, end = ' ')
        # t에 인접이고 방문한 적 없는 v
        for v in graph[t]:
            if not visited[v]:
                q.append(v)# 인큐
                visited[v] = visited[t] + 1 # 인큐 표시

    print('')
    print(visited)

bfs(1,V)