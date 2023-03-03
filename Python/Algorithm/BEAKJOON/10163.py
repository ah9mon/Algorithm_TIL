# 색종이 

'''
https://www.acmicpc.net/problem/10163
pypy로 제출해야 만점 
'''

N = int(input()) # 색종이 장수 
v = [[0]*1001 for _ in range(1001)] # 색종이 놓는 곳 

for i in range(1,N+1):
    x1, y1, dx, dy = map(int,input().split()) # 왼쪽아래 좌표 x,y / 너비, 높이  
    # 색종이 놓기 
    for row in range(y1,y1+dy):
        for col in range(x1,x1+dx):
                v[row][col] = i #색종이 번호를 할당  

# j번 색종이가 보이는 면적 찾고 출력 
for j in range(1,N+1):
    rlt = 0
    for r in range(1001):
        for c in range(1001):
            if v[r][c] == j: # j번째 색종이면  
                rlt += 1 # 넓이 + 1
    print(rlt) # 최종 넓이 출력 



            
             

