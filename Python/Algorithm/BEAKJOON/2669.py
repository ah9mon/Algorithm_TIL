# 직사각형 네개의 합집합의 면적 구하기 

v = [[0]*101 for _ in range(101)]

for _ in range(4):

    x1, y1, x2, y2 = map(int,input().split())

    for row in range(y1,y2): # 행
        for col in range(x1,x2):
            if not v[row][col]:
                v[row][col] = 1

area = 0
for r in range(101):
    area += sum(v[r])

print(area)
