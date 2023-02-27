import sys
sys.stdin = open('input_for_1984.txt')
'''
중간 평균값 구하기

최대 최소 제외한 나머지의 평균값 출력
'''
T = int(input())
for i in range(1,T+1):
    num_list = list(map(int,input().split()))
    num_list.sort()
    print(f'#{i} {round(sum(num_list[1:9])/8)}')
    