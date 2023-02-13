import pyautogui # 마우스 조작용 
from datetime import datetime # 현재시간 출력용
import time # 딜레이용
import os # 컴퓨터 끄기 용

# 마우스 현재 위치 출력 (전체 화면시 퇴실  x=684 , y=309)
# print(pyautogui.position())
# 좌표 위치 입력 (x,y,버튼,횟수, 간격)
# pyautogui.click(0,0,button='left',clicks =1, interval =1)

#무한 좌표 클릭
# while True:
#     #2초딜레이
#     time.sleep(2)

#     #좌표 위치 입력
#     pyautogui.click(0,0,button='left',clicks =1, interval =1)

#     #클릭 메세지 출력
#     print("클릭 했습니다.")


#현재 시간 출력 및 클릭
# while True:    
#     now = datetime.now()
#     now_time_str = str(now)
#     print(now_time_str[11:16]) # 현재 시각 출력 
#     time.sleep(3) # 딜레이 3초 
#     if now_time_str[11:16] == '18:00': # 만약 18시가 되면 
#         
#         #클릭
#         pyautogui.click(1675,20,button='left',clicks =1, interval =1) 퇴실 클릭 

#         #클릭 메세지 출력
#         print("클릭 했습니다.")
         
#         break
     

# #마우스 좌표 찾기 (퇴실하기 x = 687 / y = 306)
# print('현재 마우스 좌표 :', pyautogui.position())


## 컴퓨터 끄기
# os.system('shutdown -l')
# os.system('shutdown -s -t 10')


#서버시간 가져오기 
#-*- coding: euc-kr -*-
import urllib.request
month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', \
    'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

url = 'https://edu.ssafy.com/edu/main/index.do'
date = urllib.request.urlopen(url).headers['Date'][5:-4]
d, m, y, hour, min, sec = date[:2], month[date[3:6]], date[7:11], date[12:14], date[15:17], date[18:]
print(f'[{url}]의 서버시간\n{y}년 {m}월 {d}일 {hour}시 {min}분 {sec}초')