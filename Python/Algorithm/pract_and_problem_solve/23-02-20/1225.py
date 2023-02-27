# 암호생성기
'''
8개 숫자 입력 받기

첫 번째 숫자를 1 감소한 뒤, 맨뒤로 보냄

1cycle
큐에서 하나 씩 pop해서 1~5를 뻄
* 사이클을 돌다가 숫자가 감소할 때 0보다 작아지면 0으로 유지 후 프로그램 종료 -> 암호 완성
'''

import sys
from collections import deque

sys.stdin = open('input_for_1225.txt')

def password(q):
    i = 1
    while True:
        # 큐에서 하나 꺼냄
        num = q.popleft()
        if num-i > 0 : # 감소한 숫자가 0 이상인 경우
            q.append(num-i)
            i += 1
            if i > 5: # 1싸이클 끝났으면 i=1로 싸이클 다시 시작
                i = 1
        else: # 감소한 숫자가 0 이하인 경우
            q.append(0) # 0으로 유지
            return # 후 종료

for i in range(10):
    tc = input()
    q = deque()
    num_list = list(map(int,input().split()))
    for j in num_list:
        q.append(j)
    # print(q)
    # print(q.popleft())
    password(q)

    print(f'#{tc}', end = ' ')
    print(*q)
