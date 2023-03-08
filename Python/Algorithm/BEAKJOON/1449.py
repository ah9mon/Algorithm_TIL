# 수리공 항승 

'''
https://www.acmicpc.net/problem/1449

물새는 위치의 좌우 0.5 만큼씩 덮어야함

'''

# 물새는 곳의 개수 , 테이프의 길이
N,L = map(int,input().split())

leak_location = list(map(int,input().split()))
leak_location.sort()
p = [0]*(2002)
counts = 0
for i in range(N):
    if p[leak_location[i]] == 0: #테이프 안붙었으면 붙임
        p[leak_location[i]:leak_location[i]+L] = [1]*(L)
        counts += 1

print(counts)
        
        
    
    
    
