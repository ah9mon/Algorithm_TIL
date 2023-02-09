from collections import Counter

def Baby_gin(num):
    from collections import Counter # 같은 항목의 개수를 딕셔너리 형태로 반환 type은 counter({a: 1, b: 2, c: 3, ... }) 
    tri = 0
    run = 0 
    i = 0

    num_list = list(map(int,num)) # input을 리스트로 
    # print(Counter(num_list)) # Counter({1: 3, 4: 1, 5: 1, 6: 1})
    counts = list(map(list,Counter(num_list).items())) # 카운터는 인덱스 넘버로 불러오는 등 자유롭게 사용 못하므로 리스트로 변경 
    counts.sort()   # [[1, 3], [4, 1], [5, 1], [6, 1]] # [항목, 개수] 형태를 항목을 기준으로 오름차순 정렬
    #print(counts)
    while i <= len(counts) - 1 : 

        if counts[i][1] >= 3: # 개수가 3보다 크면
            counts[i][1] -= 3
            tri += 1        
            continue
        
        if i >= 2: # out of range 방지하기 위해 i / i - 1/ i - 2 로 확인   
            if counts[i][1] >= 1 and counts[i-1][1] >= 1 and counts[i-2][1] >= 1:
                counts[i][1] -= 1
                counts[i-1][1] -= 1 
                counts[i-2][1] -= 1
                run += 1
                continue

        i += 1
        
    if run + tri == 2:
        return 1
    else:
        return 0
        
T= int(input())

for i in range(1,T+1):
    num = input()
    print(f'#{i} {Baby_gin(num)}')

