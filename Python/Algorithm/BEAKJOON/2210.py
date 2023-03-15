# 숫자판 점프 

'''
https://www.acmicpc.net/problem/2210
뭔소리야 ㅅㅂ
'''
def func(y,x,c,word):
    global rlt_lst

    if c == 5: # 종료 조건 / 5번 이동하면  
        rlt_lst.add(word) # 만들어진 word set에 추가 
        return 
    
    for v in range(4): # 다음 4방향으로 이동 
        ny,nx = y + dy[v], x + dx[v] # 이동할 좌표 
        if 0<= ny <5 and 0<= nx <5: # 범위안에 있으면 
            func(ny,nx,c+1,word+graph[ny][nx]) # 이동 
    
# 입력받기 
graph = [input().split() for _ in range(5)]
# 4방향 탐색
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 중복된 것들 추가하지 않기 위해 set로
rlt_lst = set()

# 모든 점이 한번씩 시작점
for r in range(5):
    for c in range(5):
        func(r,c,0,graph[r][c])
        
# print(rlt_lst)
print(len(rlt_lst))