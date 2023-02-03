# # [0 0 3 5 2 4 9 0 6 4 0 6 0 0] 
# # [0 0 2 4 1 3 8 0 5 3 0 5 0 0] -1 씩 확인 

# # 0 0 n 0 0 [2:-2]

def window_check(list):

    # 조망 확보 가구 카운트 초기값
    count = 0 
    
    # 1층 부터 제일 높은 건물의 가장 높은 층까지 확인 
    for i in range(max(list)):
     
        if i != 0:
            for j in range(len(list)):
                if list[j] > 0:
                    list[j] = list[j] - 1 # 리스트에서 1이상의 값에 모두 -1을하면 다음층에서의 시점을 볼 수 있음 
             
                else:
                    list[j] = 0 # 리스트의 항목이 0 이라면 그대로 0으로 둠 
    

        # 조망확보 확인
        for k in range(2,len(list)-2):

            if list[k] > 0 and list[k-2] == 0 and list[k-1] == 0 and list[k+1] == 0 and list[k+2] == 0 : # 0 0 n 0 0의 형태이면 조망권이 확보된 것이므로 카운트 + 1 
                count += 1

    
    return count


for i in range(10):
    N = input()
    building_list = list(map(int,input().split()))

    print(f'#{i + 1} {window_check(building_list)}')


