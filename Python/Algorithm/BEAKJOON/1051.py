# 숫자 정사각형 

'''
https://www.acmicpc.net/problem/1051



'''
n,m = map(int,input().split())
rec = [input() for _ in range(n)]
r = min(n,m)
max_s = 1
for squ in range(1,r+1):
    for i in range(n-squ+1):
        for j in range(m-squ+1):
            # print(i,j)
            if rec[i][j] == rec[i][j+squ-1] == rec[i+squ-1][j] == rec[i+squ-1][j+squ-1]:
                # print(squ)
                if max_s < squ:
                    max_s = squ
print(max_s**2)

        
