# dfs

lines = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
M = len(lines) 
N = max(lines) # 노드의 개수

# 각 노드들과 연결되어 있는 노드 정리 
graph = [[] for _ in range(N+1)]
for i in range(0,M,2):
    graph[lines[i]].append(lines[i+1])
    graph[lines[i+1]].append(lines[i])
    
    
print(graph)

# 방문 기록
visited = [0] * (N+1)

def dfs(graph,start):
    if visited[start]: # 이미 방문했으면 
        return # 함수 종료
        
    visited[start] = 1 # 방문 체크 
    graph[start].sort() # 크기순으로 방문 
    print(start, end=' ')
    # 현재 노드와 연결되어있는 노드 방문 
    for node in graph[start]:
        # print(node, '방문시작')
        dfs(graph, node)
        # print(node, '방문종료')
        
dfs(graph, 1)        


