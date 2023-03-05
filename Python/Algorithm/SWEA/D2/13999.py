#kill fly 3
'''
N 은 5이상 15 이하 
M 은 2 이상 N이하
각 영역의 파리 수는 30 이하 
'''

import sys
sys.stdin = open('input_for_13999.txt')

def killflys():
    max_kills = 0 
    # +
    dx1 = [0, 0, -1, 1]
    dy1 = [1, -1, 0, 0] 
    # x
    dx2 = [1,-1, 1, -1]
    dy2 = [1,-1, -1, 1]
    for row in range(N):
        for col in range(N):
            kill_plus = flys[row][col]
            kill_x = flys[row][col]
            for i in range(4):
                counts_p = 1
                counts_x = 1
                ny1,nx1 = row+dy1[i], col+dx1[i]
                while 0<= ny1 < N and 0<= nx1 < N and counts_p < M:
                    kill_plus += flys[ny1][nx1]
                    counts_p += 1
                    ny1 += dy1[i]
                    nx1 += dx1[i]

                ny2,nx2 = row+dy2[i], col+dx2[i]
                while 0<= ny2 < N and 0<= nx2 < N and counts_x < M:
                    kill_x += flys[ny2][nx2]
                    counts_x += 1
                    ny2 += dy2[i]
                    nx2 += dx2[i]

            # print("좌표",row,col,"/",kill_plus, kill_x)
            max_now = max(kill_plus, kill_x)
            if  max_now > max_kills:
                max_kills = max_now 

    return max_kills

T = int(input())
for i in range(1,T+1):
    N,M = map(int,input().split())
    flys = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{i} {killflys()}')
