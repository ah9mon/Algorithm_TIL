# SWEA D3
# 그룹 나누기 
import sys 
sys.stdin = open('input_for_17027.txt')

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

# def union(x,y):
#     p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1,T+1):
    # print(f'tc : {tc}')
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    p = [i for i in range(N+1)] # 인덱스의 수가 포함된 set의 representative
    for j in range(0,2*M,2):
        # union(arr[j], arr[j+1])
        pre = find_set(arr[j+1])
        aft = find_set(arr[j])
        for k in range(N+1):
            if p[k] == pre:
                p[k] = aft

    counts = [0] * 101
    for l in range(1,N+1):
        if not counts[p[l]]:
            counts[p[l]] = 1
    
    print(f'#{tc} {sum(counts)}')

