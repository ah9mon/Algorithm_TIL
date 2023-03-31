# 수영장 
'''


'''
import sys
sys.stdin = open('input_for_14119.txt')

def func(i,price):
    global min_price
    if price > min_price:
        return
    
    if i >= 12:
        min_price = price
        return

    for j in range(3):
        # print(i)
        if not visited[i]:
            # 3개월권일 때
            if j == 2:
                visited[i:i+3] = [1]*3
                func(i+3, price+tickets[2])
                visited[i:i+3] = [0]*3
            # 1개월권일 때
            elif j == 1:
                visited[i] = 1
                func(i+1,price+tickets[1])
                visited[i] = 0
            # 1일권일 때
            else:
                visited[i] = 1
                func(i+1,price+tickets[0]*plan[i])
                visited[i] = 0    
    return

T = int(input())
for tc in range(1,T+1):
    # 이용권의 요금
    # day, month, th_month, year
    tickets = list(map(int,input().split()))
    # 이용계획 
    plan = list(map(int,input().split())) 
    min_price = tickets[-1]
    visited = [0]*14
    func(0,0)
    print(f'#{tc} {min_price}')

