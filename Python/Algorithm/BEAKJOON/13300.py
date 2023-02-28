# 방배정 
'''
https://www.acmicpc.net/problem/13300

'''
# 학생수, 방배정 인원수
N,M = map(int,input().split())
# 성별, 학년
d = [[0]*2 for _ in range(7)]
for _ in range(N):
    sex,grade = map(int,input().split())
    d[grade][sex] += 1
# print(d)
counts =0
for grd in range(1,7):
    for sx in range(2):
        if d[grd][sx] % M: # 나머지 있으면 
            counts +=  d[grd][sx] // M + 1 
        else:
            counts +=  d[grd][sx] // M 
              
print(counts)
