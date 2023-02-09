import sys
sys.stdin = open("input_for_1213.txt","rt",encoding = "UTF8")

# 주어진 문자열에서 특정한 문자열의 개수를 반환

def func(A,B):
    N = len(A)
    M = len(B)
    visited = [0] * N  # 방문 체크용
    # A에 B가 몇개 있는지 카운트
    B_counts = 0
    for i in range(N - M + 1) :
        if A[i:i + M] == B and visited[i] == 0:
            B_counts += 1

    return B_counts # 카운트 횟수

for i in range(10):
    tc = input()
    B = input()
    A = input()
    print(f'#{tc} {func(A,B)}')