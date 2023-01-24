testcase_num = int(input())

testcase_list = [input().split() for i in range(testcase_num)]

for index_num in range(len(testcase_list)):
    total = 0
    for index_num2 in range(len(testcase_list[index_num])):
        if index_num2 % 2 != 0:
            total += int(testcase_list[index_num][index_num2])

    print(f'#{index_num + 1} {total}')
