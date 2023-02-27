testcase_num = int(input()) # testcase의 수 

for i in range(testcase_num): # testcase_num만큼 반복 
    command_num = int(input()) # 커멘드 수 입력
    command_list = [input().split() for j in range(command_num)] # 커멘드의 수만큼 커멘드 항목을 갖는 리스트 만듬
    # command_list = [[1번째 커멘드], [2번쩨 커멘드], ... ,[command_num번째 커멘드]]
    
    total_distance = 0 # 총 이동 거리
    v = 0 # 속도
    
    for command1 in command_list: # command_list의 각 항목을 꺼내서 쓰는 반복문 
        command1 = list(map(int, command1))
        if command1[0] == 1: # 만약 command1[0] 이 1이면 가속  
            v += command1[1] # 속도(v)에 command1[1] 만큼 가속
            #print('현재속도',v)
            
        elif command1[0] == 2:# 만약 command1[0] 이 2이면 감속  
            if v < command1[1]:
                v = 0
            else :
                v -= command1[1] # 속도(v)에 command1[1] 만큼 감속
            #print('현재속도',v)
            
        elif command1[0] == 0:# 만약 command1[0] 이 0이면 현재속도 유지
            v += 0 
            #print('현재속도',v)
            
        total_distance += abs(v) #1초간 간거리 총 이동거리에 추가   
        #print('현재 이동거리',total_distance)
    
    print(f'#{i + 1} {total_distance}') # 총 이동거리 출력 