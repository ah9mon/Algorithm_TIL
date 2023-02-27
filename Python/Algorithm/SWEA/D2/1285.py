from collections import Counter

testcase_num = int(input())

for i in range(testcase_num):
    person_num = int(input())
    testcase_list = list(map(int,input().split()))
    #print(testcase_list)
    testcase_list_abs = list(map(abs,testcase_list))
    testcase_count = Counter(testcase_list_abs)
    testcase_count_sort = sorted(testcase_count.items())    
    # print(testcase_count_sort)
    print(f'#{i + 1} {testcase_count_sort[0][0]} {testcase_count_sort[0][1]}')
    
        
    