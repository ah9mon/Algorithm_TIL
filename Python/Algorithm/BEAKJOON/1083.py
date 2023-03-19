# 소트 

'''
https://www.acmicpc.net/problem/1083
'''

N = int(input())
arr = list(map(int,input().split()))
S = int(input())
arr_c = sorted(arr,reverse = True) # 정렬 완성본 
i = 0 

while S > 0:

    # 정렬 다 됐으면 S랑 관계없이 종료 
    if arr == arr_c:
        break 

    max_n = 0 # i~i+S 까지의 최댓값
    max_index = -1 # 그 최댓값의 인덱스 
    for index in range(i,i+S+1):

        if index == N: # out of index면 반복문 종료 
            break

        if max_n < arr[index]: # 현재값이 최댓값이면 할당해줌 
            max_n = arr[index]
            max_index = index # 인덱스도 기록해줌 
 
    if max_index != -1: # 정렬이 필요하면 (초기값이랑 같으면 이미 정렬 되어 있는 상황임) 
        del arr[max_index] # 최댓값 삭제
        arr = arr[:i] + [max_n] + arr[i:] # 정렬한 리스트로 수정 
        S -= (max_index - i) # 교환 횟수만큼 빼주기
    i += 1 # 다음칸 확인을 위해 + 1
    
print(*arr)