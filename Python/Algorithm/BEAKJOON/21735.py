#눈덩이 굴리기 
'''
https://www.acmicpc.net/problem/21735
눈덩이 굴리거나 던질 때 1초 소모 
제한 시간 M 초
+ 1 로 굴리면 a[i] 만큼 크기 증가 
+ 2 로 던지면 (현재 // 2) + a[i]

'''
def dfs(i,s,c):
    global rlt
    # 시간 제한 됐으면 
    # print(c)
    if s == M:
        if c > rlt:
            # print(*visited)
            # print(rlt)
            rlt = c
        return
    
    # 마당 끝에 갔으면 
    elif i == N - 1:
        if c > rlt:
            # print(*visited)
            # print(rlt)
            rlt = c
        return
    
    else:
        # 1칸 가는 경우 
        # visited[i+1] = 1
        dfs(i+1,s+1,c + a[i+1])
        # visited[i+1] = 0
        # 2칸 가는 경우 
        if i + 2 <= N - 1:
            # visited[i+2] = 1
            dfs(i+2,s+1,(c//2) + a[i+2])
            # visited[i+2] = 0

# 앞마당의 길이 N, 대회의 시간 M
N, M = map(int,input().split())
# 길이가 N인 수열 a
a = list(map(int,input().split()))
rlt = 0
visited = [0]*N
dfs(-1,0,1)
print(rlt)
