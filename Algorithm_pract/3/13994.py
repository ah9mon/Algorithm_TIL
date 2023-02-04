import sys
sys.stdin = open('sample_in.txt')


def max_stop(bus_info):
    '''
    1001개의 버스정류장 중 가장 많은 노선이 지나가는 버스정류장의 노선의 개수를 반환하는 함수 

    pram
    bus_info : 노선정보를 담은 리스트 (노선 정보 : [버스종류(일반/ 급행/ 광역), 출발 정류장 번호, 종점 정류장 번호])


    '''
    # 지나가는 노선을 카운트 할 버스정류장 리스트 생성
    counts = [0]*1001

    # 각 노선의 정류장 리스트 만들기 
    for info in bus_info:
        # print(info)
 
        # 일반 노선 정류장 리스트 
        if info[0] == 1: # 노선정보가 1번이면 일반 노선
           # regular_stop = list(range(info[1],info[2] + 1 )) # 시점부터 종점까지의 모든 정류장에 정차 
           counts[info[1] : info[2] + 1] = map(lambda x : x + 1 , counts[info[1] : info[2] + 1])


        # 고속 버스 노선 정류장 리스트 
        elif info[0] == 2: # 노선 정보가 2번이면 고속 버스 노선

            # 시점이 짝수번 정류장이면 종점까지 모든 짝수 정류장 정차 
            # 시점이 홀수번 정류장이면 종점까지 모든 홀수 정류장 정차 
            # 즉, 시점에서 +2 씩의 모든 정류장 정차한다는 뜻
            # express_stop = list(range(info[1],info[2],2)) + [info[2]] # 마지막 정류장은 짝/홀 여부 관계없이 무조건 정차하므로 따로 더해줌 
           counts[info[1] : info[2]: 2] = map(lambda x : x + 1 , counts[info[1] : info[2]: 2])
           counts[info[2]] += 1 # 마지막 정류장은 짝/홀 여부 관계없이 무조건 정차하므로 따로 더해줌 
        
        # 광역 버스 노선 정류장 리스트 
        elif info[0] == 3: # 노선 정보가 3번이면 광역 버스 노선 
            # wide_area_stop = [info[1], info[2]] # 시점 종점은 조건 관계 없이 무조건 정차 
            counts[info[1]] += 1
            counts[info[2]] += 1
            if info[1] % 2: # 시점이 홀수인 경우   
                for i in range(info[1] + 1, info[2]):
                    if i % 3 == 0 and i % 10 != 0: # 3의 배수이면서 10의 배수가 아닌 정류장에 정차 
                        # wide_area_stop.append(i)
                        counts[i] += 1

            else: # 시점이 짝수인 경우
                for i in range(info[1] + 1, info[2]): 
                    if i % 4 == 0: # 4의 배수인 정류장에 정차
                        # wide_area_stop.append(i)
                        counts[i] += 1

    # print(regular_stop)
    # print(express_stop)
    # print(wide_area_stop)
    # all_stops = regular_stop + express_stop + wide_area_stop
    # for stop in all_stops:
    #     counts[stop] += 1
    

    return max(counts)


T = int(input())

for i in range(1,T+1):
    N = int(input())
    bus_info = [list(map(int, input().split())) for j in range(N)]
    print(f'#{i} {max_stop(bus_info)}')