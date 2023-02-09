import sys

sys.stdin = open('input_for_pract1.txt')


def sum_all(list1,N):
    sum_all_1 = 0
    commands = [(0,0),(-1,0),(1,0),(0,-1),(0,1)] # 현재, 위, 아래, 좌, 우

    for i in range(N): # 행
        for j in range(N): # 열
            for command in commands:
                ny = i + command[0]
                nx = j + command[1]
                if 0 <= ny < N and 0 <= nx < N:
                    sum_all_1 += abs(list1[i][j] - list1[ny][nx])

    return sum_all_1 


T = int(input())

for i in range(1,T+1):
    N = int(input())
    num_list = [list(map(int,input().split())) for j in range(N)]
    print(f'#{i} {sum_all(num_list,N)}')