# subtree

import sys
sys.stdin = open('input_for_5174.txt')

def counts(n):
    global countss
    countss += 1
    for node in Tree[n]:
        counts(node)

T = int(input())

for i in range(1,T+1):
    # 간선의 개수 , 루트 노드
    E, N = map(int,input().split())
    # 인덱스 : 부모 노드 / [왼자식, 오자식]
    Tree = [[] for _ in range(E+2)]
    line = list(map(int,input().split()))
    for j in range(0,E*2,2):
        a,b = line[j], line[j+1]
        Tree[a].append(b)
        # Tree[a].sort()
    countss = 0
    counts(N)
    print(f'#{i} {countss}')


