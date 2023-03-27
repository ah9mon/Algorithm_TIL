def auto_out():
    # ëª¨ë“ˆ ë°? ?Œ¨?‚¤ì§?
    import pyautogui # ë§ˆìš°?Š¤ ì¡°ì‘?š© 
    from datetime import datetime # ?˜„?¬?‹œê°? ì¶œë ¥?š©
    import urllib.request # ?„œë²„ì‹œê°? ê°?? ¸?˜¤ê¸?
    import time # ?”œ? ˆ?´?š©
    import os # ì»´í“¨?„° ?„ê¸? ?š©

    #?˜„?¬ ?‹œê°? ì¶œë ¥ ë°? ?´ë¦?
    while True:    
        # ?„œë²„ì‹œê°? ì¶œë ¥ 
        month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', \
            'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
        
        url = 'https://edu.ssafy.com'
        date = urllib.request.urlopen(url).headers['Date'][5:-4]
        d, m, y, hour, min, sec = date[:2], month[date[3:6]], date[7:11], int(date[12:14]) + 9 , date[15:17], date[18:]
        min_str = str(min)
        hour_str = str(hour)
    
        print(f'[{url}]?˜ ?„œë²„ì‹œê°?\n{y}?…„ {m}?›” {d}?¼ {hour}?‹œ {min}ë¶? {sec}ì´?')
        time.sleep(2) # ?”œ? ˆ?´ 3ì´? 

        if hour_str == '18' and min_str == '00': # ë§Œì•½ 18?‹œê°? ?˜ë©? 
            
            #?´ë¦? #Point(x=653, y=343)
            pyautogui.click(651,341,button='left',clicks =2, interval =1) #?‡´?‹¤ ?´ë¦? 
    
            #?´ë¦? ë©”ì„¸ì§? ì¶œë ¥
            print("?´ë¦? ?–ˆ?Šµ?‹ˆ?‹¤.")
            time.sleep(2) 
            break
    #ì»´í“¨?„° ?„ê¸?
    os.system('shutdown -l') # ë¡œê·¸?•„?›ƒ
    os.system('shutdown -s -t 5') # 10ì´? ?’¤ ì»´í“¨?„° ì¢…ë£Œ



if __name__ == '__main__':
    auto_out()