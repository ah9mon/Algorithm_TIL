import sys
sys.stdin = open("vibra.txt")

 # 가로 / 세로 
def pariapari(paris,N,M): 
    max_sum = 0 
    for i in range(N -  M + 1): # 행방향
        for j in range(N - M + 1): # 열방향 
            parisum = 0
            for k in range(i,i+M):
                parisum += sum(paris[k][j:j+M]) 
            if max_sum < parisum:
                max_sum = parisum

    return max_sum




T = int(input())

for i in range(1,T+1):
    N,M = map(int,input().split())
    paris = [list(map(int,input().split())) for j in range(N)]
    print(f'#{i} {pariapari(paris,N,M)}')



