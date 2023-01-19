
def login():
    id_password = { 'djagksruf' : '1q2w3e4r' , 'hp5393' : '1q2w3e4r5t' }
    id = input('아이디를 입력하세요 : ')
    total = 0
    while True : 
        password = input('비밀번호를 입력하세요 : ')
        if  id_password[id] != password:
            print('비밀번호를 다시 입력하세요')
            total +=1
            if total == 3:
                a = '입력기회 종료'
                return a
            print(f'기회 {3-total}회 남음')

            continue
        else: 
            a = '로그인 성공'
            return a


print(login())