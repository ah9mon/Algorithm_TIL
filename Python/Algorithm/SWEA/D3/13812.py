# 진기명기 붕어빵 

'''
자격을 얻은 N명의 사람들한테만 붕어빵 팜
M초의 시간에 K개의 붕어빵 만듬 

모든 손님에게 기다리는 시간 없이 붕어빵 제공하면 'Possible'출력
못하면 'Impossible' 출력 
'''

import sys
sys.stdin = open('input_for_13812.txt')

def func():
    #M의 배수 초에 몇명 씩 오는지 카운트 
    counts = [0] * 11112
    for t in arrive:
        counts[t] += 1 # t초에 사람 한명오니까 1명 추가

    # M의 배수마다 몇명 씩 오는지 검사 
    bread = 0
    for i in range(11112):
        if i and not i % M: # M의 배수 초엔 K개의 붕어빵이 완성되므로 추가   
            bread += K
        
        bread -= counts[i] # 매초마다 오는 사람들에게 빵줘야함 

        if bread < 0: # 못주면 웨이팅해야하므로 실패
            return 'Impossible'

    # 웨이팅 없이 붕어빵 사갈 수 있음 
    return 'Possible'

T = int(input())
for i in range(1,T+1):
    # 손님 수 , K개 붕어빵 만드는 시간 M초
    N,M,K = map(int,input().split())
    # 각 사람이 언제 도착하는지 정보(초 단위)
    arrive = list(map(int,input().split()))
    print(f'#{i} {func()}')





