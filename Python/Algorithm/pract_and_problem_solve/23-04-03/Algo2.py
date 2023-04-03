
def dfs(i,prv_index,energy):
    '''
    :param i: 방문 횟수
    :param prv_index: 직전에 방문한 인덱스
    :param energy: 현재까지 에너지 사용량
    '''
    global min_energy # 최소값 갱신을 위해 global 변수 불러오기

    # a는 방문 안되어 있는데 b먼저 방문 되어 있으면 종료
    if visited[b]: # b방문 했는데
        if not visited[a]: # a 방문 안했으면
            return  # 종료

    # 현재까지의 에너지가 이미 최솟 값보다 크면 의미 없으므로 종료
    if min_energy < energy:
        return

    if i == N-1: # 강의실을 모두 돌았으면 (방문횟수(i) == N - 1 이면 사무국으로 되돌아가는 거 빼고 다 돈거임)
        energy += graph[prv_index][0] # 사무국으로 돌아가는데에 드는 에너지 더하고
        if min_energy > energy: # 최솟 값과 비교해서 더 작으면
            min_energy = energy # 최소 값 갱신
        return

    for room in range(1,N): # 방문할 다음 강의실(사무국(0) 제외)을 정하기 위한 반복문
        if not visited[room]: # 방문 안한 강의실 이면
            visited[room] = 1 # 방문체크
            dfs(i+1, room, energy + graph[prv_index][room])
            visited[room] = 0 # 복귀하면 다시 방문 안한걸로 체크

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    a, b = map(int,input().split())
    visited = [0] * N
    min_energy = N*N*100
    dfs(0,0,0)
    print(f'#{tc} {min_energy}')