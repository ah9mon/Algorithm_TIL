N = int(input())

for i in range(1,N+1):

    if  (i % 10) in [3,6,9] : # 1의 자리 확인 
        print('-', end='')

        i = i // 10  
        if i != 0 and (i % 10) in [3,6,9]: # 10의 자리 확인
            print('-',end = '')

            i = i // 10
            if i != 0 and (i % 10) in [3,6,9]: # 100의 자리 확인
                print('-',end = '')

            else:
                print(' ', end = '')

        else:
            print(' ', end = '')
    
    elif str(i)[0] in ['3','6','9'] :
        i = i // 10  
        if i != 0 and (i % 10) in [3,6,9]: # 10의 자리 확인
            print('-',end = '')

            i = i // 10
            if i != 0 and (i % 10) in [3,6,9]: # 100의 자리 확인
                print('-',end = '')

            else:
                print(' ', end = '')

        else:
            print(' ', end = '')
               
    else:
        print(i,end = ' ')     
    