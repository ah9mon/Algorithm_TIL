import sys
sys.stdin = open("input_for_where.txt")

def func(puzzle,N,K):
    counts = 0 # 연속된 1을 카운트 하기위한
    rlt = 0 # 결과를 카운트 

    # 한행 다 보고 카운트가 K 이면 rlt + 1
    for l1 in range(N): # 행
        for c1 in range(N): # 열
            if puzzle[l1][c1] : # 1이면
                counts += 1
                if counts == K and c1 == N-1: # 다음칸이 없으면
                    rlt += 1 
                elif counts == K and not puzzle[l1][c1+1]: # 다음 칸이 0 이면
                    rlt += 1  
                    
            else:
                counts = 0
        
        counts = 0 # 행 끝날 때 재사용을 위해 초기화
                
    #한호열 다 보고 카운트 K이면 rlt + 1 

    for c2 in range(N): # 열 
        for l2 in range(N): # 행
            if puzzle[l2][c2]:
                counts += 1
                if counts == K and l2 == N-1: # 다음칸이 없으면
                    rlt += 1 
                elif counts == K and not puzzle[l2+1][c2]: # 다음 칸이 0 이면 
                    rlt += 1
            else: 
                counts = 0
        counts = 0 # 열 끝날 때 재사용을 위해 초기화

    return rlt

T = int(input())

for i in range(1,T+1):
    N,K = map(int,input().split())
    puzzle = [list(map(int,input().split())) for j in range(N)]
    print(f'#{i} {func(puzzle,N,K)}')
