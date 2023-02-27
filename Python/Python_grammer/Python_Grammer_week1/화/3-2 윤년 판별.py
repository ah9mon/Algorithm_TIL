year = int(input())

if year % 4 == 0 : 

    if year % 100 == 0 : 

        if year % 400 == 0 :  

            print('윤년') # 4, 100, 400의 배수면 윤년
        else :    
            print('평년') # 400의 배수가 아니면 평년   
         
    else:
        print('윤년') # 100의 배수면 윤년
    
else:
    print('평년') # 4의 배수가 아니면 평년
