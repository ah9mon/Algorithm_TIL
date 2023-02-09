def min_max_gap(list,N):

    #최솟값 구하기
    min_num = list[0] # 최소값이 list[0]이라 가정
    for index1 in range(N): 
        if min_num > list[index1]: # 최소값보다 list[index1]이 작다면
            min_num = list[index1]
    
    # 최댓값 구하기 
    max_num = list[0] # 최댓값이 list[0]이라 가정
    for index2 in range(N): 
        if max_num < list[index2]: # 최댓값보다 list[index2]이 크다면
            max_num = list[index2]
    
    return max_num - min_num

T = int(input())

for i in range(T):
    N = int(input())
    Num_list = list(map(int,input().split()))
    print(f'#{i+1} {min_max_gap(Num_list, N)}')