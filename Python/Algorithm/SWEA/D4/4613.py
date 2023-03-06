# 러시아 국기 같은 깃발 

'''
깃발 크기 N x M 
각 칸은 흰색 파한색 빨간색으로 칠해져 있음 
위에서 한줄 이상은 모두 흰색  W
다음 몇 줄은 모두 파란색 B
나머지 줄은 모두 빨간색 R

러시아 국기 만들기 위해 새로 칠해야하는 칸의 개수의 최솟 값
'''

import sys
sys.stdin = open('input_for_4613.txt')

# 1. 재귀함수로 풀기  -> 시간 초과 ㅠ
# 각 라인의 색을 미리 정하고 카운트하기 

# def func(s,e):
#     global pos
#     global min_rlt
#     if s > e: # 각 라인의 색을 다 정했으면 

#         counts = 0
#         pos1 = "".join(pos)
#         if 'B' in pos1 and not 'BW' in pos1:
#             for i in range(N):
#                 for j in range(M):
#                     if lines[i][j] != pos1[i]:
#                         counts += 1
            
#             if counts < min_rlt:
#                 min_rlt = counts
#         return
    
#     else:
#         if pos[s-1] != 'B':
#             pos[s] = 'W'
#             func(s+1,e)
#         if pos[s-1] != 'R': 
#             pos[s] = 'B'
#             func(s+1,e)
#         if pos[s-1] != 'W':
#             pos[s] = 'R'
#             func(s+1,e)

# T = int(input())

# for i in range(1,T+1):
#     # 행, 열
#     N,M = map(int,input().split())
#     # 현재의 색정보 입력받기
#     lines = [list(input()) for _ in range(N)]
#     # 색의 경우의 수 
#     pos = ['W'] + ['N'] * (N-2) + ['R']
#     min_rlt = 2501
#     func(1,N-2)
#     print(f'#{i} {min_rlt}')


# 2. 그냥 풀기 
T = int(input())
for i in range(1,T+1):
    # 행, 열
    N,M = map(int,input().split())
    # 깃발 초기 정보 
    flag = [input() for _ in range(N)]
    min_counts = 2501

    # 흰색 영역 
    for w in range(N-2): # 흰줄이 w줄 까지인 경우
        # 흰색 칠하는 수 세기 
        counts_w = 0 
        for row_W in range(w+1):
            for col_W in range(M):
                if flag[row_W][col_W] != 'W': # 흰색이 아니면 카운트 
                    counts_w += 1
                    if counts_w >= min_counts: # 이번차례는 망하니까 무시 
                        continue
        # 파란색 영역  
        for b in range(w+1,N-1): # 파란색이 w+1 ~ b줄까지 인 경우
            # 파란색 칠하는 수 세기 
            counts_b = 0
            for row_B in range(w+1, b+1):
                for col_B in range(M):
                    if flag[row_B][col_B] != 'B': # 파란색 아니면 카운트 
                        counts_b += 1
                        if counts_b >= min_counts: # 이번차례는 망하니까 무시 
                            continue
                    
            # 빨간색 칠하기 
            counts_r = 0
            for row_R in range(b+1,N):
                for col_R in range(M):
                    if flag[row_R][col_R] != 'R': #빨간색 아니면 카운트 
                        counts_r += 1

            counts = counts_w + counts_b + counts_r
            if counts < min_counts:
                min_counts = counts

    print(f'#{i} {min_counts}')




















