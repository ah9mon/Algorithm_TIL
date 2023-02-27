def min_max_gap(list,N):
    min_num = list[0] # 최소값이 list[0]이라 가정
    for index1 in range(N): 
        if min_num > list[index1]: # 최소값보다 list[index1]이 작다면
            min_num = list[index1]
    
    max_num = list[0] # 최댓값이 list[0]이라 가정
    for index2 in range(N): 
        if max_num < list[index2]: # 최댓값보다 list[index2]이 크다면
            max_num = list[index2]
    
    return max_num - min_num

def sum_gap(list,N,M):
    sum_list = []

    for i in range(N-M+1):
        range_sum = 0  
        for num in list[i : i + M]:
            range_sum += num
        # range_sum = list[i] + list[i+1] + list[i+2] + ... +list[i + m]
        sum_list.append(range_sum)
     

    return min_max_gap(sum_list,len(sum_list))

T = int(input())

for i in range(T):
    N, M = map(int,input().split())
    num_list = list(map(int, input().split())) 
    print(f'#{i+1} {sum_gap(num_list,N,M)}')
        

