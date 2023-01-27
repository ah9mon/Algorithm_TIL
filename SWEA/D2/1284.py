testcase_num = int(input())

testcase_list = [input().split() for i in range(testcase_num)]

# print(testcase_list)



for index_num in range(len(testcase_list)): #테스트케이스 리스트의 항목 개수 만틈 반복
    water_use = int(testcase_list[index_num][-1]) # 물 사용량
    A_cost = water_use * int(testcase_list[index_num][0]) # A_cost = 물사용량 * a회사 리터당 수도 요금

    if water_use > int(testcase_list[index_num][2]): #물 사용량이 testcase_list[index_num][2] 보다 크면
        B_cost = int(testcase_list[index_num][1]) + (water_use - int(testcase_list[index_num][2])) * int(testcase_list[index_num][3]) # B_cost = 기본요금 + 초과 사용량 * 리터당 수도요금

    else: #물 사용량이 testcase_list[index_num][2] 보다 크지 않으면
        B_cost = int(testcase_list[index_num][1]) # B_cost = 기본요금
    
    if A_cost > B_cost: 
        print(f'#{index_num + 1} {B_cost}')

    elif A_cost < B_cost:
        print(f'#{index_num + 1} {A_cost}')
