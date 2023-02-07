import sys
sys.stdin = open('input.txt')

def up_and_find(ladder):
    visited = [[0]*100 for i in range(100)]
    y,x = 99, ladder[99].index(2)
    
    while y != 0 :
        visited[y][x] = 1
        # 왼
        if 0 <= x - 1 < 100 and visited[y][x-1] == 0 and ladder[y][x-1]:
            x = x - 1

            continue
            
        # 오른
        elif 0 <= x + 1 < 100 and visited[y][x+1] == 0 and ladder[y][x+1]:
            x = x + 1

            continue
           
        # 위
        else:
            y = y - 1

            
  
    
    return x

T = 10
for i in range(1,T+1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for j in range(100)]
    print(f'#{i} {up_and_find(ladder)}')
    
    