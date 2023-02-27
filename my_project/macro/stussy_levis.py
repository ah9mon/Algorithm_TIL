from datetime import datetime # 현재시간 출력용
import time # 딜레이용

#서버시간 가져오기 
# -*- coding: euc-kr -*-
import urllib.request
month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
while True:

        
        url = 'https://kr.stussy.com/collections/new-arrivals'
        date = urllib.request.urlopen(url).headers['Date'][5:-4]
        d, m, y, hour, min, sec = date[:2], month[date[3:6]], date[7:11], int(date[12:14]) + 9 , date[15:17], date[18:]
        min_str = str(min)
        hour_str = str(hour)
    
        print(f'[{url}]의 서버시간\n{y}년 {m}월 {d}일 {hour}시 {min}분 {sec}초')
        time.sleep(0.2) # 딜레이 