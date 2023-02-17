d = [[0]*3 for _ in range(3)]
j = 0
k = 0
N = 3

if d[j][k] == 0:
    d[j][k] += 1
    # 세로 금지 체크
    for l in range(N):
        # if d[l][k] == 0:
        d[l][k] += 1

    # 가로 금지
    for m in range(N):
        # if d[j][m] == 0:
        d[j][m] += 1

    # 대각선 금지
    M = max(abs(int(N - j)), abs(int(N - k)))
    for n in range(1, M):
        dx = [n, -n, n, -n]
        dy = [n, -n, -n, n]
        for o in range(4):
            nx, ny = k + dx[o], j + dy[o]
            if 0 <= ny < N and 0 <= nx < N:
                # if 0 <= ny < N and 0 <= nx < N and d[ny][nx] == 0:
                d[ny][nx] += 1
print(d)