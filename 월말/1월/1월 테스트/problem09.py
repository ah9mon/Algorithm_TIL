# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 반드시 재귀함수로 구현해야 합니다.
def dec_to_bin(number): 
    
    n_list = []
    while number >= 2 : #number가 2이상이면 반복

        if number % 2 != 0: # number가 홀수면 
            n_list.append(1) # n_list에 1 추가

            number = (number-1)/2 

            if number == 1: # number가 1이면
                n_list.append(1) # n_list에 1추가

            dec_to_bin(int(number)) # 새로운 number값으로 재귀


        else : #number가 짝수면
            n_list.append(0) #n_list에 0추가
            
            number = number/2

            if number == 1: #number가 1이면
                n_list.append(1) #n_list에 1추가

            dec_to_bin(int(number)) # 새로운 number값으로 재귀

    # n_list = [0,1,0,1] (시작 number가 10인경우)
    n_list1 = list(map(str, n_list[::-1])) # ['1','0','1','0'] #n_list를 역순으로 하나씩 문자열로 바꾼후 리스트로 만들어줌
   
    n_num = ''.join(n_list1) #'1010'
    return n_num 
 

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010
