# 신입 사원 

'''
https://www.acmicpc.net/problem/1946
'''

T = int(input())
for _ in range(T): 
    N = int(input()) # 지원자 수
    d = [0]*(N+1) # 인덱스가 1번 시험 성적 / 값이 2번 시험 성적
    
    # 입력 받기
    for _ in range(N):
        a, b = map(int,input().split()) # 1번시험 성적 2번시험 성적
        d[a] += b 
    
    counts = 1 # 1등은 무조건 + 1 
    for i in range(2,N+1): # 2등 부터 검사 
        if d[i] < d[i-1]: # 앞등보다 2번 시험 등수가 높으면 
            counts += 1 
        else: # 앞등보다 2번 시험 등수가 낮으면 
            d[i] = d[i-1] # 카운트 안하고 다음 지원자는 탈락자 앞등의 성적과 비교하기 위해 d[i]에 할당해줌 
    
    print(counts)