# 점프점프
'''
https://www.acmicpc.net/problem/11060

각 칸을 dp의 인덱스로 
각 칸을 갈 수 있는 횟수를 값으로 
'''

N = int(input())
maze = list(map(int,input().split()))
dp = [1000] * N
dp[0] = 0 
for i in range(N):
    for j in range(1,maze[i] + 1): # 점프력
        if i + j < N:
            jump_now = dp[i] + 1# 지금 칸을 지나고 i+j로 갈 때 점프 횟수
            dp[i+j] = min(jump_now, dp[i+j])
             
# print(dp)           
                
if dp[N-1] == 1000:
    print(-1)
else:
    print(dp[N-1])
