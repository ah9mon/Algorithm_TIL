# 색칠하기 
'''
1 빨강색
2 파랑색 

보라색이된 칸수 구하기 

2나 0 이면 + 1
1이나 0이면 + 2 
'''

import sys
sys.stdin = open('input_for_4836.txt')
    
T = int(input())

for i in range(1,T+1):
    # 칠할 영역의 개수
    N = int(input())
    paper = [[0]*10 for _ in range(10)]
    counts = 0
    for _ in range(N):
        # 왼쪽위 , 오른쪽 아래 , 색상정보 
        r1,c1,r2,c2,color = map(int,input().split())
        for row in range(r1,r2+1):
            for col in range(c1,c2+1):
                if color == 1:
                    if paper[row][col] in (0,2):
                        paper[row][col] += color
                else:
                    if paper[row][col] in (0,1):
                        paper[row][col] += color  
                        
                if paper[row][col] == 3:
                    counts += 1        
    
    # print(paper)
    print(f'#{i} {counts}')
                
    
    
    
    