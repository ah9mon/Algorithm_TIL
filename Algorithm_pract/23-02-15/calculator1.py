# 1222 계산기 1

import sys
sys.stdin = open('input_for_1222.txt')

def calculator(N,infix):
    stack = []
    rlt = []
    for token in infix:
        if token.isdecimal(): # 피연산자면
            rlt.append(token) # 결과에 추가
        else: # 연산자면
            if not stack: # 스택이 비어있으면
                stack.append(token) # 스택에 추가
            else:
                if stack and stack[-1] == '+':
                    rlt.append(stack.pop())
                    stack.append(token)

    # 스택에 남은 연산자 rlt에 담기
    while stack:
        rlt.append(stack.pop())

    # 연산자 모두 0으로 바꾸기
    for i in range(N):
        if not rlt[i].isdecimal():
            rlt[i] = 0

    return sum(list(map(int,rlt)))

for i in range(1,11):
    N = int(input())
    infix = input()
    print(f'#{i} {calculator(N,infix)}')
