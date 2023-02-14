# 길찾기

import sys
sys.stdin = open('input_for_1219.txt')

def dfs(visited, line_list2, v):
    '''
    dfs 방문을 통해 visited에 방문한 노드를 1로 할당하는 함수

    # param
    visited : 방문체크용 리스트
    line_list2 : 노드간 간선 데이터
    v : 방문하려는 노드
    '''

    visited[v] = 1 # 방문체크

    # 방문해야하는 노드를 nodes에 담기
    nodes = [] # 방문해야하는 노드를 담을 스택 생성
    for line in line_list2:
        if v == line[0]: # 시작 노드가 v라면
            nodes.append(line[1]) # 스택에 방문해야할 노드 추가

    nodes.sort() # 오름차순으로 방문할 것이기 때문에 정렬
    # print(nodes)

    # 스택에 담긴 방문해야하는 노드 방문하기
    for node in nodes:
        if not visited[node]: # node를 방문하지 않았다면
            dfs(visited, line_list2, node)
            # print(node, '탐색완료')
    # print(visited)

for i in range(10):
    tc, num_o_line = map(int,input().split())
    line_list = list(map(int, input().split()))

    # 데이터를 [시작노드, 도착노드] 형태로 만들어서 할당
    line_list2 = []
    for j in range(0, num_o_line * 2, 2):
        line_list2.append(line_list[j:j + 2])
    # line_list2.sort()

    # 방문체크용 리스트 생성
    visited = [0] * (100)

    dfs(visited, line_list2, 0)
    print(f'#{tc} {visited[99]}')

