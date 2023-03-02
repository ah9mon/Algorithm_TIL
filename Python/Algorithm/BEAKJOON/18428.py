# 감시 피하기 
'''
https://www.acmicpc.net/problem/18428

N x N 크기의 복도 
특정 위치에 선생님, 학생, 장애물이 위치해 있음 

T(선생님) : 상 하 좌 우 4방향 감시
S(학생)
O(장애물)
선생님은 장애물 뒤편에 숨어있는 학생은 볼 수 없음 

3개의 장애물을 설치하면 모든 학생이 모든 선생님들의 감시를 피할 수 있는지 출력

how? 
수열 만드는 것처럼 장애물 설치 후 (모든 장애물 설치의 경우의 수 확인)
감시 피하는지 확인 
학생 안만나면 rlt = true
-> "yes"
'''

def dfs():
    '''
    선생님의 위치를 시작점으로 행, 열 모두 확인해서 학생이 있으면 False 반환
    학생이 없고 장애물이나 벽에 막히면 True반환하는 함수
    '''
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(len(T)): # 선생님 한명씩 확인 
        y,x = T[i] # 선생님 좌표 (탐색 시작점 좌표)

        # 4방향 확인 위아래양옆
        for index in range(4):
            ny,nx = y + dy[index], x + dx[index] # 한칸씩 이동해서 확인 
            while 0 <= ny < N and 0 <= nx < N: # 만약 범위안에 잇으면 
                if corridor[ny][nx] == "S": # 지금 확인하는 위치가 학생이면 
                    return False # 실패
                elif corridor[ny][nx] == "T" or corridor[ny][nx] == "O": # 지금 확인하는 위치가 장애물이나 선생이면 
                    break # 그 라인은 탐색 정지 
      
                ny,nx = ny + dy[index], nx + dx[index] # 그 다음칸 확인을 위해 
    # 탐색 끝낫는데 학생을 안만낫으면 
    return True    

def set_block(cnt):
    '''
    모든 장애물을 설치하는 경우의 수를 확인
    장애물을 3개를 설치하면 dfs()함수를 실행해서 학생이 선생님의 감시를 피하는지 확인
    한가지 경우의 수라도 감시피하기 성공하면 rlt = True로 할당 해주는 함수 

    param
    cnt : 설치한 장애물의 수
    '''
    global corridor # 복도에 장애물을 설치하기 위해 global로 불러줌
    global rlt # bfs() 실행 후 감시를 피하는 경우의 수가 있다면 True로 변경하기 위해 global로 불러줌
    if cnt == 3: # 장애물 3개 설치되면 
        if dfs(): # dfs() 실행 후 True값이 반환 되면 
            rlt = True 
            return 
    else:
        # 모든 "X"의 자리에 장애물을 설치 
        for row in range(N):
            for col in range(N):
                if corridor[row][col] == "X": # 복도의 빈공간이면
                    # 장애물 설치 
                    corridor[row][col] = "O"
                    set_block(cnt + 1)
                    # 모든 장애물 설치 경우의 수를 확인하기 위해 복귀해줘야함 
                    corridor[row][col] = "X" # 복귀 

N = int(input()) # 복도의 크기 
corridor = [input().split() for _ in range(N)]
# 선생님 위치를 담은 리스트 만들기 (탐색 시작점 리스트 만들기)
T = []
for i in range(N):
    for j in range(N):
        if corridor[i][j] == "T":
            T.append((i,j))

rlt = False # 결과의 초기값

set_block(0) 
if rlt: # true면
    print("YES")
else:
    print("NO")