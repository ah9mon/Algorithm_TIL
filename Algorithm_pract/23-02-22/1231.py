# 중위 순회
# 왼쪽 부모 오른쪽


import sys
sys.stdin = open('input_for_1231.txt')

def in_order(n):
    if len(Tree[n]) == 3: # 왼자식 만 있는 경우
        in_order(int(Tree[n][2]))
        print(Tree[n][1], end='')
    elif len(Tree[n]) == 2: # 자식이 없는 경우
        print(Tree[n][1],end='')
    else: # 왼, 오 자식 다 있는 경우
        in_order(int(Tree[n][2]))
        print(Tree[n][1],end='')
        in_order(int(Tree[n][3]))

for i in range(1,11):
    N = int(input()) # 노드의 수
    Tree = [[0,0,0,0]] + [input().split() for _ in range(N)]
    print(f'#{i}', end = ' ')
    in_order(1)
    print('')



