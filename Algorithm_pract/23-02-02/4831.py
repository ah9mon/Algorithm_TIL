
def min_charging(K,N,M,M_list):
    # 충전소 리스트 만들기
    charging_spots = [0] * (N+1)
    for spot_num in M_list:
        charging_spots[spot_num] += 1

    charge_state = K # 충전 상태 
    charge_count = 0

    # 
    for n in range(1,N+1): # 정류장 번호 
        charge_state -= 1 # 정류장 1 이동했으니까 충전상태 - 1
        # print(n)

        if charge_state < 0: # 충전소 위치 때문에 종점까지 못가는 경우
            return 0

        if charge_state == 0 and charging_spots[n]: # 충전상태가 0이고 현재 충전소라면 무조건 충전 
            charge_state = K
            # print('charging 1')
            charge_count += 1
            continue

        if charging_spots[n] and (N-n) > charge_state : # 현재 정류소가 충전소라면 (그리고 종점까지 남은거리가 충전 상태보다 크다면 (이게 없으면 1번 tc의 9번정류소에서 충전함))
            if  1 not in charging_spots[n + 1 : n + charge_state + 1]: # 바로 앞 정류장 ~  갈수있는 정류장 까지 충전소가 없다면 충전 
                charge_state = K 
                # print('charging 2')
                charge_count += 1
            
            
        
        
    return charge_count



    


T = int(input()) 

for n in range(1,T+1):
    K,N,M = map(int,input().split())
    M_list = list(map(int,input().split()))
    print(f'#{n} {min_charging(K,N,M,M_list)}')

