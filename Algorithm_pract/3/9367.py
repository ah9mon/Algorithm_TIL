def continue_growth(list,N):
    '''
    연속적으로 커지는 number의 개수의 최댓값을 반환하는 함수


    param 
    N : list의 길이(항목 개수)
    list : number가 담긴 list


    인덱스를 하나씩 확인하면서 앞번째의 수와 현재 수가 연속된 값이라면 
    counts 리스트의 앞번째 값과 현재 값을 더함 
    counts는 연속된 수의 개수를 담는 리스트가 됨 
    결과적으로 counts의 리스트안의 최댓값은 최대 연속된 수의 개수
    '''
    counts = [1] * N # [1,1,1,...]
    for i in range(1,N): 
        if list[i] == list[i-1] + 1: # i번째 number가 i-1 번째 number보다 1크다면 (연속된 숫자라면)
            counts[i] += counts[i-1] # counts[i] = 연속된 수의 개수 
   
    return max(counts)

T = int(input())
for i in range(1,T+1):
    N =  int(input())
    num_list = list(map(int,input().split()))
    print(f'#{i} {continue_growth(num_list,N)}')