def min_max_gap(list,N):
    min_num = min(list)
    max_num = max(list)
    
    return max_num - min_num

T = int(input())

for i in range(T):
    N = int(input())
    Num_list = list(map(int,input().split()))
    print(f'#{i+1} {min_max_gap(Num_list, N)}')