# 그래프 경로

import sys
sys.stdin = open('input_for_4871.txt')

def dfs(S, line_info, visited):
    '''
    S,G 두 개의 노드에 경로가 존재하는지 확인하는 함수
    경로가 있으면 1 / 없으면 0 반환

    #param
    S : 시작 노드
    G : 종료 노드
    line_info : 간선 정보
    visited : 방문체크용 리스트
    '''
    visited[S] = 1 # 방문체크

    # 간성정보를 바탕으로 방문해야할 노드를 담은 리스트 생성
    nodes = []
    for line in line_info:
        if line[0] == S:
            nodes.append(line[1])
    # nodes.sort() # 오름차순으로 방문할것이므로 정렬
    # print(nodes)

    # 방문해야 할 노드 방문 시작
    for node in nodes:
        if not visited[node]: #방문 안햇으면
            dfs(node, line_info, visited) # 방문


T = int(input())

for i in range(1,T+1):
    V, E = map(int,input().split())
    line_info = [list(map(int,input().split())) for _ in range(E)]
    S, G = map(int,input().split())
    visited = [0] * (V + 1)  # 방문체크용 리스트
    dfs(S, line_info, visited)
    # print(visited)
    print(f'#{i} {visited[G]}')
