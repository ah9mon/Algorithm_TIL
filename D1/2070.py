testcase_num = int(input())

testcase = [input().split() for i in range(testcase_num)]

for index_num in range(len(testcase)):
    testcase1 = list(map(int,testcase[index_num]))
    if testcase1[0] < testcase1[1]:
        print(f'#{index_num+1} <')

    elif testcase1[0] > testcase1[1]:
        print(f'#{index_num+1} >')

    elif testcase1[0] == testcase1[1]:
        print(f'#{index_num+1} =')