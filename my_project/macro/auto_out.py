def auto_out():
    # 모듈 �? ?��?���?
    import pyautogui # 마우?�� 조작?�� 
    from datetime import datetime # ?��?��?���? 출력?��
    import urllib.request # ?��버시�? �??��?���?
    import time # ?��?��?��?��
    import os # 컴퓨?�� ?���? ?��

    #?��?�� ?���? 출력 �? ?���?
    while True:    
        # ?��버시�? 출력 
        month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', \
            'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
        
        url = 'https://edu.ssafy.com'
        date = urllib.request.urlopen(url).headers['Date'][5:-4]
        d, m, y, hour, min, sec = date[:2], month[date[3:6]], date[7:11], int(date[12:14]) + 9 , date[15:17], date[18:]
        min_str = str(min)
        hour_str = str(hour)
    
        print(f'[{url}]?�� ?��버시�?\n{y}?�� {m}?�� {d}?�� {hour}?�� {min}�? {sec}�?')
        time.sleep(2) # ?��?��?�� 3�? 

        if hour_str == '18' and min_str == '00': # 만약 18?���? ?���? 
            
            #?���? #Point(x=653, y=343)
            pyautogui.click(651,341,button='left',clicks =2, interval =1) #?��?�� ?���? 
    
            #?���? 메세�? 출력
            print("?���? ?��?��?��?��.")
            time.sleep(2) 
            break
    #컴퓨?�� ?���?
    os.system('shutdown -l') # 로그?��?��
    os.system('shutdown -s -t 5') # 10�? ?�� 컴퓨?�� 종료



if __name__ == '__main__':
    auto_out()