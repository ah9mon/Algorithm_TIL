import sys
sys.stdin = open('input_for_4881.txt')

def dp(N,num_list):
    # 3 <= N <= 10 이므로 다 계산 할 만함
    d = [[0]*(N) for _ in range(N)] # 메모이제이션 용
    d[0] = num_list[0]

    for i in range(1, N): # 행
        for j in range(N): # 열
            if j == N-1:
                d[i][j] = num_list[i][j] + min(d[i - 1][:j])
            elif not j:
                d[i][j] = num_list[i][j] + min(d[i - 1][j + 1:])
            else:
                d[i][j] = num_list[i][j] + min(min(d[i-1][:j]), min(d[i-1][j+1:]))

    print(d)
    return min(d[-1])

T = int(input())

for i in range(1,T+1):
    N = int(input())
    num_list = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{i} {dp(N,num_list)}')
