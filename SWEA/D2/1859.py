# 백만장자 프로젝트

# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

# 먼저 매매가의 최댓값 찾고 그 최댓값의 인덱스 x 찾기 
# 1 ~ x 번째 날까지 모으고 있다가 x번째날 한번에 팔기 
#  바텀업  
import sys
sys.stdin = open('input_for_1859.txt')

# dp로 풀었는데 왜 ,, 답은 똑같은데 런타임에러나오는지 ,,,
# def dp(N,price):
#     d = [0]*(N+1)
#     # max함수랑 인덱스 찾는 함수는
#     # 데이터가 커질수록 시간 오래걸리고 + 메모리 많이씀
#     # 따라서 반복문에 최소한으로 넣어줘야함 
#     max_price = max(price)
  
#     for i in range(1,N+1):

#         if price[i] != max_price: # i가 최대 가격날이 아니면 
#             d[i] = d[i-1] + max_price - price[i] # 그날의 예상 최대 이익 = 전날 이익 + 최대가격 - 현재가격

#         elif price[i] == max_price: # i가 최고가 날이면
#             d[i] = d[i-1] # 다음날부터 가격 떨어지니까 안사는게 이득
#             max_price = max(price[i+1:])

#     return d[N]

T = int(input())

for i in range(1,T+1):
    N = int(input())
    price = list(map(int,input().split())) 
    # print(f'#{i} {dp(N,price)}')
    max_price = -1
    rlt = 0
    for j in range(N-1,-1,-1):
        if price[j] > max_price:
            max_price = price[j]
        else:
            rlt += max_price - price[j]
    
    print(f'#{i} {rlt}')
            
            
        
    
