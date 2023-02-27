# 연습문제 3 DFS

# DFS 경로 출력

def DFS(v,lines, visited):
    print(v, end = ' ')
    visited[v] = 1 # 방문체크

    # 방문할 노드 리스트에 담기
    nodes = []
    for i in range(0, len(lines), 2):
        if lines[i] == v:
            nodes.append(lines[i+1])

    # print(nodes)
    # nodes.sort() #오름차순으로 방문하기위해 정렬

    # 방문시작
    for node in nodes:
        if not visited[node]: # 방문 안했으면
            # print(f'{node} 방문시작')
            DFS(node, lines, visited)


# 간선정보
lines = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# 방문체크용 리스트
visited = [0]*(max(lines) + 1)
DFS(1,lines,visited)
# print(visited)






