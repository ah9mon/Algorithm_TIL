# 고대 유적 

import sys
sys.stdin = open('input_for_9489.txt')


T = int(input())

for i in range(1,T+1):
    N,M = map(int,input().split())
    data = [input().split() for _ in range(M)]
    
    # 가로 확인 
    data_x = []
    for x in data:
        data_x += x.split('0')
        
    print(data_x)
    

    
    
    
            
             
                
            
    
    