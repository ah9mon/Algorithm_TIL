# 나무 조각 


'''
https://www.acmicpc.net/problem/2947

버블 정렬인듯 
'''

num_list = list(map(int,input().split()))

while num_list != list(range(1,6)): # 정렬될때까지 반복 
    for i in range(4): # 순서대로 반복 
        if num_list[i] > num_list[i+1]: # 만약 현재 조각 수가 다음꺼보다 크면 
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i] # 뒤바꿈
            print(*num_list) # 바뀌면 출력 


