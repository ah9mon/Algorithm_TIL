import sys
sys.stdin = open('input_for_2007.txt')

T = int(input())

for i in range(1,T+1):
    strrrrr = input()
    for j in range(1, len(strrrrr)//2):
        if strrrrr[0:j] == strrrrr[j:2*j]:
            print(f'#{i} {j}')
            break
    