# contact

'''

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD

시작 노드 주어짐
마지막 노드 중 번호가 가장 큰 거 출력

양방향 간선 / 단방향 간선 주어짐

연락 인원은 최대 100명

한 번 연락을 받으면 다시 연락 x -> visited

'''



import sys
sys.stdin = open('input_for_1238.txt')

from collections import deque
def bfs(n):
    global max_node
    q = deque()
    q.append(n) # 인큐
    visited[n] = 1 # 인큐체크
    while q: # 큐가 빌때까지
        x = q.popleft()
        print(x, end=' ')
        for node in graph[x]:
            if not visited[node]: # 방문안햇으면
                q.append(node) # 인큐
                visited[node] = 1 # 인큐 체크

    if x > max_node:
        max_node = x
    print('')

for i in range(1):
    # 데이터의 길이, 시작점
    E, N = map(int,input().split())

    # 간선 정보
    lines = list(map(int,input().split()))
    # print(lines)
    # 각 노드와 연결된 노드 그래프
    graph = [[] for _ in range(101)]

    for j in range(0,E,2):
        graph[lines[j]].append(lines[j+1])
    # 인큐 체크용
    visited = [0]*101

    # 최댓값
    max_node = 0 # 초기값

    # print(graph)
    bfs(N)
    print(max_node)


