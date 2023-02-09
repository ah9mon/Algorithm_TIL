# 가장 빠른 문자열 타이핑
# 어떤 문자열 A를 타이핑하려고 한다.
# 그냥 한 글자씩 타이핑 한다면 A의 길이만큼 키를 눌러야 할 것이다.
# 여기에 속도를 조금 더 높이기 위해 어떤 문자열 B가 저장되어 있어서 키를 한번 누른 것으로 B전체를 타이핑 할 수 있다.
# 예를 들어 A=”apple”, B=”app”일 때, 다음 그림과 같이 B를 두 번 사용하면 3번 만에 A를 타이핑 할 수 있다.
# A와 B가 주어질 때 A 전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값을 구하여라.

import sys
sys.stdin = open('input_for_the_fastest.txt')

# A 타이핑 횟수의 최솟값을 구하는 함수
# 예를 들어
# B의 길이가 M이고
# A에 2번 들어가 있다고 치면 (A의 길이 N)
# A = 'banana' B = 'na'
# A를 타이핑 하기 위해선
# 'b' 'n' B B 총 4번을 친다
# N - (1-M) * B의 개수와 같으므로 이를 리턴한다
def func(A,B):

    N = len(A)
    M = len(B)
    visited = [0] * N # 방문 체크용
    # A에 B가 몇개 있는지 카운트
    B_counts = 0
    for i in range(N - M + 1) :
        if A[i:i + M] == B and visited[i] == 0 : # 같고 카운트 안한 거면
            visited[i:i+M] = [1] * M
            # print(visited)
            B_counts += 1

    return (N + (1-M)*B_counts) # 카운트 횟수

T = int(input())

for i in range(1,T+1):
    A, B = input().split()
    print(f'#{i} {func(A,B)}')