# 쉬운 거스름돈 

# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PsIl6AXIDFAUq&categoryId=AV5PsIl6AXIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

import sys
sys.stdin = open('input_for_1970.txt')

def money(N):
    money_list = [0]*8
    money1 = [50000,10000,5000,1000,500,100,50,10]

    for i in range(8):
        if N // money1[i]:
            money_list[i] += N//money1[i]
        N = N % money1[i]
    
    m = list(map(str, money_list))
    print(' '.join(m))


T = int(input())

for i in range(1,T+1):
    N = int(input())
    print(f'#{i}')
    money(N)
        

    



