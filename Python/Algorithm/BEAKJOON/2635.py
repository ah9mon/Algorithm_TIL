# 2635

# 수 이어가기

# https://www.acmicpc.net/problem/2635


N = int(input())
p = []
p.append(N)
max_len = 0
max_p = []
for i in range(N//2,N+1):
    p = []
    p.append(N)
    p.append(i)
    j = 1
    now = p[0] - p[1]
    while now >= 0:
        j += 1
        p.append(now)
        now = p[j-1] - p[j]

    if len(p) > max_len:
        max_len = len(p)
        max_p = p

print(max_len)
for num in max_p:
    print(num,end = ' ')
