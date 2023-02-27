# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}

import calendar as cld

def ymd_func():
    date_dict = {} 
    week_list = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']

    year1 = int(input('연도를 입력하세요 : ')) # 연도 입력

    while cld.isleap(year1) != False: # year1이 윤년이 아닐때 까지 year1 입력 반복 
            print('윤년입니다. 연도를 다시 입력해주세요.')
            year1 = int(input('연도를 입력하세요 : '))
           
    print(cld.calendar(year1)) # 윤년이 아닌 경우 해당 연도의 달력 출력  
    month1 = int(input('month를 입력하세요 : ')) # 월 입력
    date1 = int(input('date를 입력하세요 : ')) # 일 입력
    
    if cld.weekday(year1, month1, date1) == 0: # 입력한 연 월 일이 월요일이라면 (cld.weekday()의 결과는 {월 : 0 , 화 : 1, 수 : 2, 목 : 3, 금 : 4, 토 : 5, 일 : 6})
        print('경고 월요일입니다.') #'경고 월요일입니다'
    
    
    date_dict['년'] = year1 
    date_dict['월'] = month1
    date_dict['일'] = date1
    date_dict['요일'] = week_list[cld.weekday(year1, month1, date1)] #week_list = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
    print(date_dict)

    return date_dict


ymd_func()
