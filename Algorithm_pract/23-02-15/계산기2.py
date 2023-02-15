# 1223

import sys
sys.stdin = open('input_for_1223.txt')

def calculator2(N,infix):
    rlt = ''
    stack = []
    for token in infix:
        if token.isdecimal(): # 피연산자면
            rlt += token
        else: # 연산자면
            if token == '*':
                while stack and stack[-1] == '*':
                    rlt += stack.pop()

                stack.append(token)

            elif token == '+':
                while stack:
                    rlt += stack.pop()

                stack.append(token)

    while stack:
        rlt += stack.pop()
    # print(rlt)

    rlt_stack = []
    for i in range(N):
        if rlt[i].isdecimal(): # 피연산자면
            stack.append(int(rlt[i]))
        else: #연산자면
            if rlt[i] == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif rlt[i] == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)

    return stack.pop()

for i in range(1,11):
    N = int(input())
    infix = input()
    print(f'#{i} {calculator2(N,infix)}')
