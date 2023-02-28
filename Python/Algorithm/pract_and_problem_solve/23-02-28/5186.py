# 이진수 2
import sys
sys.stdin = open('input_for_5186.txt')

'''
양의 실수를 이진수로
0.625 -> 0.101
12자리 이내의 이진수로 표시가능하면 0.을 제외한 나머지 숫자 출력
13자리 이상이 필요하면 'overflow' 출력
'''

T = int(input())

for tc in range(1,T+1):
    N = float(input())
    i = 1
    rlt = ''
    while N > 0:
        rlt += str(int(N//(2**(-i))))
        N %= (2**(-i))
        i += 1
    if len(rlt) < 13:
        print(f'#{tc} {rlt}')
    else:
        print(f'#{tc} overflow')

