# 단순 2진 암호코드

import sys
sys.stdin = open('input_for_1240.txt')

T = int(input())

for i in range(1,T+1):
    N , M = map(int,input().split())
    code = [input() for _ in range(N)]
    decode = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
    # 코드가 있는 행 찾기
    for n in range(N):
        if '1' in code[n]: # 1이 들어가있는 행이 코드가 있는 행이므로
            break # 끝내기 그러면 n == 코드가 있는 행
    # 코드의 끝부분 찾기
    for end in range(M-1,-1,-1):
        if code[n][end] == '1': # 끝이 1로 끝나는 곳이 코드의 끝부분이므로 end 찾음
            break # end == 코드가 끝나는 부분의 column 인덱스
    start = end - 55 # 코드가 시작되는 부분의 column 인덱스

    odd = 0 # 홀수번째 자리 숫자들의 합
    even = 0 # 짝수번째 자리 숫자들의 합
    counts = 0 # 몇번째 자리의 숫자인지 알기위해 필요한 카운트
    for j in range(start,start+56,7): # 7개씩 잘라서 디코딩
        num = decode.index(code[n][j:j+7]) # 디코딩
        if counts % 2: # 홀수번째 자리의 숫자면
            odd += num
        else: # 짝수번째 자리의 숫자면
            even += num
        counts += 1

    if not (odd + even*3) % 10: # 코드검증 후 올바른 암호 코드이면
        print(f'#{i} {odd + even}')
    else: # 올바르지 않은 코드이면
        print(f'#{i} {0}')
