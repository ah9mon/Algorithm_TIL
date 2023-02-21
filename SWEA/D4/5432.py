# 쇠막대기 자르기

# 막대의 개수 = 스택에 들어간 여는 괄호의 개수 - 1
#
import sys
sys.stdin = open('input_for_5432.txt')

T = int(input())
for i in range(1,T+1):
    stick = input()
    stack = []
    sum = 0
    for j in range(len(stick)):
        if stick[j] == '(':
            stack.append(stick[j])
            # print(f'막대기 개수 : {len(stack) - 1}')
            if j != len(stick)-1 and stick[j+1] == ')':
                sum += len(stack) - 1
                # print(f'{len(stack)-1}개 더하기')
        else:
            if j != len(stick)-1 and stick[j] == stick[j+1] == ')':
                sum += 1
                # print(f'막대기 하나 끝나서 ')
            stack.pop()

    print(f'#{i} {sum}')