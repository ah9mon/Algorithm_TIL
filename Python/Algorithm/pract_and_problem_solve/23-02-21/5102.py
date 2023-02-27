import sys
sys.stdin = open('input_for_5102.txt')

# 노드의 거리

'''
V : 노드 개수 
E : 간선 개수 
S : 출발 노드 
G : 도착 노드
'''
# from collections import deque

def bfs(s,g):
    visited = [0] * (V+1) # 인큐 체크용
    # q = deque()
    q = []
    q.append(s)
    visited[s] = 1
    while q:
        # now = q.popleft()
        now = q.pop(0)
        # print(now, end = ' ')
        for after in graph[now]:
            if not visited[after]:
                q.append(after) # 인큐
                visited[after] = visited[now] + 1

                if after == g:
                    # print(after)
                    return visited[after] - 1
    # print('')
    return 0

T = int(input())
for i in range(1,T+1):
    # 노드개수, 간선개수
    V, E = map(int,input().split())
    # 각 노드와 연결된 노드 정보를 담을 2차원 리스트
    graph = [[] for _ in range(V+1)]
    # 간선 정보 입력 받기
    for _ in range(E):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    # 출발 노드 / 도착 노드
    S, G = map(int,input().split())
    # print(S,G)
    print(f'#{i} {bfs(S,G)}')



