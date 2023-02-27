testcase_num = int(input())

testcase_list = [int(input()) for i in range(testcase_num)] # [6791400, 1646400, 1425600, 8575, 185625, 6480, 1185408, 6561, 25, 330750]

list1 = [2,3,5,7,11]


for index_num1 in range(len(testcase_list)): 
    
    list2 = [] # [a,b,c,d,e를 담을 리스트]
    
    for index in list1: # list1 = [2,3,5,7,11] 에 들어있는거 하나 씩 꺼내는 반복문

        count = 0

        while True:

            if testcase_list[index_num1] % (index ** (count + 1)) == 0 : # 2의 (n+1)승의 배수 이면 
                count += 1 # a = n + 1
            
            else: # 2의 (n+1)의 배수가 아니면 2의 n승의 배수 인것 이므로 
                list2.append(count) # n의 값 추가 
                break
        
    
    
    #total =  2 ** list2[0] * 3 ** list2[1] * 5 ** list2[2] * 7 ** list2[3] * 11 ** list2[4]
    
    # print(total)

    print(f'#{index_num1 + 1} {list2[0]} {list2[1]} {list2[2]} {list2[3]} {list2[4]}')