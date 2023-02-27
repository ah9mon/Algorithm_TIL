# 거듭제곱

import sys
sys.stdin = open('input_for_16455.txt')

def func():
    global M
    global rlt

    if M == 0:
        return
    M -= 1
    rlt *= N
    func()

for _ in range(10):
    tc = input()
    N, M = map(int,input().split())
    rlt = 1
    func()
    print(f'#{tc} {rlt}')