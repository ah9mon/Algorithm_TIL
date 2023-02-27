# 최소합 수정
# 최소합 구하기
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('input_for_4881.txt')


def soonyeol(i, N, list1, sum1):
    global min_sum
    '''
    column index 중복으로 선택하면 안되므로
    column(list1) 의 순열을 구해서 합(sum1)을 만든후 
    최소합(min_sum)과 비교해서 최종 최소합을 구하는 함수 

    #parameter
    i : 시작 인덱스
    N : 리스트의 크기 / 목표 (여기선, column의 개수)
    list1 : 순열을 구하고 싶은 리스트 (여기선, column의 범위)
    '''
    '''
    column을 선택 후 그 자리의 수를 sum1에 더함 
    '''
    # 현재 더하고 있는 합이 최소합보다 크면 현재의 순열 조합 만들기 stop
    if sum1 >= min_sum:
        return

    if i == N: # 끝까지 다 더했으면
        if min_sum > sum1: # 현재 최소합 > 현재 합이라면
            # 현재합을 min_sum에 할당
            min_sum = sum1

    else:
        # 순열 구하기
        for j in range(i, N):
            list1[i], list1[j] = list1[j], list1[i]
            # 순열의 i 번쨰 항이 정해지므로 여기서 더함
            soonyeol(i + 1, N, list1, sum1 + num_list[i][list1[i]])
            list1[i], list1[j] = list1[j], list1[i] # 복귀

T = int(input())

for i in range(1,T+1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    column = list(range(N)) # column 리스트
    min_sum = 100  # 최소합의 초기값
    sum1 = 0 # 한 조합의 합 초기값
    soonyeol(0, N, column, sum1)
    print(f'#{i} {min_sum}')







