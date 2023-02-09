def countss(P,A):
    l,r = 1, P 
    c = (r+l) // 2
    counts = 0
    while True:    
        if A > c:
            l = c
            c = (r + l) // 2 
            counts += 1
        elif A < c: 
            r = c
            c = (r + l) // 2 
            counts += 1
        elif A == c:
            return counts  

def func(P,A,B):
    if countss(P,A) < countss(P,B):
        return 'A'
    elif countss(P,A) > countss(P,B):
        return 'B'
    else: 
        return 0

T = int(input())

for i in range(1,T+1):
    p,a,b = map(int, input().split())
    print(f'#{i} {func(p,a,b)}')