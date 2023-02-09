# 각 숫자가 
# 노선 범위 안에 있는 숫자인지 검색
def stop_check(stop_list, P, route_list, N):
    counts = [0] * P
    for i in range(P):
        for j in range(N):
            route_start = route_list[j][0]
            route_last = route_list[j][1]
            if stop_list[i] in range(route_start, route_last + 1):
                counts[i] += 1
    
    
    return ' '.join(str(count) for count in counts)

T = int(input())

for i in range(1,T+1):
    N = int(input())
    route_list = [list(map(int,input().split())) for j in range(N)]
    P = int(input())
    stop_list = [int(input()) for i in range(P)]
    print(f'#{i} {stop_check(stop_list, P, route_list, N)}')

