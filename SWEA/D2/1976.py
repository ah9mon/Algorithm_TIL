# 사각 덧셈 

# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PttaaAZIDFAUq&categoryId=AV5PttaaAZIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2
import sys
sys.stdin = open('input_for_1976.txt')

def func(h1, m1, h2, m2):
    m3 = m1 + m2 
    h3 = h1 + h2
    if m3 >= 60:
        m3 -= 60
        h3 += 1
    
    if h3 > 12:
        h3 -= 12
    
    return f'{h3} {m3}'

T = int(input())

for i in range(1,T+1):
    h1, m1, h2, m2 = map(int,input().split())
    print(f'#{i} {func(h1, m1, h2, m2)}')

