def continue_count(list, N):
    '''
    주어진 리스트에서 연속된 1의 개수 중 최댓값을 반환하는 함수

    param
    N : list의 길이 
    list : N개의 0과 1의 리스트


    인덱스를 하나씩 확인하면서 현재값이 1이고 앞의 값이 1이상이면
    현재 값(1)에 앞의 값을 더함 
    연속된 1의 마지막 값이 연속된 1의 개수가 됨
    결과적으로 list에서 가장 큰 값이 연속된 1의 개수의 최댓값이 됨
    '''
    for i in range(1, N): #인덱스를 하나씩 확인
        if list[i] == 1 and list[i - 1] >= 1: #현재값이 1이고 앞의 값이 1이상이면
            list[i] += list[i -1] #현재 값(1)에 앞의 값을 더함
    
    return max(list)

T = int(input())

for i in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input()))
    print(f'#{i} {continue_count(num_list,N)}')

