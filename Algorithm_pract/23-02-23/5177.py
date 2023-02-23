# 이진힙

import sys
sys.stdin = open('input_for_5177.txt')

T = int(input())
for i in range(1,T+1):
    # 자연수의 개수
    N = int(input())
    # print(N)
    num_list = list(map(int,input().split()))

    tree = [0 for _ in range(N+1)]
    last = 1

    for j in range(N):
        if not tree[j]:
            tree[last] = num_list[j]
            continue
        else:
            last += 1
            child = last
            parent = child // 2

            tree[child] = num_list[j]

        while parent >= 1 and tree[parent] > tree[child]:
            tree[parent], tree[child] = tree[child] ,tree[parent]
            child = parent
            parent = parent // 2

    # print(tree)
    sum1 = 0
    index = N
    while index > 0:
        index //= 2
        sum1 += tree[index]

    print(f'#{i} {sum1}')





