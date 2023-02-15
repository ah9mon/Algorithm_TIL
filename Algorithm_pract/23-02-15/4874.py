# Forth

# Forth 코드의 연산 결과를 출력하는 프로그램

# 입력 : 후위 표기법의 연산 Ex. 10 2 + 3 4 + * .
import sys
sys.stdin = open('input_for_4874.txt')

# def Forth(hi):
#     stk = []
#     for char in hi:
#         if char.isdecimal(): # 피연산자
#             stk.append(int(char))
#         else: # 연산자
#             # try:
#             if char == '.': #
#                 if len(stk) == 1:
#                     return stk.pop()
#                 else:
#                     return 'error'
            
#             a = stk.pop()
#             b = stk.pop()
#             if char == '+':
#                 stk.append(a + b)
#             elif char == '*':
#                 stk.append(a * b)
#             elif char == '/':
#                 stk.append(a // b)
#             elif char == '.':
#                 stk.append(a - b)
#             #
#             # except: # stk에 수가 2개이상 없어서 오류날 때 처리
#             #     return 'error'
def Forth(hi):
    stk = []
    for char in hi:
        if char.isdecimal(): # 피연산자
            stk.append(int(char))

        else: # 연산자
            if char == '+':
                if len(stk) >= 2:
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(a+b)
                else:
                    return 'error'
            elif char == '*':
                if len(stk) >= 2:
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(a*b)
                else:
                    return 'error'
            elif char == '/':
                if len(stk) >= 2:
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(b//a)
                else:
                    return 'error'
            elif char == '-':
                if len(stk) >= 2:
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(b-a)
                else:
                    return 'error'
            elif char == '.':
                if len(stk) == 1:
                    return stk.pop()
                else:
                    return 'error'


T = int(input())

for i in range(1,T+1):
    hi = input().split()
    print(f'#{i} {Forth(hi)}')