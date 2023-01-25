# import numpy as np

# testcase_num = int(input())

# testcase_list = [input().split() for i in range(testcase_num)]

# for index_num in range(len(testcase_list)):
#     testcase = list(map(int,testcase_list[index_num]))
#     testcase_mean = round(np.mean(testcase))
#     print(f'#{index_num+1} {testcase_mean}')


testcase_num = int(input())

testcase_list = [input().split() for i in range(testcase_num)]

for index_num in range(len(testcase_list)):
    testcase = list(map(int,testcase_list[index_num]))
    testcase_mean = round(sum(testcase) / len(testcase))
    print(f'#{index_num+1} {testcase_mean}')
