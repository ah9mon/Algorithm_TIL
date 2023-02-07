import sys
sys.stdin = open('input.txt')

def turn(cube,N):
    empty = [[0] * N for k in range(N)]
    # 한줄씩 세로로 옮기기 
    for i in range(N):
        for j in range(N):
            empty[j][-(i+1)] = cube[i][j]
    
    return empty
            
            
T = int(input())

for i in range(1,T+1):
    N = int(input())
    cube = [list(map(int, input().split())) for j in range(N)]
    turn1 = turn(cube,N)
    turn2 = turn(turn1,N)
    turn3 = turn(turn2,N)
    print(f'#{i}')
    for k in range(N):
        line = ''.join(str(x) for x in turn1[k]) +' '+ ''.join(str(x) for x in turn2[k]) +' '+ ''.join(str(x) for x in turn3[k])
        print(line)        
        
    
     
        
    