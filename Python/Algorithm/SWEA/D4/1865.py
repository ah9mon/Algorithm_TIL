# 동철이의 일 분배 

# SWEA D4

import sys
sys.stdin = open('input_for_1865.txt')

def dfs(i,percent):
    global max_p

    if max_p[0] >= percent:
        return
        
    elif i == N:
        if max_p[0] < percent:
            max_p[0] = percent
        return
    
    else:
        for work in range(N):
            if not visited[work]: # 안했으면 
                visited[work] = 1
                dfs(i+1, percent * percents[i][work])
                visited[work] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 해야할 일의 수
    percents = [list(map(lambda x : float(x)/100.0 ,input().split())) for _ in range(N)] # row : 주체 column : 할일 
    visited = [0] * N
    max_p = [0.0]
    dfs(0,1.0)
    max_p[0] = str(round(max_p[0]*100,6))
    # print(max_p[0])
    p_i = max_p[0].index('.')
    if max_p[0][p_i:] != 7:
        max_p[0] += '0'*(7-len(max_p[0][p_i:]))
    print(f'#{tc} {max_p[0]}')

 

