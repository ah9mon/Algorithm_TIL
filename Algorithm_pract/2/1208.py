

def flatten(list1,n):
    for i in range(n): # n번 반복 
        max1 = max(list1) # 가장 높은거
        min1 = min(list1) # 가장 낮은거 
        max_index = list1.index(max1) # 가장 높은거 인덱스 넘버
        min_index = list1.index(min1) # 가장 낮은거 인덱스 넘버
        list1[max_index] -= 1  # 가장 높은거에서 하나 뺴고
        list1[min_index] += 1  # 가장 낮은거에 하나 더함 
    
    gap = max(list1) - min(list1) # 가장 높은거 와 가장 낮은거 차이 


    return gap

T = 10
for i in range(1,T+1):
    n = int(input())
    num_list = list(map(int,input().split()))
    #print(num_list)
    print(f'#{i} {flatten(num_list,n)}')

