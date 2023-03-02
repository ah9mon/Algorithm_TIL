# 블랙잭 

'''
카드합이 21을 넘지 않으면서 최대한 크게 만드는 게임 

숫자가 보이는 카드 N장
고른 카드의 합이 M을 넘지 않으면서 최대한 크게 
'''
def func(s,e,c):
    global d
    global max_sum
    if c == 3:
        
        sum_now = sum(d)
        if sum_now <= M:
            if max_sum < sum_now:
                max_sum = sum_now
        return
    
    # elif c > 3:
    #     return
    
    if s == e :
        return

    else:
        d[s] = cards[s]
        func(s+1,e,c+1)
        d[s] = 0
        func(s+1,e,c)


N, M = map(int,input().split())

cards = list(map(int,input().split()))
d = [0] * N
max_sum = 0 
func(0,N,0)
print(max_sum)

