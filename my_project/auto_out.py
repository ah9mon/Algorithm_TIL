def auto_out():
    # 모듈 및 패키지
    import pyautogui # 마우스 조작용 
    from datetime import datetime # 현재시간 출력용
    import urllib.request # 서버시간 가져오기
    import time # 딜레이용
    import os # 컴퓨터 끄기 용

    #현재 시간 출력 및 클릭
    while True:    
        # 서버시간 출력 
        month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', \
            'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
        
        url = 'https://edu.ssafy.com'
        date = urllib.request.urlopen(url).headers['Date'][5:-4]
        d, m, y, hour, min, sec = date[:2], month[date[3:6]], date[7:11], int(date[12:14]) + 9 , date[15:17], date[18:]
        min_str = str(date[15:17])
    
        print(f'[{url}]의 서버시간\n{y}년 {m}월 {d}일 {hour}시 {min}분 {sec}초')
        time.sleep(2) # 딜레이 3초 

        if min_str == '00': # 만약 18시가 되면 
            
            #클릭
            pyautogui.click(687,306,button='left',clicks =1, interval =1) #퇴실 클릭 
    
            #클릭 메세지 출력
            print("클릭 했습니다.")
            time.sleep(2) 
            break
    #컴퓨터 끄기
    os.system('shutdown -l') # 로그아웃
    os.system('shutdown -s -t 5') # 10초 뒤 컴퓨터 종료



if __name__ == '__main__':
    auto_out()