import sys
sys.stdin = open('input_for_4831.txt')

'''
풀충 : K
0번에서 N번 정류장 까지 
종점에 도착 못하면 0 출력 
최소 몇 번 충전해야 최대한 이동?
'''

T = int(input())

for i in range(1,T+1):
    # 풀충량, 종점 번호, 충전기 설치 대수
    K, N, M = map(int,input().split())
    charging_stop = list(map(int,input().split())) + [N]
    now = 0 # 현재 정류장 (초기값 0)
    counts = 0 # 종점까지의 이동 횟수
    while len(charging_stop):
        charge = now # 충전하는 정류장 
        M = len(charging_stop)
        # 한번 충전하면 갈수 있는 최대의 충전 정류장을 감 
        for j in range(M):
            if (charging_stop[j] - now) <= K:
                charge = charging_stop[j]
                # print('charge', charge)
            else:
                break

        now = charge    
        del charging_stop[:j]
        # print('now',now)
        if now == N: # 종점 갔으면 종료 
            print(f'#{i} {counts}')
            break
        elif len(charging_stop) == M: # 이동 못했으면 더이상 못가는거
            print(f'#{i} {0}')
            break
        counts += 1 
        # 이동 후 남은 정류장 
        # print(charging_stop)
    



            
        

