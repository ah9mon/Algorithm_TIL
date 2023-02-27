'''
문제 2 : 두더지 잡기 게임

주요 규칙
1. 두더지를 망치로 때리거나 시간이 지나서 들어가면 바로 다음 두더지가 머리를 내밀음
2. 망치는 1초에 한 칸 씩 이동 가능
3. 망치는 가로 -> 세로순으로 이동
4. 두더지가 머리를 내밀면 망치는 바로 두더지로 이동
'''
def game_rlt(r,c,abk_list):
    '''
    abk_list 안의 두더지들을 잡아서 얻을 수 있는 점수 출력하는 함수

    #param
    r, c : 망치 시작 좌표 (y,x)
    abk_list : # 두더지정보 # [[A1, B1, K1], [A2, B2, K2], [A3, B3, K3], ...]
    A, B, K : 두더지 y좌표, 두더지 x좌표, 두더지가 머리를 내밀고 유지하는 시간 K초
    '''

    point = 0

    for abk in abk_list: # 두더지 머리내밀기를 for문으로 구현
        # print(abk)

        dy = abk[0] - r # 두더지까지 가기위해 이동해야하는 y 거리
        dx = abk[1] - c # 두더지까지 가기위해 이동해야하는 x 거리
        time_for_move = abs(dy) + abs(dx) # 망치 현재 위치에서 두더지까지 가는데 걸리는 시간
        # print(f'필요한 이동시간 {time_for_move}')

        # 만약 k초 안에 두더지까지 갈 수 있다면
        if time_for_move <= abk[2]:
            # print('바로이동')
            point += 1 # 두더지 잡았으니까 점수 획득
            r, c = abk[0], abk[1] # 망치 위치를 두더지 위치로 변경


        # 두더지까지 k초 안에 못간다면
        else:
            # 만약 k초안에 dx를 다 수행할 수 있으면
            if abs(dx) <= abk[2]:
                c += dx # 가야하는 x 까지 바로 감
                # 남은 이동 시간은 K - abs(dx)
                time_left = abk[2] - abs(dx) # 남은 이동 시간
                r += (dy/abs(dy)) * time_left # 남은 시간만큼 y 이동


            # 만약 k초 안에 dx를 수행할 수 없다면
            else:
               c += (dx/abs(dx)) * abk[2] # k초 이동 # dx를 다 수행하지 못하므로 dy는 당연히 수행 못함

    return point


T = int(input())

for i in range(1,T+1):
    N = int(input())  # N : 두더지가 게임판 위로 머리를 내미는 횟수
    r, c = map(int,input().split()) # 망치 시작 좌표 (y,x)
    # ABK_list : # 두더지정보 # [[A1, B1, K1], [A2, B2, K2], [A3, B3, K3], ...]
    # A, B, K : 두더지 y좌표, 두더지 x좌표, 두더지가 머리를 내밀고 유지하는 시간 K초
    ABK_list = [list(map(int,input().split())) for _ in range(N)] # 두더지 정보 리스트
    print(f'#{i} {game_rlt(r,c,ABK_list)}')