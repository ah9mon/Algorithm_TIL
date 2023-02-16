# 계산기
import sys
sys.stdin = open('input_for_1224.txt')
# 문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오

# 우선순위
# ()
# * /
# + -
def calculator3(infix):
    rlt = ''
    stk = []

    for token in infix:
        if token.isdecimal(): # 피연산자면
            rlt += token
        else:
            # 여는괄호인 경우
            if token == '(':
                stk.append(token)
            # 닫는 괄호의 경우
            elif token == ')':
                # 닫는 괄호가 나올때 까지 결과에 스택에 담긴 연산자 추가하고
                while stk[-1] != '(':
                    rlt += stk.pop()
                stk.pop() # 여는 괄호 제거

            # * 이랑 / 인경우
            elif token == '*' or token == '/':
                # 스택이 비어있지 않고 스택의 top이 '*' 이나 '/' 아닐때까지 결과에 추가
                while stk and (stk[-1] == '*' or stk[-1] == '/'):
                    rlt += stk.pop()
                stk.append(token)

            # + 랑 - 인 경우
            elif token == '+' or token == '-':
                # 여는 괄호 나올떄까지 반복
                while stk and stk[-1] != '(':
                    rlt += stk.pop()
                stk.append(token)

    # 스택에 남아있는거 다 꺼내서 결과에 넣기
    while stk:
        rlt += stk.pop()

    # print(rlt)
    # print(n, len(rlt))
    # 후위 연산자로 계산
    # 계산을 위한 스택은 재사용 # 어차피 rlt(후위표현식) 만들면서 스택 비워놨음
    for i in range(len(rlt)):
        if rlt[i].isdecimal(): # 피연산자의 경우
            stk.append(int(rlt[i]))
        else:
            # 스택에서 숫자 2개 꺼냄
            b = stk.pop()
            a = stk.pop()
            if rlt[i] == '+':
                stk.append(a + b)
            elif rlt[i] == '-':
                stk.append(a -b)
            elif rlt[i] == '*':
                stk.append(a * b)
            elif rlt[i] == '/':
                stk.append(a // b)

    return stk.pop()

for i in range(1,11):
    N = int(input())
    infix = input()
    print(f'#{i} {calculator3(infix)}')
