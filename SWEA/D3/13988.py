#세제곱슨을 찾아라 
import sys
sys.stdin = open('input_for_13988.txt')

def func():
    j = 1
    while j**3 <= n:
        if j**3 == n:
            return j
        else:
            j += 1
    
    return -1
    

T = int(input())

for i in range(1,T+1):
    n = int(input())
    print(f'#{i} {func()}')
    
    
    