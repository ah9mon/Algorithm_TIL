# 전기버스 2
'''
다이나믹 프로그램밍 ?
dp에 각 인덱스 정류장으로 갈 수 있는 최소 충전량을 넣자
'''
import sys
sys.stdin = open('input_for_14012.txt')

def dinamic_programing():
    dp = [50]*(N + 1)
    dp[1] = 0
    for stop_num in range(1,N+1): # 1번 정류장 ~ N번 정류장 
        for go in range(1,arr[stop_num]+1): # 각 정류장의 최대로 운행할 수 있는 정류장 수만큼 반복
            if stop_num + go <= N: # 범위 안에 있으면 (out of index 방지)
                dp[stop_num + go] = min(dp[stop_num] + 1, dp[stop_num + go]) # 현재 dp에 기록되어 있는 값이랑 지금 체크한 값 중 최소 충전량을 선택

    
    # if dp[N] == 50: # 못가는 경우 
    print(f'#{tc} {dp[N] - 1}') # 위의 반복문 로직에서 마지막 정류장에서도 도착하자마자 충전 한번 했으니까 -1 해서 출력해줘야함
    return

T = int(input())
for tc in range(1,T+1):
    # arr = [정류장 수, 정류장 별 배터리 용량]
    arr = list(map(int,input().split())) + [0]
    N = arr[0]
    dinamic_programing()

