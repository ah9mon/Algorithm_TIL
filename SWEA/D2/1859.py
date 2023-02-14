# 백만장자 프로젝트

# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

# 먼저 매매가의 최댓값 찾고 그 최댓값의 인덱스 x 찾기 
# 1 ~ x 번째 날까지 모으고 있다가 x번째날 한번에 팔기 
#  바텀업  

def dp(N,price):
    d = [0]*(N+1)
    container = 0
    for i in range(1,N+1):
        
        if price[i] == max(price[i:]):
            d[i] = d[i-1] + price[i]
        else: 
            d[i] = 0
            container += 1

    return d[N]

T = int(input())

for i in range(1,T+1):
    N = int(input())
    price = [0] + list(map(int,input().split()))
    print()
    
