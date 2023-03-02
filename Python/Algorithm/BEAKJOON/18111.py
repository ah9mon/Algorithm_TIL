# 마크
'''
https://www.acmicpc.net/problem/18111
'''

N,M,B = map(int,input().split())

ground = [list(map(int,input().split())) for _ in range(N)]

mintime = 12345678910
minrlt = 257
for rlt in range(257): # 땅고르기 후 높이 
    time = 0
    minus = 0
    plus = 0
    for i in range(N):
        for j in range(M):
            a = ground[i][j] - rlt
            if a < 0: 
                minus += a
            else: 
                plus += a
    
    # minus > plus + B 의 경우 -> 실패 
    if minus > plus + B:
        continue
    # minus <= plus + B 의 경우  
    else:
        minus2 = minus + B
        if minus2 >= 0: # b로 다 채울 수 있는 경우
            time += plus*2 + abs(minus)
        else: # b로 다 못채우는 경우
            time += B
            plus2 = plus + minus2
            if plus2 >= 0: # plus로 다 채울 수 있는 경우
                time += plus2*2 + abs(minus2)*3
            else: # plus로 다 못채우는 경우
                continue # 실패 
    
    if mintime >= time:
        mintime = time
        minrlt = rlt

print(mintime,minrlt)


        

            



