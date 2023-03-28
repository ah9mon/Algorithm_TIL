def auto_out():
    # 紐⑤뱢 占�? ?占쏙옙?占쏙옙占�?
    import pyautogui # 留덉슦?占쏙옙 議곗옉?占쏙옙 
    from datetime import datetime # ?占쏙옙?占쏙옙?占쏙옙占�? 異쒕젰?占쏙옙
    import urllib.request # ?占쏙옙踰꾩떆占�? 占�??占쏙옙?占쏙옙占�?
    import time # ?占쏙옙?占쏙옙?占쏙옙?占쏙옙
    import os # 而댄벂?占쏙옙 ?占쏙옙占�? ?占쏙옙

    #?占쏙옙?占쏙옙 ?占쏙옙占�? 異쒕젰 占�? ?占쏙옙占�?
    while True:    
        # ?占쏙옙踰꾩떆占�? 異쒕젰 
        month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', \
            'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
        
        url = 'https://edu.ssafy.com'
        date = urllib.request.urlopen(url).headers['Date'][5:-4]
        d, m, y, hour, min, sec = date[:2], month[date[3:6]], date[7:11], int(date[12:14]) + 9 , date[15:17], date[18:]
        min_str = str(min)
        hour_str = str(hour)
    
        print(f'[{url}]?占쏙옙 ?占쏙옙踰꾩떆占�?\n{y}?占쏙옙 {m}?占쏙옙 {d}?占쏙옙 {hour}?占쏙옙 {min}占�? {sec}占�?')
        time.sleep(2) # ?占쏙옙?占쏙옙?占쏙옙 3占�? 

        if hour_str == '18' and min_str == '00': # 留뚯빟 18?占쏙옙占�? ?占쏙옙占�? 
            
            #?占쏙옙占�? #Point(x=653, y=343)
            pyautogui.click(651,341,button='left',clicks =2, interval =1) #?占쏙옙?占쏙옙 ?占쏙옙占�? 
    
            #?占쏙옙占�? 硫붿꽭占�? 異쒕젰
            print("?占쏙옙占�? ?占쏙옙?占쏙옙?占쏙옙?占쏙옙.")
            time.sleep(2) 
            break
    #而댄벂?占쏙옙 ?占쏙옙占�?
    os.system('shutdown -l') # 濡쒓렇?占쏙옙?占쏙옙
    os.system('shutdown -s -t 5') # 10占�? ?占쏙옙 而댄벂?占쏙옙 醫낅즺



if __name__ == '__main__':
    auto_out()