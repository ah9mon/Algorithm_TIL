import sys
sys.stdin = open('input_for_ladder2.txt')

# 도착점 에서 시작해서 출발점 x값과 이동 횟수 반환하는 함수
def up_and_find(ladder,s):
    visited = [[0] * 100 for i in range(100)]
    y , x = 99, s
    counts = 0

    while y != 0:
        visited[y][x] = 1
        # 왼
        if 0 <= x - 1 < 100 and visited[y][x - 1] == 0 and ladder[y][x - 1]:
            x = x - 1
            counts += 1

            continue
        # 오른
        elif 0 <= x + 1 < 100 and visited[y][x + 1] == 0 and ladder[y][x + 1]:
            x = x + 1
            counts += 1

            continue
        # 위
        else:
            y = y - 1
            counts += 1
    # print(f'j : {j}, move : {counts}')
    return counts,x #이동 횟수 / 시작 x 값 반환

for i in range(10):
    tc = input()
    ladder = [list(map(int,input().split())) for _ in range(100)]
    min_count = 123456789
    min_x = -1
    for j in range(100):
        if ladder[99][j]: # 1이면 출발
            s = up_and_find(ladder, j) # (이동횟수, 도착 x값)
            if s[0] < min_count: # 최소값 찾기
                min_count = s[0]
                min_x = s[1]
    # print(min_count)
    print(f'#{tc} {min_x}')



