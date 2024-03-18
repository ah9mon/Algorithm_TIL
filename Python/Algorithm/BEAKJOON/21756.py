import sys
from collections import deque

N = int(sys.stdin.readline())
lst = [i for i in range(1, N + 1)]
dq = deque(lst)

while (len(dq) > 1) :
    for i in range(len(dq)) :
        num  = dq.popleft()
        if (i % 2) :
            dq.append(num)

print(dq.pop())