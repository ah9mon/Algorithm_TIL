from collections import Counter

testcase_numbers = int(input())

for i in range(testcase_numbers):
    testcase_number = int(input())
    testcase_list = input().split()
    testcase_dict = Counter(testcase_list) # counter가 '리스트의 원소'(key) : 빈도수(value)를 갖는 딕셔너리 생성 
    # print(testcase_dict)
    testcase_dict_sorted = sorted(testcase_dict.items(), key = lambda x : x[1], reverse = True ) # value값을 기준으로 내림차순 정렬
    # print(testcase_dict_sorted)
    frequant_num = testcase_dict_sorted[0][0]
    print(f'#{i+1} {frequant_num}') 
    print(type(testcase_dict))
    print(type(testcase_dict.items()))
    