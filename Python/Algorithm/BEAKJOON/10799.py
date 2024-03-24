import sys
from collections import deque

commend = sys.stdin.readline().strip()
stack = deque()
count = 0
for i in range(len(commend)) :
    if (commend[i] == '(') :
        stack.append('(')
    elif (commend[i] == ')') :
        stack.pop()
        if (commend[i - 1] == '(') : # 레이저이면
            count += len(stack)
        elif (commend[i - 1] == ')') : # 그냥 길이 끝난거면
            count += 1

print(count)