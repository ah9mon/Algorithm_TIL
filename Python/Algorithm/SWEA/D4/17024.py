# SWEA D4
# 최소 이동 거리
import sys
sys.stdin = open('input_for_17024.txt')

T = int(input())
for tc in range(1,T+1):
    N, E = map(int,input().split())
    
    d = [10] * (N+1)
    d[0] = 0
    for _ in range(E):
        s, e, w = map(int,input().split())
        if not s: # s== 0이면 
            d[e] = w 
        else:
            d[e] = min(d[s] + w, d[e])
    
    print(f'#{tc} {d[-1]}')
        