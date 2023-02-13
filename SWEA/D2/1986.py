import sys
sys.stdin = open('input_for_1986.txt')

def zigzag(N):
    rlt = 0
    for i in range(1,N+1):
        if i % 2:
            rlt += i
        else: 
            rlt -= i
            
    return rlt
        
        

T = int(input())

for i in range(1,T+1):
    N = int(input())
    print(f'#{i} {zigzag(N)}')