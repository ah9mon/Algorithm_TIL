def sum_gap(list,N,M):
    sum_list = []

    for i in range(N-M+1):
        range_sum = sum(list[i : i + M])

        sum_list.append(range_sum)
    
    min_num = min(sum_list)
    max_num = max(sum_list)
    
    return max_num - min_num

T = int(input())

for i in range(T):
    N, M = map(int,input().split())
    num_list = list(map(int, input().split())) 
    print(f'#{i+1} {sum_gap(num_list,N,M)}')