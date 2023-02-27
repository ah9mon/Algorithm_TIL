def Minsoo_Choi(list):
    # 중복 카운트 리스트 생성 
    counts = [0] * (max(list) + 1)
    for num in list:
        counts[num] += 1

    # 최빈수 반환
    max_count = counts[0] # 0번째 항목이 최빈수라 가정
    max_index = 0
    
    for i in range(len(counts)):
        if counts[i] >= max_count: # 만약 counts[i]가 max_count보다 크다면
            max_count = counts[i] 
            max_index = i # 최빈수 

    return max_index

T = int(input())

for i in range(1,T+1):
    tc = int(input())
    rlt_list = list(map(int,input().split()))
    print(f'#{tc} {Minsoo_Choi(rlt_list)}')



    