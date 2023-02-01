# # [0 0 3 5 2 4 9 0 6 4 0 6 0 0] 
# # [0 0 2 4 1 3 8 0 5 3 0 5 0 0] -1 씩 확인 

# # 0 0 n 0 0 [2:-2]

def window_check(list):

    # 조망 확보 가구 세기
    count = 0 

    for i in range(max(list)):
        # 한층씩 확인
        # 다음층   
     
        if i != 0:
            for j in range(len(list)):
                if list[j] > 0:
                    list[j] = list[j] - 1
             
                else:
                    list[j] = 0
    

        # 조망확보 확인
        for k in range(2,len(list)-2):

            if list[k] > 0 and list[k-2] == 0 and list[k-1] == 0 and list[k+1] == 0 and list[k+2] == 0 :
                count += 1

    
    return count


for i in range(10):
    N = input()
    building_list = list(map(int,input().split()))

    print(f'#{i + 1} {window_check(building_list)}')


