# 딱지놀이 

def func():
    for i in range(4,0,-1): # 4 3 2 1 순으로 비교 
        if i in A and i in B: # i가 둘다 있으면
            # 개수 비교
            if counts_a[i] > counts_b[i]:
                print('A')
                return
            
            elif counts_a[i] < counts_b[i]:
                print('B')
                return
        elif i in A: # A만 i있으면 A승리
            print('A')
            return
        elif i in B: # B만 i있으면 B승리
            print('B')
            return
        # 둘다 i가 없으면 i-1로 넘어감 

    print('D') # 다 똑같으면 비김

N = int(input())
for _ in range(N):
    # A의 카드 입력받기 
    A = list(map(int,input().split()))
    # 1부터 4까지 각각 몇개 있는지 카운트
    counts_a = [0]*5
    for a in A[1:]:
        counts_a[a] += 1 
    # B의 카드 입력받기     
    B = list(map(int,input().split()))
    # 1부터 4까지 각각 몇개 있는지 카운트
    counts_b = [0]*5
    for b in B[1:]:
        counts_b[b] += 1
    func()





