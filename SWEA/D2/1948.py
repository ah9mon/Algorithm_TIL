

def day_counter(list):
    month_day = {1 : 31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    day_count = 0
    
    #  list[0] 과 list[2] 사이에 있는 month의 day수를 daycount에 더하기
    if list[0] < list[2]: 
        # month 차이 처리
        for month in range(list[0]+1,list[2]):
            day_count += month_day.get(month)

        # day 차이 처리
        day_count += (month_day.get(list[0]) - list[1] + 1) + list[3] # 그 달의 남은 일수 + 2번째 입력 날짜값의 일 수 

    
    elif list[0] == list[2]: # 같은 달이면 
        day_count += list[3] - list[1] + 1 # 그냥 일 수 차이 계산

    return day_count


T = int(input())

for tc in range(1,T+1):
   input_list = list(map(int,input().split()))
   print(f'#{tc} {day_counter(input_list)}')



