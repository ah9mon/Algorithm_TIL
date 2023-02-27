#파리 퇴치
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq

import sys
sys.stdin = open('input_for_2001.txt')

def kill_fly(flys,N,M):

    max_kill = -1 # 죽인 파리의 마리수 초기값
    for i in range(N-M+1): # 행방향 이동
        for j in range(N-M+1): # 열방향 이동 
            # 현재 죽인 파리 마리수 세기
            kill = 0 # 초기값
            for k in range(M): # 행마다 더하기
                kill += sum(flys[i+k][j:j+M])
            
            # 최댓값과 비교 후 조정
            if kill > max_kill: # 현재 킬수가 최대값보다 크다면
                max_kill = kill # 현재킬수를 최대값으로 할당 
            
    return max_kill

T = int(input())
for i in range(1,T+1):
    # 배열의 크기, 파리채 크기
    N,M = map(int,input().split())
    # 파리 배열 입력 받기 
    flys = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{i} {kill_fly(flys,N,M)}')