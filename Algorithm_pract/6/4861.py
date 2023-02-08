# 16332. 우영우 

import sys
sys.stdin = open("sample_input (2).txt")
 
# 회문 찾기 
# reverse 한게 같으면 반환
def search(arr,N,M):

    # 가로탐색
    for low1 in range(N):
        if M == N:   # M == N이면 인덱스 생각안하고 그냥 한행 전체를 다뤄서 비교적 쉬움 
            if arr[low1] == arr[low1][::-1]: # 정상 == 역슬라이싱이면 반환 
                return arr[low1]
        else:    
            for column1 in range(N - M + 1):   
                if arr[low1][column1:column1+M] == arr[low1][column1 + (M-1):column1-1:-1] :
                    return arr[low1][column1:column1+M]
    
    # 세로탐색
    for column2 in range(N):
        # 각열의 strings를 담은 리스트 생성
        column_list = []
        for low2 in range(N):   
            column_list.append(arr[low2][column2])
        
        # 우영우 탐색
        if M == N:     
            if column_list[:] == column_list[::-1] :
                return column_list

        else:
            for i in range(N - M + 1):
                if column_list[i:i+M] == column_list[i+(M-1):i-1:-1]:
                    return column_list[i:i+M] 

    return 'fail'

T = int(input())

for i in range(1,T+1):
    N,M = map(int,input().split())
    board = [list(input()) for _ in range(N)]
    print(f'#{i} {"".join(search(board,N,M))}')



   