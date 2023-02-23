# 노드의 합
import sys
sys.stdin = open('input_for_5178.txt')

T = int(input())

for i in range(1,T+1):
    # 노드의 개수, 리프노드의 개수, 값을 출력할 노드 번호
    N, M, L = map(int,input().split())
    tree = [0]*(1001)
    for _ in range(M):
        a, b = map(int,input().split())
        tree[a] = b

    for j in range(N-M, 0, -1):

        tree[j] = tree[j*2] + tree[j*2+1]

    print(f'#{i} {tree[L]}')




