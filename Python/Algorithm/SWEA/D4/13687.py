# 자기 방으로 돌아가기
import sys
sys.stdin = open('input_for_13687.txt')

def dfs(N,stu):
    global counts
    visited = [0]*200
    stack = []
    for i in range(N):
        # 홀수인지 짝수인지? 
        # 홀수 index = n//2
        # 짝수 index = n//2-1
        index = []
        for j in stu[i]:
            if j % 2: # 홀수면 
                index.append(j//2)
            else: # 짝수면 
                index.append(j//2-1)

        if index[0] <= index[1] and not 1 in visited[index[0]:index[1]+1]:

            visited[index[0]:index[1]+1] = [1]*(index[1]-index[0]+1)

        elif index[0] > index[1] and not 1 in visited[index[1]:index[0]+1]:

            visited[index[1]:index[0]+1] = [1]*(index[0]-index[1]+1)
            
        else:
            stack.append(stu[i])

    counts += 1

    if not stack: # 스택 비었으면 
        return #탈출
    
    dfs(len(stack),stack)

T = int(input())
for i in range(1,T+1):
    N = int(input())
    stu = [tuple(map(int,input().split())) for _ in range(N)]
    counts = 0
    dfs(N,stu)
    print(f'#{i} {counts}')
    
