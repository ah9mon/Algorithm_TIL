a = input() # 입력 형태 'n n'
b = list(a)
del b[1] # 공백제거
c = list(map(lambda x : int(x) ,b))
if c == [1,2] : #가위 1 바위 2 보 3 
    print('B')
elif c == [1,3] : #가위 1 바위 2 보 3 
    print('A')
elif c == [2,1] : #가위 1 바위 2 보 3 
    print('A')
elif c == [2,3] : #가위 1 바위 2 보 3 
    print('B')
elif c == [3,1] : #가위 1 바위 2 보 3 
    print('B')
elif c == [3,2] : #가위 1 바위 2 보 3 
    print('A')
