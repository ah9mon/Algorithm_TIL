import sys
sys.stdin = open('pract_input.txt')
# 2. 좌, 우 , 부모
#     1   2    3
#[[0,0,0][2,3,0][]]

def pre_order(n):

    if n>0:
        print(n, end = ' ')
        pre_order(left[n])
        pre_order(right[n])

def in_order(n):
    if n != 0:
        pre_order(tree[n][0])
        print(n, end=' ')
        pre_order(tree[n][1])


def post_order(n):
    if n != 0:
        pre_order(tree[n][0])
        pre_order(tree[n][1])
        print(n, end=' ') # 특정 로직을 수행하는 곳




# 1. 좌 / 우 / 부모 배열을 따로 선언해서 받기
V = int(input())

E = V - 1

edge = list(map(int,input().split()))

left = [0] * (V+1) # 부모의 인덱스로 왼쪽 자식 번호 저장
right = [0] * (V+1) # 부모의 인덱스로 오른쪽 자식 번호 저장
parent = [0] * (V+1) # 자식을 인덱스로 부모 번호 저장

'''
2번 노드
- 왼쪽 2번 
- 오른쪽 3번 
- 부모 X
'''
# tree = [[0 for _ in range(3)] for _ in range(V+1)]
#
# for i in range(E):
#     parent, child = edge[i * 2], edge[i * 2 + 1]
#
#     # [0,0,0] 왼쪽 자식 / 오른쪽 자식 / 부모 노드
#     if not tree[parent][0]: # 부모노드의 왼쪽 자식이 없다면
#         tree[parent][0] = child
#
#     else: # 왼쪽 자식이 있고, 오른쪽이 없으면 오른쪽 넣고
#         tree[parent][1] = child
#
#     tree[child][2] = parent
#
#     print(tree)

# root
root = 0

for i in range(E):

    p1, c1 = edge[i * 2], edge[i * 2 + 1] # 부모, 자식

    if left[p1] == 0: # 왼쪽 자식이 없으면
        left[p1] = c1 # 부모의 인덱스로 자식 번호 저장
    else: # 왼쪽 자식이 있으면
        right[p1] = c1 # 부모의 인덱스로 자식 번호 저장
    parent[c1] = p1 # 자식을 인덱스로 부모를 저장

for i in range(1,V+1):
    if not parent[i]:
        root = i
        break

pre_order(1)

