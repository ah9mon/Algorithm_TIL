testcase_num = int(input())

num_list = [input().split() for i in range(testcase_num)]

for n in range(len(num_list)):
    num_list1 = list(map(int,num_list[n]))
    num_list1.sort()
    print(f'#{n+1} {num_list1[-1]}')