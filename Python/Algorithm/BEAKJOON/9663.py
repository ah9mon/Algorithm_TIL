# N-queen

# https://www.acmicpc.net/problem/9663

# 퀸 상하 좌유 대각선


def N_queen(law):
    global cnt
    # for next_law in range(law,N):
    #     if not 0 in visited[next_law]:
    #         return
    #

    if law == N:
        cnt += 1
        return

    else:
        for i in range(N): # 열
            if visited[law][i] == 0: # 퀸을 둘 수 있으면
                visited[law][i] += 1
                # 세로 금지 체크
                for l in range(N):
                    # if d[l][k] == 0:
                    visited[l][i] += 1

                # 가로 금지
                for m in range(N):
                    # if d[j][m] == 0:
                    visited[law][m] += 1

                # 대각선 금지
                M = max(abs(int(N - i)), abs(int(N - law)))
                for n in range(1, M):
                    dx = [n, -n, n, -n]
                    dy = [n, -n, -n, n]
                    for o in range(4):
                        nx, ny = i + dx[o], law + dy[o]
                        if 0 <= ny < N and 0 <= nx < N:
                            # if 0 <= ny < N and 0 <= nx < N and d[ny][nx] == 0:
                            visited[ny][nx] += 1

                N_queen(law+1)

                # 복귀
                visited[law][i] -= 1
                # 세로 금지 체크
                for l in range(N):
                    # if d[l][k] == 0:
                    visited[l][i] -= 1

                # 가로 금지
                for m in range(N):
                    # if d[j][m] == 0:
                    visited[law][m] -= 1

                # 대각선 금지
                M = max(abs(int(N - i)), abs(int(N - law)))
                for n in range(1, M):
                    dx = [n, -n, n, -n]
                    dy = [n, -n, -n, n]
                    for o in range(4):
                        nx, ny = i + dx[o], law + dy[o]
                        if 0 <= ny < N and 0 <= nx < N:
                            # if 0 <= ny < N and 0 <= nx < N and d[ny][nx] == 0:
                            visited[ny][nx] -= 1



N = int(input()) # 체스판 크기 N x N # 놓아야하는 퀸 개수
visited = [[0]*N for _ in range(N)]
cnt = 0
N_queen(0)
print(cnt)









