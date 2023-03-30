# 장훈이의 높은 선반 
# SWEA D4
'''
'''
import sys
sys.stdin = open('input_for_14034.txt')

import copy
T = int(input())
for tc in range(1,T+1):
    # 점원의 인원 수, 선반의 높이 
    N, B = map(int,input().split())
    # print(N,B)
    # 점원들의 키 
    H = list(map(int,input().split())) 
    # H.sort(reverse=True)
    # print(H)
    # index : 탑의 높이 / 값 : 탑을 만든 사람의 수 
    max_h = sum(H)
    dp = [0] * (max_h + 1)
    dp[0] = dp[-1]  = 1 # 0층 높이랑 max_h 높이는 무조건 만들 수 있으니까 1
    d = copy.deepcopy(dp)

    # 1부터 sum(H)까지 각 높이의 탑을 만들 수 있는지 체크 (만들 수 있으면 1)
    for i in range(N): # 특정 점원의 키를 하나씩 꺼내서 쌓기 위해 반복문 돌림 
        for j in range(max_h): # 쌓여져 있는 곳을 찾기위해 반복 돌림 
            if d[j] : # H[i-1]를 쌓아서 만든 dp 확앤해서 쌓여져 있으면 그 위에 쌓기 위해 쌓여져 있는지 확인 
                dp[j+H[i]] = 1 
        d = copy.deepcopy(dp) # H[i] 쌓는 경우의 dp 완성했으면 복사해줌 
        # print(d)
    
    for k in range(B,max_h+1): # dp[B:] 확인해서 
        if d[k] : # 해당 높이가 만들 수 있는 높이면 
            print(f'#{tc} {k-B}') # B와의 차이 출력 
            break
