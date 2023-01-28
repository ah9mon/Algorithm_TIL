testcase_num = int(input())

Ns_list = [int(input()) for i in range(testcase_num)] #[1, 2, 11, 1295, 1692]
# print(testcase_list)

set_0_to_9 = set(map(str,range(10))) #{'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
# print(set_0_to_9)

for index_num in range(len(Ns_list)): 
    N = Ns_list[index_num] 
    N_set = set()
    count_num = 1
    k = 1
    while True:
        kN = k * N
        #print(kN)
        for num in str(kN): #kN의 각 자리수(num) 마다
            N_set.add(num) # num을 N_set에 추가

        if N_set == set_0_to_9: #N_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}가 되면
            print(f'#{index_num + 1} {count_num * N}')
            break # while문 탈출하고 다음 index_num으로 

        k += 1 # k = k + 1
        count_num += 1 # count_num = count_num + 1 # 몇번째 셋는지 count

    

