# 백준 월드컵
'''
https://www.acmicpc.net/problem/6987

6개국이 5번씩 경기 

가능결과 1 
승: 15 / 패 : 15
총 30 
가능결과 2 
승 : 13 / 패 : 13 / 무 : 4
총 30

불가능결과 1 
승 : 14 / 패 : 14 / 무 : 2
총 30 
-> 왜 ? C가 패가 2 이상이어야함 -> 이걸 어캐 체크하냐 ,,,

불가능결과 2 
승 : 13 / 패 : 14 / 무 : 2
총 29 -> 총 30 경기 인데 29만 나옴 불가능 

조건
1. 승 무 패 카운트
2. 무가 홀수면 안됨 
3. 승 패 합한게 짝수 

'''
    
import sys

sys.stdin = open('input_for_6986.txt')

from itertools import combinations

def func(n):
    global rltt
    if n == 15: # 15경기 다했으면 
        for i in range(6):
            for j in range(3):
                if arr[i][j] != 0: # 승 무 패 중에 0 이 아닌게 있으면 
                    return 
        rltt = 1        
        return 
    
    c1, c2 = match[n] # 경기하는 팀
    rlt_of_match = [(0,2),(1,1),(2,0)] # 승 무 패 
    for k in range(3):
        if arr[c1][rlt_of_match[k][0]] > 0 and arr[c2][rlt_of_match[k][1]] > 0 :
            arr[c1][rlt_of_match[k][0]] -= 1 
            arr[c2][rlt_of_match[k][1]] -= 1
            func(n+1) 
            arr[c1][rlt_of_match[k][0]] += 1 
            arr[c2][rlt_of_match[k][1]] += 1 


rlt = [0]*4

for tc in range(4):

    lst = list(map(int,sys.stdin.readline().split()))

    if sum(lst) != 30: # 총 30 경기 아니면  
        continue
    elif sum(lst[0:18:3]) != sum(lst[2:18:3]): # 승과 패 수가 다르면 
        continue
    elif sum(lst[1:18:3]) % 2: # 무가 짝수가 아니면 
        continue
        
    arr = [lst[i:i+3] for i in range(0,18,3)]

    match = list(combinations(range(6), 2))
    rltt = 0
    func(0)
    rlt[tc] = rltt

print(*rlt)