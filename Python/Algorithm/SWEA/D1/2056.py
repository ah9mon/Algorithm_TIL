testcase_num = int(input())

day_list = [input() for i in range(testcase_num)]
print(day_list)

for day in day_list:    
    year = day[0:4]
    month = day[4:6]
    day1 = day[6:8]
    #print(year, month, day1)
    if int(month) in [1,3,5,7,8,10,12]:
        if int(day1) <= 31:
            print(f'#{day_list.index(day)+ 1} {year}/{month}/{day1}')
        else:
            print(f'#{day_list.index(day)+ 1} -1')
    elif int(month) == 2:
        if int(day1) <= 28:
            print(f'#{day_list.index(day)+ 1} {year}/{month}/{day1}')
        else:
            print(f'#{day_list.index(day)+ 1} -1')
    elif int(month) in [4,6,9,11]:
        if int(day1) <= 30:
            print(f'#{day_list.index(day)+ 1} {year}/{month}/{day1}')
        else:
            print(f'#{day_list.index(day)+ 1} -1')    
    else :
        print(f'#{day_list.index(day)+ 1} -1')            