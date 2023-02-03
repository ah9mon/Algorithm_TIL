
def factorization(N):
    '''
    주어진 N=2**a x 3**b x 5**c x 7**d x 11**e 에 대하여 
    소인수분해 후 a b c d e 값을 반환하는 함수

    param
    N : 2**a x 3**b x 5**c x 7**d x 11**e 의 형태인 자연수 

    division_num_list의 인수들을 나머지가 0이 아닐때 까지 나눌때마다 카운트

    '''

    division_num_list = [2, 3, 5, 7, 11]
    division_counts = [0] * 5
    
    for i in range(len(division_num_list)):
    
        while not N % division_num_list[i] : # 나머지가 0이 아니면 중단
            N = N / division_num_list[i] 
    
            division_counts[i] += 1 # 카운트 
    
    

    return f'{division_counts[0]} {division_counts[1]} {division_counts[2]} {division_counts[3]} {division_counts[4]}'


T = int(input())
for i in range(1,T+1):
    number = int(input())
    print(f'#{i} {factorization(number)}')
    